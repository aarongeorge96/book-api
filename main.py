from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from database import SessionLocal, BookDB
import os


class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    status: str = "unread"
    rating: Optional[int] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def serve_homepage():
    with open("templates/index.html", "r") as f:
        return f.read()


@app.get("/books")
def get_all_books(db: Session = Depends(get_db)):
    return db.query(BookDB).all()


@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books")
def add_book(book: Book, db: Session = Depends(get_db)):
    new_book = BookDB(
        title=book.title,
        author=book.author,
        status=book.status,
        rating=book.rating,
        notes=book.notes
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted", "book_id": book_id}