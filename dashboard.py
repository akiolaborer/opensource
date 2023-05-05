from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = Dash(__name__, external_stylesheets=external_stylesheets)

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
'''
 CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA,
MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, 
SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR
'''
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
 
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
 
# 出力させたいMarkdownでの文章を変数に格納しておく。
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''
app.layout = html.Div(children=[
    html.H1(children='Dash動作確認'),
 
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
 
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Markdown(
        children=
        markdown_text
    )
])
 
if __name__ == '__main__':
    app.run_server(debug=True)