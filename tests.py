# tests.py

import unittest
from operations import *

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        # Clear data structures before each test
        books.clear()
        members.clear()

    def test_add_book_and_member(self):
        self.assertTrue(add_book("B1", "Book One", "Author A", "Fiction", 2))
        self.assertFalse(add_book("B1", "Duplicate", "Author B", "Fiction", 1))
        self.assertTrue(add_member(1, "Alice"))
        self.assertFalse(add_member(1, "Bob"))

    def test_search_book(self):
        add_book("B2", "Python Programming", "Guido", "Non-Fiction", 1)
        results = search_book("python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "B2")  # ISBN

    def test_borrow_and_return(self):
        add_book("B3", "Data Structures", "Cormen", "Non-Fiction", 1)
        add_member(2, "Bob")
        self.assertTrue(borrow_book(2, "B3"))
        # After borrow, no copies left
        self.assertEqual(books["B3"]["copies"], 0)
        # Cannot borrow again
        self.assertFalse(borrow_book(2, "B3"))
        # Return book
        self.assertTrue(return_book(2, "B3"))
        self.assertEqual(books["B3"]["copies"], 1)
        # Returning again should fail
        self.assertFalse(return_book(2, "B3"))

    def test_borrow_limit(self):
        add_book("B4", "Book4", "Author4", "Fiction", 3)
        add_book("B5", "Book5", "Author5", "Fiction", 3)
        add_book("B6", "Book6", "Author6", "Fiction", 3)
        add_book("B7", "Book7", "Author7", "Fiction", 3)
        add_member(3, "Charlie")
        # Borrow three books
        self.assertTrue(borrow_book(3, "B4"))
        self.assertTrue(borrow_book(3, "B5"))
        self.assertTrue(borrow_book(3, "B6"))
        # Fourth borrow should fail (limit 3)
        self.assertFalse(borrow_book(3, "B7"))

    def test_delete_operations(self):
        add_book("B8", "Book8", "Author8", "Fiction", 1)
        add_member(4, "Dana")
        borrow_book(4, "B8")
        # Deleting borrowed book or member with borrowed books should fail
        self.assertFalse(delete_book("B8"))
        self.assertFalse(delete_member(4))
        # After return, deletion should succeed
        return_book(4, "B8")
        self.assertTrue(delete_book("B8"))
        self.assertTrue(delete_member(4))

if __name__ == "__main__":
    unittest.main()
