# demo.py

from operations import *

def demo():
    print("=== Library System Demo ===")
    # Add some genres (already defined in operations.py)
    # Add books
    add_book("ISBN001", "The Hobbit", "J.R.R. Tolkien", "Fantasy", 3)
    add_book("ISBN002", "1984", "George Orwell", "Fiction", 2)
    add_book("ISBN003", "Dune", "Frank Herbert", "Sci-Fi", 1)
    # Attempt to add a duplicate
    add_book("ISBN001", "Duplicate Book", "Author", "Fiction", 1)

    # Add members
    add_member(101, "Alice")
    add_member(102, "Bob")
    add_member(101, "Charlie")  # duplicate ID

    # Search books
    search_book("the")    # matches "The Hobbit"
    search_book("George") # matches author of "1984"
    search_book("xyz")    # no matches

    # Borrow books
    borrow_book(101, "ISBN001")  # Alice borrows The Hobbit
    borrow_book(101, "ISBN002")  # Alice borrows 1984
    borrow_book(101, "ISBN003")  # Alice borrows Dune
    borrow_book(101, "ISBN002")  # Should fail: limit or no copies
    borrow_book(102, "ISBN001")  # Bob borrows The Hobbit
    borrow_book(102, "ISBN001")  # Bob tries to borrow The Hobbit again (no copies)

    # Return books
    return_book(101, "ISBN001")  # Alice returns The Hobbit
    return_book(101, "ISBN999")  # Error: ISBN doesn't exist
    return_book(102, "ISBN001")  # Bob returns The Hobbit

    # Update book
    update_book("ISBN002", copies=5)  # increase copies
    update_book("ISBN004", title="New")  # non-existent book

    # Delete book (should fail if borrowed)
    delete_book("ISBN002")  # ISBN002 may or may not be borrowed
    delete_book("ISBN003")  # delete Dune if no borrow

    # Delete member
    delete_member(102)  # Bob (should fail if borrowed list not empty)
    delete_member(103)  # non-existent member

    # Final state
    print("\nFinal Books Catalog:")
    for isbn, info in books.items():
        print(isbn, info)
    print("\nFinal Members List:")
    for mem in members:
        print(mem)

if __name__ == "__main__":
    demo()
