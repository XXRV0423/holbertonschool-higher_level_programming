-- Lists all the cities with their state name using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states_id
ORDER BY cities.id ASC;
