-- Created on Feb 14, 2014
-- @author: Colin Taylor colin2328@gmail.com
-- Feature 208- number of attempts that were correct


set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)


SELECT 208,
	users.user_id,
	FLOOR((UNIX_TIMESTAMP(submissions.submission_timestamp)
			- UNIX_TIMESTAMP('2012-03-05 12:00:00')) / (3600 * 24 * 7)) AS week,
	COUNT(*),
    @current_date
FROM `moocdb`.users AS users
INNER JOIN `moocdb`.submissions AS submissions
	ON submissions.user_id = users.user_id
INNER JOIN `moocdb`.assessments
	ON assessments.submission_id = submissions.submission_id
WHERE users.user_dropout_week IS NOT NULL
AND assessments.assessment_grade = 1
AND submissions.validity = 1
GROUP BY users.user_id, week
HAVING week < 15
AND week >= 0;
