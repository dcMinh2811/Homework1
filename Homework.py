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
            self.borrowedBooks = []

    def add_book(self, book):
        self.availableBooks.push(book)
        self.allBooks[book.title] = book
        
    def request_book(self, student, book_title):
        if book_title in self.allBooks:
            book = self.allBooks[book_title]
            if book in self.availableBooks.stack:
                    self.borrowedBooks.append({book_title: student.name})
                    self.availableBooks.pop(book)
            else:
                book.waitingQueue.push(student.name)
            
    def return_book(self, book):
        for item in self.borrowedBooks:
            if book.title in item:
                self.availableBooks.push(book)
                self.borrowedBooks.remove(item)
                nextRequest = book.waitingQueue.pop()
                requestedBook = book.title
                self.request_book(Student(nextRequest,"",""), requestedBook)



# Interactive system
existingBooks = []
existingStudents = []
library = Library()

while True:
    name = input("What's your name? ").strip().lower()
    print("\n~What do you want to do?\nPick one of those actions: Create book/Add book/Request book/Return book(if you had borrowed it before)/Cancel~")
    action = input("Action: ").strip().lower()

    def action_CreateBook(book):
        Book(book)

    def action_AddBook(book):
        library.add_book(book)

    def action_RequestBook(student, book_title):
        library.request_book(student, book_title)

    def action_ReturnBook(book):
        library.return_book(book)

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
        if action == actions[0]:
            book_title = input("Book title: ").strip().lower()
            book = Book(book_title)
            existingBooks.append(book)
        elif action == actions[1]:
            if len(existingBooks) > 0:
                print("Choose one of the following books to add:")
                for book in existingBooks:
                    print(book.title)
                chosenBook = input("Chosen book: ").strip().lower()
                for book in existingBooks:
                    if book.title == chosenBook:
                        library.add_book(book)
                        break
                else:
                    print("Book not found")
            else:
                print("No books to add. Try to create a book first")
        elif action == actions[2]:
            book_title = input("Book title: ").strip().lower()
            library.request_book(register_name(name), book_title)
        elif action == actions[3]:
            if len(library.allBooks) > 0:
                print("Choose one of the following books to return:")
                for book in library.allBooks.values():
                    print(book.title)
                chosenBook = input("Chosen book: ").strip().lower()
                if chosenBook in library.allBooks:
                    library.return_book(library.allBooks[chosenBook])
                else:
                    print("Book not found")
            else:
                print("No books in the library")
        else:
            print("Canceling")
            break
    else:
        print("Unknown action")

    # Output
    print("Existing books:", [book.title for book in existingBooks])
    print("All Books:", [title for title in library.allBooks])

    for title in library.allBooks:
        queue = library.allBooks[title].waitingQueue.queue
        print(f'"{title}" queue: {queue}')

    print("Available Books:", [book.title for book in library.availableBooks.stack])
    print("Borrowed Books:", library.borrowedBooks)
