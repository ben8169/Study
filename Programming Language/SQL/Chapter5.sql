CREATE DATABASE naver_db;

INSERT INTO buy VALUES( NULL, 'BLK', '지갑', NULL, 30, 2);
INSERT INTO buy VALUES( NULL, 'BLK', '맥북프로', '디지털', 1000, 1);

#05-2 제약조건
USE naver_db;
DROP TABLE IF EXISTS buy, member;
CREATE TABLE member
(	mem_id CHAR(8) NOT NULL PRIMARY KEY,
	mem_name VARCHAR(10) NOT NULL,
    height TINYINT UNSIGNED NULL
    -- CONSTRAINT PRIMARY KEY 기본키이름정하기 (mem_id)
);

DESCRIBE member;

ALTER TABLE member
	ADD CONSTRAINT
    PRIMARY KEY (mem_id);

CREATE TABLE buy
(	num INT AUTO_INCREMENT  NOT NULL PRIMARY KEY,
	mem_id CHAR(8) NOT NULL,
	prod_name CHAR(6)  NOT NULL,
    FOREIGN KEY (mem_id) REFERENCES member(mem_id)
);

ALTER TABLE buy
	ADD CONSTRAINT
    FOREIGN KEY (mem_id)
		REFERENCES member(mem_id);
        
        
#기준 테이블의 열이 변경되는 경우
INSERT INTO member VALUES('BLK', '블랙핑크', 163);
INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
INSERT INTO buy VALUES(NULL, 'BLK', '맥북');

SELECT M.mem_id, M.mem_name, B.prod_name
	FROM buy B
		JOIN member M
        ON B.mem_id = M.mem_id;
        
#PK-FK 관계에서는 기준 테이블의 이름 변경, 삭제 불가능
-- UPDATE member SET mem_id = 'PINK' WHERE mem_id='BLK';
-- DELETE FROM member WHERE mem_id = 'BLK'; 

#이를 대체하기 위한 CASCADE
DROP TABLE IF EXISTS buy;
CREATE TABLE buy
(	num 						INT AUTO_INCREMENT  NOT NULL PRIMARY KEY,
	mem_id 					CHAR(8) NOT NULL,
	prod_name 			CHAR(6)  NOT NULL
);

ALTER TABLE buy
	ADD CONSTRAINT
	FOREIGN KEY (mem_id) REFERENCES member(mem_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE;
    
    
INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
INSERT INTO buy VALUES(NULL, 'BLK', '맥북');

UPDATE member SET mem_id = 'PINK' WHERE mem_id = 'BLK';

SELECT M.mem_id, M.mem_name, B.prod_name
	FROM buy B
		JOIN member M
        ON B.mem_id = M.mem_id;
        
DELETE FROM member WHERE mem_id='PINK';
SELECT * FROM buy;

# UNIQUE
-- CREATE TABLE ...
-- (...
-- 	email CHAR(30) NULL UNIQUE
-- )

# CHECK - > 데이터를 점검하는 기능
DROP TABLE IF EXISTS member, buy;
CREATE TABLE member
(	mem_id CHAR(8) NOT NULL PRIMARY KEY,
	mem_name VARCHAR(10) NOT NULL,
    height TINYINT UNSIGNED NULL CHECK (height >= 100),
    phone1 CHAR(3) NULL
);

INSERT INTO member VALUES ('BLK', '블랙핑크', 163, NULL);
INSERT INTO member VALUES ('TWC', '트와이스', 99, NULL);

ALTER TABLE member
	ADD CONSTRAINT
    CHECK (phone1 IN ('02', '031', '032', '054', '055', '061'));

INSERT INTO member VALUES ('TWC', '트와이스', 167, '02');
INSERT INTO member VALUES ('BLK', '블랙핑크', 163, '010');


#default
DROP TABLE IF EXISTS member, buy;
CREATE TABLE member
(	mem_id CHAR(8) NOT NULL PRIMARY KEY,
	mem_name VARCHAR(10) NOT NULL,
    height TINYINT UNSIGNED NULL DEFAULT 160,
    phone1 CHAR(3) NULL
);

ALTER TABLE member
	ALTER COLUMN phone1 SET DEFAULT '02'
    
    
INSERT INTO member VALUES('SPC','우주소녀', default, default);
SELECT * FROM member;


# 05-3 VIEW
# 1. 보안에 도움이 된다.
# 2. 복잡한 sql을 단순하게 저장해 놓고 쓸 수 있다.
USE market_db;
CREATE VIEW v_viewtest1
AS 
	SELECT B.mem_id AS "Member ID", M.mem_name AS "Member Name" , B.prod_name AS "Product Name", CONCAT (M.phone1, M.phone2) AS "Office Phone"
    FROM buy B
		JOIN member M
        ON B.mem_id = M.mem_id;
SELECT DISTINCT `Member ID`, `Member Name` FROM v_viewtest1; -- 백틱을 사용

DROP VIEW v_viewtest1;

#뷰의 정보 확인
USE market_db;
CREATE OR REPLACE VIEW v_viewtest2
AS
	SELECT mem_id, mem_name, addr FROM member;

DESCRIBE member;
DESC v_viewtest2;


SHOW CREATE TABLE buy;
SHOW CREATE VIEW v_viewtest2;

#뷰를 통한 데이터 수정/삭제
UPDATE v_member SET addr = '부산' WHERE mem_id='BLK';
INSERT INTO v_member(mem_id, mem_name, addr) VALUES('BTS', '방탄소년단', '경기');

CREATE VIEW v_height167
AS 
	SELECT * FROM member WHERE height >= 167;
    
SELECT * FROM v_height167;
DELETE FROM v_height167 WHERE height < 167; -- 의미x
INSERT INTO v_height167 VALUES('TRA', '티아라',6,'서울',NULL,NULL,159,'2005-01-01'); -- 의미 XA
#WITH CHECK OPTION -> 뷰에 설정된 값의 범위가 벗어나는 값이 입력되지 않도록 함
ALTER VIEW v_height167
AS
	SELECT * FROM member WHERE height >= 167
		WITH CHECK OPTION ;
INSERT INTO v_height167(height) VALUES(160);

CHECK TABLE v_height167;




