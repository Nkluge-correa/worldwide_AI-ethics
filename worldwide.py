import dash
import time
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, dash_table

FONT_SIZE = 22
OPEN_BUTTON = 'light'
OUTLINE_BUTTON = True
STYLE_BUTTON = {'border': 0, 'font-weight': 'bold'}
CLOSE_BUTTON = 'primary'
COLOR_GRAPH_RGB = 'rgba(172, 50, 75, 1.0)'
COLOR_GRAPHS_HEX = '#923146'
FONT_SIZE = 22
FONT_SIZE_CARD = 18
FONT_SIZE_HEADER = 30
FONT_SIZE_N_GRAMS = 18

app = dash.Dash(__name__,
                meta_tags=[
                    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                external_stylesheets=[dbc.themes.SLATE, dbc.icons.BOOTSTRAP])

server = app.server
app.title = 'Worldwide AI Ethics 🌎🌍🌏'

df = pd.read_parquet('data/arxiv_submissions')

fig = go.Figure(layout={'template': 'plotly_dark'})
for column in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='Nº of Submissions (' +
                             column + '): %{y} <extra></extra>',
                             showlegend=True))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        tickangle=45,
        ticks='inside',
        tickfont=dict(
            size=12,
            color='white',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zeroline=False,
        showline=False,
        showticklabels=True,
        side='left',
        tickfont=dict(
            size=12,
            color='white',
        ),
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=20),
    font_color='white',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)

df = pd.read_parquet('data/arxiv_submissions_cs')

fig1 = go.Figure(layout={'template': 'plotly_dark'})
for column in df.columns:
    fig1.add_trace(go.Scatter(x=df.index, y=df[column],
                              line=dict(width=3), name=column, mode='lines',
                              hoverlabel=dict(namelength=-1),
                              hovertemplate='Nº of Submissions (' +
                              column + '): %{y} <extra></extra>',
                              showlegend=True))

fig1.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        tickangle=45,
        ticks='inside',
        tickfont=dict(
            size=12,
            color='white',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zeroline=False,
        showline=False,
        showticklabels=True,
        side='left',
        tickfont=dict(
            size=12,
            color='white',
        ),
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=20),
    font_color='white',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)

documents_dive = pd.read_parquet('data/documents_dive')

modal_article = html.Div(
    [
        html.A(['Article ', html.I(className='bi bi-info-circle')],
               id="open-body-abstract", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Worldwide AI Ethics: a review of _200_ guidelines and recommendations for AI governance ⚖️'), style={})),
                dbc.ModalBody([
                    dcc.Markdown(
                        '''**Since the end of our last "_AI winter_," 1987 - 1993, AI research and its industry have seen massive growth, either in developed technologies, investment, media attention, or new tasks that autonomous systems are nowadays able to perform. By looking at the history of submissions in ArXiv ([between 2009 and 2021](https://arxiv.org/about/reports/submission_category_by_year)), an open-access repository of electronic preprints and postprints, starting from 2018, Computer Science-related papers have been the most common sort of submitted material.** ''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Graph(id='arxiv_sub', className='hidden-mobile',
                              figure=fig), html.Br(),
                    dcc.Markdown('''**Also, when we examine the category of Computer Science alone, "_Computer Vision and Pattern Recognition_," "_Machine Learning_," and "_Computation and Language_" are the most submitted types of sub-categories. Note that all of these are areas where Machine Learning is notably established as its current paradigm.** ''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Graph(id='arxiv_CS', className='hidden-mobile',
                              figure=fig1), html.Br(),
                    dcc.Markdown(
                        '''**Besides the number of papers being produced, we have never had more capital being invested in AI-related companies and startups, either by governments or Venture Capital firms (more than 90 billion USD$ in 2021 in the US alone), and AI-related patents being registered (Zhang et al., [2022](https://aiindex.stanford.edu/report/)). This rapid expansion of the AI field/industry also came with another boom, the "_AI Ethics boom_," where a never before seen demand for regulation and normative guidance of these technologies has been put forward. Drawing on the work done by past meta-analysts in the field, this study presents a systematic review of 200 documents related to AI ethics and governance. We present a collection of typologies used to classify our sample, all condensed in an interactive and open-access online tool, coupled with a critical analysis of "_what is being said_" and "_who is saying it_" in our AI ethics global landscape.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '## _Explore the Worldwide Dataset_ 🔎'), html.Br(),
                    dcc.Dropdown(id='documents',
                                 options=documents_dive.index,
                                 value=documents_dive.index[0], clearable=False,
                                 style={'margin-top': '10px'}
                                 ), html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Loading(id='loading_4', type='default', children=[
                                dbc.Card([
                                    dbc.CardHeader("Details",
                                                   className='card-header-style', style={'font-size': FONT_SIZE_HEADER}),
                                    dbc.CardBody([
                                        dcc.Markdown(''' ''', id='document-details',
                                                     className='card-body-style', style={'font-size': FONT_SIZE_CARD}),
                                    ]),

                                ], color='#272b30', outline=False, inverse=True, className='card-style')
                            ])
                        ], md=4, style={}),
                        dbc.Col([
                            dcc.Loading(id='loading_5', type='default', children=[
                                dbc.Card([
                                    dbc.CardHeader("Abstract",
                                                   className='card-header-style', style={'font-size': FONT_SIZE_HEADER}),
                                    dbc.CardBody([
                                        dcc.Markdown('', id='document-abstract',
                                                     className='card-body-style', style={'font-size': FONT_SIZE_CARD}),
                                    ]),

                                ], color='#272b30', outline=True, inverse=True, className='card-style')
                            ])
                        ], md=4, style={}),
                        dbc.Col([
                            dcc.Loading(id='loading_6', type='default', children=[
                                dbc.Card([
                                    dbc.CardHeader("Principles",
                                                   className='card-header-style', style={'font-size': FONT_SIZE_HEADER}),
                                    dbc.CardBody([
                                        dcc.Markdown('', id='document-principles',
                                                     className='card-body-style', style={'font-size': FONT_SIZE_CARD}),
                                    ]),

                                ], color='#272b30', outline=True, inverse=True, className='card-style')
                            ])
                        ], md=4, style={}),
                    ], justify='center'), html.Br(),
                    dcc.Markdown('### Cite as 🤗'), html.Br(),
                    dcc.Markdown('''

                    ````markdown

                    @article{correa2022worldwide,
                        title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
                        author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, 
                                Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, 
                                Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund},
                        journal={arXiv preprint arXiv:2206.11922},
                        year={2022}
                    }
                    ````
                    ''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    html.Div([
                        html.H4([
                            dbc.Badge([html.I(className="bi bi-heart-fill"), "  Open-Source"], href="https://github.com/Nkluge-correa/worldwide_AI-ethics",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-bar-chart-fill"), "  Power BI Version"], href="https://en.airespucrs.org/worldwide-ai-ethics",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-file-pdf-fill"), "  Full Article"], href="https://doi.org/10.48550/arXiv.2206.11922",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                        ])
                    ], style={'text-align': 'center'}),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-abstract',
                        className='ms-auto',
                        outline=True,
                        size='xl',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-abstract',
            fullscreen=True,
        ),
    ], style={},
)

df = pd.read_parquet('data/titles_abstracts')

df = pd.DataFrame({
    'Documents': [f'**[{df.document_title[i]}]({df.document_url[i]})**' for i in range(len(df.document_title))],
    'Abstract': df.abstract
})

table = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c, 'presentation': 'markdown'}
             for c in ['Documents']],
    tooltip_data=[{
        'Documents': {'value': row['Abstract'], 'type': 'markdown'},
    } for row in df.to_dict('records')],
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color:  #272b30; color: white; bottom: auto;'
    }],
    tooltip_delay=0,
    tooltip_duration=None,
    style_table={'text-align': 'justify', 'text-justify': 'inter-word',
                 'height': '2550px', 'overflowY': 'scroll'},
    page_current=0,
    page_size=200,
    style_cell={
        'text-align': 'center', 'text-justify': 'inter-word',
        'fontSize': 14, 'padding': '10px',
        'backgroundColor': '#272b30'
    },
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto'
    },
    style_header={
        'backgroundColor': '#272b30',
        'fontWeight': 'bold',
        'text-align': 'center',
        'fontSize': FONT_SIZE
    },
)

with open('data/countries_in_dataset.geojson') as fp:
    countries = json.load(fp)

df = pd.read_parquet('data/countries')

fig2 = go.Figure(go.Choroplethmapbox(geojson=countries, locations=df.code, z=df.n_of_publications,
                                     colorscale="oryel", zmin=0, zmax=12, showscale=False,
                                     marker_opacity=0.5, marker_line_width=0))

fig2.update_layout(
    mapbox_style="carto-darkmatter",
    mapbox_zoom=1.2,
    mapbox_center={"lat": 0., "lon": 0.},
    geo=dict(bgcolor='rgba(0,0,0,0)'),
    title="<b><i>Publications by Country</i></b>",
    font_color='white',
    hoverlabel=dict(bgcolor='black', font_size=20),
    margin=dict(l=0, r=0, b=0, t=30, pad=4,
                autoexpand=True),
    legend=dict(font_size=18),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)


modal_map = html.Div(
    [
        html.A([html.I(className='bi bi-info-circle')],
               id="open-body-map", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Publications by Country 🏳️‍🌈'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**Looking at the distribution among world regions (aggregated by continent), we see that the bulk of produced documents come from Europe, North America, and Asia, while regions like South America, Africa and Oceania represent less than $4,5\%$ of our entire sample size. If it was not for the significant participation of Intergovernmental Organizations, like NATO, UN, UNESCO, that represent $6\%$ of our sample size ($13$ documents), other world regions/countries would be even more underrepresented.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown('''**$77\%$ of our total sample size are represented by $13$ countries, United States of America, United Kingdom, Germany, Canada, China, Japan, France, Finland, Netherlands, Switzerland, Belgium, Brazil, and South Korea, while a myriad of $24$ countries ($12,5\%$) represents the remainder of our sample, together with Intergovernmental organizations, like the EU ($9 = 4,5\%$) and the UN ($6 = 3\%$).**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-map',
                        className='ms-auto',
                        outline=True,
                        size='xl',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-map',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-bottom': '5px'},

)

df = pd.read_parquet('data/institutions')

fig3 = go.Figure(go.Bar(
    x=df.n_of_publications,
    y=['<b>'+elem+'</b>' for elem in df.institution_type],
    text=df.n_of_publications,
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig3.update_layout(
    title="<b><i>Publications by Institutions</i></b>",
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),

    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

modal_institution = html.Div(
    [
        html.A([html.I(className='bi bi-info-circle')],
               id="open-body-institution", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Publications by Institution Type 🏢'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**Except for institutions like IBM ($5$), Microsoft ($4$), and UNESCO ($3$), most other institutions do not have more than two published documents. We can also see that the bulk of our sample was produced by governmental institutions and private corporations ($48\%$),  followed by CSO/NGO ($17\%$), non-profit organizations ($16\%$), and academic institutions ($12,5\%$).**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown('''**However, this trend only follows if we look at the totality of our sample size. If we look at documents produced by continents, for example, in North America ($69$), private corporations ($24 = 34,7\%$) and nonprofit organizations ($18 = 26\%$) produced most documents, followed by governmental institutions ($12 = 17,4\%$). Meanwhile, when we look at Europe, the global trend is restored.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown(
                        '''**An in-depth analysis segmented by countries shows that the engagement of certain types of AI stakeholders (i.e., institution types) differs between countries. For example, in China ($11$), the majority of documents are produced by academic institutions ($5 = 45,4\%$), while in Germany ($20$), most documents in our sample were produced by private corporations ($6 = 30\%$), and CSO/NGO ($4 = 20\%$). Other insights can be found in our [Power BI dashboard](https://en.airespucrs.org/worldwide-ai-ethics).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-institution',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        outline=True,
                        size='xl',
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-institution',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/gender')

fig4 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in df.authors],
    y=df.number_of_authors,
    text=df.number_of_authors,
    width=[0.8, 0.8],
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig4.update_layout(
    title={
        'text': "<b><i>Gender Distribution</i></b>",
        'y': 1.,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    margin=dict(l=0, r=0, b=0, t=30),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_gender = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-gender", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Authors by Gender ♂ ☿ ♀ '), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**To infer the gender of the authors responsible for the documents in our sample, we performed an analysis based on the names of each author. Given the variety/diversity that names can possess, it was necessary to use automation.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '''**To make an accurate inference, it was also necessary to extract (in addition to each author's name) the most likely nationality associated with each name. For this, we used (in addition to the country/origin of each document) [nationalize.io](https://nationalize.io/), an API service that predicts the nationality of a person given their name. After that, we grouped the names of authors who had the same origin/nationality associated with their names.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''**Finally, we used the API services of the [genderize.io](https://genderize.io/) platform to infer the gender of each name. Each request was made by providing the name to be inferred and the ISO-2 code of the nationality associated with that name. In the end, $830$ names were extracted from the $200$ documents analyzed. From those names, $558$ unique names were found, each associated with one of $36$ different nationalities.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True),
                    dcc.Markdown('''**The final count shows that $66\%$ of the sample ($132$ documents) do not identify the authors. The distribution of authors with "_male_" names was favorable for the remainder of our dataset ($549 = 66\%$). $34\%$ ($281$) of these names were inferred as "_female_."**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-gender',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        outline=True,
                        size='xl',
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-gender',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/principles')

fig5 = go.Figure(go.Bar(
    x=df.n_of_citations,
    y=['<b>'+elem+'</b>' for elem in df.principles],
    text=df.n_of_citations,
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig5.update_layout(
    title={
        'text': "<b><i>Principle's Distribution</i></b>",
        'y': 1.,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),
    margin=dict(l=0, r=0, b=0, t=30,),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

df = pd.read_parquet('data/Accountability_gram')

fig_a = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_a.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)

df = pd.read_parquet('data/Beneficence_gram')

fig_b = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_b.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Children_gram')

fig_c = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_c.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Dignity_gram')

fig_d = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_d.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_parquet('data/Diversity_gram')

fig_e = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_e.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Freedom_gram')

fig_f = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_f.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Formation_gram')

fig_g = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_g.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Centeredness_gram')

fig_h = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_h.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_parquet('data/Property_gram')

fig_i = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_i.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Justice_gram')

fig_j = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_j.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Labor_gram')

fig_k = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_k.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)

df = pd.read_parquet('data/Open_gram')

fig_l = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_l.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Privacy_gram')

fig_m = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_m.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Reliability_gram')

fig_n = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_n.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Sustainability_gram')

fig_o = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_o.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Transparency_gram')

fig_p = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_p.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)


df = pd.read_parquet('data/Truthfulness_gram')

fig_q = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')
fig_q.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=FONT_SIZE_N_GRAMS,
)

modal_principles = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-principle", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Citations by Principle 🔍'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**The top five principles advocated in the documents of our sample are similar to the results shown by Jobin et al. ([2019](https://www.nature.com/articles/s42256-019-0088-2)) and Hagendorff ([2020](https://link.springer.com/article/10.1007/s11023-020-09517-8)), with the addition of Reliability/Safety/Security/Trustworthiness ($78\%$), which was also cited as top five in Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)) meta analysis ($80\%$). Since each document presents its own passage about each principle, if there were, for example, $134$ documents that upheld privacy, we collected $134$ different definitions/recommendations involving this principle.**''', className='modal-body-text-style', style={
                                 'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown('''**Looking at principle distribution filtered by continent, the top five principles remain the same in both North America and Europe, but the Asian continent introduces the principle of Beneficence/Non-Maleficence as is 5th ($74\%$) most cited principle, putting Accountability/Liability in 6th place ($70\%$). Filtering our results by country, we see no change in the top five principles when comparing EUA and the UK. However, looking under the top five principles, we begging to see differences, like Freedom/Autonomy/Democratic Values/Technological Sovereignty ($38\%$) and Beneficence/Non-Maleficence ($34,4\%$) being the 6th and 7th most cited principles in the EUA, and Open source/Fair Competition/Cooperation ($45,8\%$) and Diversity/Inclusion/Pluralism/Accessibility ($41,6\%$) being 6th and 7th most cited principles in the UK.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown('''**When examining principle distribution filtered by institution type, we also can find many insights. For example, looking at our total sample, we see that the main preoccupation of governmental institutions (world-wide) is the need for transparent systems ($89,5\%$), private corporations maily advocate for Reliability ($87,5\%$), and CSO/NGOs primarily defend the principle of fairness ($88,2\%$).**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown(
                        '''**To create an "_overall definition_" of each principle/group of principles, we utilize a [text mining](https://en.wikipedia.org/wiki/Text_mining) technique called [n-gram analysis](https://en.wikipedia.org/wiki/N-gram), were we counted the successive repetition of words (and groups of words) in every principle found in the documents of our sample. Thus, the bellow definitions were created to contemplate the recurring themes we encountered. Below we also present count charts for four-grams of each principle.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''
                    ### **`Accountability/Liability`** 
                    
                    "**_Accountability refers to the idea that developers and deployers of AI technologies should be compliant with regulatory bodies, also meaning that such actors should be accountable for their actions and the impacts caused by their technologies_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='account', className='hidden-mobile',
                              figure=fig_a), html.Br(),
                    dcc.Markdown('''
                    ### **`Beneficence/Non-Maleficence`**
                    
                    "**_Beneficence and non-maleficence are concepts that come from bioethics and medical ethics. In AI ethics, these principles state that human welfare (and harm aversion) should be the goal of AI-empowered technologies. Sometimes, this principle is also tied to the idea of Sustainability, stating that AI should be beneficial not only to human civilization but to our natural environment and other living creatures_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='benef', className='hidden-mobile',
                              figure=fig_b), html.Br(),
                    dcc.Markdown('''
                    ### **`Children & Adolescents Rights`** 
                    
                    "**_The idea that the rights of children and adolescents must be respected by AI technologies. AI stakeholders should safeguard, respect, and be aware of the fragilities associated with young people_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='child', className='hidden-mobile',
                              figure=fig_c), html.Br(),
                    dcc.Markdown('''
                    ### **`Dignity/Human Rights`** 
                     
                    "**_This principle is based on the idea that all individuals deserve proper treatment and respect. In AI ethics, the respect for human dignity is often tied to human rights (i.e., [Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights))_.**" ''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='digni', className='hidden-mobile',
                              figure=fig_d), html.Br(),
                    dcc.Markdown('''
                    ### **`Diversity/Inclusion/Pluralism/Accessibility`** 
                    
                    "**_This set of principles advocates the idea that the development and use of AI technologies should be done in an inclusive and accessible way, respecting the different ways that the human entity may come to express itself (gender, ethnicity, race, sexual orientation, disabilities, etc.). This meta-principle is strongly tied to another set of principles: Justice/Equity/Fairness/Non-discrimination_.**" ''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='diver', className='hidden-mobile',
                              figure=fig_e), html.Br(),
                    dcc.Markdown('''
                    ### **`Freedom/Autonomy/Democratic Values/Technological Sovereignty`** 
                    
                    "**_This set of principles advocates the idea that the autonomy of human decision-making must be preserved during human-AI interactions, whether that choice is individual, or the freedom to choose together, such as the inviolability of democratic rights and values, also being linked to technological self-sufficiency of Nations/States_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='free', className='hidden-mobile',
                              figure=fig_f), html.Br(),
                    dcc.Markdown('''
                    ### **`Human Formation/Education`** 
                    
                    "**_Such principles defend the idea that human formation and education must be prioritized in our technological advances. AI technologies require a considerable level of expertise to be produced and operated, and such knowledge should be accessible to all. This principle seems to be strongly tied to Labor Rights. The vast majority of documents concerned with workers and the work-life point to the need for re-educating and re-skilling the workforce as a mitigation strategy against technological unemployment_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='educa', className='hidden-mobile',
                              figure=fig_g), html.Br(),
                    dcc.Markdown('''
                    ### **`Human-Centeredness/Alignment`**
                     
                    "**_Such principles advocate the idea that AI systems should be centered on and aligned with human values. AI technologies should be tailored to align with our values (e.g., value-sensitive design). This principle is also used as a "catch-all" category, many times being defined as a collection of "principles that are valued by humans" (e.g., freedom, privacy, non-discrimination, etc.)_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='align', className='hidden-mobile',
                              figure=fig_h), html.Br(),
                    dcc.Markdown('''
                    ### **`Intellectual Property`** 
                    
                    "**_This principle seeks to ground the property rights over AI products and/or processes of knowledge generated by individuals, whether tangible or intangible_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='intellec', className='hidden-mobile',
                              figure=fig_i), html.Br(),
                    dcc.Markdown('''
                    ### **`Justice/Equity/Fairness/Non-discrimination`**
                    
                    "**_This set of principles upholds the idea of non-discrimination and bias mitigation (discriminatory algorithmic biases AI systems can be subject to). It defends the idea that, regardless of the different sensitive attributes that may characterize an individual, all should be treated fairly_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='justice',  className='hidden-mobile',
                              figure=fig_j), html.Br(),
                    dcc.Markdown('''
                    ### **`Labor Rights`** 
                    
                    "**_Labor rights are legal and human rights related to the labor relations between workers and employers. In AI ethics, this principle emphasizes that workers' rights should be preserved regardless of whether labor relations are being mediated/augmented by AI technologies or not. One of the main preoccupations pointed out when this principle is presented is the mitigation of technological unemployment (e.g., through Human Formation/Education)_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='labor', className='hidden-mobile',
                              figure=fig_k), html.Br(),
                    dcc.Markdown('''
                    ### **`Open source/Fair Competition/Cooperation`** 
                     
                    "**_This set of principles advocates different means by which joint actions can be established and cultivated between AI stakeholders to achieve common goals. It also advocates for the free and open exchange of valuable AI assets (e.g., data, knowledge, patent rights, human resources) to mitigate possible AI/technology monopolies_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='open', className='hidden-mobile',
                              figure=fig_l), html.Br(),
                    dcc.Markdown('''
                    ### **`Privacy`** 
                    
                    "**_The idea of privacy can be defined as the individual's right to expose oneself voluntarily, and to the extent desired, to the world. In AI ethics, this principle upholds the right of a person to control the exposure and availability of personal information when mined as training data for AI systems. This principle is also related to concepts such as data minimization, anonymity, informed consent, and other data protection-related concepts_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='privacy', className='hidden-mobile',
                              figure=fig_m), html.Br(),
                    dcc.Markdown('''
                    ### **`Reliability/Safety/Security/Trustworthiness`** 
                    
                    "**_This set of principles upholds the idea that AI technologies should be reliable, in the sense that their use can be verifiably attested as safe and robust, promoting user trust and better acceptance of AI technologies_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='reliab', className='hidden-mobile',
                              figure=fig_n), html.Br(),
                    dcc.Markdown('''
                    ### **`Sustainability`** 
                    
                    "**_This principle can be understood as a form of "intergenerational justice," where the well-being of future generations must also be counted during AI development. In AI ethics, sustainability refers to the idea that the development of AI technologies should be carried out with an awareness of their long-term implications, such as environmental costs and non-human life preservation/well-being_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='sustaina', className='hidden-mobile',
                              figure=fig_o), html.Br(),
                    dcc.Markdown('''
                    ### **`Transparency/Explainability/Auditability`** 
                    
                    "**_This set of principles supports the idea that the use and development of AI technologies should be done transparently for all interested stakeholders. Transparency can be related to the transparency of an organization or the transparency of an algorithm. This set of principles is also related to the idea that such information should be understandable to nonexperts, and when necessary, subject to being audited_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='trans', className='hidden-mobile',
                              figure=fig_p), html.Br(),
                    dcc.Markdown('''
                    **`Truthfulness`** 
                    
                    "**_This principle upholds the idea that AI technologies must provide truthful information. It is also related to the idea that people should not be deceived when interacting with AI systems. This principle is strongly related to the mitigation of automated means of disinformation_.**"''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Graph(id='truth', className='hidden-mobile',
                              figure=fig_q), html.Br(),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-principle',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-principle',
            fullscreen=True,
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/time_line')

fig6 = go.Figure(data=go.Scatter(x=df.years, y=df.n_of_published_documents, mode='lines+markers',
                                 name='',
                                 line=dict(color=COLOR_GRAPHS_HEX, width=6),
                                 marker=dict(size=12),
                                 connectgaps=True,
                                 hovertemplate='<b>Nº of Publications</b>: %{y} <extra></extra>'
                                 ))

fig6.add_trace(go.Scatter(
    x=[df.years[0], df.years[8]],
    y=[df.n_of_published_documents[0],
       df.n_of_published_documents[8]],
    mode='markers',
    marker=dict(color=COLOR_GRAPHS_HEX, size=16),
    hoverinfo='skip'
))

fig6.update_layout(
    xaxis=dict(
        showline=False,
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        tickfont=dict(
            size=12,
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        side='right',
        tickfont=dict(
            size=12,
        ),
    ),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=14),
)

fig6.update_layout(
    title="<b><i>Publication Timeline</i></b>",
    template='plotly_dark',
    hovermode='x unified',
    hoverlabel=dict(font_size=14),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    )
)

modal_years = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-years", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Published Documents by Year 📅'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**With respect to the year of publication of the documents from our sample, one can see that the majority of documents ($129 = 64,5\%$) Were published between the years 2017 and 2019. What we may call the "_AI ethics boom_" would be the significant production of documents in the year 2018, which represents $30,5\%$ ($61$) of our entire sample.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown(
                        '''**Note: documents with _unspecified_ dates of publication ($27 = 13,5\%$) are also quite prevalent in our sample.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-years',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-years',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/document_nature')

fig7 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in df.document_nature],
    y=df.n_of_documents,
    text=df.n_of_documents,
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig7.update_layout(
    title={
        'text': "<b><i>Nature/Content</i></b>",
        'y': 1.,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    margin=dict(l=0, r=0, b=20, t=30),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_nature = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-nature", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Publications by Type (Nature/Content) 📝'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**This type relates to the nature/content of the document, and three categories were defined (these categories were _not defined as mutually exclusive_):**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''
                    ### **`Descriptive`** 
                    
                    **Descriptive documents take the effort of presenting factual definitions related to AI technologies. These definitions serve to contextualize "_what we mean_" when we talk about AI, and how the vocabulary utilized in this field can be understood.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Normative`** 
                    
                    **Normative documents present norms, ethical principles, recommendations, and imperative affirmations about what such technologies should, or should not, be used/developed for.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Practical`** 
                    
                    **Practical documents present development tools to implement ethical principles and norms, be they qualitative (e.g., Self-assessment surveys) or quantitative (e.g., Debiasing Algorithms for ML models).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**The majority of our sample is comprised of normative samples ($96\%$), which a third of the time also presents descriptive contents ($55,5\%$), and more rarely, practical implementations $54 (27\%)$.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-nature',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-nature',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/document_regulation')

fig8 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in df.document_regulation],
    y=df.n_of_documents,
    text=df.n_of_documents,
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig8.update_layout(
    title={
        'text': "<b><i>Regulation</i></b>",
        'y': 1.,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    margin=dict(l=0, r=0, b=20, t=30),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_regulation = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-regulation", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Publications by Type (Form of Regulation) 📏'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**This type relates to the form of regulation that the document proposes. For this, three categories were defined (these categories were _defined as mutually exclusive_):**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''
                    ### **`Government-Regulation`** 
                     
                    **This category is designed to encompass documents made by governmental institutions to regulate the use and development of AI, strictly (_Legally binding horizontal regulations_) or softly (_Legally non-binding guidelines_).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Self-Regulation/Voluntary Self-Commitment`** 
                    
                    **This category is designed to encompass documents made by private organizations and other bodies that defend a form of Self-Regulation governed by the AI industry itself. It also encompasses voluntary self-commitment made by independent organizations (NGOs, Professional Associations, etc.).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Recommendation`** 
                    
                    **This category is designed to encompass documents that only suggest possible forms of governance and ethical principles that should guide organizations seeking to use, develop, or regulate AI technologies.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**When we look at the form of regulation proposed by the documents of our sample, more than half ($56\%$) are only recommendations to different AI stakeholders, while $24\%$ present self-regulatory/voluntary self-commitment style guidelines, and only $20\%$ propose a form of regulation administered by a given state/country.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-regulation',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='body-regulation',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/document_normative')

fig9 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in df.document_normative],
    y=df.n_of_documents,
    text=df.n_of_documents,
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig9.update_layout(
    title={
        'text': "<b><i>Normative Strength</i></b>",
        'y': 1.,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    margin=dict(l=0, r=0, b=20, t=30),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_normative = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-normative", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Publications by Type (Normative Strength) ⚡'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**This type relates to the normative strength of the regulation mechanism proposed by the document. For this, two categories were defined (these categories were _not defined as mutually exclusive_):**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''
                    ### **`Legally non-binding guidelines`** 
                    
                    **These documents propose an approach that intertwines AI principles with recommended practices for companies and other entities (i.e., soft law solutions).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Legally binding horizontal regulations`**
                    
                    **These documents propose an approach that focuses on regulating specific uses of AI on legally binding horizontal regulations, like mandatory requirements and prohibitions.**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**This lack of convergence to a more "_government based_" form of regulation is reflected in the normative strength of these documents, where the vast majority (98%) only serve as "_soft laws_," i.e., guidelines that do not entail any form of a legal obligation, while only 4,5% present more strict forms of regulation. Since only governmental institutions can come up with legally binding norms (other forms of institutions lack this power), and governmental institutions produced only $24\%$ of our sample, some may argue that this imbalance lies in this fact.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True), html.Br(),
                    dcc.Markdown('''**However, filtering only the documents produced by governmental institutions, the disproportion does not go away, with only $18,7\%$ of documents proposing legally binding forms of regulation. The countries that seem to be spearheading this still weak trend are Canada, Germany, and the United Kingdom, with Australia, Norway, and the USA coming right behind.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-normative',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-normative',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/document_impact')

fig10 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in df.document_impact],
    y=df.n_of_documents,
    text=df.n_of_documents,
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

fig10.update_layout(
    title={
        'text': "<b><i>Impact Scope</i></b>",
        'y': 1.,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    margin=dict(l=0, r=0, b=20, t=30),
    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12)
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_impact = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-impact", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Nº of Publications by Type (Impact Scope) 💥'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**This type relates to the impact scope that motivates the document. With impact scope, we mean the related risks and benefits regarding the use of AI that motivate the type of regulation suggested by the document. For this, three categories were defined (these categories were _defined as mutually exclusive_):**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''
                    ### **`Short-Termism`** 
                    
                    **This category is designed to encompass documents in which the scope of impact and preoccupation focus mainly on short-term problems, i.e., problems we are facing with current AI technologies (e.g., algorithmic discrimination, algorithmic opacity, privacy, legal accountability).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Long-Termism`** 
                    
                    **This category is designed to encompass documents in which the scope of impact and preoccupation focus mainly on long-term problems, i.e., problems we may come to face with future AI systems. Since such technologies are not yet a reality, such risks can be classified as hypothetical or, at best, uncertain (e.g., sentient AI, misaligned AGI, super intelligent AI, AI-related existential risks).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''
                    ### **`Short-Termism & Long-Termism`** 
                    
                    **This category is designed to encompass documents in which the scope of impact is both short and long-term, i.e., they present a "_mid-term_" scope of preoccupation. These documents address issues related to the Short-Termism category, while also pointing out the long-term impacts of our current AI adoption (e.g., AI interfering in democratic processes, autonomous weapons, existential risks, environmental sustainability, labor displacement, the need for updating our educational systems).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**Looking at the totality of our sample size, we see clearly that short-term ($47\%$) and "_mid-term_" (i.e., Short-Termism & Long-Termism = $52\%$) prevail over more long-term preoccupations ($2\%$). When we filter our sample by impact scope and institution type, it seems to us that private corporations think more about the short-term ($33\%$), governmental institutions about the short/long-term ($28\%$), and academic ($66\%$) and non-profit organizations ($33\%$) with the long-term impacts of AI technologies.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}, mathjax=True)
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-impact',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-impact',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

df = pd.read_parquet('data/principle_definition')

accordion = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [dcc.Markdown(f'**{x}**')
                     for x in df.accountability.dropna(axis=0)],
                    title="Accountability 👩🏾‍⚖️",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.beneficence.dropna(axis=0)],
                    title="Beneficence ⚕️",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.children_rights.dropna(axis=0)],
                    title="Children's Rights 👶",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.dignity.dropna(axis=0)],
                    title="Human Rights ✊🏿",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.diversity.dropna(axis=0)],
                    title="Diversity 🌈",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.autonomy.dropna(axis=0)],
                    title="Autonomy 🕊️",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.human_formation.dropna(axis=0)],
                    title="Human Formation 📚",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.human_centeredness.dropna(axis=0)],
                    title="Human-Centeredness 👨‍👨‍👦‍👦",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.intellectual_property.dropna(axis=0)],
                    title="Intellectual Property 🧠",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.fairness.dropna(axis=0)],
                    title="Fairness ⚖️",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.labor_rights.dropna(axis=0)],
                    title="Labor Rights 👷",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.cooperation.dropna(axis=0)],
                    title="Cooperation 🤝",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.privacy.dropna(axis=0)],
                    title="Privacy 🔒",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.reliability.dropna(axis=0)],
                    title="Reliability 💪",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.sustainability.dropna(axis=0)],
                    title="Sustainability ♻️",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.transparency.dropna(axis=0)],
                    title="Transparency 🕵",
                ),
                dbc.AccordionItem(
                    [dcc.Markdown(f"**{x}**")
                     for x in df.truthfulness.dropna(axis=0)],
                    title="Truthfulness 🤥",
                ),
            ],
            id="accordion",
            start_collapsed=True,
        ),
    ]
)

modal_divergence = html.Div(
    [
        html.A(['Divergence ', html.I(className="bi bi-arrow-left-right")],
               id="open-body-divergence", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Divergence in Definitions 🤔'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''**Here we can see cases of "_principle definition divergence_," i.e., divergent forms of defining ethical principles. As an example, let us look at our most cited principle: Transparency/Explainability/Auditability.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '''**When examining the definition proposed in "_[ARCC: An Ethical Framework for Artificial Intelligence](https://www.tisi.org/13747)_":**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **"_Promote algorithmic transparency and algorithmic audit, to achieve understandable and explainable AI systems. Explain the decisions assisted/made by AI systems when appropriate. Ensure individuals' right to know, and provide users with sufficient information concerning the AI system's purpose, function, limitation, and impact._"**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '''**In comparison with the one provided in "_[A practical guide to Responsible Artificial Intelligence (AI)](https://www.pwc.com/gx/en/issues/data-and-analytics/artificial-intelligence/what-is-responsible-ai/responsible-ai-practical-guide.pdf)_":**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **"_To instill trust in AI systems, people must be enabled to look under the hood at their underlying models, explore the data used to train them, expose the reasoning behind each decision, and provide coherent explanations to all stakeholders promptly. These explanations should be tailored to the different stakeholders, including regulators, data scientists, business sponsors, and end consumers_."**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**Both definitions seem similar, but the "_AI-devil is in the details_." Only the first definition entails the concept of auditing, which means (in some interpretations) a third-party review of the system in question. Also, while the first document mentions that "_one must explain_," "_ensure the right_," and "_provide enough information for people_," clearly imposing the idea of a "_duty to explain_" (without specifying who should explain), together with the "_right to know_",  the second document says that people have "_to be able to look under the hood_" (also without specifying who should be able to look), without bringing the idea of right or duty. Also, only the second one proposes that this knowledge should be tailored and accessible to different types of stakeholders, since an explanation fit for a machine learning engineer may not be fit for a consumer of an AI-empowered product.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**Keeping in mind that the concept of transparency/interpretability is a well-fundamental idea/concept in AI (especially machine learning research), being still subject to divergence in its interpretation/application, what kinds of differences may occur when we look at "_not so well defined_" principles, like human-centeredness.**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '''**In "_Data, Responsibly (Vol. 1) Mirror, Mirror_," (Khan & Stoyanovich, [2020](https://dataresponsibly.github.io/comics/)), we find the following recommendation:**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **"_Maybe what we need instead is to ground the design of AI systems in people. Using the data of the people, collected and deployed with an equitable methodology as determined by the people, to create technology that is beneficial for the people._"**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '''**While in "_[Everyday Ethics for Artificial Intelligence](https://www.ibm.com/watson/assets/duo/pdf/everydayethics.pdf)_",the following norm is suggested:**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **"_AI should be designed to align with the norms and values of your user group in mind_."**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**The first document mentions ideas like "_the use of an equitable methodology_" and "_technology that is beneficial for the people_." This idea of "_people_" seems to refer to a large and diverse group (perhaps "_all people_"). Meanwhile, the second specifically states "_your user group in mind_,"  which could mean "_a small and select group of people_," if that is what the designers have in mind as "_their users_."**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''**Many other differences can be found in our sample, for example:**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown('''- **"_[Tieto's AI ethics guidelines](https://www.tietoevry.com/en/newsroom/all-news-and-releases/press-releases/2018/10/tieto-strengthens-commitment-to-ethical-use-of-ai/)_" takes a different take on explainability, saying its systems "_can be explained and explain itself_", potting some of the responsibility of explainability in the AI system itself, making it a "_stakeholder_" in the accountability chain (a curious approach).**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **"_[The Toronto Declaration](https://www.torontodeclaration.org/declaration-text/english/)_" gives an extensive and nonexhaustive definition of what "_discrimination_" means under international laws, while most other documents resume themselves in only citing the concept, leaving open to interpretation the types of "_discrimination that is permissible_".**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **In "_[Artificial Intelligence and Machine Learning: Policy Paper](https://www.internetsociety.org/resources/doc/2017/artificial-intelligence-and-machine-learning-policy-paper/)_", fairness is related to the idea of "_AI provides socio-economic opportunities for all_" (benefits), in "_[Trustworthy AI in Aotearoa: AI Principles](https://aiforum.org.nz/wp-content/uploads/2020/03/Trustworthy-AI-in-Aotearoa-March-2020.pdf)_" fairness is also defined as "_AI systems do not unjustly harm_" (impacts), which we can relate to the difference between certain notions of algorithmic fairness (predictive parity vs equalized odds).**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown('''- **While some documents (e.g., "_[Telefónica's Approach to the Responsible Use of AI](https://www.telefonica.com/en/wp-content/uploads/sites/5/2021/08/ia-responsible-governance.pdf)_") state how privacy and security are essential for AI systems developments, only some (e.g., "_[Big Data, Artificial Intelligence, Machine Learning, and Data Protection](https://ico.org.uk/media/for-organisations/documents/2013559/big-data-ai-ml-and-data-protection.pdf)_") specify what "_good privacy criteria_" are (e.g., data minimization).**''',
                                 className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                    dcc.Markdown(
                        '''- **While most documents interpret accountability/liability as "_developers being responsible for their projects_" (e.g., "_[Declaration of Ethical Principles for AI in Latin America](https://ia-latam.com/etica-ia-latam/)_"), some documents also put this responsibility on users, and even algorithms "_themselves_" (e.g., "_[The Ethics of Code: Developing AI for Business with Five Core Principles](https://www.sage.com/~/media/group/files/business-builders/business-builders-ethics-of-code.pdf?la=en)_").**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}), html.Br(),
                    dcc.Markdown(
                        '''**Besides the ones mentioned above, many other forms of comparisons can be made using our dataset (available for download at the bottom of this page).**''', className='modal-body-text-style', style={'font-size': FONT_SIZE}),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-divergence',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-divergence',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

offcanvas = html.Div(
    [
        html.A([html.I(className="bi bi-search-heart")],
               id="open-offcanvas", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Offcanvas(
            [modal_divergence, accordion],
            id="offcanvas",
            scrollable=True,
            title="Ethical Principles ✊🏿",
            placement='end',
            is_open=False,
            style={'width': '100vw', 'text-align': 'justify',
                   'font-size': 20,
                   'text-justify': 'inter-word'}
        ),
    ], style={'display': 'inline-block', 'margin-left': '15px'}
)

download_data = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  Data'], id='btn_data',
               outline=True, color='light', style={'font-weight': 'bold'}),
    dcc.Download(id="download-data")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})

download_html = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  HTML'], id='btn_html',
               outline=True, color='light', style={'font-weight': 'bold'}),
    dcc.Download(id="download-html")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})

download_png = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  PNG'], id='btn_png',
               outline=True, color='light', style={'font-weight': 'bold'}),
    dcc.Download(id="download-png")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Div([dcc.Markdown('# `Worldwide AI Ethics`', className='title-style'),
                  html.Img(src=dash.get_asset_url(
                      'globe.svg'), height="50px", className='title-icon-style')],
                 style={'text-align': 'center',
                        'margin-top': '25px',
                        'margin-bottom': '20px'}),
        html.Div([
            html.Div([
                dcc.Markdown('''
                **_Worldwide AI Ethics is a systematic literature review done by AIRES researchers at PUCRS. Building on the work done by other meta-analysts, this study presents a systematic review of 200 documents related to AI ethics and governance, presenting a collection of typologies used to classify our sample, all condensed into an interactive, freely accessible online tool._**
                ''', style={'text-align': 'center'})
            ], style={'max-width': '800px'}),
        ], style={'width': '100%', 'display': 'flex', 'justify-content': 'center'}),
        html.Div([modal_article], style={
                 'textAlign': 'center', 'margin-top': '20px', 'margin-bottom': '15px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([
                    table,
                    ], md=2,  className='hidden-mobile'),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        modal_map,
                        dcc.Graph(id='map', figure=fig2)
                    ], md=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_institution,
                        dcc.Graph(id='institution', figure=fig3)
                    ], md=12),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_gender,
                        dcc.Graph(id='gender', figure=fig4)
                    ], md=4),
                    dbc.Col([
                        html.Div([modal_principles, offcanvas]),
                        dcc.Graph(id='principles', figure=fig5)
                    ], md=8),
                ], style={}),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        modal_years,
                        dcc.Graph(id='years', figure=fig6)
                    ], md=12),
                ], style={'margin-top': '15px'}),
                dbc.Row([
                    dbc.Col([
                        modal_nature,
                        dcc.Graph(id='nature', figure=fig7)
                    ], md=3),
                    dbc.Col([
                        modal_regulation,
                        dcc.Graph(id='regulation', figure=fig8)
                    ], md=3),
                    dbc.Col([
                        modal_normative,
                        dcc.Graph(id='normative', figure=fig9)
                    ], md=3),
                    dbc.Col([
                        modal_impact,
                        dcc.Graph(id='impact', figure=fig10)
                    ], md=3),
                ], style={'margin-top': '15px'}),

            ], md=10),
        ], style={'margin-left': '5px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([
                download_data, download_html, download_png
            ], md=12, style={'textAlign': 'center', 'margin-top': '20px', 'margin-bottom': '30px'})
        ])
    ])


@app.callback(
    Output('body-abstract', 'is_open'),
    [
        Input('open-body-abstract', 'n_clicks'),
        Input('close-body-abstract', 'n_clicks'),
    ],
    [State('body-abstract', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
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
    **Name of the Document**: {info_document.document_name}. \n
    **Origin**: {info_document.country}.\n
    **Institution**: {info_document.institutions}.\n
    **Document Size**: {info_document.document_size}.\n
    **Gender Distribution**: {info_document.authors_gender}.\n
    **Document Nature**: {info_document.document_nature}.\n
    **Type of Regulation Proposed**: {info_document.document_regulation}.\n
    **Normative Strength**: {info_document.document_normative}.\n
    **Impact Scope**: {info_document.document_impact}.\n
    '''

    return (document_details,
            info_document.document_abstract,
            info_document.principles_definition)


@app.callback(
    Output('body-map', 'is_open'),
    [
        Input('open-body-map', 'n_clicks'),
        Input('close-body-map', 'n_clicks'),
    ],
    [State('body-map', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-institution', 'is_open'),
    [
        Input('open-body-institution', 'n_clicks'),
        Input('close-body-institution', 'n_clicks'),
    ],
    [State('body-institution', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-gender', 'is_open'),
    [
        Input('open-body-gender', 'n_clicks'),
        Input('close-body-gender', 'n_clicks'),
    ],
    [State('body-gender', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-principle', 'is_open'),
    [
        Input('open-body-principle', 'n_clicks'),
        Input('close-body-principle', 'n_clicks'),
    ],
    [State('body-principle', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-years', 'is_open'),
    [
        Input('open-body-years', 'n_clicks'),
        Input('close-body-years', 'n_clicks'),
    ],
    [State('body-years', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-nature', 'is_open'),
    [
        Input('open-body-nature', 'n_clicks'),
        Input('close-body-nature', 'n_clicks'),
    ],
    [State('body-nature', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-regulation', 'is_open'),
    [
        Input('open-body-regulation', 'n_clicks'),
        Input('close-body-regulation', 'n_clicks'),
    ],
    [State('body-regulation', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-normative', 'is_open'),
    [
        Input('open-body-normative', 'n_clicks'),
        Input('close-body-normative', 'n_clicks'),
    ],
    [State('body-normative', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body-impact', 'is_open'),
    [
        Input('open-body-impact', 'n_clicks'),
        Input('close-body-impact', 'n_clicks'),
    ],
    [State('body-impact', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("download-data", "data"),
    Input("btn_data", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'data/data_en.rar')


@app.callback(
    Output("download-html", "data"),
    Input("btn_html", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'data/html_files.rar')


@app.callback(
    Output("download-png", "data"),
    Input("btn_png", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'data/png_files.rar')


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    State("offcanvas", "is_open"),
)
def toggle_offcanvas_scrollable(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    Output('body-divergence', 'is_open'),
    [
        Input('open-body-divergence', 'n_clicks'),
        Input('close-body-divergence', 'n_clicks'),
    ],
    [State('body-divergence', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=False)
