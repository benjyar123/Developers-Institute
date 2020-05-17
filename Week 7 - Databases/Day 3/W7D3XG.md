Exercise 2 – Happy Halloween
There is a zombie plague approaching! The DVD rental company is offering to lend all of its DVDs to the local shelters, so that the citizens can watch the movies together in the shelters until the zombies are destroyed by the armed forces. Prepare tables of the following data:

1. How many stores there are, and in which city and country they are located.

SELECT count(city) as stores, country, city
FROM city
JOIN country ON city.country_id = country.country_id
JOIN address ON city.city_id = address.city_id
Group by city, country
Order by country, city, count(city)

2. How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.

SELECT store_id, sum(length) as total_minutes
FROM inventory
JOIN film ON inventory.film_id = film.film_id
Group by store_id

3. Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs…)





4. A list of all customers in the cities where the stores are located.
5. A list of all customers in the countries where the stores are located.
6. Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
Hint : use the CHECK contraint
7. For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).




SELECT city, country, store_id
FROM city
JOIN country ON city.country_id = country.country_id
JOIN address ON city.city_id = address.city_id
JOIN store ON address.address_id = store.address_id