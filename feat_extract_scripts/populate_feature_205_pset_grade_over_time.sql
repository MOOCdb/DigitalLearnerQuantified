-- Created on Feb 3rd, 2014
-- @author:  Colin Taylor
-- Feature 205: Pset Grade over time: pset grade - avg (pset grade from previos weeks)
-- Meant to be run in order to run after populate_feature_204_pset_grade.sql

DROP PROCEDURE IF EXISTS Populate_205;
CREATE PROCEDURE Populate_205()
BEGIN
    DECLARE x  INT;
    SET x = 1;
    SET @current_date = CAST('0000-00-00 00:00:00' AS DATETIME);
    WHILE x  <= 13 DO
        INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)
        SELECT 205, d1.user_id, x AS week, d1.longitudinal_feature_value -
            (SELECT AVG(longitudinal_feature_value)
            FROM `moocdb`.user_longitudinal_feature_values AS d2 WHERE longitudinal_feature_id = 204 AND longitudinal_feature_week < x AND d1.user_id = d2.user_id),
            @current_date
        FROM `moocdb`.user_longitudinal_feature_values AS d1 WHERE longitudinal_feature_id = 204 AND longitudinal_feature_week = x;
        SET  x = x + 1;
    END WHILE;
END;

CALL Populate_205();
