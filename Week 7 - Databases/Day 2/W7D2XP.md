<!-- Exercise 1

1. ‘lea Dupont’ was inserted wrong. Update her first_name to uppercase.
 -->
UPDATE students SET first_name = 'Lea' WHERE first_name = 'lea';

<!-- 2. ‘Lea Dupont’ and ‘Marc Dupont’ are twins, they should have the same birth_date. Update both their birth_date to 02/11/1998 -->

UPDATE students SET birth_date = '1998-11-02' WHERE last_name = 'Dupont';

<!-- 3. Delete the record where “Lea” is the first_name and ‘Dupont’ is the last_name -->

DELETE FROM students WHERE first_name = 'Lea' and last_name = 'Dupont';

<!-- Count -->
<!-- 1. Count how many students are in the table -->

SELECT count(* ) FROM students;

<!-- 2. Count how many students were born after 1/01/2000 -->

SELECT count(* ) FROM students WHERE birth_date > '2000-01-01';

<!-- Insert / Alter -->
<!-- 1. Add a column to the table student, called math_grade -->

ALTER TABLE students
ADD grade integer;

<!-- 2. Add the grade 80 to the student which id is 1 -->

UPDATE students SET grade = 80 WHERE id = 1;

<!-- 3. Add the grade 90 to the students which id are 2 and 4
 -->
UPDATE students SET grade = 90 WHERE id = 1 OR id = 4;

<!-- 4. Add the grade 100 to the student which id is 6
 -->
UPDATE students SET grade = 100 WHERE id = 6;

<!-- 5. Count how many students have a grade bigger than 83
 -->
SELECT count(* ) FROM students WHERE grade > 80;

<!-- 6. Add another student named Omer Simpson with the same birth_date (as the one already in the table). Give him the grade 70
 -->
INSERT INTO students (first_name, last_name, birth_date, grade) VALUES ('Omer', 'Simpson', '1980-10-03', 70);

<!-- 7. Count how many grades have each student (depending on their first and last name). Use an alias called total_grade to fetch the grades. (Omer Simpson should have 2 grades). Hint : use GROUP BY
 -->
SELECT first_name, last_name, count(grade) AS total_grade FROM students GROUP BY first_name, last_name;