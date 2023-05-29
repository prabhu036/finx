import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

def ROC(data,n):
    N=data['Close'].diff(n)
    D=data['Close'].shift(n)
    ROC=pd.Series(N/D,name='Rate of change')
    data=data.join(ROC)
    return data
data=web.DataReader('NSEI',data_source='yahoo',start='23/5/21',end='23/5/23')
data=pd.DataFrame(data)

n=5
Nifty_ROC=ROC(data,n)
ROC=Nifty_ROC['Rate of change']
print (Nifty_ROC)
