import dash
from flask_caching import Cache
import dash_bootstrap_components as dbc
from dash import html, Output, Input, State

from toggle import toggle_offcanvas

app = dash.Dash(__name__,
                meta_tags=[
                    {
                        "name": "author",
                        "content": "Nicholas Kluge"
                    },
                    {
                        "name": "description",
                        "content": "Worldwide AI Ethics Dashboard.",
                    },
                    {
                        "name": "viewport",
                        "content": "width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,"
                    },
                    {
                        "property": "og:type",
                        "content": "website"
                    },
                    {
                        "property": "og:title",
                        "content": "Worldwide AI Ethics Dashboard."
                    },
                    {
                        "property": "og:description",
                        "content": "Worldwide AI Ethics Dashboard.",
                    },
                    {
                        "property": "og:image",
                        "content": "assets/logo.svg"
                    },
                    {
                        "property": "twitter:title",
                        "content": "Worldwide AI Ethics Dashboard."
                    },
                    {
                        "property": "twitter:description",
                        "content": "Worldwide AI Ethics Dashboard."
                    },
                    {
                        "property": "twitter:image",
                        "content": "assets/logo.svg",
                    },
                ],
                external_stylesheets=[dbc.themes.SLATE, dbc.icons.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True)

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

server = app.server
app.title = 'Worldwide AI Ethics 🌎🌍🌏'

sidebar = html.Div(
    [
        html.H1("Worldwide", className="nav-header"),
        html.H2("AI Ethics", className="nav-header"),
        html.Hr(),
        html.P(
            "A review of 200 guidelines and recommendations for AI governance ⚖️", className="lead",
            style={'color': '#f4f5f5'}),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink(
                    "Home", href="/", className="nav-link")),
                dbc.NavItem(dbc.NavLink(
                    "Worldwide AI Ethics", href="/worldwide-ai-ethics", className="nav-link")),
                dbc.NavItem(dbc.NavLink(
                    "GitHub", href="https://github.com/Nkluge-correa/worldwide_AI-ethics", className="nav-link", target="_blank")),
            ],
            vertical=True,
        ),
        html.Div(
            html.P(
                "Copyright © 2023, Nkluge-correa.",
                style={'color': '#f4f5f5'}), style={'position': 'fixed', 'bottom': '0'})
    ],
    className="nav-bar",
)

offcanvas_sidebar = html.Div(
    [
        dbc.Offcanvas(
            sidebar,
            id="offnavbar",
            title="",
            is_open=False,
            style={'width': '20.5rem'},
            scrollable=True,
            close_button=False,
        ),
    ]
)


app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Div([
            html.Div([
                html.Div([
                    html.A([html.Img(src=dash.get_asset_url(
                        'home.svg'), height="50px", style={'padding-bottom': '10px'}), ' Worldwide AI Ethics'],
                        id="open-navbar", n_clicks=0, className="icon-button", style={'font-size': 30})
                ], className='inner-header-bar'),
            ], className='outer-header-bar'),
            offcanvas_sidebar
        ]),
        html.Div(dash.page_container, style={"padding-top": "6em"}),
    ],
)


@app.callback(
    Output("offnavbar", "is_open"),
    Input("open-navbar", "n_clicks"),
    [State("offnavbar", "is_open")],
)
def toggle_navbar(n1, is_open):
    return toggle_offcanvas(n1, is_open)


if __name__ == "__main__":
    app.run_server(debug=False)
