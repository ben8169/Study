#06-1 인덱스

USE market_db;
CREATE TABLE table1 (
	col1 INT PRIMARY KEY,		
	col2 INT UNIQUE,
	col3 INT UNIQUE
);
SHOW INDEX FROM table1;	#Key_name = PRIMARY -> 클러스터형 인덱스!

USE market_db;
DROP TABLE IF EXISTS buy, member;
CREATE TABLE member
(   mem_id 		CHAR(8),
	mem_name	VARCHAR(10),
	mem_number INT,
    addr CHAR(2)
);

INSERT INTO member VALUES('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES('OMY', '오마이걸', 7, '서울');

ALTER TABLE member
	ADD CONSTRAINT
    PRIMARY KEY (mem_id);
SELECT * FROM member;	-- mem_id 기준 정렬


ALTER TABLE member DROP PRIMARY KEY;
ALTER TABLE member
	ADD CONSTRAINT
    PRIMARY KEY (mem_name);
SELECT * FROM member;

#보조 인덱스(책 뒤의 찾아보기를 추가한다고 책의 정렬이 바뀌지는 않는다)
ALTER TABLE member DROP PRIMARY KEY;
ALTER TABLE member
	ADD CONSTRAINT
    UNIQUE (mem_name);
SELECT * FROM member;
SHOW INDEX from member;


INSERT INTO member VALUES('GRL', '소녀시대', 8, '서울');
SELECT * FROM member;

#06-2 인덱스의 내부 작동
# 1page = 16KB
# 페이지 분할에 주의



#06-3 인덱스의 실제사용
#CREATE [UNIQUE] INDEX 인덱스 이름
#  ON  테이블이름 (열 이름) [ASC|DESC]

#DROP INDEX 인덱스 이름 ON 테이블 이름 
USE market_db;
SELECT * FROM member;
SHOW INDEX FROM member;
SHOW TABLE STATUS LIKE 'member';

CREATE INDEX idx_member_addr
	ON member (addr);
ANALYZE TABLE member; -- 생성된 인덱스를 실제로 적용시키는 줄
SHOW INDEX FROM member;
SHOW TABLE STATUS LIKE 'member'; -- Index_length 가 0이다? ANALYZE

CREATE UNIQUE INDEX idx_member_mem_name
	ON member (mem_name);
SHOW INDEX FROM member;

ANALYZE TABLE member; 
SHOW INDEX FROM member;

SELECT * FROM member;
SELECT mem_id, mem_name, addr 
	FROM member
    WHERE mem_name = '에이핑크';	-- 인덱스  써서 조회함
    
CREATE INDEX idx_member_mem_number
	ON member (mem_number);
ANALYZE TABLE member;

SELECT mem_name, mem_number
		FROM member
        WHERE mem_number >= 7; 
        
#인덱스 제거
SHOW INDEX FROM member;
DROP INDEX idx_member_mem_name ON member;
DROP INDEX idx_member_addr On member;
DROP INDEX idx_member_mem_number ON member;
ALTER TABLE member
	DROP PRIMARY KEY; -- mem_id 열을 buy가 참조하고 있어서 삭제 불가
    
SELECT table_name, constraint_name
	FROM information_schema.referential_constraints
    WHERE constraint_schema = 'market_db';
    
    
ALTER TABLE buy
	DROP FOREIGN KEY buy_ibfk_1;
ALTER TABLE member
	DROP PRIMARY KEY;
    


    