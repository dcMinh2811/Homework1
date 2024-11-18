#Basic classes
class Book:
    def __init__(self, title, author, id_number):
        self.title = title
        self.author = author
        self.id_number = id_number
        self.waitingQueue = Queue()
    
    def get_book(self):
        book_info = (self.title, self.author, self.id_number,self.waitingQueue)
        return book_info

class Student:
    def __init__(self, name, class_number, student_id):
        self.name = name
        self.class_number = class_number
        self.student_id = student_id
    
    def get_student(self):
        student_info = (self.name, self.class_number, self.student_id)
        return student_info

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        if item not in self.stack:
            self.stack.insert(-1, item)

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
            self.allBooks = Stack().stack.copy()
            self.availableBooks = Stack()
            self.borrowedBooks = []

    def add_book(self, book):
        self.availableBooks.push(book)
        self.allBooks = self.availableBooks.stack.copy()
        
    def request_book(self, student, book_title):
        for book in self.allBooks:
            if book.get_book()[0] == book_title:
                if book in self.availableBooks.stack:
                        self.borrowedBooks.append({book_title: student.name})
                        self.availableBooks.pop(book)
                else:
                    book.get_book()[-1].push(student.get_student()[0])
            
    def return_book(self, book):
        for item in self.borrowedBooks:
            if book.get_book()[0] in item:
                self.availableBooks.push(book)
                self.borrowedBooks.remove(item)
                nextRequest = book.get_book()[-1].pop()
                requestedBook = book.get_book()[0]
                self.request_book(Student(nextRequest,"",""), requestedBook)

        
# Create some books
book1 = Book("Doraemon Tập 1", "Fujiko F. Fujio", "B001")
book2 = Book("Harry Potter Tập 1", "J.K. Rowling", "B002")
# Create students
student1 = Student("Minh", "7A", "S001")
student2 = Student("Linh", "7B", "S002")
# Test your library system
library = Library()
library.add_book(book1)
library.add_book(book2)
library.request_book(student1, "Doraemon Tập 1")
library.request_book(student2, "Doraemon Tập 1") # Should go to waiting list
print("All Books:",[book.get_book() for book in library.allBooks][0][0])

for book in library.allBooks:
    title = book.get_book()[0]
    queue = book.get_book()[-1].queue
    print(f'"{title}" queue: {queue}')

print("Available Books:", [book.title for book in library.availableBooks.stack])

print("Borrowed Books:", library.borrowedBooks)