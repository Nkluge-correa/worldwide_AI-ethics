
from dash import html
import dash_bootstrap_components as dbc

badges = html.Span([
    dbc.Badge([html.I(className="bi bi-github"), "  Nkluge-correa"], href="https://nkluge-correa.github.io/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
])
