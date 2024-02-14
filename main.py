import streamlit as st

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            st.write("No books available.")
        else:
            for book in books:
                book_info = book.strip().split(',')
                st.write(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self, title, author, release_year, num_pages):
        try:
            release_year = int(release_year)
            num_pages = int(num_pages)
        except ValueError:
            st.error("Release year and number of pages must be integers.")
            return

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        self.file.flush()  # Anlık olarak dosyaya yazma işlemi
        self.file.close()  # Dosyayı kapat
        self.file = open("books.txt", "a+")  # Dosyayı tekrar aç
        st.success("Book added successfully.")

    def remove_book(self, title):
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        for book in books:
            if title not in book:
                updated_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        st.success("Book removed successfully.")

# Creating Library object
lib = Library()

# Streamlit App


st.markdown('<span style="color:#FF594F"><h1>Library Management System 📚</h1></span>', unsafe_allow_html=True)

choice = st.sidebar.selectbox("Select an option:", ["List Books", "Add Book", "Remove Book"])

if choice == "List Books":
    lib.list_books()
elif choice == "Add Book":
    title = st.text_input("Enter book title:")
    author = st.text_input("Enter book author:")
    release_year = st.text_input("Enter first release year:")
    num_pages = st.text_input("Enter number of pages:")
    if st.button("Add Book"):
        lib.add_book(title, author, release_year, num_pages)
elif choice == "Remove Book":
    title = st.text_input("Enter the title of the book to remove:")
    if st.button("Remove Book"):
        lib.remove_book(title)
