'''
Created on Nov 21, 2013
@author: Colin Taylor colin2328@gmail.com
Feature 203- A student's average number of attempts as compared with other students as a percent of max
Requires that populate_feature_9_average_number_of_attempts.sql has already been run!
'''

def main(conn, conn2, dbName, startDate,currentDate,parent_conn = None):
    cursor = conn.cursor()
    cursor2 = conn2.cursor()

    sql = '''SELECT user_id, longitudinal_feature_week,longitudinal_feature_value
            FROM `%s`.user_longitudinal_feature_values
            WHERE longitudinal_feature_id = 9;
            ''' % (dbName)

    cursor.execute(sql)

    week_values = {}
    for [user_id, week, value] in cursor:
        if week in week_values:
            week_values[week].append(value)
        else:
            week_values[week] = [value]


    data_to_insert = []
    for [user_id, week, value] in cursor:
        data_to_insert.append((user_id, week,
            value / max(week_values[week]),currentDate))
    cursor.close()

    sql = "INSERT INTO `%s`.user_longitudinal_feature_values(longitudinal_feature_id, user_id," % dbName

    sql = sql + '''
                longitudinal_feature_week,
                longitudinal_feature_value,
                date_of_extraction)
                VALUES (203, %s, %s, %s, %s)
                '''

    cursor = conn.cursor()
    cursor.executemany(sql, data_to_insert)
    cursor.close()
    conn.commit()

    if parent_conn:
        parent_conn.send(True)
    return True
