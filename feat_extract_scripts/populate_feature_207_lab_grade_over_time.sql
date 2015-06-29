-- Created on Feb 3rd, 2014
-- @author:  Colin Taylor
-- Feature 207: Lab Grade over time: lab grade - avg (lab grade from previos weeks)
-- Meant to be run in order to run after populate_feature_206_pset_grade.sql

DROP PROCEDURE IF EXISTS `moocdb`.Populate_207;
CREATE PROCEDURE `moocdb`.Populate_207()
    BEGIN
        DECLARE x  INT;
        SET x = 1;
        set @current_date = cast('CURRENT_DATE_PLACEHOLDER' as datetime);
        WHILE x  <= 13 DO
            INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)
            SELECT 207, d1.user_id, x AS week, d1.longitudinal_feature_value -
                (SELECT AVG(longitudinal_feature_value)
                FROM `moocdb`.user_longitudinal_feature_values AS d2 WHERE longitudinal_feature_id = 206 AND longitudinal_feature_week < x AND d1.user_id = d2.user_id) AND date_of_extraction >= @current_date,
                @current_date
            FROM `moocdb`.user_longitudinal_feature_values AS d1 WHERE longitudinal_feature_id = 206 AND longitudinal_feature_week = x AND date_of_extraction >= @current_date;
            SET  x = x + 1;
        END WHILE;
    END;

CALL `moocdb`.Populate_207();
