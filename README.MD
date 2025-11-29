\# Book API



A personal book list API built with FastAPI and SQLite.



\## Features



\- Add, view, and delete books

\- Track reading status (unread, reading, read)

\- Add ratings and notes

\- Web interface included

\- REST API with auto-generated docs



\## Tech Stack



\- \*\*Backend:\*\* Python, FastAPI

\- \*\*Database:\*\* SQLite with SQLAlchemy

\- \*\*Frontend:\*\* HTML, CSS, JavaScript



\## Installation



1\. Clone the repository:

```

&nbsp;  git clone https://github.com/aarongeorge96/book-api.git

&nbsp;  cd book-api

```



2\. Create a virtual environment:

```

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate  # Windows

&nbsp;  source venv/bin/activate  # Mac/Linux

```



3\. Install dependencies:

```

&nbsp;  pip install fastapi uvicorn sqlalchemy

```



4\. Run the server:

```

&nbsp;  uvicorn main:app --reload

```



5\. Open in browser:

```

&nbsp;  http://localhost:8000

```



\## API Endpoints



| Method | Endpoint | Description |

|--------|----------|-------------|

| GET | /books | List all books |

| GET | /books/{id} | Get a specific book |

| POST | /books | Add a new book |

| DELETE | /books/{id} | Delete a book |



\## API Documentation



FastAPI generates interactive docs automatically:



\- Swagger UI: `http://localhost:8000/docs`

\- ReDoc: `http://localhost:8000/redoc`



\## Project Structure

```

book-api/

├── main.py          # API routes

├── database.py      # Database setup

├── books.db         # SQLite database (created on first run)

└── templates/

&nbsp;   └── index.html   # Web interface

```



\## License



MIT

