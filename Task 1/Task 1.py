# TASK 1.2
# Record structure declaration
class Book:
    def __init__(self, id, title, author, year):
        self.__id = id  # store unique ID
        self.__title = title  # store title of the book
        self.__author = author  # store main author of the book
        self.__year = year  # store year of publication

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year


books_arr = []  # create an array to store the records about the books
# input data for 10 books from the user
for i in range(10):
    book_id = int(input("Enter the book's ID: "))
    while book_id < 100 or book_id > 999:
        print("Code needs to between 100 and 999.")
        book_id = int(input("Enter the book's ID: "))
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year = int(input("Enter the year of publication: "))
    book = Book(book_id, title, author, year)
    books_arr.append(book)  # store each book as a separate record in the array

# Output the data in each record with an appropriate message
for i in range(10):
    print("Book ID: " + str(books_arr[i].get_id()))
    print("Title: " + books_arr[i].get_title())
    print("Main author: " + books_arr[i].get_author())
    print("Year of publication: " + str(books_arr[i].get_year()) + "\n")

# TASK 1.3

# Store the records in a serial file
import pickle

fh = open("Task 1 serial.bin", "wb")
for i in range(10):
    pickle.dump(books_arr[i], fh)
fh.close()

# TASK 1.4
# Read records
import pickle

fh = open("Task 1 serial.bin", "rb")
new_books_arr = []  # store books from file
while True:
    new_books_arr.append(pickle.load(fh))
fh.close()

# Output records with appropriate message
for i in range(10):
    print("Book ID: " + str(books_arr[i].get_id()))
    print("Title: " + books_arr[i].get_title())
    print("Main author: " + books_arr[i].get_author())
    print("Year of publication: " + str(books_arr[i].get_year()) + "\n")


# TASK 1.5
# Hashing algorithm
def hash_code(code):
    # hash_val = int(str(code ** 5)[2:5]) + (code * 3 + 109) % 5
    # exp = code ** 5
    # sli_1 = 0  # int(str(exp)[2:5])
    hash_val = code * 2  # + len(str(code)) % 3
    # hash_val = sli_1 + sli_2
    return hash_val * 100
