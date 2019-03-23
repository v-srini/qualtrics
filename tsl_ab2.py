import pandas as pd
import numpy  as np
from sutils import *

file = "tsl_ab2.csv"
df = pd.read_csv(file, skiprows=range(1,3))

survey = {  'wtp': { 'que' : {'phon': 'Q12', 'tsla': 'Q21'}, 
                     'opt' : {1: 'price'}
                   },

            'nps': { 'que' : {'phon': 'Q13', 'tsla': 'Q22'}
                   },

            'act': { 'que' : {'all': 'Q2'}, 
                     'opt' : {1: 'Commute', 2: 'At Work', 3: 'Outdoors', 4: 'Travel', 5: 'At Home', 6: 'Other'},
                     'code': {'Never': 1, 'Rarely': 2, 'Moderately': 3, 'Often': 4, 'Always': 5}
                   },

          'aware': { 'que' : {'all': 'Q4'},
                     'opt' : {1: 'Cars', 2: 'Wall', 3: 'Bank', 4: 'Musk', 5: 'Other'}
                   },

            'buy': { 'que' : {'all': 'Q3'},
                     'code': {'This month': 1, 'In 1-6 months': 2, 'Within 12 months': 3, 'After 12 months': 4, 'Never': 5}
                   },

           'cool': { 'que' : {'phon': 'Q11', 'tsla': 'Q20'},
                     'code': {'Strongly Disagree': 1, 'Somewhat Disagree': 2, 'Neutral': 3, 'Somewhat Agree': 4, 'Strongly Agree': 5}
                   }
         }


survey_data_extract(survey, df, '')

men_mask = df['D1.2'].values != 'Female'
men_df = df[men_mask]
survey_data_extract(survey, men_df, 'men_')

women_mask = df['D1.2'].values != 'Male'
women_df = df[women_mask]
survey_data_extract(survey, women_df, 'wom_')

city_mask = df['D3.2'].values == 'City/Urban'
city_df = df[city_mask]
survey_data_extract(survey, city_df, 'city_')

rural_mask = df['D3.2'].values != 'City/Urban'
rural_df = df[rural_mask]
survey_data_extract(survey, rural_df, 'rural_')

coast_mask = (df['D3.1'].values == 'Northeast') | (df['D3.1'].values == 'West')
coast_df = df[coast_mask]
survey_data_extract(survey, coast_df, 'coast_')

inlan_mask = (df['D3.1'].values != 'Northeast') & (df['D3.1'].values != 'West')
inlan_df = df[inlan_mask]
survey_data_extract(survey, inlan_df, 'inlan_')
