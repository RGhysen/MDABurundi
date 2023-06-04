import dash
import dash_bootstrap_components as dbc
<<<<<<< HEAD
import os
=======
>>>>>>> 780801e9ed38dc89b7de1f3b1f1fab026bb97be3

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)
<<<<<<< HEAD
# for heroku

server = app.server
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')
=======
>>>>>>> 780801e9ed38dc89b7de1f3b1f1fab026bb97be3
