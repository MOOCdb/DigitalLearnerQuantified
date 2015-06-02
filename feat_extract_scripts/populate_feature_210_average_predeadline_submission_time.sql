-- Created on Feb 17, 2014
-- @author: Colin Taylor colin2328@gmail.com
-- Feature 210- Average time between problem submission and problem due date (in seconds)

-- Comments from Sebastien Boyer : If predeadlines are not available replace problems.problem_hard_deadline with end_date

set @current_date = cast('0000-00-00 00:00:00' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)


SELECT 210,
	users.user_id,
	FLOOR((UNIX_TIMESTAMP(submissions.submission_timestamp)
			- UNIX_TIMESTAMP('2012-03-05 12:00:00')) / (3600 * 24 * 7)) AS week,
	AVG((UNIX_TIMESTAMP(submissions.submission_timestamp)
			- UNIX_TIMESTAMP(problems.problem_hard_deadline))) AS time_difference,
    @current_date
FROM `moocdb`.submissions
INNER JOIN `moocdb`.users
	ON submissions.user_id = users.user_id
INNER JOIN `moocdb`.problems
	ON submissions.problem_id = problems.problem_id
WHERE users.user_dropout_week IS NOT NULL
AND submissions.validity = 1
GROUP BY users.user_id, week
HAVING week < 15
AND week >= 0;
