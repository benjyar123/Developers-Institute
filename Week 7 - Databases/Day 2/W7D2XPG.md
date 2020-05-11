<!-- 1. Get a list of all film languages
 -->
select language_id, count(language_id) from film group by language_id

<!-- 2. Get a list of all films joined with their languages – select only the film title, description, and language name. Try your query with different joins:
 -->
SELECT film.title, film.description, language.name
FROM film
INNER JOIN language
ON film.language_id = language.language_id

<!-- 3. Get all films, even if they don’t have languages
 -->
select title from film;

<!-- 4. Get all languages, even if there are no films in those languages. Which languages are these?
 -->
SELECT name FROM language;

<!-- 5. You are going to babysit your cousin, and you want to find a few movies that he can watch with you. Find out how many films there are for each rating
 -->
SELECT rating, count(rating) FROM film GROUP BY rating

<!-- 6. Get a list of all the movies that have a rating of G or PG-13
 -->
SELECT title, rating FROM film WHERE rating = 'G' or rating = 'PG-13';

<!-- 7. Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
 -->
SELECT title, rating, length, rental_rate 
FROM film 
WHERE (rating = 'G' OR rating = 'PG-13') AND LENGTH < 120 AND rental_rate <3.00 
ORDER BY title ASC;

<!-- 8. Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
Now find the customer’s address, and use UPDATE to change it to an address of your own (or make one up). -->


UPDATE customer SET (first_name, last_name) = ('Benjy', 'Aarons-Richardson') WHERE customer_id = '2';

UPDATE address 
SET (address, address2, district, postal_code) = ('Buckingham Palace', 'Westminster', 'London', 'SW1A 1AA') 
WHERE address_id = '6';