CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age 
FROM users;

SELECT * 
FROM users;

SELECT rowid, first_name 
FROM users;

SELECT first_name, age 
FROM users
ORDER BY age ASC;

SELECT first_name, age 
FROM users
ORDER BY age DESC;

SELECT first_name, age, balance 
FROM users
ORDER BY age ASC, balance DESC;

SELECT country FROM users;

SELECT DISTINCT country FROM users;

SELECT DISTINCT country 
FROM users ORDER BY country;

SELECT DISTINCT first_name, country 
FROM users;

SELECT DISTINCT first_name, country 
FROM users ORDER BY country DESC;

SELECT first_name, age, balance FROM users 
WHERE age >= 30;

SELECT first_name, age, balance FROM users 
WHERE age >= 30 AND balance > 500000;

SELECT first_name, last_name FROM users 
WHERE first_name LIKE '%호%';

SELECT first_name FROM users 
WHERE first_name LIKE '%준';

SELECT first_name, phone FROM users 
WHERE phone LIKE '02-%';

SELECT first_name, age FROM users 
WHERE age LIKE '2_';

SELECT first_name, phone FROM users 
WHERE phone LIKE '%-51__-%';

SELECT first_name, country FROM users 
WHERE country IN ('경기도', '강원도');

SELECT first_name, country FROM users 
WHERE country = '경기도' OR country = '강원도';

SELECT first_name, country FROM users 
WHERE country NOT IN ('경기도', '강원도');

SELECT first_name, rowid FROM users 
LIMIT 10;

SELECT first_name, balance FROM users 
ORDER BY balance DESC LIMIT 10;

SELECT first_name, age FROM users
ORDER BY age LIMIT 5;

SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

SELECT country, COUNT(age) FROM users
GROUP BY country;

SELECT last_name, COUNT(*) AS number_of_name 
FROM users GROUP BY last_name;


--CREATE--
CREATE TABLE classmates (
  name TEXT NOT NULL, 
  age INTEGER NOT NULL, 
  address TEXT NOT NULL
);

