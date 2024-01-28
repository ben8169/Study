#07-1 스토어드 프로시저 사용방법
USE market_db;
DROP PROCEDURE IF EXISTS user_proc;
DELIMITER $$
CREATE PROCEDURE user_proc()
BEGIN
	SELECT * FROM member;
END $$
DELIMITER ;

CALL user_proc();
DROP PROCEDURE user_proc;

USE market_db;
DROP PROCEDURE IF EXISTS user_proc1;
DELIMITER $$
CREATE PROCEDURE user_proc1(IN userName VARCHAR(10))
BEGIN
	SELECT * FROM member WHERE mem_name = userName;
END $$
DELIMITER ;

CALL user_proc1('에이핑크')


DROP PROCEDURE IF EXISTS user_proc2;
DELIMITER $$
CREATE PROCEDURE user_proc2(
	IN userNumber INT,
	IN userHeight INT
)
BEGIN
	SELECT * FROM member
		WHERE mem_number > userNumber AND height >  userHeight;
END $$
DELIMITER ;

CALL user_proc2(6,165)


DROP PROCEDURE IF EXISTS user_proc3;
DELIMITER $$
CREATE PROCEDURE user_proc3(
	IN txtValue CHAR(10),
	OUT outValue INT
)
BEGIN
	INSERT INTO noTable VALUES (NULL, txtValue);		-- 아직 없는 noTable을 미리 선언할 수 있음.
	SELECT MAX(id) INTO outValue FROM noTable;
END $$
DELIMITER ;

CREATE TABLE IF NOT EXISTS noTable(
	id INT AUTO_INCREMENT PRIMARY KEY,
    txt CHAR(10)
);

CALL user_proc3('테스트1', @myValue);
SELECT CONCAT('입력된 ID 값=>', @myValue);




DROP PROCEDURE IF EXISTS ifelse_proc;
DELIMITER $$
CREATE PROCEDURE ifelse_proc(
	IN memName VARCHAR(10)
)
BEGIN
	DECLARE debutYear INT;
    SELECT YEAR(debut_date) into debutYear FROM member
		WHERE mem_name = memName;
	IF (debutYear >= 2015) THEN
		SELECT  '신인 가수네요, 화이팅!' AS '메시지';
	ELSE
		SELECT  '고참 가수네요, 수고하셨습니다!' AS '메시지';
	END IF;
END $$
DELIMITER ;

CALL ifelse_proc('오마이걸');
CALL ifelse_proc('블랙핑크');


DROP PROCEDURE IF EXISTS while_proc;
DELIMITER $$
CREATE PROCEDURE while_proc()
BEGIN
	DECLARE hap INT;
    DECLARE num INT;
    SET hap = 0;
    SET num = 1;
    
    WHILE (num <= 100) DO
		SET hap  = hap + num;
        SET num = num + 1;
	END WHILE;
    SELECT hap AS '1~100 합계';
END $$
DELIMITER ;

CALL while_proc();


DROP PROCEDURE IF EXISTS dynamic_proc;
DELIMITER $$
CREATE PROCEDURE dynamic_proc(
	IN tableName VARCHAR(20)
)
BEGIN
	SET @sqlQuery = CONCAT('SELECT * FROM' , tablename);
    PREPARE myQuery FROM @sqlQuery;
    EXECUTE myQuery;
    DEALLOCATE PREPARE myQuery;
END $$
DELIMITER ;
 
CALL dynamic_proc('number');


#07-2 스토어드 함수와 커서
#스토어드 함수
#프로시저와 다르게 SELECT로 호출하며, 함수 내부에 SELECT 사용 불가
SET GLOBAL log_bin_trust_function_creators = 1;

USE market_db;
DROP FUNCTION IF EXISTS sumFunc;
DELIMITER $$
CREATE FUNCTION sumFunc (number1 INT, number2 INT)
	RETURNS INT 	-- 여기는 returns [형식] 
BEGIN
	RETURN number1 + number2;		-- 여기는 return [값]
END $$
DELIMITER ;

SELECT sumFunc(100,200) AS'합계';



DROP FUNCTION IF EXISTS calcYearFunc;
DELIMITER $$
CREATE FUNCTION calcYearFunc(dYear INT)
	RETURNS INT
BEGIN
	DECLARE runYear INT;
    SET runYear = YEAR(CURDATE())  - dYear;
    RETURN runYear;
END $$
DELIMITER ;
SELECT calcYearFunc(2010) AS '활동 햇수';

SELECT calcYearFunc(2007) INTO @debut2007;
SELECT calcYearFunc(2013) INTO @debut2013;
SELECT @debut2007-@debut2013 AS '2007과 2013의 차이';

SELECT mem_id, mem_name, calcYearFunc(YEAR(debut_date)) AS '활동 횟수'
	FROM member;
    
SHOW CREATE FUNCTION calcYearFunc;

#커서
USE member_db;
DROP PROCEDURE IF EXISTS cursor_proc;
DELIMITER $$
CREATE PROCEDURE cursor_proc()	
BEGIN
	DECLARE memNumber INT;
    DECLARE cnt INT DEFAULT 0;
    DECLARE totNumber INT DEFAULT 0;
    DECLARE endOfRow BOOLEAN DEFAULT FALSE;
    
    DECLARE memberCursor CURSOR FOR		-- 1.커서 선언하기
		SELECT mem_number FROM member;
	
    DECLARE CONTINUE HANDLER		-- 2.반복조건 선언하기
		FOR NOT FOUND SET endOfRow = TRUE;
        
	OPEN memberCursor;		-- 3. 커서 열기
    
    cursor_loop: LOOP
		FETCH memberCursor INTO memNumber;		-- 4. 데이터 가져오기 및 데이터 처리하기
        
        IF endOfRow THEN
			LEAVE cursor_loop;
		END IF;
        
        SET cnt = cnt + 1;
        SET totNumber = totNumber + memNumber;
	END LOOP cursor_loop;
    
    SELECT (totnumber / cnt) AS '회원의 평균 인원 수';
    
    CLOSE memberCursor;		-- 5. 커서 닫기
    
END $$
DELIMITER ;

CALL cursor_proc();



#07-3 자동 실행되는 트리거
USE market_db;
CREATE TABLE IF NOT EXISTS trigger_table (id INT, txt VARCHAR(10));
INSERT INTO trigger_table VALUES(1, '레드벨벳');
INSERT INTO trigger_table VALUES(2, '잇지');
INSERT INTO trigger_table VALUES(3, '블랙핑크');

DROP TRIGGER IF EXISTS myTrigger;
DELIMITER $$
CREATE TRIGGER myTrigger
	AFTER DELETE
    ON trigger_table
FOR EACH ROW
BEGIN
	SET @msg = '가수 그룹이 삭제됨' ;
END $$
DELIMITER ;


SELECT * FROM trigger_table;
INSERT INTO trigger_table VALUES (4, '마마무');
SET @msg = ' '; 
UPDATE trigger_table SET txt = '블핑' WHERE id = 3; -- 아무 반응 없다
SELECT @msg;
DELETE FROM trigger_table WHERE id = 2;
SELECT @msg;


USE market_db;
CREATE TABLE singer (SELECT mem_id, mem_name, mem_number, addr FROM member);
CREATE TABLE backup_singer
(	mem_id 			CHAR(8) NOT NULL,
	mem_name 	VARCHAR(10) NOT NULL,
    mem_number INT NOT NULL,
    addr 				 CHAR(2) NOT NULL,
    modType		 CHAR(2),
    modDate 		 DATE,
    modUser		 VARCHAR(30)
);

DROP TRIGGER IF EXISTS singer_updateTrg;
DELIMITER $$
CREATE TRIGGER singer_updateTrg
	AFTER UPDATE
    ON singer
    FOR EACH ROW
BEGIN
	INSERT INTO backup_singer VALUES (OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr , '수정', CURDATE(), current_user() );
END $$
DELIMITER ;

DROP TRIGGER IF EXISTS singer_deleteTrg;
DELIMITER $$
CREATE TRIGGER singer_deleteTrg
	AFTER UPDATE
    ON singer
    FOR EACH ROW
BEGIN
	INSERT INTO backup_singer VALUES (OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr , '삭제', CURDATE(), current_user() );
END $$
DELIMITER ;

UPDATE singer SET addr = '영국' WHERE mem_id = 'BLK';
DELETE FROM singer WHERE mem_number >=7;
SELECT * FROM backup_singer;


TRUNCATE TABLE singer;	 -- == DELETE 아니므로 작동안함
SELECT * FROM backup_singer;


# trigger 사용 시 NEW / OLD 임시 테이블 존재!

