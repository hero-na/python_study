import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe = pd.read_csv('lec25.csv',nrows=2,header= None)

dframe

dframe.to_csv('mytextdata_out.csv')