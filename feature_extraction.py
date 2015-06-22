import time
from sql_functions import *
#list of features:
from feature_dict import *

def extractFeature(dbName, userName, passwd, host, port, startDate, currentDate, dirName,
                    featureID, timeout):
    begin = time.time()
    if featureID not in featureDict:
        print "unsupported feature"
        return False
    feature = featureDict[featureID]
    isSQL = (feature['extension'] == '.sql')
    print "extracting feature %s: %s" % (featureID, feature["name"])
    if isSQL:
        conn = openSQLConnectionP(dbName, userName, passwd, host, port)
        featureFile = dirName+'/'+feature['filename']+feature['extension']
        this_file = os.path.dirname(os.path.realpath(__file__))
        featureFile = this_file+'/'+featureFile
        toBeReplaced = ['moocdb', '2012-03-05 12:00:00', '0000-00-00 00:00:00']
        toReplace = [dbName, startDate, currentDate]
        success = runSQLFile(conn, featureFile, dbName, toBeReplaced,
                toReplace, timeout)
        closeSQLConnection(conn)
    else:
        conn = openSQLConnectionP(dbName, userName, passwd, host, port)
        conn2 = openSQLConnectionP(dbName, userName, passwd, host, port)
        featureFile = dirName+'/'+feature['filename']
        success = runPythonFile(conn, conn2, dirName, feature['filename'],
                dbName, startDate, currentDate, timeout)
        closeSQLConnection(conn)
        closeSQLConnection(conn2)
    end = time.time()
    print "Elapsed time = ", end-begin
    if not success:
        print "feature ", feature['name'], "failed"
        return False
    else:
        return True
#import getpass
#extractFeature('201x_2013_spring', 'sebboyer', getpass.getpass(),
#'alfa6.csail.mit.edu', 3306, '2013-04-09 00:00:00', '2015-06-22 16:00:00',
#    'feat_extract_scripts', 112, 1800)

def extractAllFeatures(dbName, userName, passwd, host, port, startDate,
                        currentDate,dirName, featuresToSkip, timeout):

    pass
    for feature in featuresFromFeaturesToSkip(featuresToSkip):
        success = extractFeature(dbName, userName, passwd, host, port, startDate,
                                currentDate, dirName, feature, timeout)
        if not success:
            cont = ""
            while not (cont == "y" or cont == "n"):
                cont = raw_input("Continue with rest of feature extraction? (y/n)")
            if cont == "n":
                break


