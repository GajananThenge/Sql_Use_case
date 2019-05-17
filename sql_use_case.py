# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:12:36 2019

@author: gthenge
"""

import pandas as pd
import pandasql as ps

# =============================================================================
# KPI's
# 1. %ACtive Users
High during June,July,August : might be due to summer Holidays. Demand is more in these months


# 2. Percentage of Completed Trips	Rejected Trips	Cancelled Trips
# Give an insight :
  Trip rejection Ratio is highest in Churned January,February,December


# 3. Churned Captain Rate: Churned Captain/(Active Captains +New Captains)
Churned Captain Rate is highest dunring Feb,July,Aug.



# 4. % of new Captians added.
# This will show expansion of employee numbers 
# =============================================================================


path= r"C:\Users\gthenge\Desktop\User  Table.xlsx"

#['User id', 'Gender']
Table1  = pd.read_excel(path,sheet_name="Sheet1")

#['Trip id', 'Trip Date ', 'Captain ID ', 'User ID']
Table2  = pd.read_excel(path,sheet_name="Sheet2")

# =============================================================================
# How many women took a trip? How many trips?
# Please have a check on this
# =============================================================================
q1 = """ SELECT count(*) as [Women],count([Trip id]) as [No of Trips] FROM Table1 join Table2 on Table1.[User id]=Table2.[User id] where Gender="F" """
print(ps.sqldf(q1, locals()))
# =============================================================================
# How many men took a trip on the same day they joined?
# =============================================================================
q2 = """SELECT count(*) FROM Table1 join Table2 on Table1.[User id]=Table2.[User id] where Gender="M" and Table1.[Join Date]= Table2.[Trip Date]"""
print(ps.sqldf(q2, locals()))





##################################################################################################################################
Gradient Descent

Gradient Descent is most popular optimisation technique,used in machine learning and deep learning.
It can be combined with almost every algorithm to minimize errors or losses.

It is an optimization algorithm based on convex function that tweaks its parameters
iteratively to minimize a given function to its local minimum.

It simply calculate parameters or coefficient that minimize a cost function to its maximum extent.


https://www.google.com/search?q=generalise+cost+function&safe=active&rlz=1C1GCEV_enIN846IN846&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi3qqPP66HiAhVytHEKHUSgCNQQ_AUIDigB&biw=1536&bih=674&dpr=1.25#imgrc=zgqwMH1c8jnwXM:
https://towardsdatascience.com/step-by-step-guide-to-building-your-own-neural-network-from-scratch-df64b1c5ab6e
https://towardsdatascience.com/gradient-descent-in-a-nutshell-eaf8c18212f0


During forward propagation, a series of calculations is 
performed to generate a prediction and to calculate the 
cost. The cost is a function that we wish to minimize.
In our case, the cost function will be: 

https://www.google.com/search?q=generalise+cost+function&safe=active&rlz=1C1GCEV_enIN846IN846&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi3qqPP66HiAhVytHEKHUSgCNQQ_AUIDigB&biw=1536&bih=674&dpr=1.25#imgdii=_6HgD3Q7NQFflM:&imgrc=BOR0HhrNw26oWM:


https://ml4a.github.io/ml4a/how_neural_networks_are_trained/

**** https://hackernoon.com/gradient-descent-aynk-7cbe95a778da

https://missinglink.ai/guides/neural-network-concepts/complete-guide-artificial-neural-networks/
https://missinglink.ai/guides/neural-network-concepts/neural-network-bias-bias-neuron-overfitting-underfitting/




