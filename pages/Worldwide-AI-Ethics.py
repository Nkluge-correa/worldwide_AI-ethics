import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, callback

from badges import badges
from toggle import toggle_modal
from graphs import countries, institutions, authors, principles
from graphs import timeline, nature, regulation, normative, impact

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
                Worldwide AI Ethics (WAIE) is a systematic literature review done by AIRES researchers at PUCRS. Building on the work done by other meta-analysts, \
                    this study presents a systematic review of 200 AI Ethics guidelines.''', className='page-intro')
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
                        dcc.Graph(id='map', figure=countries, config={
                                  'displayModeBar': False},
                                  className='graph-div')
                    ], md=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_institution,
                        dcc.Graph(id='institution', figure=institutions,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_gender,
                        dcc.Graph(id='gender', figure=authors,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=4),
                    dbc.Col([
                        html.Div([modal_principles, offcanvas_principles]),
                        dcc.Graph(id='principles', figure=principles,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=8),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_years,
                        dcc.Graph(id='years', figure=timeline, config={
                                  'displayModeBar': False},
                                  className='graph-div')
                    ], md=12),
                ], style={'margin-top': '15px'}),
                dbc.Row([
                    dbc.Col([
                        modal_nature,
                        dcc.Graph(id='nature', figure=nature,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=3),
                    dbc.Col([
                        modal_regulation,
                        dcc.Graph(id='regulation', figure=regulation,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=3),
                    dbc.Col([
                        modal_normative,
                        dcc.Graph(id='normative', figure=normative,
                                  config={'displayModeBar': False})
                    ], md=3),
                    dbc.Col([
                        modal_impact,
                        dcc.Graph(id='impact', figure=impact,
                                  config={'displayModeBar': False},
                                  className='graph-div')
                    ], md=3),
                ], style={'margin-top': '15px'}),

            ], md=10),
        ], style={'margin-left': '5px'}),
        html.Br(),
        dbc.Row([
                    html.Div([dcc.Markdown('## Explore the WAIE Dataset', className='title-style'),],
                        className='title-div'),
                    html.Br(),
                    dcc.Dropdown(id='documents',
                                 options=tuple([x["document_name"] for x in documents_dive]),
                                 value="""An Open Letter to the Global South: Bring the 'rest' in (Uma Carta Aberta ao Sul Global: Tragam o “resto” para dentro)""", 
                                 clearable=False,
                                 style={'margin-top': '10px'}
                                 ), html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Loading(type='circle', color='#dc3d87', children=[
                                dbc.Card([
                                    dbc.CardHeader("Details",
                                                   className='card-header-style', ),
                                    dbc.CardBody([
                                        dcc.Markdown(''' ''', id='document-details',
                                                     className='card-body-style', ),
                                    ]),

                                ], color='#32383e', outline=False, inverse=True, className='card-style')
                            ])
                        ], md=4),
                        dbc.Col([
                            dcc.Loading(type='circle', color='#dc3d87', children=[
                                dbc.Card([
                                    dbc.CardHeader("Abstract",
                                                   className='card-header-style', ),
                                    dbc.CardBody([
                                        dcc.Markdown('', id='document-abstract',
                                                     className='card-body-style', ),
                                    ]),

                                ], color='#32383e', outline=True, inverse=True, className='card-style')
                            ])
                        ], md=4),
                        dbc.Col([
                            dcc.Loading(type='circle', color='#dc3d87', children=[
                                dbc.Card([
                                    dbc.CardHeader("Principles",
                                                   className='card-header-style',),
                                    dbc.CardBody([
                                        dcc.Markdown('', id='document-principles',
                                                     className='card-body-style',),
                                    ]),

                                ], color='#32383e', outline=True, inverse=True, className='card-style')
                            ])
                        ], md=4),
                    ], justify='center'), html.Br(),
        ]),
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

    document = [d for d in documents_dive if d.get("document_name") == value][0]
    document_details = f'''
    Name of the Document: [{document['document_name']}]({document['document_url']}).\n
    Origin: {document['country']} ({document['world_region']}).\n
    Institution: {document['institution']} ({', '.join(map(str, document['institution_type'])) if isinstance(document['institution_type'], list) else str(document['institution_type'])}).\n
    Document Size: {document['document_size']}.\n
    Gender Distribution: M : {document['number_of_male_authors']} | F : {document['number_of_female_authors']}.\n
    Document Nature: {', '.join(map(str, document['document_nature'])) if isinstance(document['document_nature'], list) else str(document['document_nature'])}.\n
    Type of Regulation Proposed: {document['document_regulation']}.\n
    Normative Strength: {', '.join(map(str, document['document_normative'])) if isinstance(document['document_normative'], list) else str(document['document_normative'])}.\n
    Impact Scope: {document['document_impact']}.\n
    '''

    principles = ""
    for p, d in document['principles_definition'].items():
        if d:
            principles += f"- **{p}**: _{d}_\n"
        else:
            pass

    return (document_details,
            document['abstract'],
            principles)


@callback(
    [
        Output('four-gram-definiton', 'children'),
        Output('four-gram-graph', 'figure'),
    ],
    Input('principle', 'value'),
)
def display_principle_gram(value):

    principles_definition = principles_definition_dict[value]

    principles_text = f"""
    ### `{value}`

    "_{principles_definition}_"
    """

    principle_df = pd.read_parquet(
        f"data/n-grams/{principles_dict[value]}.parquet")

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
        'data/data.rar')


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
