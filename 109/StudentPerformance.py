import random
from turtle import st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("StudentsPerformance.csv")
marks = df["reading score"].tolist()

mean = sum(marks) / len(marks)
stddeviation = statistics.stdev(marks)
median = statistics.median(marks)
mode = statistics.mode(marks)

firststdstart, firststdend = mean - stddeviation, mean + stddeviation
secondstdstart, secondstdend = mean - (2*stddeviation), mean + (2*stddeviation)

fig = ff.create_distplot([marks], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[firststdstart, firststdstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[firststdstart, firststdend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[secondstdstart, secondstdstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[secondstdstart, secondstdend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.show()

datawithin1std = [result for result in marks if result > firststdstart and result < firststdend]
datawithin2std = [result for result in marks if result > secondstdstart and result < secondstdend]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(stddeviation))
print("{}% of data lies within 1 standard deviation".format(len(datawithin1std)*100.0/len(marks)))
print("{}% of data lies within 2 standard deviations".format(len(datawithin2std)*100.0/len(marks)))
