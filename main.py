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
        dbPort,startDate,currentDate,numWeeks, features_to_skip, timeout):
    ## Feature extraction
    print "Extracting features"
    featExtractDirName = 'feat_extract_scripts'

    fe.extractAllFeatures(dbName, userName, passwd, dbHost, dbPort, startDate,
            currentDate,numWeeks, featExtractDirName, features_to_skip, timeout)
    print "done"

def main(dbName=None, userName=None, passwd=None, dbHost=None,
        dbPort=None,startDate=None,currentDate=None,
        features_to_skip=None, timeout = None, preprocess = False,numWeeks =None):
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
    if not numWeeks:
        numWeeks = 15
    if not features_to_skip:
        ##3,4,5,14,103,104,105,201,301 depend on collaborations table- not populated yet
        features_to_skip = [3,4,5,14, 103,104,105, 201, 301,302]
    if not timeout:
        ##set how long you're willing to wait for a feature (in seconds)
        timeout = 1800

    if preprocess:
        run_preprocess(dbName, userName, passwd, dbHost, dbPort, startDate, currentDate)

    run_feature_extraction(dbName, userName, passwd, dbHost,
            dbPort,startDate,currentDate,numWeeks,features_to_skip, timeout)

if __name__ == "__main__":
    '''
    with collab:
        3091x_2013_spring: start date: 2/5/2013 (19 weeks)
        6002x_spring_2013: start date: 3/3/2013 (17 weeks)
        6002x_fall_2012: start date: 9/5/2012 (15 weeks)

    without:
        201x_2013_spring: start date: 4/15/2013 (15 weeks)
        203x_2013_3t: start date: 10/28/2013 (7 weeks)
        1473x_2013_spring: start date: 2/12/2013 (14 weeks)
        3091x_2012_fall: start date: 10/9/2012 (14 weeks)
    '''
    main(dbName            = '6002x_spring_2013',
         timeout           = 600,
         preprocess        = True,
         startDate         = '2013-03-03 00:00:00',
         numWeeks          = 17,
         #features_to_skip  = [4,104,105,17,204,205,206,207,302]
         features_to_skip  =
         [1,2,3,4,5,6,7,8,13,14,15,16,17,18,103,104,105,109,201,204,205,206,207,208,210,301,302]
         #features_to_skip = [3,4,5,14,17,103,104,105,201,204,205,206,207,301,302]
        )
