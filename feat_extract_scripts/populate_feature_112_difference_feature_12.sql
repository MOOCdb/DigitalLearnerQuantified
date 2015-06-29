-- Takes 8 seconds to execute
-- Created on July 2, 2013
-- @author: Franck for ALFA, MIT lab: franck.dernoncourt@gmail.com
-- Feature 112: difference of Feature 12 (number of problem attempted (feature 6) / number of correct problems (feature 8))
-- 130667 rows
set @current_date = cast('CURRENT_DATE_PLACEHOLDER' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)

SELECT 112,
	features.user_id,
	features2.longitudinal_feature_week,
	-- features.longitudinal_feature_value,
	-- features2.longitudinal_feature_value,
  -- added this to fix divide by zero error
	IFNULL(features2.longitudinal_feature_value  / features.longitudinal_feature_value, 0),
    @current_date
FROM `moocdb`.user_longitudinal_feature_values AS features,
	`moocdb`.user_longitudinal_feature_values AS features2
WHERE
	-- same user
	features.user_id = features2.user_id
	-- 2 successive weeks
	AND features.longitudinal_feature_week = features2.longitudinal_feature_week - 1
	-- we are only interested in feature 5 (average length of forum posts)
	AND features.longitudinal_feature_id = 12
	AND features2.longitudinal_feature_id = 12
    AND features.date_of_extraction >= @current_date
    AND features2.date_of_extraction >= @current_date

-- LIMIT 1000
