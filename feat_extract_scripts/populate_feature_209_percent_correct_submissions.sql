-- Created on Feb 14, 2014
-- @author: Colin Taylor colin2328@gmail.com
-- Feature 209- Percentage of total submissions that were correct (feature 208 / feature 7)
-- Must have run populate_feature_208 and populate_feature_7 first!

set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)


SELECT 209,
	features.user_id,
	features.longitudinal_feature_week,
	features2.longitudinal_feature_value  / features.longitudinal_feature_value,
    @current_date
FROM `moocdb`.user_longitudinal_feature_values AS features,
	`moocdb`.user_longitudinal_feature_values AS features2
WHERE features.user_id = features2.user_id
	AND features.longitudinal_feature_week = features2.longitudinal_feature_week
	AND features.longitudinal_feature_id = 7
	AND features2.longitudinal_feature_id = 208
;
