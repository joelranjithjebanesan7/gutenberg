from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = ['name', 'birth_year', 'death_year']

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = ['name']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = ['name']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = ['code']

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['mime_type', 'url']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    class Meta:
        model = BooksBook
        fields = [
            'gutenberg_id', 'title', 'download_count',
            'authors', 'languages', 'subjects', 'bookshelves', 'formats'
        ]

    def get_authors(self, obj):
        authors = BooksAuthor.objects.filter(
            booksbookauthors__book=obj
        )
        return AuthorSerializer(authors, many=True).data

    def get_bookshelves(self, obj):
        shelves = BooksBookshelf.objects.filter(
            booksbookbookshelves__book=obj
        )
        return [s.name for s in shelves]

    def get_subjects(self, obj):
        subjects = BooksSubject.objects.filter(
            booksbooksubjects__book=obj
        )
        return [s.name for s in subjects]

    def get_languages(self, obj):
        langs = BooksLanguage.objects.filter(
            booksbooklanguages__book=obj
        )
        return [l.code for l in langs]

    def get_formats(self, obj):
        formats = BooksFormat.objects.filter(book=obj)
        return FormatSerializer(formats, many=True).data