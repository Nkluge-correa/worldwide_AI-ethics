import dash
import time
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, callback

from toggle import toggle_modal
from badges import badges
from graphs import fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10

from worldwide_elements import principles_definition_dict, principles_dict
from worldwide_elements import modal_article, documents_dive, table, modal_map
from worldwide_elements import modal_institution, modal_gender, modal_principles
from worldwide_elements import modal_years, modal_nature, modal_regulation, modal_normative
from worldwide_elements import modal_impact, offcanvas_principles, download_data, download_html, download_png

dash.register_page(__name__,
                   path='/worldwide-ai-ethics',
                   title='Worldwide AI Ethics 🌎🌍🌏',
                   name='Worldwide AI Ethics 🌎🌍🌏')


layout = html.Div(
    children=[
        html.Div([dcc.Markdown('# Worldwide AI Ethics', className='title-style'),
                  html.Img(src=dash.get_asset_url(
                      'logo.svg'), height="60px", className='title-icon-style')],
                 className='title-div'),
        html.Div([
            html.Div([
                dcc.Markdown('''
                Worldwide AI Ethics is a systematic literature review done by AIRES researchers at PUCRS. Building on the work done by other meta-analysts, this study presents a systematic review of 200 AI Ethics guidelines.''', className='page-intro')
            ], className='page-intro-inner-div'),
        ], className='page-intro-outer-div'),
        html.Div([modal_article], className='middle-toggles'),
        dbc.Row([
            dbc.Col([
                    html.Div(table, style={
                             "border-style": "solid", "border-color": "#696b6f"}),
                    ], md=2,  className='hidden-mobile'),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        modal_map,
                        dcc.Graph(id='map', figure=fig2, config={
                                  'displayModeBar': False},
                                  className='graph-div')
                    ], md=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_institution,
                        dcc.Graph(id='institution', figure=fig3,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_gender,
                        dcc.Graph(id='gender', figure=fig4,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=4),
                    dbc.Col([
                        html.Div([modal_principles, offcanvas_principles]),
                        dcc.Graph(id='principles', figure=fig5,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=8),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_years,
                        dcc.Graph(id='years', figure=fig6, config={
                                  'displayModeBar': False},
                                  className='graph-div')
                    ], md=12),
                ], style={'margin-top': '15px'}),
                dbc.Row([
                    dbc.Col([
                        modal_nature,
                        dcc.Graph(id='nature', figure=fig7,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=3),
                    dbc.Col([
                        modal_regulation,
                        dcc.Graph(id='regulation', figure=fig8,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=3),
                    dbc.Col([
                        modal_normative,
                        dcc.Graph(id='normative', figure=fig9,
                                  config={'displayModeBar': False})
                    ], md=3),
                    dbc.Col([
                        modal_impact,
                        dcc.Graph(id='impact', figure=fig10,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=3),
                ], style={'margin-top': '15px'}),

            ], md=10),
        ], style={'margin-left': '5px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([
                download_data, download_html, download_png
            ], md=12, style={'textAlign': 'center', 'margin-top': '20px'})
        ]),
        html.Div([
            html.Div([badges], className='badges'),
        ], className='badges-div'),
    ])


@callback(
    Output('body-abstract', 'is_open'),
    [
        Input('open-body-abstract', 'n_clicks'),
        Input('close-body-abstract', 'n_clicks'),
    ],
    [State('body-abstract', 'is_open')],
)
def toggle_abstract(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    [
        Output('document-details', 'children'),
        Output('document-abstract', 'children'),
        Output('document-principles', 'children'),
    ],
    Input('documents', 'value'),
)
def display_documents_dive(value):
    time.sleep(1)

    info_document = documents_dive.loc[value]
    document_details = f'''
    Name of the Document: {info_document.document_name}.\n
    Origin: {info_document.country}.\n
    Institution: {info_document.institutions}.\n
    Document Size: {info_document.document_size}.\n
    Gender Distribution: {info_document.authors_gender}.\n
    Document Nature: {info_document.document_nature}.\n
    Type of Regulation Proposed: {info_document.document_regulation}.\n
    Normative Strength: {info_document.document_normative}.\n
    Impact Scope: {info_document.document_impact}.\n
    '''

    return (document_details,
            info_document.document_abstract,
            info_document.principles_definition)


@callback(
    [
        Output('four-gram-definiton', 'children'),
        Output('four-gram-graph', 'figure'),
    ],
    Input('principle', 'value'),
)
def display_principle_gram(value):
    time.sleep(1)

    principles_definition = principles_definition_dict[value]

    principles_text = f"""
    ### `{value}`

    "_{principles_definition}_"
    """

    principle_df = pd.read_parquet(
        f"data/{principles_dict[value]}.parquet")

    principle_fig = px.bar(principle_df, x='Top four-grams', y='Word Count',
                           color='Word Count', color_continuous_scale='oryel')

    principle_fig.update_layout(
        template='plotly_dark',
        hoverlabel=dict(font_size=18),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        uniformtext_minsize=18,
        xaxis_title=None,
        yaxis_title=None
    )

    return (principles_text, principle_fig)


@callback(
    Output('body-map', 'is_open'),
    [
        Input('open-body-map', 'n_clicks'),
        Input('close-body-map', 'n_clicks'),
    ],
    [State('body-map', 'is_open')],
)
def toggle_map(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-institution', 'is_open'),
    [
        Input('open-body-institution', 'n_clicks'),
        Input('close-body-institution', 'n_clicks'),
    ],
    [State('body-institution', 'is_open')],
)
def toggle_institution(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-gender', 'is_open'),
    [
        Input('open-body-gender', 'n_clicks'),
        Input('close-body-gender', 'n_clicks'),
    ],
    [State('body-gender', 'is_open')],
)
def toggle_gender(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-principle', 'is_open'),
    [
        Input('open-body-principle', 'n_clicks'),
        Input('close-body-principle', 'n_clicks'),
    ],
    [State('body-principle', 'is_open')],
)
def toggle_principle(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-years', 'is_open'),
    [
        Input('open-body-years', 'n_clicks'),
        Input('close-body-years', 'n_clicks'),
    ],
    [State('body-years', 'is_open')],
)
def toggle_years(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-nature', 'is_open'),
    [
        Input('open-body-nature', 'n_clicks'),
        Input('close-body-nature', 'n_clicks'),
    ],
    [State('body-nature', 'is_open')],
)
def toggle_nature(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-regulation', 'is_open'),
    [
        Input('open-body-regulation', 'n_clicks'),
        Input('close-body-regulation', 'n_clicks'),
    ],
    [State('body-regulation', 'is_open')],
)
def toggle_regulation(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-normative', 'is_open'),
    [
        Input('open-body-normative', 'n_clicks'),
        Input('close-body-normative', 'n_clicks'),
    ],
    [State('body-normative', 'is_open')],
)
def toggle_normative(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output('body-impact', 'is_open'),
    [
        Input('open-body-impact', 'n_clicks'),
        Input('close-body-impact', 'n_clicks'),
    ],
    [State('body-impact', 'is_open')],
)
def toggle_impact(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)


@callback(
    Output("download-data", "data"),
    Input("btn_data", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'data/data_en.rar')


@callback(
    Output("download-html", "data"),
    Input("btn_html", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'data/html_files.rar')


@callback(
    Output("download-png", "data"),
    Input("btn_png", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'data/png_files.rar')


@callback(
    Output('body-all-principles', 'is_open'),
    [
        Input('open-body-all-principles', 'n_clicks'),
        Input('close-body-all-principles', 'n_clicks'),
    ],
    [State('body-all-principles', 'is_open')],
)
def toggle_abstract(n1, n2, is_open):
    return toggle_modal(n1, n2, is_open)
