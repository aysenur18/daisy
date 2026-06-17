from datetime import date


class Author:
    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name


class Book:
    def __init__(self, isbn, title, authors):
        self.isbn = isbn
        self.title = title
        self.authors = authors  # List of Author objects
        self.available = True

    def check_availability(self):
        return self.available


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.loans = []

    def borrow_book(self, loan):
        self.loans.append(loan)

    def return_book(self, loan):
        if loan in self.loans:
            self.loans.remove(loan)


class Librarian:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def issue_book(self, book, member, due_date):
        if not book.check_availability():
            print(f"'{book.title}' is not available.")
            return None

        loan = Loan(
            loan_id=id(book),
            book=book,
            member=member,
            issue_date=date.today(),
            due_date=due_date
        )

        book.available = False
        member.borrow_book(loan)

        print(f"Book '{book.title}' issued to {member.name}.")
        return loan

    def receive_book(self, loan):
        loan.return_date = date.today()
        loan.book.available = True
        loan.member.return_book(loan)

        print(f"Book '{loan.book.title}' returned by {loan.member.name}.")


class Loan:
    def __init__(self, loan_id, book, member, issue_date, due_date):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = None

    def calculate_fine(self):
        if self.return_date and self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            return days_late * 1.0  # $1 per day
        return 0.0


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.members = []
        self.librarians = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def register_member(self, member):
        self.members.append(member)

    def add_librarian(self, librarian):
        self.librarians.append(librarian)


# Example Usage
if __name__ == "__main__":
    author = Author(1, "J.K. Rowling")
    book = Book("9780747532743", "Harry Potter", [author])

    member = Member(101, "Alice", "alice@example.com")
    librarian = Librarian(1, "John")

    library = Library("Central Library", "123 Main St")
    library.add_book(book)
    library.register_member(member)
    library.add_librarian(librarian)

    loan = librarian.issue_book(
        book,
        member,
        date(2026, 7, 1)
    )

    if loan:
        librarian.receive_book(loan)
        print("Fine:", loan.calculate_fine())