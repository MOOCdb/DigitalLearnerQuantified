#contains a dictionary of all the potential features that can be extracted
#each feature in turn contains a dictionary of its salient features:
#feature_id:
#    name: descriptive name of feature,
#    filename: filename containing feature script without extension,
#    extension: either .sql or .py,
#    default: default value of feature,
#    dependencies: later features that depend on this extraction being run first,
#    desc: description of what this feature is looking at
featureDict = {
     1:  {'name': "dropout",
         'filename': 'populate_feature_1_dropout',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': "Whether or not the student has dropped out by this week (this is the label used in prediction)."},
      2:  {'name': "sum_observed_events_duration",
         'filename': 'populate_feature_2_sum_observed_events_duration',
         'extension': '.sql',
         'default': 0,
         'dependencies':[10],
         'desc': "Total time spent on each resource during the week. "},
     3:  {'name': "number_of_forum_posts",
         'filename': 'populate_feature_3_number_of_forum_posts',
         'extension': '.sql',
         'default': 0,
         'dependencies':[103],
         'desc': " Number of forum posts during the week."},
     4:  {'name': "number_of_wiki_edits",
         'filename': 'populate_feature_4_number_of_wiki_edits',
         'extension': '.sql',
         'default': 0,
         'dependencies':[104],
         'desc': "Number of wiki edits during the week. "},
     5:  {'name': "average_length_of_forum_posts",
         'filename': 'populate_feature_5_average_length_of_forum_posts',
         'extension': '.sql',
         'default': 0,
         'dependencies':[105],
         'desc': " Average length of forum posts during the week."},
     6:  {'name': "distinct_attempts",
         'filename': 'populate_feature_6_distinct_attempts',
         'extension': '.sql',
         'default': 0,
         'dependencies':[11,111],
         'desc': "Number of distinct problems attempted during the week. "},
     7:  {'name': "number_of_attempts",
         'filename': 'populate_feature_7_number_of_attempts',
         'extension': '.sql',
         'default': 0,
         'dependencies':[209],
         'desc': " Number of potentially non-distinct problem attempts during the week."},
     8:  {'name': "distinct_problems_correct",
         'filename': 'populate_feature_8_distinct_problems_correct',
         'extension': '.sql',
         'default': 0,
         'dependencies':[10,11,110,111],
         'desc': "Number of distinct problems correct during the week. "},
     9:  {'name': "average_number_of_attempts",
         'filename': 'populate_feature_9_average_number_of_attempts',
         'extension': '.sql',
         'default': 0,
         'dependencies':[109,202,203],
         'desc': "Average number of problem attempts during the week. "},
     10: {'name': "sum_observed_events_duration_per_correct_problem",
         'filename': 'populate_feature_10_sum_observed_events_duration_per_correct_problem',
         'extension': '.sql',
         'default': -1,
         'dependencies':[110],
         'desc': " Total time spent on all resources during the week (feat. 2) divided by number of correct problems (feat. 8)."},
     11: {'name': "number_problem_attempted_per_correct_problem",
         'filename': 'populate_feature_11_number_problem_attempted_per_correct_problem',
         'extension': '.sql',
         'default': -1,
         'dependencies':[111],
         'desc': " Number of problems attempted (feat. 6) divided by number of correct problems (feat. 8)."},
     12: {'name': "average_time_to_solve_problem",
         'filename': 'populate_feature_12_average_time_to_solve_problem',
         'extension': '.sql',
         'default': -1,
         'dependencies':[112],
         'desc': " Average of (max(attempt.timestamp) - min(attempt.timestamp)) for each problem during the week."},
     13: {'name': "observed_event_timestamp_variance",
         'filename': 'populate_feature_13_observed_event_timestamp_variance',
         'extension':  '.py',
         'default': 0,
         'dependencies':[],
         'desc': "Variance of a students observed event timestamps in one week. "},
     14: {'name': "number_of_collaborations",
         'filename': 'populate_feature_14_number_of_collaborations',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Number of collaborations during the week."},
     15: {'name': "max_duration_resources",
         'filename': 'populate_feature_15_max_duration_resources',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Duration of longest observed event"},
     16: {'name': "sum_observed_events_lecture",
         'filename': 'populate_feature_16_sum_observed_events_lecture',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Total time spent on all lecture-related resources during the week."},
     17: {'name': "sum_observed_events_book",
         'filename': 'populate_feature_17_sum_observed_events_book',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Total time spent on all book-related resources during the week."},
     18: {'name': "sum_observed_events_wiki",
         'filename': 'populate_feature_18_sum_observed_events_wiki',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Total time spent on all wiki-related resources during the week."},
     103:{'name': "difference_feature_3",
         'filename': 'populate_feature_103_difference_feature_3',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Number of forum posts in current week divided by number of forum posts in previous week (difference of feature 3)."},
     104:{'name': "difference_feature_4",
         'filename': 'populate_feature_104_difference_feature_4',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Number of wiki edits in current week divided by number of wiki edits in previous week (difference of feature 4)."},
     105:{'name': "difference_feature_5",
         'filename': 'populate_feature_105_difference_feature_5',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Average length of forum posts in current week divided by average length of forum posts in previous week, where number of forum posts in previous week is > 5 (difference of feature 5)."},
     109:{'name': "difference_feature_9",
         'filename': 'populate_feature_109_difference_feature_9',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Average number of attempts in current week divided by average number of attempts in previous week (difference of feature 9)."},
     110:{'name': "difference_feature_10",
         'filename': 'populate_feature_110_difference_feature_10',
         'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " (Total time spent on all resources during current week (feat. 2) divided by number of correct problems during current week (feat. 8)) divided by same thing from previous week (difference of feature 10)."},
     111:{'name': "difference_feature_11",
             'filename': 'populate_feature_111_difference_feature_11',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " (Number of problems attempted (feat. 6) divided by number of correct problems (feat. 8)) divided by same thing from previous week (difference of feature 11)."},
     112:{'name': "difference_feature_12",
             'filename': 'populate_feature_112_difference_feature_12',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " (Average of (max(attempt.timestamp) - min(attempt.timestamp)) for each problem during current week) divided by same thing from previous week (difference of feature 12)."},
     201:{'name': "number_of_forum_responses",
             'filename': 'populate_feature_201_number_of_forum_responses',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Number of forum responses per week (also known as CF1)."},
     202:{'name': "percentile_of_average_number_of_attempts",
             'filename': 'populate_feature_202_percentile_of_average_number_of_attempts',
             'extension':  '.py',
         'default': 0,
         'dependencies':[],
         'desc': " Each students average number of attempts during the week (feat. 9) compared with other students as a percentile."},
     203:{'name': "percent_of_average_number_of_attempts",
             'filename': 'populate_feature_203_percent_of_average_number_of_attempts',
             'extension':  '.py',
         'default': 0,
         'dependencies':[],
         'desc': " Each students average number of attempts during the week (feat. 9) compared with other students as a percent of max."},
     204:{'name': "pset_grade",
             'filename': 'populate_feature_204_pset_grade',
             'extension': '.sql',
         'default': 0,
         'dependencies':[205],
         'desc': " Number of homework problems correct in a week divided by number of homework problems in the week."},
     205:{'name': "pset_grade_over_time",
             'filename': 'populate_feature_205_pset_grade_over_time',
             'extension': '.sql',
         'default': -1,
         'dependencies':[],
         'desc': " Pset grade from current week (feature 204) - avg(pset grade from previous week)."},
     206:{'name': "lab_grade",
             'filename': 'populate_feature_206_lab_grade',
             'extension': '.sql',
         'default': 0,
         'dependencies':[207],
         'desc': " Number of lab problems correct in a week divided by number of lab problems in the week."},
     207:{'name': "lab_grade_over_time",
             'filename': 'populate_feature_207_lab_grade_over_time',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Lab grade from current week (feature 206) - avg(lab grade from previous week)."},
     208:{'name': "attempts_correct",
             'filename': 'populate_feature_208_attempts_correct',
             'extension': '.sql',
         'default': -1,
         'dependencies':[209],
         'desc': " Number of attempts (any type) that were correct during the week."},
     209:{'name': "percent_correct_submissions",
             'filename': 'populate_feature_209_percent_correct_submissions',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Percentage of total submissions that were correct (feature 208 / feature 7)."},
     210:{'name': "average_predeadline_submission_time",
             'filename': 'populate_feature_210_average_predeadline_submission_time',
             'extension': '.sql',
         'default': -1,
         'dependencies':[],
         'desc': " Average time between problem submissions and problem due date (in seconds)."},
     301:{'name': "std_hours_working",
             'filename': 'populate_feature_301_std_hours_working',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Standard deviation of the hours the user produces events and collaborations. Tries to capture how regular a student is with her schedule while doing a MOOC."},
     302:{'name': "time_to_react",
             'filename': 'populate_feature_302_time_to_react',
             'extension': '.sql',
         'default': 0,
         'dependencies':[],
         'desc': " Average time in days a student takes to react when a new resource in posted. Tried to capture how fast a student is reacting to new content."},
}

def returnFeatures():
    return featureDict

def skippedDependencies(featuresToSkip):
    sd = set(featuresToSkip)
    for f in featuresToSkip:
        dependencies = returnFeatures()[f]['dependencies']
        for d in dependencies:
            if d not in sd:
                sd.add(d)
    return sd

def featuresFromFeaturesToSkip(featuresToSkip):
   return sorted([f for f in returnFeatures().keys() if f not in skippedDependencies(featuresToSkip)])
