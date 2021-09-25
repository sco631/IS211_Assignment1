"""Class with two arguments with blank strings then setting object variables"""
class Book:
     author = ""
     title  = ""
     def __init__(self, titleN, authorN):
         self.title  = titleN
         self.author = authorN

     def display(self):
         print(f"\'{self.title}\', written by {self.author}")
ob1 = Book("Of Mice and Men",  "John Steinbeck")
ob2 = Book("To kill a Mockingbird", "Harper Lee")
"""Prints out objects"""
ob1.display()
ob2.display()













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
