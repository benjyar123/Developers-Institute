<!-- Exercise 1 -->

<!-- 1. Create a new table called customer_review, to contain data about film reviews that customers will make. It should have the following columns:
review_id – a primary key, non null, auto-increment
film_id – references the film table. The film that is being reviewed.
language_id – references the language table. What language the review is in.
title – the title of the review
score – the rating of the review (1-10)
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated. -->

CREATE TABLE public.customer_review
(
    review_id integer NOT NULL DEFAULT nextval('customer_review_review_id_seq'::regclass),
    film_id integer,
    language_id integer,
    title character varying COLLATE pg_catalog."default",
    score integer,
    review_text character varying COLLATE pg_catalog."default",
    last_update time without time zone,
    CONSTRAINT customer_review_pkey PRIMARY KEY (review_id)
)

<!-- 
2. Add 3 movie reviews. Make sure you link them to valid objects in the other tables. -->

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES ('133', '1', 'Chamber Italian', '8', 'Fantastic film. Bit long. Not sure why it is in English.', 'NOW()')

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES ('384', '1', 'Gross Wonderful', '9', 'Probably the best film you will see this afternoon', 'NOW()')

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES ('8', '1', 'Airport Pollock', '3', 'Terrible. What a load of Pollocks.', 'NOW()')

<!-- 3. Use SQL to delete 2 of the reviews by ID.
Exercise 2 -->

DELETE FROM customer_review WHERE review_id > 1

<!-- Exercise 2 -->
<!-- 1. Find out how many rentals are still outstanding. (ie. have not been returned to the store yet) -->

SELECT count(* ) FROM rental WHERE return_date IS null

<!-- 2. Mark the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
 -->
SELECT payment.rental_id, payment.amount, rental.return_date
FROM payment
INNER JOIN rental
ON payment.rental_id = rental.rental_id
WHERE rental.return_date IS null
ORDER BY payment.amount DESC
LIMIT 30

