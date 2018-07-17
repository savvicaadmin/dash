import dash, os
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)
pwd = os.getcwd()
csv_files= {
    'Jan, 2018': 'costs_jan.csv',
    'Feb, 2018': 'costs_feb.csv',
    'Mar, 2018': 'costs_mar.csv',
    'Apr, 2018': 'costs_apr.csv',
    'May, 2018': 'costs_may.csv',
    'Jun, 2018': 'costs_jun.csv'
}
#app.config['suppress_callback_exceptions']=True

app.layout = html.Div([
    html.H1('AWS cost Page', style={'color':'red', 'fontsize': 18, 'marginTop': 25 ,'allign': 'center'}),
    html.Label('Select from dropdown'),
    dcc.Dropdown(
        id='month-dropdown',
        options=[
            {'label':'Jan, 2018','value':'Jan, 2018'},
            {'label':'Feb, 2018','value':'Feb, 2018'},
            {'label':'Mar, 2018','value':'Mar, 2018'},
            {'label':'Apr, 2018','value':'Apr, 2018'},
            {'label':'May, 2018','value':'May, 2018'},
            {'label':'Jun, 2018','value':'Jun, 2018'}
        ],
        value='Jun, 2018',
    ),
    dcc.Graph(id='month-graph')
])
@app.callback(
    dash.dependencies.Output('month-graph', 'figure'),
    [dash.dependencies.Input('month-dropdown', 'value')])
def update_output(value):
    print (value)
    month = csv_files[str(value)]
    print (month)
    print (pwd+"/"+month)
    df1 = pd.read_csv(pwd+"/"+month)
    return {
            'data': [
                {'x':list(df1.Service), 'y':list(df1.EC2_Instances), 'type':'line', 'name':'Ec2 Instances'},
                {'x':list(df1.Service), 'y':list(df1.EC2_ELB), 'type':'line', 'name':'EC2_ELB'},
                {'x':list(df1.Service), 'y':list(df1.S3), 'type':'line', 'name':'S3'},
                #{'x':list(df1.Date), 'y':list(df1.CloudWatch), 'type':'line', 'name':'CloudWatch'},
                {'x':list(df1.Service), 'y':list(df1.SQS), 'type':'line', 'name':'SQS'},
                {'x':list(df1.Service), 'y':list(df1.Route_53), 'type':'line', 'name':'Route_53'},
                {'x':list(df1.Service), 'y':list(df1.SNS), 'type':'line', 'name':'SNS'},
                #{'x':list(df1.Date), 'y':list(df1.VPC), 'type':'line', 'name':'Route_53'},
            ],
                'layout': {'title':'COST GRAPH'}
        }

if __name__ == '__main__':
    app.run_server(debug=True)