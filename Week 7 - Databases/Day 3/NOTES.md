joining multiple tables...

SELECT first_name, last_name, sum(length) as screentime
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
GROUP BY actor.first_name, actor.last_name
ORDER BY screentime DESC
 

 can save output like this

 create table screen_time as (
SELECT first_name, last_name, sum(length) as screentime
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
GROUP BY actor.first_name, actor.last_name
ORDER BY screentime DESC
 )