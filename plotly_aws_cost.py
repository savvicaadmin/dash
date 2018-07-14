import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer as dr

import pandas as pd
import numpy as num

df1 = pd.read_csv("/home/arpit/Downloads/cost_aws.csv")
app = dash.Dash()

app.layout = html.Div(children=[
                            html.H1(children='AWS cost'),
                            dcc.Graph(
                                id='first_graph',
                                figure={
                                    'data': [
                                        {'x':list(df1.Date), 'y':list(df1.EC2_Instances), 'type':'line', 'name':'Ec2 Instances'},
                                        {'x':list(df1.Date), 'y':list(df1.EC2_ELB), 'type':'line', 'name':'EC2_ELB'},
                                        {'x':list(df1.Date), 'y':list(df1.S3), 'type':'line', 'name':'S3'},
                                        {'x':list(df1.Date), 'y':list(df1.CloudWatch), 'type':'line', 'name':'CloudWatch'},
                                        {'x':list(df1.Date), 'y':list(df1.SQS), 'type':'line', 'name':'SQS'},
                                        {'x':list(df1.Date), 'y':list(df1.CloudFront), 'type':'line', 'name':'CloudFront'},
                                        {'x':list(df1.Date), 'y':list(df1.Route_53), 'type':'line', 'name':'Route_53'},
                                        {'x':list(df1.Date), 'y':list(df1.SNS), 'type':'line', 'name':'SNS'}
                                        #{'x':list(df1.Date), 'y':list(df1.Total_cost), 'type':'line', 'name':'Total cost'}
                                    ],
                                    'layout': {
                                        'title':'COST GRAPH'
                                    }
                                }
                            )
                        ])

if __name__ == '__main__':
    app.run_server(debug=True)