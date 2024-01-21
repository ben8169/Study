#SELECT 문을 배워보자!
USE market_db;
SELECT * FROM member;

SELECT mem_id, mem_name,mem_number FROM member;
SELECT addr "주소" FROM member; -- alias

SELECT height FROM member WHERE mem_name LIKE '__소녀';
SELECT mem_name, height FROM member WHERE height >= (SELECT height FROM member WHERE mem_name LIKE '%구'); -- SUB QUERY

# WHERE + IN('서울','경기') / + BETWEEN A AND B / LIKE '우%' / LIKE '블랙__'

# ========================================================================================================================================================================================#
#03-2 SELECT + ORDER BY, LIMIT, DISTINCT
#ORDER BY
SELECT mem_id, mem_name, height FROM member ORDER BY height ASC;
SELECT mem_id, mem_name, height FROM member ORDER BY height DESC;

SELECT mem_name, height, debut_date FROM member WHERE MONTH(debut_date) > 6 ORDER BY MONTH(debut_date) ASC, height DESC; -- 항상 WHERE > ORDER BY 순 / 동일한 경우 두번째 조건으로 정렬

#LIMIT
SELECT * FROM member;
SELECT * FROM member LIMIT 0, 3;

#DISTINCT
SELECT addr FROM member ORDER BY addr;
SELECT DISTINCT addr FROM member;

#GROUP BY
SELECT * FROM buy; 
SELECT mem_id, amount FROM buy ORDER BY mem_id, amount;

##집계 함수
##SUM
SELECT SUM(amount*price) "총 매출" FROM buy;
SELECT mem_id "회원 아이디", SUM(amount) "총 구매 개수" FROM buy GROUP BY mem_id; -- 관습상 alias -> "" / INSERT -> ''
SELECT mem_id "회원 아이디", SUM(amount*price) "총 구매 금액" FROM buy GROUP BY mem_id;

##AVG
SELECT AVG(amount) "인당 평균 구매 개수"  FROM buy;
SELECT mem_id "회원 아이디", AVG(amount) "평균 구매 개수"  FROM buy GROUP BY mem_id;

##COUNT
SELECT * FROM member;
SELECT COUNT(*) FROM member;
SELECT COUNT(phone1) "연락처가 있는 회원" FROM member;

##HAVING
SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액" 
	FROM buy
	GROUP BY mem_id -- SUM만 쓴 상태
    HAVING SUM(price*amount) > 1000 -- WHERE 대신 집계함수와 쓸 수 있는 조건절 / GROUP BY > HAVING 순
    ORDER BY SUM(price*amount);
    
# ========================================================================================================================================================================================#
#03-3 데이터 변경 -> INSERT, UPDATE, DELETE
CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);
INSERT INTO hongong1 VALUES(1, '우디', 25);
INSERT INTO hongong1(toy_id,toy_name) VALUES(2,'버즈');
INSERT INTO hongong1(toy_name, age, toy_id) VALUES ('제시', 20, 3);

CREATE TABLE hongong2 (
	toy_id INT AUTO_INCREMENT primary key,  -- AUTO_INCREMENT 하는 열은 무조건 PK설정!!
    toy_name CHAR(4),
    age INT);

INSERT INTO hongong2 VALUES(NULL, '보핍', 25);
INSERT INTO hongong2 VALUES(NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES(NULL, '렉스', 21);
SELECT * FROM hongong2;

ALTER TABLE hongong2 AUTO_INCREMENT=100;
INSERT INTO hongong2 VALUES (NULL, '재남', 35);
SELECT * FROM hongong2;

CREATE TABLE hongong3(
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
	toy_name CHAR(4) NOT NULL,
    age INT);
ALTER TABLE hongong3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;
SELECT * FROM hongong3;

SHOW GLOBAL variables;

INSERT INTO hongong3 VALUES (NULL, '토마스', 20), (NULL, '제임스', 23), (NULL, '고든', 25);
SELECT * FROM hongong3;

# INSERT INTO ~ SELECT
SELECT COUNT(*) FROM world.city;
DESC world.city; -- Describe
SELECT * FROM world.city LIMIT 0, 5;

CREATE TABLE city_popul (city_name CHAR(35), population INT);
INSERT INTO city_popul SELECT Name, Population FROM world.city;

#UPDATE
USE market_db;
UPDATE city_popul
	SET city_name = '서울'
	WHERE city_name = 'Seoul';
SELECT * FROM city_popul WHERE city_name LIKE '서_';

UPDATE city_popul
	SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
SELECT * FROM city_popul WHERE city_name in ('뉴욕');

UPDATE city_popul
	SET population = population / 10000;
SELECT * FROM city_popul LIMIT 20;


#DELETE
DELETE FROM city_popul
	WHERE city_name LIKE 'New%'
    LIMIT 5;
    
#대용량 테이블 삭제
CREATE TABLE big_table1 (SELECT * FROM world.city, sakila.country);
CREATE TABLE big_table2 (SELECT * FROM world.city, sakila.country);
CREATE TABLE big_table3 (SELECT * FROM world.city, sakila.country);
SELECT COUNT(*) FROM big_table1;

DELETE FROM big_table1;
DROP TABLE big_table2;
TRUNCATE TABLE big_table3;