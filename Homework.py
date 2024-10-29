#Basic classes
class Book:
    def __init__(self, title, author, id_number):
        self.title = title
        self.author = author
        self.id_number = id_number
    
    def get_book(self):
        book_info = (self.title, self.author, self.id_number)
        return book_info


class Student:
    def __init__(self, name, class_number, student_id):
        self.name = name
        self.class_number = class_number
        self.student_id = student_id
    
    def get_student(self):
        student_info = (self.name, self.class_number, self.student_id)
        return student_info
    
#Library management system
class Library:
    def __init__(self):
            self.availableBooks = []
            self.borrowedBooks = {}
            self.waitingQueue = {}

    def add_book(self, book):
        if book.title not in self.availableBooks:
            self.availableBooks.append(book.title)
        
    def request_book(self, student, book_title):
        if book_title in self.availableBooks:
            self.availableBooks.remove(book_title)
            self.borrowedBooks[book_title] = student.name
        else:
            self.waitingQueue[book_title] = student.name
            
    def return_book(self, book):
        if book.title in self.borrowedBooks and book not in self.availableBooks:
            del self.borrowedBooks[book.title]
            self.availableBooks.append(book.title)

        for key, value in self.waitingQueue.items():
            if book == key:
                Library.request_book(value, key)
            else:
                print("No one's looking for this book yet.")
        
# Part 3: Testing the System
# Create some books
book1 = Book("Doraemon Tập 1", "Fujiko F. Fujio", "B001")
book2 = Book("Harry Potter Tập 1", "J.K. Rowling", "B002")
book3 = Book("The Little Prince", "Antoine de Saint-Exupéry", "B003")

# Create some students
student1 = Student("Minh", "7A", "S001")
student2 = Student("Linh", "7B", "S002")

# Create the Library system and add books
Library = Library()
Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)

# Test borrowing books
Library.request_book(student1, "Doraemon Tập 1")  # Minh borrows "Doraemon Tập 1"
Library.request_book(student2, "Doraemon Tập 1")  # Linh should be added to the waiting list

# Return a book and handle waiting list
Library.return_book(book1)  # Minh returns "Doraemon Tập 1", Linh should borrow it


# Create some books
book1 = Book("Doraemon Tập 1", "Fujiko F. Fujio", "B001")
book2 = Book("Harry Potter Tập 1", "J.K. Rowling", "B002")
# Create students
student1 = Student("Minh", "7A", "S001")
student2 = Student("Linh", "7B", "S002")
# Test your library system
library = Library
library.add_book(book1)
library.add_book(book2)
library.request_book(student1, "Doraemon Tập 1")
library.request_book(student2, "Doraemon Tập 1") # Should go to waiting list

print(f"Available Books: {library.availableBooks}")
print("Waiting Queue:",library.waitingQueue)
print("Borrowed Books",library.borrowedBooks)