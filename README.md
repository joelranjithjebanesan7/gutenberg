# Project Gutenberg Books API

This is a Django REST API that allows querying and retrieving metadata about books from the [Project Gutenberg](https://www.gutenberg.org/) database.

It supports powerful filters, pagination, and sorting by popularity.

---

## API Features

The `/api/books/` endpoint allows:

- Filtering by:
  - Title (partial, case-insensitive)
  - Author (partial, case-insensitive)
  - Language (e.g., `en`, `fr`)
  - Mime-type (e.g., `text/plain`, `application/epub+zip`)
  - Topic (matches subject or bookshelf)
  - Project Gutenberg ID

- Pagination (25 books per page)
- Sorted by download count (most popular books first)
- Download links by format (mime-type)

---

## Example API Response

```json
{
  "count": 2940,
  "next": "/api/books/?page=2",
  "results": [
    {
      "id": 1,
      "gutenberg_id": 1342,
      "title": "Pride and Prejudice",
      "download_count": 20340,
      "authors": [{"name": "Jane Austen", "birth_year": 1775}],
      "languages": ["en"],
      "subjects": ["Love stories", "England -- Fiction"],
      "bookshelves": ["Best Books Ever Listings"],
      "formats": [
        {
          "mime_type": "text/plain",
          "url": "https://www.gutenberg.org/ebooks/1342.txt.utf-8"
        }
      ]
    }
  ]
}


Project Setup (Local)
  1. Clone the repository

      git clone https://github.com/joelranjithjebanesan7/gutenberg.git
      cd gutenberg/gutenberg_app
2. Create .env file
      POSTGRES_DB=gutenberg
      POSTGRES_USER=be_user
      POSTGRES_PASSWORD=your_db_password
      POSTGRES_HOST=db
      POSTGRES_PORT=5432
      DEBUG=1
      SECRET_KEY=your_secret_key
      DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
3. Run with Docker Compose
      docker-compose build
      docker-compose up
API Access
    Main API: /api/books/
    Swagger docs: /swagger/

Author
Joel Ranjith Jebanesan
