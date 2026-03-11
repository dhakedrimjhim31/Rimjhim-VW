
from flask import Blueprint, request, jsonify
from models.book_model import db, Book

book_bp = Blueprint("book_bp", __name__)


# Add Book
@book_bp.route("/books", methods=["POST"])
def add_book():

    data = request.json

    book = Book(
        title=data["title"],
        author=data["author"],
        copies=data["copies"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added"})


# Display all books
@book_bp.route("/books", methods=["GET"])
def get_books():

    books = Book.query.all()

    result = []

    for b in books:
        result.append({
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "copies": b.copies
        })

    return jsonify(result)


# Borrow book
@book_bp.route("/borrow/<int:id>", methods=["POST"])
def borrow_book(id):

    book = Book.query.get(id)

    if book.copies == 0:
        return jsonify({"message": "Book unavailable"}), 400

    book.copies -= 1
    db.session.commit()

    return jsonify({"message": "Book borrowed"})


# Books currently unavailable
@book_bp.route("/books/unavailable")
def unavailable_books():

    books = Book.query.filter_by(copies=0).all()

    result = []

    for b in books:
        result.append({
            "title": b.title,
            "author": b.author
        })

    return jsonify(result)