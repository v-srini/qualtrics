import os
import pandas as pd
import numpy  as np
import logging as log
from sutils import *

log.basicConfig(level = log.DEBUG)
log.basicConfig(format='[%(process)d]: %(levelname)s %(message)s')

file = "tsl.csv"
if (os.path.isfile(file)):
  pass
else:
  print "File \'"+file+"\' not found"
  exit(0)

df = pd.read_csv(file, skiprows=range(1,7))

survey = {  'wtp': { 'que' : {'city': 'Q25', 'wild': 'Q26', 'tsla': 'Q28'}, 
                     'opt' : {1: 'price'}
                   },

            'nps': { 'que' : {'city': 'Q12', 'wild': 'Q24', 'tsla': 'Q27'}
                   },

            'act': { 'que' : {'city': 'Q11', 'wild': 'Q13', 'tsla': 'Q15'}, 
                     'opt' : {1: 'Commute', 2: 'At Work', 3: 'Outdoors', 4: 'Travel', 5: 'At Home', 6: 'Other'},
                     'code': {'Never': 1, 'Rarely': 2, 'Moderately': 3, 'Often': 4, 'Always': 5}
                   },

          'brand': { 'que' : {'all': 'Q16'},
                     'nmsk': {'city': 'Q12', 'wild': 'Q24', 'tsla': 'Q27'},
                     'opt' : {1: 'honest', 2: 'original', 3: 'bold', 4: 'cool', 5: 'reliable', 6: 'technical', 7: 'aesthetic', 8: 'compact', 9: 'rugged', 10: 'sturdy'},
                     'code': {'1-low': 1, '2-moderate': 2, '3-average': 3, '4-good': 4, '5-high': 5}
                   },

            'buy': { 'que' : {'all': 'Q17'},
                     'nmsk': {'city': 'Q12', 'wild': 'Q24', 'tsla': 'Q27'},
                     'code': {'This month': 1, 'In 1-6 months': 2, 'Within 12 months': 3, 'After 12 months': 4, 'Never': 5}
                   }
         }


survey_data_extract(survey, df, '')

men_mask = df['Q4'].values != 'Female'
men_df = df[men_mask]
survey_data_extract(survey, men_df, 'men_')

women_mask = df['Q4'].values != 'Male'
women_df = df[women_mask]
survey_data_extract(survey, women_df, 'wom_')
