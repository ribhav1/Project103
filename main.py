import pandas as pd
import plotly_express as px

df = pd.read_csv('data.csv')

fig = px.scatter(df, x="Date", y="Cases", color="Country")

fig.show()