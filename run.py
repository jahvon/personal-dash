import os
from dash import app

port = int(os.environ.get("PORT", 8000))
app.run(
    debug = True,
    host='0.0.0.0',
    port = port
)
