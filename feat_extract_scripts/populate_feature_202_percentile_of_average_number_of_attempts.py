'''
Created on Nov 21, 2013
@author: Colin Taylor colin2328@gmail.com
Feature 202- A student's average number of attempts as compared with other students as a percentile
Requires that populate_feature_9_average_number_of_attempts.sql has already been run!
'''

from  scipy.stats import percentileofscore

def main(conn, conn2, dbName, startDate, currentDate, parent_conn = None):
    cursor = conn.cursor()


    sql = '''SELECT user_id, longitudinal_feature_week,longitudinal_feature_value
          FROM `%s`.user_longitudinal_feature_values
          WHERE longitudinal_feature_id = 9;
          ''' % (dbName)

    cursor.execute(sql)

    week_values = {}
    data = []
    for [user_id, week, value] in cursor:
        data.append((user_id, week, value))
        if week in week_values:
            week_values[week].append(value)
        else:
            week_values[week] = [value]


    data_to_insert = []
    for i, [user_id, week, value] in enumerate(data):
        data_to_insert.append((user_id, week,
            percentileofscore(week_values[week], value),currentDate))
    cursor.close()

    sql = "INSERT INTO `%s`.user_longitudinal_feature_values(longitudinal_feature_id, user_id," % dbName

    sql = sql + '''
                longitudinal_feature_week,
                longitudinal_feature_value,
                date_of_extraction)
                VALUES (202, %s, %s, %s, %s)
                '''

    cursor = conn.cursor()
    cursor.executemany(sql, data_to_insert)
    cursor.close()
    conn.commit()

    if parent_conn:
        parent_conn.send(True)
    return True
