# Write your MySQL query statement below

-- select Person.firstName, Person.lastName, Address.city, Address.state from Person, Address where Person.id = Address.id;

select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;