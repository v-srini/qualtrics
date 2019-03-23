import pandas as pd
import numpy as np
from qutils import *

def survey_data_extract (survey, df, prefix):
  
  for theme in survey:

    filt = prefix+theme

    for qq in survey[theme]['que']:
      
      if 'opt' in survey[theme]:

        for op in survey[theme]['opt']:
          qno = survey[theme]['que'][qq]+'_'+str(op)
          qnm = qq+'_'+survey[theme]['opt'][op]

          if 'code' in survey[theme]:
            code_l = survey[theme]['code']
            print filt+', '+qnm+', '+mean_sd_len_print(codify(code_l, df[qno].values))
          else:
            print filt+', '+qnm+', '+mean_sd_len_print(df[qno].values)

          if 'nmsk' in survey[theme]:
            for mm in survey[theme]['nmsk']:
              qnm = mm+'_'+survey[theme]['opt'][op]
              code_l = survey[theme]['code']
              mask = df[survey[theme]['nmsk'][mm]].notnull()
              print filt+', '+qnm+', '+mean_sd_len_print(codify(code_l, df[qno][mask].values))

      else:
        qno = survey[theme]['que'][qq]
        qnm = qq

        if 'code' in survey[theme]:
          code_l = survey[theme]['code']
          print filt+', '+qnm+', '+mean_sd_len_print(codify(code_l, df[qno].values))
        else:
          print filt+', '+qnm+', '+mean_sd_len_print(df[qno].values)

        if 'nmsk' in survey[theme]:
          for mm in survey[theme]['nmsk']:
            qnm = mm
            mask = df[survey[theme]['nmsk'][mm]].notnull()
            print filt+', '+qnm+', '+mean_sd_len_print(codify(code_l, df[qno][mask].values))
