
-- Let's create a table to store informaitn about parts.

CREATE TABLE car_parts (
    part_id INT PRIMARY KEY,
    part_name VARCHAR(50), 
    supplier VARCHAR(50),
    quantity_in_stock INT,
    price_usd DECIMAL(10, 2)
);

-- Insert a few rows into the car_parts table.

INSERT INTO car_parts (part_id, part_name, supplier, quantity_in_stock, price_usd) 
VALUES
    (1, 'Brake Rotor', 'BrakeCo', 500, 75.50),
    (2, 'Oil Filter', 'FilterTech', 1200, 15.25),
    (3, 'Spark Plug', 'PowerSpark', 800, 5.00);


-- Retrieve all data from the car_parts table.

SELECT * 
FROM car_parts;

