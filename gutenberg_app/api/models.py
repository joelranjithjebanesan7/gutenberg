from django.db import models


class BooksAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'


class BooksBook(models.Model):
    id = models.AutoField(primary_key=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'books_book'


class BooksBookAuthors(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    author = models.ForeignKey(BooksAuthor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_authors'

class BooksBookBookshelves(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey('BooksBookshelf', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_bookshelves'


class BooksBookLanguages(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    language = models.ForeignKey('BooksLanguage', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_languages'
        


class BooksBookSubjects(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    subject = models.ForeignKey('BooksSubject', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_subjects'


class BooksBookshelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'books_bookshelf'


class BooksFormat(models.Model):
    id = models.AutoField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(BooksBook,on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_format'


class BooksLanguage(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        db_table = 'books_language'


class BooksSubject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'
