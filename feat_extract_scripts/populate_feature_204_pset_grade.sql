-- Created on Jan 31, 2014
-- @author:  Colin Taylor
-- Feature 204: Pset Grade: Number of homework problems correct in a week's problems / number of homework problems in a week
-- Meant to be run in order to run after problems_populate_module_week.sql

set @current_date = cast('CURRENT_DATE_PLACEHOLDER' as datetime);

INSERT INTO `moocdb`.user_longitudinal_feature_values(longitudinal_feature_id, user_id, longitudinal_feature_week, longitudinal_feature_value,date_of_extraction)



SELECT 204, submissions.user_id, problems.problem_week AS week, COUNT(*) /
	(SELECT COUNT(*)  FROM `moocdb`.problems AS p2 WHERE p2.problem_type_id = 1
		AND p2.problem_week = problems.problem_week GROUP BY problem_week) AS pset_grade,
    @current_date
FROM `moocdb`.submissions
INNER JOIN `moocdb`.problems
	ON submissions.problem_id = problems.problem_id
INNER JOIN `moocdb`.assessments
	ON assessments.submission_id = submissions.submission_id
INNER JOIN `moocdb`.users
	ON submissions.user_id = users.user_id
WHERE users.user_dropout_week IS NOT NULL
AND problems.problem_type_id = 1
AND assessments.assessment_grade = 1
AND submissions.validity = 1
GROUP BY submissions.user_id, problems.problem_week
HAVING week < 15
AND week >= 0;
