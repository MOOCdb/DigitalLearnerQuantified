from feature_extraction.feature_dict import *

def main(conn, conn2, dbName,startDate,currentDate):
    cursor = conn.cursor()
    check_exists = '''
    SELECT count(*)
    FROM `%s`.`longitudinal_features`
    ''' % (dbName)
    cursor.execute(check_exists)
    data = cursor.fetchone()
    if data:
        if int(data[0]) < len(returnFeatures()):
            cursor.close()
            cursor = conn.cursor()
            insertion = '''INSERT INTO `%s`.`longitudinal_features`
                                        (`longitudinal_feature_id`,
                                         `longitudinal_feature_name`,
                                         `longitudinal_feature_description`)
                           VALUES ''' % dbName;
            values = [insertion]
            features = returnFeatures()
            for feature_id in features.keys():
                name = features[feature_id]['name']
                description = features[feature_id]['desc']
                values.append("(%s, '%s','%s')," % (feature_id,name,description))
            values[-1] = values[-1][:-1]
            values.append(';')
            values = "".join(values)
            cursor.execute(values)
            conn.commit()
            cursor.close()
