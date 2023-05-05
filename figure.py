import plotly.graph_objects as plotly

fig = plotly.Figure(data=plotly.Bar(y=[2, 3, 1])) 
fig.write_html('figure.html', auto_open=False)