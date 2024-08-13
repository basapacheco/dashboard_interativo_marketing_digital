import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Cargar los datos
ga_data = pd.read_json('../data/google_analytics_data.json')
fb_data = pd.read_json('../data/facebook_ads_data.json')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard de Marketing Digital'),
    dcc.Graph(id='ga-sessions'),
    dcc.Graph(id='fb-impressions'),
    dcc.Dropdown(
        id='campaign-filter',
        options=[{'label': campaign, 'value': campaign} for campaign in fb_data['campaign_name'].unique()],
        value=fb_data['campaign_name'].unique()[0]
    ),
])

@app.callback(
    Output('ga-sessions', 'figure'),
    Input('campaign-filter', 'value')
)
def update_ga_sessions(selected_campaign):
    filtered_data = ga_data[ga_data['campaign_name'] == selected_campaign]
    fig = px.line(filtered_data, x='date', y='sessions', title='Sessões ao longo do tempo')
    return fig

@app.callback(
    Output('fb-impressions', 'figure'),
    Input('campaign-filter', 'value')
)
def update_fb_impressions(selected_campaign):
    filtered_data = fb_data[fb_data['campaign_name'] == selected_campaign]
    fig = px.bar(filtered_data, x='campaign_name', y='impressions', title='Impressões por Campanha')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
