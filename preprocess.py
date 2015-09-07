import sql_functions
import os
'''

Author : Sebastien Boyer

Pre-processing database before feature extraction


'''


def preprocess(dbName, userName, passwd, host, port, dirName, startDate, currentDate):


# fileName, wordsToBeReplaced, wordsToReplace
    preprocessing_files = [
        #[
         #'create_longitudinal_features.sql',
         #['moocdb'],
         #[dbName]
        #],
        #[
         #'populate_longitudinal_features.py',
         #[],
         #[]
        #],

        #[
         #'create_models_table.sql',
         #['moocdb'],
         #[dbName]
         #],

        #[
         #'create_experiments_table.sql',
         #['moocdb'],
         #[dbName]
        #],


        [
         'create_user_longitudinal_feature_values.sql',
         ['moocdb'],
         [dbName]
        ],

        [
         'users_populate_dropout_week.sql',
         ['START_DATE_PLACEHOLDER','moocdb'],
         [startDate,dbName]
        ]



    ]

    conn = sql_functions.openSQLConnectionP(dbName, userName, passwd, host,port)

    for fileName, toBeReplaced, replaceBy in preprocessing_files:
        if fileName[-2:] == 'py':
            print "executing: ", fileName
            sql_functions.runPythonFile(conn,conn,dirName,
                    fileName[:-3],dbName,startDate, currentDate)
        else:
            this_file = os.path.dirname(os.path.realpath(__file__))
            fileLocation = dirName+'/'+fileName
            fileLocation = this_file+'/'+fileLocation
            newFile = sql_functions.replaceWordsInFile(fileLocation, toBeReplaced, replaceBy)
            print "executing: ", fileName
            sql_functions.executeSQL(conn, newFile)
        conn.commit()

    sql_functions.closeSQLConnection(conn)
