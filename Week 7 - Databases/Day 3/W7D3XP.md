<!-- Exercise 1 -->

<!-- 1. Last time we discovered that the films in the database were all in English. Use UPDATE to change a few of them to another language. Make sure that you use valid languages… -->


UPDATE film SET language_id = 2 WHERE film_id IN (1, 2, 3, 4, 5);

UPDATE film SET language_id = 3 WHERE film_id IN (11, 12, 13, 14, 15);

<!-- 2. Use your new knowledge to add 3 new customers to the database. -->

INSERT INTO customer (store_id, first_name, last_name, email, address_id)
VALUES (1, 'Harry', 'Potter', 'wizard@hogwarts.com', 10)

INSERT INTO customer (store_id, first_name, last_name, email, address_id)
VALUES (1, 'Testy', 'McTestFace', 'testy@mctestface.com', 67)

INSERT INTO customer (store_id, first_name, last_name, email, address_id)
VALUES (1, 'Mickey', 'Mouse', 'mouse@disney.com', 2)

<!-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table? -->

address_id must already exist in address table
if that id is already being used by a different customer the new customer will now be assigned their address

<!-- 3. Add 3 new films to the database, using INSERT. Do you need to do any steps in preparation? -->

INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating)
VALUES ('Blues Brothers', 'A musical comedy', 1980, 1, 7, 5, 133, 15, 'PG')

INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating)
VALUES ('Raiders of the Lost Ark', 'An epic adventure film', 1981, 1, 5, 3, 115, 10, 'PG')

INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating)
VALUES ('Back to the Future', 'A time travel adventure film', 1985, 1, 5, 3, 116, 10, 'PG')

Not sure what preparation was needed didn't get that...

<!-- 4. Last time we created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
 -->
It just went when I clicked delete

<!-- 5. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he is talking about?

1) The film is about a sumo wrestler, and one of the actors is Penelope Monroe. -->

SELECT title, description, first_name, last_name as film_search
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE last_name LIKE 'Monroe' 
AND first_name LIKE 'Penelope' 
AND description LIKE '%Sumo%' 

Answer: Park Citizen

<!-- 2) A short documentary (less than 1 hour long), rated ‘R’. -->

SELECT title, length, rating, name as film_search
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE rating = 'R' 
AND length < 60
AND name = 'Documentary'

Answer: Cupboard Sinners

<!-- 3) A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005. -->

SELECT title, first_name, last_name, amount, return_date as film_search
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film on inventory.film_id = film.film_id
WHERE amount > 4.00
AND last_name = 'Mahan'
AND return_date < '2005-08-01'
AND return_date > '2005-07-28'

Answer: Sugar Wonka

<!-- 4) His friend Matthew Mahan watched this film, too. It had the word ‘boat’ in the title or description, and it looked like it was a very expensive DVD to replace. -->

SELECT title, description, first_name, last_name, replacement_cost as film_search
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film on inventory.film_id = film.film_id
WHERE last_name = 'Mahan'
AND replacement_cost > 15
AND description LIKE '%Boat%'

Answer: Might be Money Harold (19.99) or Stone Fire (17.99)

<!-- 6. Get a list of all the Action films that Joe Swank has acted in
Before you start, could there be a shortcut to getting this information? Maybe a view? -->

SELECT title, name, first_name, last_name as film_search
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE last_name = 'Swank'
AND first_name = 'Joe'
AND name = 'Action'


<!-- 7. Use one of the customers that you created in step 2 above to ‘rent’ 3 movies.
8. ‘Return’ 2 of the 3 movies from the previous step. -->