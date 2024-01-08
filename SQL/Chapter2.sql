SELECT * FROM product; #모든 행의 모든 열
SELECT product_name, product_company FROM product;  #모든 행의 특정 열
SELECT * FROM product WHERE product_name = '바나나'; #특정 행의 모든 열
SELECT product_name FROM product WHERE product_cost = 1500; #특정 행의 특정 열
