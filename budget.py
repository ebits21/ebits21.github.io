#! python3
#budget.py
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def split_withdrawl(record):
    '''splits withdrawl value by 2 if split_value is split
      
       Returns: the Withdrawl series
    '''
    if record['Split_Value'] == 'split':
        return record['Withdrawl']/2
    return record['Withdrawl']
    
def subtract_returns(record):
    return record['Withdrawl']-record['Deposit']

#read master records, parse dates into datetime objects
df = pd.read_csv(r'./master.csv', parse_dates=['Date'], header=None, 
                 names=['Date','Description','Withdrawl','Deposit','Account',
                        'Category','Tag','Split_Value'])

#get rid of transfers and deposits
#pandas cannot use 'and', must use & compares boolean lists.  
df = df[(df.Category != 'Transfer') & (df.Category != 'Deposit')]
df = df.set_index(df.Date).sort_index() #set index to the date and sort

#split withdrawls, .apply passes the columns of df when axis=1
df.Withdrawl = df.apply(split_withdrawl, axis=1)
df.Withdrawl = df.apply(subtract_returns, axis=1)

#group records by month and category, return a sum of each group.
monthlyRecord = df.groupby([pd.TimeGrouper('M', label='right'), 
                            df.Category]).agg(np.sum)
                            
#send months from row index to the column index and fill missing values.
monthlyRecord = monthlyRecord.unstack(level=0).fillna(0)

#rename columns using set_levels.
monthlyRecord.columns = monthlyRecord.columns.set_levels([['Withdrawl', 
       'Deposit'],['Dec 2015', 'Jan 2016', 'Feb 2016', 'March 2016', 
        'April 2016','May 2016','June 2016']])
        
monthlyRecord.Withdrawl.transpose().plot(kind='barh', colormap='Paired', 
                                         stacked=True)
plt.axis(xmin=0)
plt.legend(loc='upper center', bbox_to_anchor=(0.65,1.10), ncol=5,
           fancybox=True, shadow=True)

#find monthly total for each category and save to new dataframe.
totals = monthlyRecord.sum().to_frame('Totals')
totals = totals.unstack()

#save to html.
with open('.//Analysis.html', 'w') as f:
    f.write('<img src="Budget_May.png" width="980px"></img>')
    monthlyRecord.Withdrawl.to_html(f)
    totals.to_html(f)