1. Add the following new items to the public.items table:
Small Desk – 100
Large desk – 300
Fan – 80

INSERT INTO items (id, item, price) VALUES (1, 'Small Desk', 100);
INSERT INTO items (id, item, price) VALUES (1, 'Large Desk', 300);
INSERT INTO items (id, item, price) VALUES (1, 'Fan', 80);

2. Add 5 new customers to the public.customers table:

Greg Jones
Sandra Jones
Scott Scott
Trevor Green
Melanie Johnson

INSERT INTO customers (id, first_name, last_name) VALUES (1, 'Greg', 'Jones');
INSERT INTO customers (id, first_name, last_name) VALUES (2, 'Sandra ', 'Jones');
INSERT INTO customers (id, first_name, last_name) VALUES (3, 'Scott ', 'Scott ');
INSERT INTO customers (id, first_name, last_name) VALUES (4, 'Trevor ', 'Green');
INSERT INTO customers (id, first_name, last_name) VALUES (5, 'Melanie ', 'Johnson');

3. Use SQL to get the following data from the database:

All the items
All the items with a price above 80
All the items with a price below 30
All the customers with the last name ‘Smith’
All the customers with a first name that is not ‘Craig’

SELECT * FROM items;
SELECT * FROM items WHERE price > 80;
SELECT * FROM items WHERE price < 30;
SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE NOT first_name = 'Craig';