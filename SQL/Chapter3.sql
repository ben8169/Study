#SELECT 문을 배워보자!
USE market_db;
SELECT * FROM member;

SELECT mem_id, mem_name,mem_number FROM member;
SELECT addr 주소 FROM member; -- alias

SELECT height FROM member WHERE mem_name LIKE '__소녀';
SELECT mem_name, height FROM member WHERE height >= (SELECT height FROM member WHERE mem_name LIKE '%구'); -- SUB QUERY

# WHERE + IN('서울','경기') / + BETWEEN A AND B / LIKE '우%' / LIKE '블랙__'

#03-2 SELECT + ORDER BY, LIMIT, DISTINCT
#ORDER BY
SELECT mem_id, mem_name, height FROM member ORDER BY height ASC;
SELECT mem_id, mem_name, height FROM member ORDER BY height DESC;

SELECT mem_name, height, debut_date FROM member WHERE MONTH(debut_date) > 6 ORDER BY MONTH(debut_date) ASC, height ASC; -- 항상 WHERE > ORDER BY 순 / 동일한 경우 두번째 조건으로 정렬

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
    
    