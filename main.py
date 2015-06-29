import preprocess as pre
import feature_extraction as fe
import getpass
import datetime

def run_preprocess(dbName, userName, passwd, dbHost, dbPort, startDate, currentDate):
    ## Preprocessing the MOOCdb database before feature extraction (only once)
    print "Preprocessing database"
    preprocessDirName = 'preprocessing_scripts'
    pre.preprocess(dbName, userName, passwd, dbHost, dbPort, preprocessDirName, startDate, currentDate)
    print "done"

def run_feature_extraction(dbName, userName, passwd, dbHost,
        dbPort,startDate,currentDate,features_to_skip, timeout):
    ## Feature extraction
    print "Extracting features"
    featExtractDirName = 'feat_extract_scripts'

    fe.extractAllFeatures(dbName, userName, passwd, dbHost, dbPort, startDate,
            currentDate,featExtractDirName, features_to_skip, timeout)
    print "done"

def main(dbName=None, userName=None, passwd=None, dbHost=None,
        dbPort=None,startDate=None,currentDate=None,
        features_to_skip=None, timeout = None, preprocess = False):
    if not dbHost:
        dbHost = 'alfa6.csail.mit.edu'
    if not dbPort:
        dbPort = 3306
    if not dbName:
        dbName = '3091x_2013_spring'
    if not passwd:
        passwd = getpass.getpass()
    if not userName:
        userName = 'sebboyer'
    if not startDate:
        startDate='2013-04-09 00:00:00'
    if not currentDate:
        currentDateObject = datetime.datetime.now()
        currentDate = currentDateObject.isoformat()
        print "currentDate: ",currentDate
    if not features_to_skip:
        ##3,4,5,14,103,104,105,201,301 depend on collaborations table- not populated yet
        features_to_skip = [3,4,5,14, 103,104,105, 201, 301,302]
    if not timeout:
        ##set how long you're willing to wait for a feature (in seconds)
        timeout = 1800

    if preprocess:
        run_preprocess(dbName, userName, passwd, dbHost, dbPort, startDate, currentDate)

    run_feature_extraction(dbName, userName, passwd, dbHost,
            dbPort,startDate,currentDate, features_to_skip, timeout)

if __name__ == "__main__":
    main(dbName='6002x_spring_2013', timeout = 600, preprocess = True,
            startDate = '2013-04-09 00:00:00',
        features_to_skip = [4,  104,105, 17,204,205,206,207,302]
        #features_to_skip = [3,4,5,14,17,103,104,105,201,204,205,206,207,301,302],
            )
