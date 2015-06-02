-- Takes 1 second to execute
-- Created on July 2, 2013
-- @author: Franck for ALFA, MIT lab: franck.dernoncourt@gmail.com
-- Feature 103: difference of number of forum posts
-- 2433 rows
set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)

SELECT 103,
	features.user_id,
	features2.longitudinal_feature_week,
	-- features.longitudinal_feature_value,
	-- features2.longitudinal_feature_value,
	features2.longitudinal_feature_value  / features.longitudinal_feature_value,
    @current_date
FROM `moocdb`.user_longitudinal_feature_values AS features,
	`moocdb`.user_longitudinal_feature_values AS features2

WHERE
	-- same user
	features.user_id = features2.user_id
	-- 2 successive weeks
	AND features.longitudinal_feature_week = features2.longitudinal_feature_week - 1
	-- we need compute the percentage of change if we had at least 5 posts in the previous week
	AND features.longitudinal_feature_value > 5
	-- we are only interested in feature 3 (forum posts)
	AND features.longitudinal_feature_id = 3
	AND features2.longitudinal_feature_id = 3
