# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd


df = pd.read_csv("credit-risk/data/historical_loan.csv")

df.describe()
df.info()

df[df.years.isnull()]
df[df.years == 0]


#df.fillna(0, inplace = True)

df.years.hist()
df.years.median()

df.groupby(["grade", "ownership"]
    ).agg({"amount": sum, 
           "income": max}
    ).rename(columns={"totalamount": "amount", 
                      "maxincome": "income"}
    ).reset_index()

