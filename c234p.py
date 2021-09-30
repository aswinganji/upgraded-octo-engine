import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('projectC234_EPL.csv')

goal_column = data['Goals']
sorted_club_data_by_ascending_order = goal_column.groupby(dataset['Club'])

sumofgoal = sorted_club_data_by_ascending_order.sum()
sortedgoal = sumofgoal.sort_values(ascending = False)
print('Primear League Goals :\n',sortedgoal)

epl_top = data.sort_values(by = ['Goals'],ascending = False)[:10]
print("Top 10\n", epl_top)

fig = px.bar(epl_top x='Name',y='Goals',color='Goals',hover_data=['Club','Age'],text = 'Goals')
fig.show()