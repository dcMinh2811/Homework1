#Basic classes
class Book:
    def __init__(self, title, author, id_number):
        self.title = title
        self.author = author
        self.id_number = id_number
        self.waitingQueue = Queue()
    
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
            self.availableBooks = Stack()
            self.borrowedBooks = []

    def add_book(self, book):
        self.availableBooks.push(book)
        
    def request_book(self, student, book_title):
        for book in self.availableBooks.stack:
            if book.title == book_title:
                self.borrowedBooks.append({book_title: student.name})
                self.availableBooks.pop(book)
            else:
                for book in self.borrowedBooks:
                    for key in book.keys():
                        if key == book_title:
                                Book(key,"","").waitingQueue.push(student)
            
    def return_book(self, book):
        for item in self.borrowedBooks:
            if book.title in item:
                self.availableBooks.push(book)
                self.borrowedBooks.remove(item)
                nextRequest = book.waitingQueue.pop()
                for key, value in nextRequest:
                    self.request_book(Student(value,"",""), key)

        
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


print("Available Books:", [book.title for book in library.availableBooks.stack])

for book in [book1, book2]:
    name = [student.name for student in book.waitingQueue.queue]
    if name:
        print(f"{book.title} queue: {name}")
    else:
        print(f"{book.title} queue: Empty")

print("Borrowed Books:", library.borrowedBooks)