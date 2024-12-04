#Basic classes
class Book:
    def __init__(self, title):
        self.title = title
        self.waitingQueue = Queue()
    
    def get_book(self):
        book_info = (self.title,self.waitingQueue)
        return book_info

class Student:
    def __init__(self, name):
        self.name = name
    
    def get_student(self):
        student_info = (self.name)
        return student_info

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        if item not in self.stack:
            self.stack.append(item)

    def pop(self, item):
        if item in self.stack:
            self.stack.remove(item)

class Queue:
    def __init__(self):
        self.queue = []

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    
    def push(self, item):
        if item not in self.queue:
            self.queue.append(item)

#Library management system
class Library:
    def __init__(self):
            self.allBooks = {}
            self.availableBooks = Stack()
            self.borrowedBooks = {}

    def add_book(self, book):
        self.availableBooks.push(book)
        self.allBooks[book.title] = book
        
    def request_book(self, student, book_title):
        book_title = book_title.lower().strip()
        if book_title in self.allBooks:
            book = self.allBooks[book_title]
            if book in self.availableBooks.stack:
                self.borrowedBooks[book] = student
                self.availableBooks.pop(book)
                print(f"{student.name} borrowed {book.title}")
            else:
                book.waitingQueue.push(student)
        else:
            print(f"'{book_title}' isn't in the library")

    def return_book(self, book_title):
        book_title = book_title.lower().strip()
        if book_title in self.allBooks:
            book = self.allBooks[book_title]
            if book in self.borrowedBooks:
                self.availableBooks.push(book)
                del self.borrowedBooks[book]
                nextStudent = book.waitingQueue.pop()
                requestedBook = book.title
                if nextStudent:
                    self.request_book(Student(nextStudent), requestedBook)
        else:
            print(book_title, "is a non-existent book")



# Interactive system
nonLibraryBooks = []
existingStudents = []
library = Library()
library.add_book(Book("book"))
library.add_book(Book("book2"))
library.request_book(Student("minh"),"book")



while True:
    name = input("What's your name? ").strip().lower()
    print("\n~What do you want to do?\nPick one of those actions: Create book/Add book/Request book/Return book(if you had borrowed it before)/Cancel~")
    action = input("Action: ").strip().lower()
    actions = ["create book", "add book", "request book", "return book", "cancel"]

    def register_name(name):
        for student in existingStudents:
            if student.name == name:
                return student
        student = Student(name)
        existingStudents.append(student)
        return student

    if action in actions:
        print("Enter required information:")
        #create
        if action == "create book":
            book_title = input("Book title: ").strip().lower()
            book = Book(book_title)
            nonLibraryBooks.append(book)
        #add
        elif action == "add book":
            if len(nonLibraryBooks) > 0:
                print("Choose one of the following books to add:")
                for book in nonLibraryBooks:
                    print(book.title)
                chosenBook = input("Chosen book: ").strip().lower()
                for book in nonLibraryBooks:
                    if book.title == chosenBook:
                        library.add_book(book)
                        nonLibraryBooks.remove(book)
                        break
            else:
                print("No books to add. Try to create a book first")
        #request
        elif action == "request book":
            if len(library.allBooks) > 0:
                book_title = input("Book title: ").strip().lower()
                library.request_book(register_name(name), book_title)
            else:
                print("No book to request")
        #return
        elif action == "return book":
            print("Choose one of the following books to return:")
            for book in library.borrowedBooks.keys():
                print(book.title)
            chosenBook = input("Chosen book: ").strip().lower()
            if chosenBook not in [book.title for book in library.availableBooks.stack] and chosenBook in [book.title for book in library.borrowedBooks.keys()]:
                library.return_book(chosenBook)
            else:
                print("Incorrect book.")
        #cancel
        elif action == "cancel":
            print("Canceling")
            break
    else:
        print("Unknown action")

    # Output
    print("\n-------------------------------------------------------------------------")
    print("Existing books:", [book.title for book in nonLibraryBooks])
    print("All Books:", [title for title in library.allBooks])

    for title in library.allBooks:
        queue = [student.name for student in library.allBooks[title].waitingQueue.queue]
        print(f'"{title}" queue: {queue}')

    print("Available Books:", [book.title for book in library.availableBooks.stack])
    print("Borrowed Books:", [book.title for book in library.borrowedBooks.keys()])
    print("-------------------------------------------------------------------------\n")
