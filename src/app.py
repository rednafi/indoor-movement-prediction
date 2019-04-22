import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly_express as px

tips = pd.read_csv('/home/redowan/code/time-series-dash-app/data/indoor_movement_red.csv')

col_options = [{'label': 'time', 'value': 'time'},
                {'label': 'RSS_anchor1', 'value': 'RSS_anchor1'},
                {'label': 'RSS_anchor2', 'value': 'RSS_anchor2'},
                {'label': 'RSS_anchor3', 'value': 'RSS_anchor3'},
                {'label': 'RSS_anchor4', 'value': 'RSS_anchor4'},
                {'label': 'class', 'value': 'target_label'},
                {'label': '_id', 'value': '_id'},
                {'label': 'linear', 'value': 'linear'},
                {'label': 'spline', 'value': 'spline'},
                ]

dimensions = ['x', 'y', 'color', 'line_shape']

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Demo: Plotly Express in Dash with Tips Dataset"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),

       
        dcc.Graph(id="graph", style={"width": "70%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color, line):
    return px.line(tips, x=x, y=x, color= color , line_shape = line,
        facet_row = 'target_label',
        height = 750)
        

if __name__ == '__main__':
      
      app.run_server(host = '0.0.0.0', port =27013)