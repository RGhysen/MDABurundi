import dash
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)
# for heroku

server = app.server
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')
