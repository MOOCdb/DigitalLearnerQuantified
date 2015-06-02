-- Created on Nov 21, 2013
-- @author: Colin Taylor colin2328@gmail.com
-- Feature 201- number of forum responses per week (also known as CF1)
set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)

SELECT 201,
	users.user_id,
	FLOOR((UNIX_TIMESTAMP(collaborations.collaboration_timestamp)
			- UNIX_TIMESTAMP('2012-03-05 12:00:00')) / (3600 * 24 * 7)) AS week,
	COUNT(*),
    @current_date
FROM `moocdb`.users AS users
INNER JOIN `moocdb`.collaborations AS collaborations
	ON collaborations.user_id = users.user_id
WHERE users.user_dropout_week IS NOT NULL
AND collaborations.collaboration_type_id = 2
GROUP BY users.user_id, week
HAVING week < 15
AND week >= 0
;

