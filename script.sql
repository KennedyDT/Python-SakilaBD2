use sakila;
show tables;

/* Crear un procedimiento almacenado llamado "get_rental_history" que reciba el ID de un cliente
 *  como parámetro y devuelva su historial de alquileres.
*/
create or replace procedure get_rental_history (in customerId INT)
begin 
	select c.first_name , f.title , r.rental_id , r.rental_date
	from customer as c
	join rental as r on c.customer_id = r.customer_id 
	join inventory as i on r.inventory_id  = i.inventory_id 
	join film as f on i.film_id = f.film_id 
	
	where c.customer_id = customerId; 
end

call get_rental_history(3);

/*
Obtener ingresos totales por cliente: Crea un procedimiento almacenado que reciba el ID
de un cliente como parámetro y devuelva el total de ingresos generados por ese 
cliente en alquileres.*/

create or replace procedure get_payment_history (in customerId INT)
begin 
	select c.customer_id  ,c.first_name , sum(p.amount) as payment, count(p.customer_id) as cant_rental
	from customer as c
	join payment as p on c.customer_id = p.customer_id
	
	where c.customer_id = customerId; 
end

call get_payment_history(2);


/*Obtener películas más populares: Crea un procedimiento almacenado que devuelva las películas más
 *  populares basándose en el número de veces que han sido alquiladas.*/

create or replace procedure get_populary_films (in limite int)
begin 
	select f.film_id , f.title ,count(f.film_id) as cant  
	from film as f
	join inventory as i on  f.film_id = i.film_id 
	join rental as r on i.inventory_id = r.inventory_id
	group by f.film_id
	order by cant desc 
	limit limite;

end

call get_populary_films(5);


/*---------------TRIGERS----------------------*/
/*realizar un SP para verificar el stock disponible de una pelicula antes de poder realizar 
 * un alquiler. Para ello pueden utilizar la tabla rental.*/
CREATE OR REPLACE PROCEDURE get_film_available (IN filmID INT)
BEGIN
    SELECT r.rental_id , r.return_date, f.film_id ,count(f.film_id) as available 
	FROM rental as r
	join inventory as i on r.inventory_id = i.inventory_id 
	join film as f on i.film_id = f.film_id 
	where r.return_date is null and f.film_id = filmID
	group by f.film_id;
END

call get_film_available(3);





/*Registro de auditoría de cambios en la tabla "customer": Crea un trigger que se active
antes de actualizar o eliminar un registro en la tabla "customer". El trigger puede insertar
los detalles del registro modificado o eliminado en una tabla de auditoría para realizar un
seguimiento de los cambios realizados en los datos de los clientes.*/

CREATE TABLE customer_audit (
  audit_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  store_id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100),
  address_id INT,
  active BOOLEAN,
  action VARCHAR(10),
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TRIGGER customer_audit_trigger BEFORE UPDATE ON customer
FOR EACH ROW
BEGIN
  IF (OLD.store_id <> NEW.store_id OR
      OLD.first_name <> NEW.first_name OR
      OLD.last_name <> NEW.last_name OR
      OLD.email <> NEW.email OR
      OLD.address_id <> NEW.address_id OR
      OLD.active <> NEW.active) THEN
    INSERT INTO customer_audit (customer_id, store_id, first_name, last_name, email, address_id, active, action)
    VALUES (OLD.customer_id, OLD.store_id, OLD.first_name, OLD.last_name, OLD.email, OLD.address_id, OLD.active, 'UPDATE');
  END IF;
end


UPDATE `customer` SET `first_name`='LOla' WHERE `customer_id`=1;
SELECT * FROM customer_audit

/*Validar la edad del cliente al insertar un nuevo alquiler: Crea un trigger que se active antes
de insertar un registro en la tabla "rental". El trigger puede verificar la edad del cliente
basándose en la fecha de nacimiento proporcionada y asegurarse de que cumpla con los
requisitos de edad para alquilar una película.*/

use sakila;
ALTER TABLE customer
ADD age INT DEFAULT 0;
select c.customer_id, count(*)  from customer c; 
select * from customer c2 where age < 18;
UPDATE customer
SET age = FLOOR(RAND() * 71) + 10;

/*En esta sentencia, multiplicamos el resultado de la función RAND() por 71 (el rango total de
 *  valores entre 0 y 70) y luego sumamos 10 para obtener valores en el rango deseado entre 10 y 80 (ambos inclusive).*/

create or replace procedure get_customer_age (in customerId INT)
begin 
	select c.customer_id  ,c.first_name ,c.last_name , c.age 
	from customer as c
	where c.customer_id = customerId; 
end

call get_customer_age(2);


