# operations.py

# Define the valid genres as a tuple (immutable)
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Romance", "Fantasy", "Biography")

# Books dictionary: key = ISBN (str), value = dict with title, author, genre, copies
books = {}

# Members list: each element is a dict with keys: id, name, borrowed_books (list of ISBNs)
members = []

def add_book(isbn, title, author, genre, copies):
    """
    Add a new book to the collection.
    - isbn (str): unique book identifier.
    - title (str), author (str), genre (str), copies (int): book details.
    Genre must be in the predefined genres tuple. ISBN must be unique.
    """
    if isbn in books:
        print(f"Error: ISBN {isbn} already exists.")
        return False
    if genre not in genres:
        print(f"Error: Genre '{genre}' is not valid.")
        return False
    if copies < 1:
        print("Error: Number of copies must be at least 1.")
        return False
    books[isbn] = {"title": title, "author": author, "genre": genre, "copies": copies}
    print(f"Book '{title}' added successfully with ISBN {isbn}.")
    return True

def add_member(member_id, name):
    """
    Register a new member.
    - member_id (int): unique member ID.
    - name (str): member's name.
    ID must be unique.
    """
    # Check uniqueness
    for mem in members:
        if mem["id"] == member_id:
            print(f"Error: Member ID {member_id} already exists.")
            return False
    members.append({"id": member_id, "name": name, "borrowed_books": []})
    print(f"Member '{name}' added with ID {member_id}.")
    return True

def search_book(query):
    """
    Search books by title or author (case-insensitive substring match).
    Returns list of (ISBN, details) tuples that match the query in title or author.
    """
    results = []
    for isbn, info in books.items():
        if query.lower() in info["title"].lower() or query.lower() in info["author"].lower():
            results.append((isbn, info))
    if results:
        print(f"Search results for '{query}':")
        for isbn, info in results:
            print(f"ISBN: {isbn}, Title: {info['title']}, Author: {info['author']}, Genre: {info['genre']}, Copies: {info['copies']}")
    else:
        print(f"No books found matching '{query}'.")
    return results

def update_book(isbn, title=None, author=None, genre=None, copies=None):
    """
    Update an existing book's details. Only non-None parameters will be updated.
    Genre must remain valid. Copies (total) can be changed if it does not conflict
    with currently borrowed count.
    """
    if isbn not in books:
        print(f"Error: ISBN {isbn} not found.")
        return False
    book = books[isbn]
    # Update fields if provided
    if title is not None:
        book["title"] = title
    if author is not None:
        book["author"] = author
    if genre is not None:
        if genre not in genres:
            print(f"Error: Genre '{genre}' is not valid.")
            return False
        book["genre"] = genre
    if copies is not None:
        if copies < 0:
            print("Error: Copies cannot be negative.")
            return False
        # Check borrowed count: how many are currently loaned out?
        borrowed_count = 0
        for mem in members:
            borrowed_count += mem["borrowed_books"].count(isbn)
        if copies < borrowed_count:
            print("Error: New copies count is less than the number of borrowed copies.")
            return False
        # Adjust available copies. If we track copies as available, ensure it is at least 0.
        book["copies"] = copies - borrowed_count
        print(f"Book ISBN {isbn} copies updated. (Borrowed: {borrowed_count}, Available now: {book['copies']})")
    print(f"Book ISBN {isbn} updated successfully.")
    return True

def update_member(member_id, name=None):
    """
    Update a member's details. Currently only name can be changed.
    """
    for mem in members:
        if mem["id"] == member_id:
            if name is not None:
                mem["name"] = name
                print(f"Member ID {member_id} name updated to {name}.")
            return True
    print(f"Error: Member ID {member_id} not found.")
    return False

def delete_book(isbn):
    """
    Delete a book from the system if no member has borrowed it.
    """
    if isbn not in books:
        print(f"Error: ISBN {isbn} does not exist.")
        return False
    # Check if any member has this book borrowed
    for mem in members:
        if isbn in mem["borrowed_books"]:
            print(f"Cannot delete: Book ISBN {isbn} is currently borrowed by a member.")
            return False
    del books[isbn]
    print(f"Book ISBN {isbn} deleted successfully.")
    return True

def delete_member(member_id):
    """
    Delete a member if they have no borrowed books.
    """
    for i, mem in enumerate(members):
        if mem["id"] == member_id:
            if mem["borrowed_books"]:
                print(f"Cannot delete: Member ID {member_id} has borrowed books.")
                return False
            members.pop(i)
            print(f"Member ID {member_id} deleted successfully.")
            return True
    print(f"Error: Member ID {member_id} not found.")
    return False

def borrow_book(member_id, isbn):
    """
    Borrow a book for a member.
    Conditions: member exists, book exists, member has <3 books borrowed,
    book copies available > 0.
    """
    # Find member
    member = next((mem for mem in members if mem["id"] == member_id), None)
    if not member:
        print(f"Error: Member ID {member_id} not found.")
        return False
    if isbn not in books:
        print(f"Error: Book ISBN {isbn} not found.")
        return False
    if len(member["borrowed_books"]) >= 3:
        print("Error: Borrowing limit reached (3 books).")
        return False
    if books[isbn]["copies"] <= 0:
        print(f"Error: No available copies of ISBN {isbn}.")
        return False
    # Perform borrow
    books[isbn]["copies"] -= 1
    member["borrowed_books"].append(isbn)
    print(f"Member ID {member_id} has borrowed book ISBN {isbn}.")
    return True

def return_book(member_id, isbn):
    """
    Return a book from a member.
    """
    member = next((mem for mem in members if mem["id"] == member_id), None)
    if not member:
        print(f"Error: Member ID {member_id} not found.")
        return False
    if isbn not in member["borrowed_books"]:
        print(f"Error: Member ID {member_id} did not borrow ISBN {isbn}.")
        return False
    member["borrowed_books"].remove(isbn)
    books[isbn]["copies"] += 1
    print(f"Member ID {member_id} has returned book ISBN {isbn}.")
    return True
