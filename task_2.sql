CREATE TABLE IF NOT EXISTS alx_book_store.books (
    ID INT PRIMARY KEY,
    Title VARCHAR(255),
    AuthorID INT,
    Price DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS alx_book_store.authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS alx_book_store.customers (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS alx_book_store.orders (
    ID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE
);

CREATE TABLE IF NOT EXISTS alx_book_store.order_details (
    OrderID INT,
    BookID INT,
    Quantity INT
);
