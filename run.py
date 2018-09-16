"""
Script used to start-up flask application
"""
import os
from dash import app

PORT = int(os.environ.get("PORT", 8000))
app.run(
    debug=True,
    host='0.0.0.0',
    port=PORT
)
