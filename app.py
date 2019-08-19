import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Life Expectancy from 1970"
mytitle = "Life Expectancy of Three Countries"
x_values = ['1970', '1980', '1990', '2000', '2010']
y1_values = [71.64, 76.09, 78.84, 81.08, 82.84]
y2_values = [70.01, 73.61, 73.21, 76.64, 78.54]
y3_values = [59.08, 66.84, 69.29, 71.96, 75.24]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'Japan'
name2 = 'United States'
name3 = 'China'
tabtitle = 'Life Expectancy'
sourceurl = 'https://www.google.com/publicdata/explore?ds=d5bncppjof8f9_&met_y=sp_dyn_le00_in&idim=country:JPN:USA:CHN&hl=en&dl=en'
githublink = 'https://github.com/ayk-oishi/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
