# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


## Loading dataframe from JSON file
data_json = pd.read_json("./data/demo_data.json")
print(data_json)
"""
# Result:
#            CAN  SGN  SIN
# headphone    1    3    0
# laptop       5    8    5
"""

## Loading dataframe from CSV file
data_csv = pd.read_csv("./data/demo_data.csv", index_col=0)
print(data_csv)
"""
# Result:
#              CAN  SGN  SIN
#  headphone    1    3    0
#  laptop       5    8    5
#
"""

## Loading dataframe from Excel file
data_excel = pd.read_excel("./data/demo_data.xlsx", index_col=0)
print(data_excel)
"""
# Result:
#              CAN  SGN  SIN
#  headphone    1    3    0
#  laptop       5    8    5
"""

# The most important operators in Pandas
## Creating sample data
dates = pd.date_range('20190101', periods=50)
data = pd.DataFrame(np.random.randn(50, 4), index=dates, columns=list('ABCD'))

## head() the first 5 rows of dataframe
print(data.head())
"""
# Result:
#                   A         B         C         D
#  2019-01-01  -1.005372  0.142613 -0.181516  1.036709
#  2019-01-02   0.790087  0.294033 -0.602744  1.035578
#  2019-01-03  -1.703856  0.126258  1.080593 -0.421066
#  2019-01-04  -0.558818 -2.923537 -1.721127 -0.275644
#  2019-01-05  -1.408334 -0.860980  0.052589  1.104063
"""

## head(number) - The first "number" rows of dataframe
print(data.head(10))
"""
# Result:
#                   A         B         C         D
#  2019-01-01  -1.005372  0.142613 -0.181516  1.036709
#  2019-01-02   0.790087  0.294033 -0.602744  1.035578
#  2019-01-03  -1.703856  0.126258  1.080593 -0.421066
#  2019-01-04  -0.558818 -2.923537 -1.721127 -0.275644
#  2019-01-05  -1.408334 -0.860980  0.052589  1.104063
#  2019-01-06   0.418509  0.607834  0.017931  0.748909
#  2019-01-07   0.336740 -0.406930  1.420234 -1.702862
#  2019-01-08   0.739592  1.051292 -0.757623 -1.156324
#  2019-01-09  -0.225760  0.416810  0.128996 -1.450296
#  2019-01-10   0.527811  1.771893 -0.551995  1.101953
"""

## tail(number) - The last "number" rows of dataframe
print(data.tail(7))
"""
# Result:
#                  A         B         C         D
#  2019-02-13  0.834528  2.912336 -0.957908  0.758701
#  2019-02-14 -0.866577 -0.886605 -0.339376  1.296223
#  2019-02-15  0.324452 -1.030220  0.854473  1.471936
#  2019-02-16  2.657040 -1.169546 -1.746896 -0.745877
#  2019-02-17  1.494073 -0.709933 -0.086347 -0.512125
#  2019-02-18 -1.455421 -0.370378  1.475331 -0.867604
#  2019-02-19 -1.542814  0.355690 -0.705522  0.069457
"""

## info() - Showing your dataframe detail information
data.info()
"""
# Result:
#  <class 'pandas.core.frame.DataFrame'>
#  DatetimeIndex: 50 entries, 2019-01-01 to 2019-02-19
#  Freq: D
#  Data columns (total 4 columns):
#  A    50 non-null float64
#  B    50 non-null float64
#  C    50 non-null float64
#  D    50 non-null float64
#  dtypes: float64(4)
#  memory usage: 2.0 KB
"""

## select a column of dataframe
print(data['A'].head())
"""
# Result
#  2019-01-01   -1.005372
#  2019-01-02    0.790087
#  2019-01-03   -1.703856
#  2019-01-04   -0.558818
#  2019-01-05   -1.408334
#  Freq: D, Name: A, dtype: float64
"""

## select multiple columns of dataframe
print(data[['A', 'D']].head())
"""
# Result
#                   A         D
#  2019-01-01  -1.005372  1.036709
#  2019-01-02   0.790087  1.035578
#  2019-01-03  -1.703856 -0.421066
#  2019-01-04  -0.558818 -0.275644
#  2019-01-05  -1.408334  1.104063
"""

## select row of dataframe by labled
print(data.loc['2019-02-19'])
"""
# Result
#  A   -1.542814
#  B    0.355690
#  C   -0.705522
#  D    0.069457
#  Name: 2019-02-19 00:00:00, dtype: float64
"""

## select row of dataframe and columns of result
print(data.loc['2019-02-19', ['A', 'B']])
"""
# Result
#  A   -1.542814
#  B    0.355690
#  Name: 2019-02-19 00:00:00, dtype: float64
"""

## select range of rows
print(data.loc['2019-02-02':'2019-02-5'])
"""
# Result
#                   A         B         C         D
#  2019-02-02   1.343458 -0.940805 -0.671073 -0.102026
#  2019-02-03   0.815890  1.190464 -0.479341 -0.105754
#  2019-02-04  -0.256803  0.595940  0.279049  2.010431
#  2019-02-05   0.311328 -0.111790 -0.515169 -0.014552
"""

## select by indexes
print(data.iloc[[1,3],:])
"""
# Result
#                  A         B         C         D
#  2019-01-02   0.790087  0.294033 -0.602744  1.035578
#  2019-01-04  -0.558818 -2.923537 -1.721127 -0.275644
"""

## select by slice of index
print(data.iloc[10:13])
"""
# Result
#                   A         B         C         D
#  2019-01-11   0.530191 -1.301325 -0.050186  0.267728
#  2019-01-12  -0.652778 -0.611594  0.291840 -0.935883
#  2019-01-13   1.602400 -0.137409  1.002766  0.820419
"""

## select by callable
print(data.loc[lambda row: row.D > 0])
"""
# Result:
#                   A         B         C         D
#  2019-01-01  -0.862970  1.312603 -0.427154  1.222134
#  2019-01-03   0.173703 -0.258924 -0.014464  0.320602
#  2019-01-04   0.252102 -1.914325  0.649628  0.885115
#  2019-01-06  -0.461437  0.063366  0.569461  0.427437
#  2019-01-08  -0.956210  0.067605 -2.273661  0.833149
#  2019-01-09   0.340620 -1.976085 -1.144538  0.425282
#  2019-01-11   0.530191 -1.301325 -0.050186  0.267728
#  2019-01-13   1.602400 -0.137409  1.002766  0.820419
#  2019-01-15  -1.083804  1.790858 -0.301093  0.674832
#  2019-01-16  -0.143779  2.104730 -1.228123  1.568482
#  2019-01-22  -0.821942  1.381137 -1.812166  0.785756
#  2019-01-23  -1.404428  0.563167  2.138703  2.387186
#  2019-01-28   0.271000 -0.633658 -0.839952  0.816997
#  2019-01-29  -0.259307  1.638976 -0.648043  0.715521
#  2019-02-01   0.109348 -0.624031 -0.283261  0.138264
#  2019-02-03  -1.319024 -0.131162  2.011317  1.312116
#  2019-02-04   0.910435 -0.636221 -0.857388  0.456990
"""

## Handling duplicated data
### Creating demo data
employees = [('Mark', 34, 'Toronto'),
            ('Kana', 30, 'Delhi'),
            ('Tam', 26, 'Ha Noi'),
            ('Kana', 30, 'Delhi'),
            ('Kana', 30, 'Delhi'),
            ('Kana', 30, 'Delhi'),
            ('Hashima', 40, 'London'),
            ('Rook', 30, 'Delhi')
            ]
df = pd.DataFrame(employees, columns=['Name', 'Age', 'City'])
print(df)
"""
#        Name  Age     City
#  0     Mark   34  Toronto
#  1     Kana   30    Delhi
#  2      Tam   26   Ha Noi
#  3     Kana   30    Delhi
#  4     Kana   30    Delhi
#  5     Kana   30    Delhi
#  6  Hashima   40   London
#  7     Rook   30    Delhi
"""

### Checking duplicated data by row
print(df.duplicated())
"""
# Result
#  0    False
#  1    False
#  2    False
#  3     True
#  4     True
#  5     True
#  6    False
#  7    False
#  dtype: bool
"""

### Getting duplicated rows
print(df[df.duplicated()])
"""
# Result
#     Name  Age   City
#  3  Kana   30  Delhi
#  4  Kana   30  Delhi
#  5  Kana   30  Delhi
"""

### Drop duplicated rows
print(df.drop_duplicates())
"""
# Result
#        Name  Age     City
#  0     Mark   34   Toronto
#  1     Kana   30    Delhi
#  2      Tam   26   Ha Noi
#  6  Hashima   40   London
#  7     Rook   30    Delhi
"""

### Drop duplicated rows with keep='last'
print(df.drop_duplicates(keep='last'))
"""
# Result
#        Name  Age     City
#  0     Mark   34  Toronto
#  2      Tam   26   Ha Noi
#  5     Kana   30    Delhi
#  6  Hashima   40   London
#  7     Rook   30    Delhi
"""

### Drop duplicated rows with keep=False
print(df.drop_duplicates(keep=False))
"""
# Result
#        Name  Age     City
#  0     Mark   34  Toronto
#  2      Tam   26   Ha Noi
#  6  Hashima   40   London
#  7     Rook   30    Delhi
"""

### Getting duplicated data by specific rows
print(df[df.duplicated(['Age', 'City'])])
"""
# Result
#     Name  Age   City
#  3  Kana   30  Delhi
#  4  Kana   30  Delhi
#  5  Kana   30  Delhi
#  7  Rook   30  Delhi
"""

## Applying function
print(df[df['Age'].apply(lambda x: x > 30)])
"""
# Result
#        Name  Age     City
#  0     Mark   34  Toronto
#  6  Hashima   40   London
"""
