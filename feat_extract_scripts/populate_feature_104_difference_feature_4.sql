-- Takes 1 seconds to execute
-- Created on July 2, 2013
-- @author: Franck for ALFA, MIT lab: franck.dernoncourt@gmail.com
-- Feature 104: difference of number of wiki edits
-- 85 rows
set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)

SELECT 104,
	features.user_id,
	features2.longitudinal_feature_week,
	-- features.longitudinal_feature_value,
	-- features2.longitudinal_feature_value,
  -- added this to fix divide by zero error
	IFNULL(features2.longitudinal_feature_value  / features.longitudinal_feature_value,0),
    @current_date
FROM `moocdb`.user_longitudinal_feature_values AS features,
	`moocdb`.user_longitudinal_feature_values AS features2

WHERE
	-- same user
	features.user_id = features2.user_id
	-- 2 successive weeks
	AND features.longitudinal_feature_week = features2.longitudinal_feature_week - 1
	-- we need compute the percentage of change if we had at least 5 wiki edits in the previous week
	AND features.longitudinal_feature_value > 5
	-- we are only interested in feature 4 (wiki edits)
	AND features.longitudinal_feature_id = 4
	AND features2.longitudinal_feature_id = 4
    AND features.date_of_extraction >= @current_date
    AND features2.date_of_extraction >= @current_date

-- LIMIT 1000
