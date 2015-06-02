-- Takes 300 seconds to execute
-- Created on August 23, 2013
-- @author: Franck for ALFA, MIT lab: franck.dernoncourt@gmail.com
-- Feature 17: Total time spent on all resources - book only - during the week

set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)


SELECT 17,
	users.user_id,
	FLOOR((UNIX_TIMESTAMP(observed_events.observed_event_timestamp)
			- UNIX_TIMESTAMP('2012-03-05 12:00:00')) / (3600 * 24 * 7)) AS week,
	SUM(observed_events.observed_event_duration),
    @current_date
FROM `moocdb`.users AS users
INNER JOIN `moocdb`.observed_events AS observed_events
 ON observed_events.user_id = users.user_id
INNER JOIN `moocdb`.urls AS urls
 ON urls.url_id=observed_events.url_id
INNER JOIN `moocdb`.resources AS resources
 ON resources.resource_uri = urls.url
INNER JOIN `moocdb`.resource_types AS resource_types
 ON resource_types.resource_type_id = resources.resource_type_id
WHERE users.user_dropout_week IS NOT NULL
	-- AND users.user_id < 100
	AND resource_types.resource_type_id = 3 -- 3 is book
	AND FLOOR((UNIX_TIMESTAMP(observed_events.observed_event_timestamp)
			- UNIX_TIMESTAMP('2012-03-05 12:00:00')) / (3600 * 24 * 7)) < 15
    AND observed_events.validity = 1
GROUP BY users.user_id, week
HAVING week < 15
AND week >= 0
;

