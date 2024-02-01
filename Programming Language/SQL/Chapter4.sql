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
		ON member.mem_id = buy.mem_id;
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
	FROM member M
        RIGHT OUTER JOIN buy B
        ON M.mem_id = B.mem_id
	ORDER BY M.mem_id;
    
-- SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
-- 	FROM member M
--         LEFT OUTER JOIN buy B
--         ON M.mem_id = B.mem_id
-- 	ORDER BY M.mem_id;

#  가입만 하고 한번도 구매한 적 없는 회원 목록 추출
# 1 여기서 buy가 왼쪽이 되어야, 구매 내역이 NULL인 친구도 포함해서 전부 나옴.
SELECT M.mem_id, M.mem_name, M.addr, concat(M.phone1,M.phone2) "phone", B.prod_name
	FROM member M
		LEFT JOIN buy B
        ON M.mem_id = B.mem_id
	WHERE B.prod_name IS NULL
    ORDER BY M.mem_id;
    
#2 다음 두 쿼리는 같다.
-- SELECT * 
-- 	FROM A
--     LEFT JOIN B
--     
-- SELECT *
-- 	FROM B
--     RIGHT JOIN A

#3 FULL OUTER JOIN 이란 것이 존재한다.

# 기타 조인
## 상호 조인 (cross join) --ON 사용 불가능, 결과 내용은 의미없고, 주로 대용량 데이터 생성할 때 사용
SELECT *
	FROM buy
		CROSS JOIN member;
    
CREATE TABLE cross_table
	SELECT *
		FROM sakila.actor
			CROSS JOIN world.country;
            
SELECT * FROM cross_table LIMIT 10;

## 자체 조인(self join) -- 여러 col에 같은 데이터
USE market_db;
CREATE TABLE emp_table (emp CHAR(4), manager CHAR(4), phone VARCHAR(8));

INSERT INTO emp_table VALUES('대표', NULL, '0000');
INSERT INTO emp_table VALUES( '영업이사' ,'대표'  ,'1111' );
INSERT INTO emp_table VALUES(  '관리이사', '대표' ,'2222' );
INSERT INTO emp_table VALUES( '정보이사' ,'대표'  , '3333');
INSERT INTO emp_table VALUES( '영업과장' ,'영업이사'  ,'1111-1 ');
INSERT INTO emp_table VALUES( '경리부장' , '관리이사' , '2222-1');
INSERT INTO emp_table VALUES(  '인사부장', '관리이사' , '2222-2');
INSERT INTO emp_table VALUES( '개발팀장' , '정보이사' , '3333-1');
INSERT INTO emp_table VALUES( '개발주임' , '정보이사' , '3333-1-1');


SELECT A.emp "직원",  B.emp "직속상관", B.phone "직속상관연락처"
	FROM emp_table A
		INNER JOIN emp_table B
        ON A.manager = B.emp
	WHERE A.emp = '경리부장';

# 04-3 SQL 프로그래밍
-- DROP PROCEDURE IF EXISTS ifProc1;
-- DELIMITER $$
-- CREATE PROCEDURE ifProc1()
-- BEGIN
-- 	IF 100 = 100 THEN
-- 		SELECT '100은 100과 같습니다'; -- select + 문자열은 print와 비슷한 기능
-- 	END IF;
--     END $$
--     DELIMITER ;
--     CALL ifProc1;
    
    

DROP PROCEDURE IF EXISTS ifProc2();
DELIMITER $$
CREATE PROCEDURE ifProc2()
BEGIN 
	DECLARE myNum INT;
    SET myNum = 200;
    IF myNum = 100 THEN
		SELECT '100입니다';
	ELSE
		SELECT '100이 아닙니다';
	END IF;
END $$
DELIMITER ;
CALL ifProc2();


DROP PROCEDURE IF EXISTS ifProc3();
DELIMITER $$
CREATE PROCEDURE ifProc3()
BEGIN
	DECLARE debutDate DATE;
    DECLARE curDate DATE;
    DECLARE days INT;
    
    SELECT debut_date INTO debutDate
		FROM market_db.member
        WHERE mem_id = 'APN';
        
	SET curDATE = current_date();
    SET days = DATEDIFF(curDATE, debutDate);
    
    IF (days/365) >= 5 THEN
		SELECT CONCAT('데뷔한 지', days, '일이나 지났습니다. 핑순이들 축하합니다!');
	ELSE
		SELECT '데뷔한 지 ' + days + '일밖에 안되엇네요. 핑순이들 화이팅~';
	END IF
END $$
DELIMITER ;
CALL ifProc3();


DROP PROCEDURE IF EXISTS caseProc();
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
	DECLARE point INT;
    DECLARE credit CHAR(1);
    SET point = 88;
    
    CASE 
		WHEN point >= 90 THEN
			SET credit = 'A';
		WHEN point >= 80 THEN
			SET credit = 'B';
		WHEN point >= 70 THEN
			SET credit = 'C';
		WHEN point >= 60 THEN
			SET credit = 'D';
		ELSE
			SET credit = 'F';
	END CASE;
    SELECT CONCAT('취득 점수==>', point), concat('학점==>',credit);
END $$
DELIMITER ;
CALL caseProc();
        
#실전
SELECT mem_id, SUM(price*amount) "총구매액"
	FROM buy
	GROUP BY mem_id
   ORDER BY 총구매액 DESC;
   
SELECT B.mem_id, M.mem_name, SUM(price*amount) "총구매액",
	CASE
		WHEN (SUM(price*amount)>=1500) THEN '최우수고객'
        WHEN (SUM(price*amount)>=1000) THEN '우수고객'
        WHEN (SUM(price*amount)>=1) THEN '일반고객'
        ELSE '유령고객'
	END "회원등급"
	FROM buy B
		RIGHT JOIN member M
        ON B.mem_id = M.mem_id
	GROUP BY M.mem_id  -- 구매 테이블에는 4명만 존재하므로, 더 넓은 M.mem_id 사용해야 함
    ORDER BY 총구매액 DESC;
    

DROP PROCEDURE IF EXISTS whileProc();
DELIMITER $$
CREATE PROCEDURE whileProc()
BEGIN
	DECLARE i INT;
    DECLARE hap INT;
    SET i = 1;
    SET hap = 0;
    
    WHILE (i<=100) DO
		SET hap = hap + i;
        SET i = i + 1;
	END WHILE;
    SELECT '1부터 100까지의 합 ==>' , hap;
END $$
DELIMITER ;
CALL whileProc();


DROP PROCEDURE IF EXISTS whileProc2();
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
	DECLARE i INT;
    DECLARE hap INT;
    SET i = 1;
    SET hap = 0;
    
    myWhile:
    WHILE (i<=100) DO
		IF (i%4 = 0) THEN
			SET i = i+1;
            ITERATE myWhile;
		END IF;
        SET hap = hap + i;
        IF (hap>1000) THEN
			LEAVE myWhile;
		END IF;
        SET i = i+1;
	END WHILE;
    
    SELECT '4의 배수를 제외하고 1부터 100까지의 합, 1000 넘으면 종료 ==>'  + hap;
END $$
DELIMITER ;
CALL whileProc2();



#동적 SQL => PREPARE & EXECUTE & DEALLOCATEq


use market_db;
PREPARE myQuery FROM 'SELECT * FROM member WHERE mem_id = "BLK"';
EXECUTE myQuery;
DEALLOCATE PREPARE myQuery;



DROP TABLE IF EXISTS gate_table;
CREATE TABLE gate_table (id INT AUTO_INCREMENT PRIMARY KEY, entry_time DATETIME);

SET @curDate = current_timestamp();
SET @curDate2= current_timestamp();

PREPARE myQuery FROM 'INSERT INTO gate_table VALUES(NULL, ?)' ;
EXECUTE myQuery USING @curDate;
EXECUTE myQuery USING @curDate2;
DEALLOCATE PREPARE myQuery;

SELECT * FROM gate_table;

