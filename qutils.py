import pandas as pd
import numpy as np

def mean_sd_len_print (str_list):

  ll = [x for x in str_list if str(x) != 'nan']
  ll = map(int, ll)

  mean = round(np.mean(ll), 2)
  std  = round(np.std(ll), 2)

  return str(mean)+', '+str(std)+', '+str(len(ll)) 
  
def codify (code_list, str_list):
  ii = 0
  codified_ll = [] 

  ll = [x for x in str_list if str(x) != 'nan']
  while ii < len(ll):
    codified_ll.insert(ii, code_list[ll[ii]])
    ii += 1 

  return codified_ll
