import dash
from dash.dependencies import Output,Input
import dash_core_components as dcc
import dash_html_components as html
from random import random
import plotly
import dash_bootstrap_components as dbc
import time


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(
    html.Div([
        html.H1(children='식재료 관리', style={'textAlign': 'center'}),
        html.H4(children='부족한 식재료를 확인하세요 ', style={'textAlign': 'center'}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='live-update-graph-pie_1')
            ]),
            dbc.Col([
                dcc.Graph(id='live-update-graph-pie_2')
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='live-update-graph-pie_3')
            ]),
            dbc.Col([
                dcc.Graph(id='live-update-graph-pie_4')
            ])
        ]),

        #dcc.Graph(id='live-update-graph-scatter', animate=True),
        #html.Div(id='live-update-text')
      #  dcc.Graph(id='live-update-graph-pie'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,
            n_intervals=0
        )
    ])
)

''''
@app.callback(Output('live-update-graph-scatter', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_scatter(self):

    traces = list()
    for t in range(2):
        traces.append(plotly.graph_objs.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[(t + 1) * random() for i in range(5)],
            name='Scatter {}'.format(t),
            mode='lines+markers'
            ))
    return {'data': traces}
'''
@app.callback(Output('live-update-graph-pie_1', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_pie_1(self):

    labels = ['딸기',' ']
    values = [1, 99]
    traces = list()

    traces.append(plotly.graph_objs.Pie(labels = labels, values = values, hole = .6,
                                        marker = {'colors': ['rgb(252, 74,133 )','rgb(254, 222, 233)']} ))
    layout = plotly.graph_objs.Layout(
        height = 400,
        width = 400,
        showlegend=False
)
    return {'data': traces, 'layout': layout}


@app.callback(Output('live-update-graph-pie_2', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_pie_2(self):
    labels = ['바나나', ' ']
    values = [random() for i in range(2)]
    traces = list()

    traces.append(
        plotly.graph_objs.Pie(labels=labels, values=values, hole=.6,
                              marker={'colors': ['rgb(252, 237,96 )', 'rgb(254, 250, 211)']}))
    layout = plotly.graph_objs.Layout(
        #annotations = {'text':'바나나'}
        height=400,
        width=400,
        showlegend = False
    )
    return {'data': traces, 'layout': layout}

@app.callback(Output('live-update-graph-pie_3', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_pie_3(self):
    labels = ['수박', ' ']
    values = [random() for i in range(2)]
    traces = list()

    traces.append(
        plotly.graph_objs.Pie(labels=labels, values=values, hole=.6,
                              marker={'colors': ['rgb(65, 227,33 )', 'rgb(209, 248, 201)']}))
    layout = plotly.graph_objs.Layout(
        #annotations = {'text':'바나나'}
        height=400,
        width=400,
        showlegend = False
    )
    return {'data': traces, 'layout': layout}

@app.callback(Output('live-update-graph-pie_4', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_pie_4(self):
    labels = ['블루베리', ' ']
    values = [random() for i in range(2)]
    traces = list()

    traces.append(
        plotly.graph_objs.Pie(labels=labels, values=values, hole=.6,
                              marker={'colors': ['rgb(280, 97,255 )', 'rgb(231, 204, 255)']}))
    layout = plotly.graph_objs.Layout(
        #annotations = {'text':'바나나'}
        height=400,
        width=400,
        showlegend = False
    )
    return {'data': traces, 'layout': layout}

'''
@app.callback(Output('live-update-graph-pie', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_pie(self):

    y_ex = random()

    traces = list()
    #for t in range(1):
    traces.append(plotly.graph_objs.pie(
        labels = '딸기',
        values = list(sightings_by_class.values()),
        name='pie {}'.format(1)
            ))
    layout = plotly.graph_objs.Layout(
    #barmode='group'
)
    return {'data': traces, 'layout': layout}
'''
if __name__ == '__main__':
    app.run_server(debug=True)

    time.sleep(5)

    driver.get('http://127.0.0.1:8050/')
