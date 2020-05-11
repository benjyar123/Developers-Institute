SELECT * FROM actor WHERE first_name IN ('David', 'Morgan', 'Will')

select last_name, count(first_name) as c from actor where last_name like 'A%' group by last_name having count(last_name) > 2
