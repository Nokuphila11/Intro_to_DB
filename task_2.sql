USE alx_book_store;

CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(100),
  author_id INT,
  price DECIMAL(10,2)
);

CREATE TABLE authors (
  author_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE
);

CREATE TABLE order_details (
  order_detail_id INT PRIMARY KEY,
  order_id INT,
  book_id INT,
  quantity INT
);
