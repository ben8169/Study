### 04-1 데이터 형식
USE market_db;
CREATE TABLE hongong4(
	tinyint_col TINYINT,
    smallint_col SMALLINT,
    int_col INT,
    bigint_col BIGINT);
    
    INSERT INTO hongong4 VALUES(127,32767, 2147483647,9*10^18);
	INSERT INTO hongong4 VALUES(127,32767, 2147483647,9*10^20);
    
    # TEXT, BLOB
    CREATE TABLE netflix_db;
    USE netflix_db;
    CREATE TABLE movie
		(movie_id INT,
        movie_title VARCHAR(30),
        movie_director VARCHAR(20),
        movie_star VARCHAR(20),
        movie_script LONGTEXT,
        movie_film LONGBLOB
        )
        

# 변수의 사용
USE market_db;
SET @myVar1 = 5;
SET @myVar2 = 4.25;

SELECT @myVar1;
SELECT @myVar1 + @myVar2;

SET @txt = '가수 이름 ==>';
SET @height = 166;
SELECT @txt, mem_name FROM member WHERE height > @height;

#PREPARE, EXECUTE
SET @count = 3;
# SELECT mem_name, height FROM member ORDER BY height LIMIT @count  -- 작동 안됨 
PREPARE mySQL FROM 'SELECT mem_name, height FROM member ORDER BY height LIMIT ?'; -- >?는 ellipsis 같은 너낌 
EXECUTE mySQL USING @count; -- USING으로 ?에 count 대입하는 것.

# 형 변환
##explicit conversion -> CAST, CONVERT
SELECT AVG(price) "평균 가격" FROM buy;
SELECT CAST(AVG(price) AS SIGNED) "평균 가격" FROM buy; -- 그냥 SIGNED == SIGNED INTEGER / 그냥  UNSIGNED == UNSIGNED INTEGER
SELECT CONVERT (AVG(price), SIGNED) "평균 가격" FROM buy;

SELECT CAST('2024$1$21' AS DATE);
SELECT CONVERT ('2024,3^4', DATE);

SELECT num, CONCAT(CAST(price AS CHAR), 'x', CAST(amount AS CHAR), '=' ) "가격X수량", price*amount "구매액"
	FROM buy;
    
## implicit conversion
SELECT '100'+'200';
SELECT concat('100','200');



### 04-2 조인
# 내부 조인(기본) -> 두 테이블에 모두 있는 내용 조인
USE market_db;
SELECT  *
	FROM buy
		INNER JOIN member
		ON buy.mem_id = member.mem_id
    WHERE buy.mem_id = 'GRL'; 			-- 1.GRL을 buy에서 조회  2. member에서 동일한 아이디 검색 3. 두 행을 결합
    

SELECT buy.mem_id, member.mem_name, buy.prod_name, member.addr, CONCAT(member.phone1, member.phone2) '연락처'
	FROM buy
		INNER JOIN member
        ON buy.mem_id = member.mem_id;
        
SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, CONCAT(M.phone1, M.phone2) '연락처'
	FROM buy B
		INNER JOIN member AS M
        ON B.mem_id = M.mem_id;

#응용--> 한번이라도 구매한 분들께 감사편지 보내기!
SELECT DISTINCT(M.mem_id), M.mem_name, M.addr
	FROM buy B
		JOIN member  M
        ON M.mem_id = B.mem_id
	ORDER BY M.mem_id;
        
# 외부 조인 -> 한곳이라도 있으면 조인할때
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
	FROM buy B
		INNER JOIN member M
        ON B.mem_id = M.mem_id
	ORDER BY M.mem_id;
    
    