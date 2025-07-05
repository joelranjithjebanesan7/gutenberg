from django.shortcuts import render

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
# from rest_framework.pagination import PageNumberPagination
from .models import BooksBook
from .serializers import BookSerializer
from django.db.models import Q

# class BookPagination(PageNumberPagination):
#     "Allowing 25 data per response"
#     page_size = 25

class BookListAPIView(generics.ListAPIView):
    """
    View to retrieve list of books with 25 data with filters
    """
    queryset = BooksBook.objects.all().order_by('-download_count')
    serializer_class = BookSerializer
    # pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_queryset(self):
        queryset = super().get_queryset()

        author = self.request.query_params.get('author')
        title = self.request.query_params.get('title')
        language = self.request.query_params.getlist('language')
        mime_type = self.request.query_params.get('mime_type')
        topic = self.request.query_params.get('topic')
        gutenberg_ids = self.request.query_params.getlist('gutenberg_id')

        if author:
            queryset = queryset.filter(
                booksbookauthors__author__name__icontains=author
            )

        if title:
            queryset = queryset.filter(title__icontains=title)

        if gutenberg_ids:
            queryset = queryset.filter(gutenberg_id__in=gutenberg_ids)

        if language:
            queryset = queryset.filter(
                booksbooklanguages__language__code__in=language
            )

        if mime_type:
            queryset = queryset.filter(
                booksformat__mime_type__icontains=mime_type
            )

        if topic:
            queryset = queryset.filter(
                Q(booksbooksubjects__subject__name__icontains=topic) |
                Q(booksbookbookshelves__bookshelf__name__icontains=topic)
            )

        return queryset.distinct().prefetch_related(
            'booksbookauthors_set__author',
            'booksbookbookshelves_set__bookshelf',
            'booksbooksubjects_set__subject',
            'booksbooklanguages_set__language',
            'booksformat_set'
        )
