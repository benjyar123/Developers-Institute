1. Fetch the first four students. You have to order the answer by last_name alphabetically(show their first_name and last_name)

SELECT (first_name, last_name) FROM students ORDER BY last_name ASC LIMIT 4;

2. Fetch the birth_date of the youngest student (show his first_name and last_name and birthdate)

SELECT (first_name, last_name, birth_date) FROM students ORDER BY birth_date DESC LIMIT 1;

3. Fetch three students, skipping the first two students.

SELECT (first_name, last_name) FROM students OFFSET 2 LIMIT 3;






