-- CREATE TABLE weniv_product
-- (
--     id   SERIAL PRIMARY KEY,
--     name VARCHAR(30),
--     cost INT         
-- );

-- INSERT INTO weniv_product (id, name, cost) VALUES
-- (1, 'desk', 200000),
-- (2, 'monitor', 500000),
-- (3, 'calender', 30000),
-- (4, 'pen', 1000),
-- (5, 'chair', 50000),
-- (6, 'bookshelf', 70000),
-- (7, 'wristband', 300),
-- (8, 'laptop case', 30000),
-- (9, 'sticker', 2500),
-- (10, 'key ring', 3500);

-- INSERT INTO weniv_product (id, name)
-- VALUES (11, 'mouse');

-- INSERT INTO weniv_product values (12, 'pen', 500);
-- select * from weniv_product;

-- INSERT INTO weniv_product values (13, 'headphones', 80000);
-- select * from weniv_product;

-- INSERT INTO weniv_product values (14, 'clock', 100000);
-- select * from weniv_product;

-- INSERT INTO weniv_product values (15, 'backpack', 45000);
-- select * from weniv_product;

-- INSERT INTO weniv_product VALUES
-- (17, 'note carde', 30000),
-- (18, 'pencil case', 12000),
-- (19, 'USB drive', 20000),
-- (20, 'ruler', 5000);

-- id가 1인 상품, 210000
-- UPDATE weniv_product
-- SET cost=210000
-- where id=1;

-- UPDATE weniv_product
-- SET cost=cost+500
-- where cost<1000;

-- DELETE FROM weniv_product
-- where id=11;

-- DELETE FROM weniv_product;

-- SELECT count(*) from weniv_product
-- where id=11;

