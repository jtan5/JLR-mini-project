CREATE DATABASE IF NOT EXISTS cafe_db;
USE cafe_db;


CREATE TABLE IF NOT EXISTS products(
    product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    product_size VARCHAR(20) NULL DEFAULT "N/A",
    product_name VARCHAR(255) NOT NULL,
    unit_price DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    stock INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS couriers(
    courier_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    courier_name VARCHAR(50) NOT NULL,
    courier_phone_number VARCHAR(20) NOT NULL,
    servicing_area VARCHAR(50) NOT NULL,
    `availability` TINYINT NULL
);

CREATE TABLE IF NOT EXISTS customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    customer_name VARCHAR(50) NOT NULL DEFAULT 'Somebody',
    customer_address VARCHAR(20) NULL,
    customer_postcode VARCHAR(20) NULL,
    servicing_area VARCHAR(50) NOT NULL,
    `availability` TINYINT NULL
);

CREATE TABLE IF NOT EXISTS orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    courier_id INT NOT NULL,
    order_status VARCHAR(50) NOT NULL DEFAULT "New",
    customer_id INT NOT NULL,
    new_order TINYINT NOT NULL,
    temp_description INT NULL,
    FOREIGN KEY (courier_id)
        REFERENCES couriers(courier_id)
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id )
        ON UPDATE NO ACTION ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS order_prod(
    `index` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    order_id INT NOT NULL,
    courier_id INT NOT NULL,
    product_id INT NOT NULL,
    product_quantity INT NOT NULL,
    customer_id INT NOT NULL,
    new_order TINYINT NOT NULL,
    temp_description INT NULL,
    FOREIGN KEY (courier_id )
        REFERENCES couriers(courier_id )
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (customer_id )
        REFERENCES customers(customer_id)
        ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (order_id )
        REFERENCES orders(order_id )
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (product_id )
        REFERENCES products(product_id )
        ON UPDATE NO ACTION ON DELETE NO ACTION
);
