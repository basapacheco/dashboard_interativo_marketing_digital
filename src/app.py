import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os

# Definir caminho para os dados
data_path = '../data'

# Carregar os dados do Google Analytics e Facebook Ads
ga_data_file = os.path.join(data_path, 'google_analytics_data.json')
fb_data_file = os.path.join(data_path, 'facebook_ads_data.json')

ga_data = pd.read_json(ga_data_file)
fb_data = pd.read_json(fb_data_file)

# Transformar colunas de datas para datetime
ga_data['date'] = pd.to_datetime(ga_data['date'])
fb_data['date'] = pd.to_datetime(fb_data['date'])

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Definir layout do aplicativo
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

# Callback para atualizar o gráfico de sessões do Google Analytics
@app.callback(
    Output('ga-sessions', 'figure'),
    Input('campaign-filter', 'value')
)
def update_ga_sessions(selected_campaign):
    filtered_data = ga_data[ga_data['campaign_name'] == selected_campaign]
    fig = px.line(filtered_data, x='date', y='sessions', title='Sessões ao longo do tempo')
    return fig

# Callback para atualizar o gráfico de impressões do Facebook Ads
@app.callback(
    Output('fb-impressions', 'figure'),
    Input('campaign-filter', 'value')
)
def update_fb_impressions(selected_campaign):
    filtered_data = fb_data[fb_data['campaign_name'] == selected_campaign]
    fig = px.bar(filtered_data, x='campaign_name', y='impressions', title='Impressões por Campanha')
    return fig

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
