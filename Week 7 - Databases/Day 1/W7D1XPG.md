1. Insert in the table : your last_name, first_name and birth_date

INSERT INTO students (last_name, first_name, birth_date) VALUES ('Aarons-Richardson', 'Benjy', '1985-12-02');


2. Insert in the table, two more students. Be careful, you have to add them at the same time (with one request).

INSERT INTO students (last_name, first_name, birth_date)
	VALUES 
	('Mouse', 'Mickey', '1928-11-18'),
	('Man', 'Bat', '1939-05-01');

1. Fetch all the data from the table

SELECT * FROM students;

2. Fetch all the students first_name and last_name

SELECT (first_name, last_name) FROM students;

3. Fetch only the student where the id is equal to 2 (show his first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE id = 2;

4. Fetch only the student where the last_name is equal to Dupont AND the first_name is equal to Marc (show his first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE last_name = 'Dupont' AND first_name = 'Marc';

5. Fetch only the students where the last_name is equal to Dupont OR the first_name is equal to Marc. (show their first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE last_name = 'Dupont' OR first_name = 'Marc';

6. Fetch the students which first_name contains the letter a. (show their first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE first_name LIKE '%a%';

7. Fetch the students which first_name starts with the letter a. (show their first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE first_name ILIKE 'a%';

8. Fetch the students which first_name ends with the letter a. (show their first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE first_name LIKE '%a';

9. Fetch the students where the second to last letter of the first name is a (Example: Leah). (show their first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE first_name LIKE '%a_';

10. Fetch the students which the id are 1 AND 3. (show their first_name and last_name)

SELECT (first_name, last_name) FROM students WHERE id = 1 OR id = 3;

11. Fetch the students, which birth_date is equal or after the 1/01/2000. (show their first_name and last_name and birthdate)

SELECT (first_name, last_name, birth_date) FROM students WHERE birth_date > '2000-01-01';

