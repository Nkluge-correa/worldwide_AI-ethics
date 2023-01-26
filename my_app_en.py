import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, State, dash_table

FONT_SIZE = 22
OPEN_BUTTON = 'dark'
CLOSE_BUTTON = 'light'
COLOR_GRAPH_RGB = 'rgba(172, 50, 75, 1.0)'
COLOR_GRAPHS_HEX = '#923146'

dff = pd.read_excel('arxiv_submissions_data_en.xlsx',
                    'Arxiv').set_index('Date')

fig = go.Figure(layout={'template': 'plotly_dark'})
for column in dff.columns:
    fig.add_trace(go.Scatter(x=dff.index, y=dff[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='Nº of Submissions (' +
                             column + '): %{y} <extra></extra>',
                             showlegend=True))
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(size=12))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(size=12))
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

dff = pd.read_excel('arxiv_submissions_data_en.xlsx',
                    'Arxiv(CS)').set_index('Date')

fig1 = go.Figure(layout={'template': 'plotly_dark'})
for column in dff.columns:
    fig1.add_trace(go.Scatter(x=dff.index, y=dff[column],
                              line=dict(width=3), name=column, mode='lines',
                              hoverlabel=dict(namelength=-1),
                              hovertemplate='Nº of Submissions (' +
                              column + '): %{y} <extra></extra>',
                              showlegend=True))
fig1.update_yaxes(showgrid=True, gridcolor='lightgray',
                  showticklabels=True, tickfont=dict(size=12))
fig1.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
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

modal_article = html.Div(
    [
        dbc.Button(['Article ', html.I(className="bi bi-file-text-fill")],
                   id='open-fs', outline=False, color=OPEN_BUTTON),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Worldwide AI Ethics: a review of *200* guidelines and recommendations for AI governance ⚖️'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''Since the end of our last *“AI winter,”* 1987 - 1993, AI research and its industry have seen massive growth, either in developed technologies, investment, media attention, or new tasks that autonomous systems are nowadays able to perform. By looking at the history of submissions in ArXiv ([between 2009 and 2021](https://arxiv.org/about/reports/submission_category_by_year)), an open-access repository of electronic preprints and postprints, starting from 2018, **Computer Science-related papers have been the most common sort of submitted material.** ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_sub', figure=fig), html.Br(),
                    dcc.Markdown('''Also, when we examine the category of Computer Science alone, **"*Computer Vision and Pattern Recognition*," "*Machine Learning*,"** and **"*Computation and Language*"** are the most submitted types of sub-categories. **Note that all of these are areas where Machine Learning is notably established as its current paradigm.** ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_CS', figure=fig1), html.Br(),
                    dcc.Markdown('''Besides the number of papers being produced, we have never had more capital being invested in AI-related companies and startups, either by governments or Venture Capital firms **(more than 90 billion USD$ in 2021 in the US alone)**, and AI-related patents being registered (Zhang et al., [2022](https://aiindex.stanford.edu/report/)). This rapid expansion of the AI field/industry also came with another boom, the *"AI Ethics boom,"* where a never before seen demand for regulation and normative guidance of these technologies has been put forward. Drawing on the work done by past meta-analysts in the field, **this study presents a systematic review of 200 documents related to AI ethics and governance.** We present a collection of **typologies used to classify our sample**, all condensed in an **interactive and open-access online tool**, coupled with a critical analysis of *"what is being said"* and *"who is saying it"* in our AI ethics global landscape.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('### Cite as 🤗'),
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
                    ''', style={'font-size': FONT_SIZE,
                                'text-align': 'justify',
                                'text-justify': 'inter-word'}),
                    html.Div([
                        html.H4([
                            dbc.Badge([html.I(className="bi bi-envelope"), "  Contact Us"], href="mailto:airespucrs@airespucrs.org",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-bar-chart-fill"), "  Power BI Version"], href="https://www.airespucrs.org/worldwide-ai-ethics",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-file-pdf-fill"), "  Full Article"], href="https://doi.org/10.48550/arXiv.2206.11922",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                        ])
                    ], style={'text-align': 'center'}),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-fs',
                        className='ms-auto',
                        outline=True,
                        size='xl',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-fs',
            fullscreen=True,
        ),
    ], style={'display': 'inline-block', 'margin-right': '15px'},
)

dff = pd.read_excel('meta_en.xlsx', 'meta_text')

names = []
for i in range(len(dff['Document Title'])):
    x, y = dff['Document Title'][i], dff['Document URL'][i]
    names.append(f'[{x}]({y})')

df = pd.DataFrame({
    'Documents': names,
    'Abstract': list(dff['Abstract'])
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
                 'height': '1020px', 'overflowY': 'scroll'},
    page_current=0,
    page_size=200,
    style_cell={
        'text-align': 'center', 'text-justify': 'inter-word', 'fontSize': 14, 'padding': '10px',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_countries')

fig2 = go.Figure(data=go.Choropleth(
    locations=dff['Code'],
    z=dff['Nº of Publications'],
    text=dff['Countries'],
    colorscale='oryel',
    showscale=False,
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
))

fig2.update_layout(
    height=200,
    font_color='white',
    hoverlabel=dict(bgcolor='black', font_size=20),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='rgba(0,0,0,0)'
    ),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    legend=dict(font_size=18),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


modal_map = html.Div(
    [
        dbc.Button(
            ['Publications by Country ', html.I(className="bi bi-flag-fill")], id='open-body-scroll-map', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Publications by Country 🏳️‍🌈'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''Looking at the distribution among world regions (aggregated by continent), we see that the bulk of produced documents come from **Europe, North America, and Asia**, while regions like **South America, Africa and Oceania represent less than 4,5% of our entire sample size**. If it was not for the **significant participation of Intergovernmental Organizations,** like NATO, UN, UNESCO, **that represent 6% of our sample size (13 documents),** other world regions/countries would be even more underrepresented.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''77% of our total sample size are represented by 13 countries, **United States of America, United Kingdom, Germany, Canada, China, Japan, France, Finland, Netherlands, Switzerland, Belgium, Brazil, and South Korea,** while a myriad of **24 countries (12,5%) represents the remainder of our sample**, together with Intergovernmental organizations, like the EU (9 = 4,5%) and the UN (6 = 3%).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-scroll-map',
                        className='ms-auto',
                        outline=True,
                        size='xl',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-map',
            size='xl',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px'},

)

dff = pd.read_excel('meta_en.xlsx', 'meta_institutions')

fig3 = go.Figure(go.Bar(
    x=dff['Nº of Publications'],
    y=['<b>'+elem+'</b>' for elem in list(dff['Institution Type'])],
    text=dff['Nº of Publications'],
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig3.update_traces(textposition='none')
fig3.update_yaxes(tickfont=dict(size=12))
fig3.update_xaxes(visible=True, tickfont=dict(size=12))
fig3.update_layout(
    height=200,
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=False,
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
        dbc.Button(
            ['Institution ', html.I(className="bi bi-building")], id='open-body-scroll-institution', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Publications by Institution Type 🏢'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''Except for institutions like **IBM (5)**, **Microsoft (4)**, and **UNESCO (3)**, **most other institutions do not have more than two published documents**. We can also see that the **bulk of our sample was produced by governmental institutions and private corporations (48%)**,  followed by **CSO/NGO (17%)**, **non-profit organizations (16%)**, and **academic institutions (12,5%)**. ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''However, **this trend only follows if we look at the totality of our sample size**. If we look at documents produced by **continents**, for example, in **North America (69), private corporations (24 = 34,7%) and nonprofit organizations (18 = 26%) produced most documents**, followed by governmental institutions (12 = 17,4%). Meanwhile, when we look at **Europe**, the **global trend is restored**. ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''An in-depth analysis **segmented by countries** shows that the **engagement** of certain types of **AI stakeholders** (i.e., institution types) **differs between countries.** For example, in **China (11),  the majority of documents are produced by academic institutions (5 = 45,4%), while in Germany (20), most documents in our sample were produced by private corporations (6 = 30%), and CSO/NGO (4 = 20%).** Other insights can be found in our [Power BI dashboard](https://en.airespucrs.org/worldwide-ai-ethics).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-scroll-institution',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        outline=True,
                        size='xl',
                    )
                ),
            ],
            id='modal-body-scroll-institution',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_gender')

fig4 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in list(dff['Authors'])],
    y=dff['Nº'],
    text=dff['Nº'],
    width=[0.8, 0.8],
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig4.update_traces(textposition='none')
fig4.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig4.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig4.update_layout(
    height=200,
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_mode='hide',
    barmode='group',
    bargroupgap=0.8
)

modal_gender = html.Div(
    [
        dbc.Button(
            ['Gender ', html.I(className="bi bi-gender-ambiguous"),
             html.I(className="bi bi-gender-female"),
             html.I(className="bi bi-gender-male"),
             html.I(className="bi bi-gender-trans")], id='open-body-scroll-gender', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Authors by Gender ♂ ☿ ♀ '), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''When removing documents with unspecified authors, we counted a total of **561 male authors (66,6%)** and **281 female authors (33,3%).** The dominance of male authors over female authors is **a trend that can be found in practically every world region and country, regardless of institution type.**''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''The gender of the authors was determined by searching their names and profile pictures on different types of platforms (e.g., *LinkedIn, Researchgate,  University websites,  personal websites, etc.*)  through search engines. ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-scroll-gender',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        outline=True,
                        size='xl',
                    )
                ),
            ],
            id='modal-body-scroll-gender',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_principles')

fig5 = go.Figure(go.Bar(
    x=dff['Nº of Citations'],
    y=['<b>'+elem+'</b>' for elem in list(dff['Principles'])],
    text=dff['Nº of Citations'],
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig5.update_traces(textposition='none')
fig5.update_yaxes(tickfont=dict(size=12))
fig5.update_xaxes(visible=True, tickfont=dict(size=12))
fig5.update_layout(
    height=300,
    template='plotly_dark',
    hoverlabel=dict(font_size=18),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=False,
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

dff = pd.read_excel('meta_en.xlsx', 'Accountability_gram')

figa = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figa.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Beneficence_gram')

figb = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figb.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Children_gram')

figc = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figc.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Dignity_gram')

figd = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figd.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Diversity_gram')

fige = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
fige.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Freedom_gram')

figf = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figf.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Formation_gram')

figg = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figg.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Centeredness_gram')

figh = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figh.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Property_gram')

figi = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figi.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Justice_gram')

figj = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figj.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Labor_gram')

figk = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figk.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)

dff = pd.read_excel('meta_en.xlsx', 'Open_gram')

figl = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figl.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Privacy_gram')

figm = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figm.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Reliability_gram')

fign = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
fign.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Sustainability_gram')

figo = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figo.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Transparency_gram')

figp = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figp.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_en.xlsx', 'Truthfulness_gram')

figq = px.bar(dff, x='Top four-grams', y='Word Count',
              color='Word Count', color_continuous_scale='oryel')
figq.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)

modal_principles = html.Div(
    [
        dbc.Button(
            ['Citations by Principle ', html.I(className="bi bi-search")], id='open-body-scroll-principle', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Citations by Principle 🔍'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''The **top five principles** advocated in the documents of our sample are similar to the results shown by Jobin et al. ([2019](https://www.nature.com/articles/s42256-019-0088-2)) and Hagendorff ([2020](https://link.springer.com/article/10.1007/s11023-020-09517-8)), **with the addition of Reliability/Safety/Security/Trustworthiness (78%)**, which was also cited as top five in Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)) meta analysis **(80%)**. Since each document presents its own passage about each principle, if there were, for example, 134 documents that upheld privacy, we collected 134 different definitions/recommendations involving this principle. All being accessible in our [Power BI dashboard](https://en.airespucrs.org/worldwide-ai-ethics).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''Looking at **principle distribution filtered by continent**, the **top five principles remain the same** in both **North America** and **Europe**, but the **Asian continent** introduces the principle of **Beneficence/Non-Maleficence as is 5th (74%) most cited principle**, putting Accountability/Liability in 6th place (70%). **Filtering our results by country**, we see **no change in the top five principles** when comparing **EUA** and the **UK**. However, looking **under the top five principles**, we begging to see **differences**, like **Freedom/Autonomy/Democratic Values/Technological Sovereignty (38%)** and **Beneficence/Non-Maleficence (34,4%)** being the **6th** and **7th most cited principles in the EUA**, and **Open source/Fair Competition/Cooperation (45,8%)** and **Diversity/Inclusion/Pluralism/Accessibility (41,6%)** being **6th** and **7th most cited principles in the UK**.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''When examining **principle distribution filtered by institution type**, we also can find many insights. For example, looking at our total sample, we see that the **main preoccupation of governmental institutions** (world-wide) is the need for **transparent systems (89,5%)**, **private corporations** maily advocate for **Reliability (87,5%)**, and **CSO/NGOs** primarily defend the principle of **fairness (88,2%)**. ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''To create an "**overall definition**" of each principle/group of principles, we utilize a **[text mining](https://en.wikipedia.org/wiki/Text_mining)** technique called **[n-gram analysis](https://en.wikipedia.org/wiki/N-gram)**, were we counted the successive repetition of words (and groups of words) in every principle found in the documents of our sample. Thus, the bellow definitions were created to contemplate the recurring themes we encountered. *Below we also present count charts for four-grams of each principle.*''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''- **Accountability/Liability:** accountability refers to the idea that developers and deployers of AI technologies should be compliant with regulatory bodies, also meaning that such actors should be accountable for their actions and the impacts caused by their technologies;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Graph(id='account',
                              figure=figa), html.Br(),
                    dcc.Markdown('''- **Beneficence/Non-Maleficence:** beneficence and non-maleficence are concepts that come from bioethics and medical ethics. In AI ethics, these principles state that human welfare (and harm aversion) should be the goal of AI-empowered technologies. Sometimes, this principle is also tied to the idea of Sustainability, stating that AI should be beneficial not only to human civilization but to our natural environment and other living creatures; ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}),
                    dcc.Graph(id='benef', figure=figb), html.Br(),
                    dcc.Markdown('''- **Children & Adolescents Rights:** the idea that the rights of children and adolescents must be respected by AI technologies. AI stakeholders should safeguard, respect, and be aware of the fragilities associated with young people;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Graph(id='child', figure=figc), html.Br(),
                    dcc.Markdown('''- **Dignity/Human Rights:** this principle is based on the idea that all individuals deserve proper treatment and respect. In AI ethics, the respect for human dignity is often tied to human rights (i.e., Universal Declaration of Human Rights); ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                    dcc.Graph(id='digni', figure=figd), html.Br(),
                    dcc.Markdown('''- **Diversity/Inclusion/Pluralism/Accessibility:** this set of principles advocates the idea that the development and use of AI technologies should be done in an inclusive and accessible way, respecting the different ways that the human entity may come to express itself (gender, ethnicity, race, sexual orientation, disabilities, etc.). This meta-principle is strongly tied to another set of principles: Justice/Equity/Fairness/Non-discrimination; ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}),
                    dcc.Graph(id='diver', figure=fige), html.Br(),
                    dcc.Markdown('''- **Freedom/Autonomy/Democratic Values/Technological Sovereignty:** this set of principles advocates the idea that the autonomy of human decision-making must be preserved during human-AI interactions, whether that choice is individual, or the freedom to choose together, such as the inviolability of democratic rights and values, also being linked to technological self-sufficiency of Nations/States;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Graph(id='free', figure=figf), html.Br(),
                    dcc.Markdown('''- **Human Formation/Education:** such principles defend the idea that human formation and education must be prioritized in our technological advances. AI technologies require a considerable level of expertise to be produced and operated, and such knowledge should be accessible to all. This principle seems to be strongly tied to Labor Rights. The vast majority of documents concerned with workers and the work-life point to the need for re-educating and re-skilling the workforce as a mitigation strategy against technological unemployment;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}),
                    dcc.Graph(id='educa', figure=figg), html.Br(),
                    dcc.Markdown('''- **Human-Centeredness/Alignment:** such principles advocate the idea that AI systems should be centered on and aligned with human values. AI technologies should be tailored to align with our values (e.g., value-sensitive design). This principle is also used as a "catch-all" category, many times being defined as a collection of "principles that are valued by humans" (e.g., freedom, privacy, non-discrimination, etc.);''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                    dcc.Graph(id='align', figure=figh), html.Br(),
                    dcc.Markdown('''- **Intellectual Property:** this principle seeks to ground the property rights over AI products and/or processes of knowledge generated by individuals, whether tangible or intangible;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Graph(id='intellec',
                              figure=figi), html.Br(),
                    dcc.Markdown('''- **Justice/Equity/Fairness/Non-discrimination:** this set of principles upholds the idea of non-discrimination and bias mitigation (discriminatory algorithmic biases AI systems can be subject to). It defends the idea that, regardless of the different sensitive attributes that may characterize an individual, all should be treated "fairly";''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}),
                    dcc.Graph(id='justice',
                              figure=figj), html.Br(),
                    dcc.Markdown('''- **Labor Rights:** labor rights are legal and human rights related to the labor relations between workers and employers. In AI ethics, this principle emphasizes that workers' rights should be preserved regardless of whether labor relations are being mediated/augmented by AI technologies or not. One of the main preoccupations pointed out when this principle is presented is the mitigation of technological unemployment (e.g., through Human Formation/Education);''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}),
                    dcc.Graph(id='labor', figure=figk), html.Br(),
                    dcc.Markdown('''- **Open source/Fair Competition/Cooperation:** this set of principles advocates different means by which joint actions can be established and cultivated between AI stakeholders to achieve common goals. It also advocates for the free and open exchange of valuable AI assets (e.g., data, knowledge, patent rights, human resources) to mitigate possible AI/technology monopolies;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Graph(id='open', figure=figl), html.Br(),
                    dcc.Markdown('''- **Privacy:** the idea of privacy can be defined as the individual's right to "expose oneself voluntarily, and to the extent desired, to the world." In AI ethics, this principle upholds the right of a person to control the exposure and availability of personal information when mined as training data for AI systems. This principle is also related to concepts such as data minimization, anonymity, informed consent, and other data protection-related concepts; ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}),
                    dcc.Graph(id='privacy',
                              figure=figm), html.Br(),
                    dcc.Markdown('''- **Reliability/Safety/Security/Trustworthiness:** this set of principles upholds the idea that AI technologies should be reliable, in the sense that their use can be verifiably attested as safe and robust, promoting user trust and better acceptance of AI technologies;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}),
                    dcc.Graph(id='reliab', figure=fign), html.Br(),
                    dcc.Markdown('''- **Sustainability:** this principle can be understood as a form of "intergenerational justice," where the well-being of future generations must also be counted during AI development. In AI ethics, sustainability refers to the idea that the development of AI technologies should be carried out with an awareness of their long-term implications, such as environmental costs and non-human life preservation/well-being;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Graph(id='sustaina',
                              figure=figo), html.Br(),
                    dcc.Markdown('''- **Transparency/Explainability/Auditability:** this set of principles supports the idea that the use and development of AI technologies should be done transparently for all interested stakeholders. Transparency can be related to "the transparency of an organization" or "the transparency of an algorithm." This set of principles is also related to the idea that such information should be understandable to nonexperts, and when necessary, subject to being audited;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}),
                    dcc.Graph(id='trans', figure=figp), html.Br(),
                    dcc.Markdown('''- **Truthfulness:** this principle upholds the idea that AI technologies must provide truthful information. It is also related to the idea that people should not be deceived when interacting with AI systems. This principle is strongly related to the mitigation of automated means of disinformation.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Graph(id='truth', figure=figq), html.Br(),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-principle',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-principle',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_year')

fig6 = go.Figure(data=go.Scatter(x=list(dff['Years']), y=list(dff['Nº of Published Documents']), mode='lines+markers',
                                 name='',
                                 line=dict(color=COLOR_GRAPHS_HEX, width=6),
                                 marker=dict(size=12),
                                 connectgaps=True,
                                 hovertemplate='<b>Nº of Publications</b>: %{y} <extra></extra>'
                                 ))
fig6.add_trace(go.Scatter(
    x=[list(dff['Years'])[0], list(dff['Years'])[-1]],
    y=[list(dff['Nº of Published Documents'])[0],
       list(dff['Nº of Published Documents'])[-1]],
    mode='markers',
    marker=dict(color=COLOR_GRAPHS_HEX, size=16),
    hoverinfo='skip'
))
fig6.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor=COLOR_GRAPHS_HEX,
        linewidth=2,
        ticks='outside',
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
        side='right',
        tickfont=dict(
            size=12,
            color='white',
        ),
    ),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=14),
)

fig6.update_layout(
    height=300,
    font_color='white',
    hovermode='x',
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
        dbc.Button(
            ['Published Documents by Year ', html.I(className="bi bi-calendar-fill")], id='open-body-scroll-years', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Published Documents by Year 📅'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''With respect to the year of publication of the documents from our sample, one can see that **the majority of documents (129 = 64,5%) Were published between the years 2017 and 2019.** What we may call the *"AI ethics boom"* would be the **significant production of documents in the year 2018**, which represents **30,5% (61)** of our entire sample.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''**Note:** documents with **unspecified** dates of publication **(27 = 13,5%)** are also quite **prevalent** in our sample.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                          'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-years',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-years',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_nature')

fig7 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in list(dff['Documents Nature/Content'])],
    y=dff['Nº of Documents'],
    text=dff['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig7.update_traces(textposition='none')
fig7.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig7.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig7.update_layout(
    height=300,
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8,
)

modal_nature = html.Div(
    [
        dbc.Button(
            ['Nature/Content ', html.I(className="bi bi-file-earmark-text-fill")], id='open-body-scroll-nature', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Publications by Type (Nature/Content) 📝'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the nature/content of the document, and **three categories** were defined (these categories were *not defined as mutually exclusive*):''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''- **Descriptive:** descriptive documents take the effort of presenting factual definitions related to AI technologies. These definitions serve to contextualize "what we mean" when we talk about AI, and how the vocabulary utilized in this field can be understood;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Normative:** normative documents present norms, ethical principles, recommendations, and imperative affirmations about what such technologies should, or should not, be used/developed for;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                               'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Practical:** practical documents present development tools to implement ethical principles and norms, be they qualitative (e.g., Self-assessment surveys) or quantitative (e.g., Debiasing Algorithms for ML models).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''The majority of our sample is comprised of **normative samples (96%)**, which a **third of the time also presents descriptive contents (55,5%)**, and more **rarely**, **practical** implementations **54 (27%)**.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-nature',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-nature',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_regulation')

fig8 = go.Figure(go.Bar(
    x=['<b>'+elem +
        '</b>' for elem in list(dff['Documents Form of Regulation'])],
    y=dff['Nº of Documents'],
    text=dff['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig8.update_traces(textposition='none')
fig8.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig8.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig8.update_layout(
    height=300,
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_regulation = html.Div(
    [
        dbc.Button(
            ['Regulation ', html.I(className="bi bi-rulers")], id='open-body-scroll-regulation', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Publications by Type (Form of Regulation) 📏'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the form of regulation that the document proposes. For this, **three categories** were defined (these categories were *defined as mutually exclusive*):''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''- **Government-Regulation:** this category is designed to encompass documents made by governmental institutions to regulate the use and development of AI, strictly (Legally binding horizontal regulations) or softly (Legally non-binding guidelines);''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Self-Regulation/Voluntary Self-Commitment:** this category is designed to encompass documents made by private organizations and other bodies that defend a form of Self-Regulation governed by the AI industry itself. It also encompasses voluntary self-commitment made by independent organizations (NGOs, Professional Associations, etc.);''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Recommendation:** this category is designed to encompass documents that only suggest possible forms of governance and ethical principles that should guide organizations seeking to use, develop, or regulate AI technologies.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''When we look at the form of regulation proposed by the documents of our sample, **more than half (56%) are only recommendations** to different AI stakeholders, while **24% present self-regulatory/voluntary self-commitment style guidelines**, and only **20%** propose a **form of regulation administered by a given state/country**.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-regulation',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-regulation',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_normative')

fig9 = go.Figure(go.Bar(
    x=['<b>'+elem +
        '</b>' for elem in list(dff['Documents Normative Strength'])],
    y=dff['Nº of Documents'],
    text=dff['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig9.update_traces(textposition='none')
fig9.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig9.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=12))
fig9.update_layout(
    height=300,
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

modal_normative = html.Div(
    [
        dbc.Button(
            ['Normative Strength ', html.I(className="bi bi-lightning-fill")], id='open-body-scroll-normative', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Publications by Type (Normative Strength) ⚡'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the normative strength of the regulation mechanism proposed by the document. For this, **two categories** were defined (these categories were *not defined as mutually exclusive*):''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''- **Legally non-binding guidelines:** these documents propose an approach that intertwines AI principles with recommended practices for companies and other entities (i.e., soft law solutions);''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Legally binding horizontal regulations:** these documents propose an approach that focuses on regulating specific uses of AI on legally binding horizontal regulations, like mandatory requirements and prohibitions.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''This lack of convergence to a more **"government based"** form of regulation is reflected in the normative strength of these documents, where the **vast majority (98%) only serve as "soft laws,"** i.e., guidelines that do not entail any form of a legal obligation, while **only 4,5% present more strict forms of regulation.** Since only governmental institutions can come up with legally binding norms (other forms of institutions lack this power), and **governmental institutions produced only 24% of our sample**, some may argue that this imbalance lies in this fact.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''However, **filtering** only the documents produced by **governmental institutions**, the **disproportion does not go away**, with **only 18,7% of documents proposing legally binding forms of regulation**. The countries that seem to be spearheading this still weak trend are **Canada**, **Germany**, and the **United Kingdom**, with Australia, Norway, and the USA coming right behind.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-normative',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-normative',
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

dff = pd.read_excel('meta_en.xlsx', 'meta_impact')

fig10 = go.Figure(go.Bar(
    x=['<b>'+elem+'</b>' for elem in list(dff['Documents Impact Scope'])],
    y=dff['Nº of Documents'],
    text=dff['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))
fig10.update_traces(textposition='none')
fig10.update_yaxes(showgrid=False, visible=True,
                   showticklabels=True, tickfont=dict(size=12))
fig10.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(size=12))
fig10.update_layout(
    height=300,
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    barmode='group',
    bargroupgap=0.8
)

modal_impact = html.Div(
    [
        dbc.Button(
            ['Impact Scope ', html.I(className="bi bi-asterisk")], id='open-body-scroll-impact', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº of Publications by Type (Impact Scope) 💥'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the impact scope that motivates the document. With impact scope, we mean the related risks and benefits regarding the use of AI that motivate the type of regulation suggested by the document. For this, **three categories** were defined (these categories were *defined as mutually exclusive*):''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''- **Short-Termism:** this category is designed to encompass documents in which the scope of impact and preoccupation focus mainly on short-term problems, i.e., problems we are facing with current AI technologies (e.g., algorithmic discrimination, algorithmic opacity, privacy, legal accountability);  ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Long-Termism:** this category is designed to encompass documents in which the scope of impact and preoccupation focus mainly on long-term problems, i.e., problems we may come to face with future AI systems. Since such technologies are not yet a reality, such risks can be classified as hypothetical or, at best, uncertain (e.g., sentient AI, misaligned AGI, super intelligent AI, AI-related existential risks);''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Markdown('''- **Short-Termism & Long-Termism:** this category is designed to encompass documents in which the scope of impact is both short and long-term, i.e., they present a "mid-term" scope of preoccupation. These documents address issues related to the Short-Termism category, while also pointing out the long-term impacts of our current AI adoption (e.g., AI interfering in democratic processes, autonomous weapons, existential risks, environmental sustainability, labor displacement, the need for updating our educational systems).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''Looking at the totality of our sample size, we see clearly that **short-term (47%)** and **"mid-term" (i.e., Short-Termism & Long-Termism = 52%)** prevail over more **long-term preoccupations (2%)**. When we filter our sample by **impact scope and institution type**, it seems to us that **private corporations think more about the short-term (33%)**, **governmental institutions about the short/long-term (28%)**, and **academic (66%) and non-profit organizations (33%) with the long-term** impacts of AI technologies.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-impact',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-impact',
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

dff = pd.read_excel('meta_en.xlsx', 'principle_by_principle')

accountability = [dcc.Markdown(x) for x in list(
    dff['Accountability'].dropna(axis=0))]
beneficence = [dcc.Markdown(x)
               for x in list(dff['Beneficence'].dropna(axis=0))]
children = [dcc.Markdown(x) for x in list(
    dff["Children's Rights"].dropna(axis=0))]
dignity = [dcc.Markdown(x) for x in list(dff['Dignity'].dropna(axis=0))]
diversity = [dcc.Markdown(x) for x in list(dff['Diversity'].dropna(axis=0))]
freedom = [dcc.Markdown(x) for x in list(dff['Autonomy'].dropna(axis=0))]
education = [dcc.Markdown(x) for x in list(
    dff['Human Formation'].dropna(axis=0))]
alignment = [dcc.Markdown(x) for x in list(
    dff['Human Centeredness'].dropna(axis=0))]
intellectual = [dcc.Markdown(x) for x in list(
    dff['Intellectual Property'].dropna(axis=0))]
justice = [dcc.Markdown(x) for x in list(dff['Fairness'].dropna(axis=0))]
labor = [dcc.Markdown(x) for x in list(dff['Labor Rights'].dropna(axis=0))]
openess = [dcc.Markdown(x) for x in list(dff['Cooperation'].dropna(axis=0))]
privacy = [dcc.Markdown(x) for x in list(dff['Privacy'].dropna(axis=0))]
reliability = [dcc.Markdown(x)
               for x in list(dff['Reliability'].dropna(axis=0))]
sustainability = [dcc.Markdown(x) for x in list(
    dff['Sustainability'].dropna(axis=0))]
transparency = [dcc.Markdown(x)
                for x in list(dff['Transparency'].dropna(axis=0))]
truth = [dcc.Markdown(x) for x in list(dff['Truthfulness'].dropna(axis=0))]

accordion = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    accountability,
                    title="Accountability 👩🏾‍⚖️",
                ),
                dbc.AccordionItem(
                    beneficence,
                    title="Beneficence ⚕️",
                ),
                dbc.AccordionItem(
                    children,
                    title="Children's Rights 👶",
                ),
                dbc.AccordionItem(
                    dignity,
                    title="Human Rights ✊🏿",
                ),
                dbc.AccordionItem(
                    diversity,
                    title="Diversity 🌈",
                ),
                dbc.AccordionItem(
                    freedom,
                    title="Autonomy 🕊️",
                ),
                dbc.AccordionItem(
                    education,
                    title="Human Formation 📚",
                ),
                dbc.AccordionItem(
                    alignment,
                    title="Human-Centeredness 👨‍👨‍👦‍👦",
                ),
                dbc.AccordionItem(
                    intellectual,
                    title="Intellectual Property 🧠",
                ),
                dbc.AccordionItem(
                    justice,
                    title="Fairness ⚖️",
                ),
                dbc.AccordionItem(
                    labor,
                    title="Labor Rights 👷",
                ),
                dbc.AccordionItem(
                    openess,
                    title="Cooperation 🤝",
                ),
                dbc.AccordionItem(
                    privacy,
                    title="Privacy 🔒",
                ),
                dbc.AccordionItem(
                    reliability,
                    title="Reliability 💪",
                ),
                dbc.AccordionItem(
                    sustainability,
                    title="Sustainability ♻️",
                ),
                dbc.AccordionItem(
                    transparency,
                    title="Transparency 🕵",
                ),
                dbc.AccordionItem(
                    truth,
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
        dbc.Button(
            ['Divergence ', html.I(className="bi bi-arrow-left-right")], id='open-body-scroll-divergence', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Divergence in Definitions 🤔'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('''Here we can see cases of *"principle definition divergence,"* i.e., **divergent forms of defining ethical principles**. As an example, let us look at our most cited principle: **Transparency/Explainability/Auditability.**''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''When examining the definition proposed in "[ARCC: An Ethical Framework for Artificial Intelligence](https://www.tisi.org/13747):" ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Markdown('''- *"Promote algorithmic transparency and algorithmic audit, to achieve understandable and explainable AI systems. Explain the decisions assisted/made by AI systems when appropriate. Ensure individuals’ right to know, and provide users with sufficient information concerning the AI system’s purpose, function, limitation, and impact."* ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''In comparison with the one provided in "[A practical guide to Responsible Artificial Intelligence (AI)](https://www.pwc.com/gx/en/issues/data-and-analytics/artificial-intelligence/what-is-responsible-ai/responsible-ai-practical-guide.pdf):"''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Markdown('''- *"To instill trust in AI systems, people must be enabled to look under the hood at their underlying models, explore the data used to train them, expose the reasoning behind each decision, and provide coherent explanations to all stakeholders promptly. These explanations should be tailored to the different stakeholders, including regulators, data scientists, business sponsors, and end consumers."*''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''Both definitions seem similar, but the *"AI-devil is in the details."* Only the **first definition entails the concept of auditing,** which means (in some interpretations) a third-party review of the system in question. Also, while the first document mentions that *"one must explain,"* *"ensure the right,"* and *"provide enough information for people,"* clearly imposing the idea of a *"duty to explain"* (**without specifying who should explain**), together with the *"right to know"*,  the second document says that people have *"to be able to look under the hood"* (**also without specifying who should be able to look**), without bringing the idea of right or duty. Also, **only the second one proposes that this knowledge should be tailored and accessible to different types of stakeholders**, since an explanation fit for a machine learning engineer may not be fit for a consumer of an AI-empowered product.''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''Keeping in mind that the concept of **transparency/interpretability is a well-fundamental idea/concept in AI** (especially machine learning research), being still subject to divergence in its interpretation/application, what kinds of differences may occur when we look at *"not so well defined"* principles, like **human-centeredness.**''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''In "Data, Responsibly (Vol. 1) Mirror, Mirror," (Khan & Stoyanovich, [2020](https://dataresponsibly.github.io/comics/)), we find the following recommendation:''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Markdown('''- *"Maybe what we need instead is to ground the design of AI systems in people. Using the data of the people, collected and deployed with an equitable methodology as determined by the people, to create technology that is beneficial for the people."*''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''While in "[Everyday Ethics for Artificial Intelligence](https://www.ibm.com/watson/assets/duo/pdf/everydayethics.pdf)",the following norm is suggested:''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                       'text-justify': 'inter-word'}),
                    dcc.Markdown('''- *"AI should be designed to align with the norms and values of your user group in mind."*''', style={'font-size': FONT_SIZE,
                                                                                                                                          'text-align': 'justify',
                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''The first document mentions ideas like *"the use of an equitable methodology"* and *"technology that is beneficial for the people."* This idea of *"people"* seems to refer to a large and diverse group (perhaps "all people"). Meanwhile, the second specifically states *"your user group in mind,"*  which could mean *"a small and select group of people,"* if that is what the designers have in mind as *"their users."*''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''Many other differences can be found in our sample, for example:''', style={'font-size': FONT_SIZE,
                                                                                                               'text-align': 'justify',
                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''- “[Tieto's AI ethics guidelines](https://www.tietoevry.com/en/newsroom/all-news-and-releases/press-releases/2018/10/tieto-strengthens-commitment-to-ethical-use-of-ai/)” takes a different take on explainability, saying its systems *“can be explained and explain itself”*, potting some of the responsibility of explainability in the **AI system itself**, making it a “stakeholder” in the accountability chain (a curious approach); ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Markdown('''- “[The Toronto Declaration](https://www.torontodeclaration.org/declaration-text/english/)” gives an extensive and nonexhaustive definition of what *“discrimination”* means under international laws, while most other documents resume themselves in only citing the concept, leaving open to interpretation the types of *“discrimination that is permissible”*;''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}),
                    dcc.Markdown('''- In “[Artificial Intelligence and Machine Learning: Policy Paper](https://www.internetsociety.org/resources/doc/2017/artificial-intelligence-and-machine-learning-policy-paper/)”, fairness is related to the idea of *“AI provides socio-economic opportunities for all”* (**benefits**), in “[Trustworthy AI in Aotearoa: AI Principles](https://aiforum.org.nz/wp-content/uploads/2020/03/Trustworthy-AI-in-Aotearoa-March-2020.pdf)” fairness is also defined as *“AI systems do not unjustly harm”* (**impacts**), which we can relate to the **difference between certain notions of algorithmic fairness** (predictive parity vs equalized odds); ''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Markdown('''- While some documents (e.g., “[Telefónica's Approach to the Responsible Use of AI](https://www.telefonica.com/en/wp-content/uploads/sites/5/2021/08/ia-responsible-governance.pdf)”) state how privacy and security are essential for AI systems developments, only some (e.g., “[Big Data, Artificial Intelligence, Machine Learning, and Data Protection](https://ico.org.uk/media/for-organisations/documents/2013559/big-data-ai-ml-and-data-protection.pdf)”) specify what *“good privacy criteria”* are (e.g., **data minimization**).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}),
                    dcc.Markdown('''- While most documents interpret accountability/liability as *“developers being responsible for their projects”* (e.g., “[Declaration of Ethical Principles for AI in Latin America](https://ia-latam.com/etica-ia-latam/)”), **some documents also put this responsibility on users**, and even algorithms “themselves” (e.g., “[The Ethics of Code: Developing AI for Business with Five Core Principles](https://www.sage.com/~/media/group/files/business-builders/business-builders-ethics-of-code.pdf?la=en)”).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('''Besides the ones mentioned above, many other forms of comparisons can be made using our dataset (available for download at the bottom of this page).''', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        outline=True,
                        size='xl',
                        id='close-body-scroll-divergence',
                        className='ms-auto',
                        n_clicks=0,
                        color=CLOSE_BUTTON
                    )
                ),
            ],
            id='modal-body-scroll-divergence',
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
        dbc.Button(
            ['Ethical Principles ', html.I(className="bi bi-search-heart")], id='open-offcanvas', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Offcanvas(
            [modal_divergence, accordion],
            id="offcanvas",
            scrollable=True,
            title="Ethical Principles 🌈👨‍👨‍👦‍👦🕊️✊🏿👷♻️",
            placement='end',
            is_open=False,
            style={'width': '50vw'}
        ),
    ], style={'display': 'inline-block', 'margin-left': '15px'}
)

badges = html.Span([
    dbc.Badge([html.I(className="bi bi-heart-fill"), "  Open-Source"], href="https://github.com/Nkluge-correa/worldwide_AI-ethics",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
    dbc.Badge([html.I(className="bi bi-robot"), "  AIRES at PUCRS"], href="https://en.airespucrs.org/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
    dbc.Badge([html.I(className="bi bi-filetype-py"), "  Made with Python"], href="https://www.python.org/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
    dbc.Badge([html.I(className="bi bi-github"), "  Made by Nkluge-correa"], href="https://nkluge-correa.github.io/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'})
])

download_data = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  Data'], id='btn_data',
               outline=False, color='secondary'),
    dcc.Download(id="download-data")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})

download_html = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  HTML'], id='btn_html',
               outline=False, color='secondary'),
    dcc.Download(id="download-html")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})

download_png = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  PNG'], id='btn_png',
               outline=False, color='secondary'),
    dcc.Download(id="download-png")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})

download_png = html.Div([
    dbc.Button('Download PNG files', id='btn_png',
               outline=False, color='secondary'),
    dcc.Download(id="download-png")
], style={
    'margin-right': '5px',
    'margin-left': '5px',
    'display': 'inline-block'})


app = dash.Dash(__name__,
                meta_tags=[
                    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                external_stylesheets=[dbc.themes.SLATE, dbc.icons.BOOTSTRAP])

server = app.server
app.title = 'Worldwide AI Ethics 🌐'


app.layout = dbc.Container(
    fluid=True,
    children=[
        html.H1('Worldwide AI Ethics 🌍🌎🌏', style={'textAlign': 'center',
                                                  'margin-top': '20px'}),
        html.Div([badges], style={
                 'textAlign': 'center'}),
        html.Div([modal_article, offcanvas], style={
                 'textAlign': 'center', 'margin-top': '20px'}),
        dbc.Row([
            dbc.Col([
                    table
                    ], md=2),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        modal_map,
                        dcc.Graph(id='map', figure=fig2)
                    ], md=4),
                    dbc.Col([
                        modal_institution,
                        dcc.Graph(id='institution', figure=fig3)
                    ], md=4),
                    dbc.Col([
                        modal_gender,
                        dcc.Graph(id='gender', figure=fig4)
                    ], md=4),

                ]),
                dbc.Row([
                    dbc.Col([
                        modal_principles,
                        dcc.Graph(id='principles', figure=fig5)
                    ], md=4),
                    dbc.Col([
                        modal_years,
                        dcc.Graph(id='years', figure=fig6)
                    ], md=8),
                ]),
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
                        dcc.Graph(id='genergrgder', figure=fig10)
                    ], md=3),
                ]),

            ], md=10),
        ]),
        dbc.Row([
            dbc.Col([
                download_data, download_html, download_png
            ], md=12, style={'textAlign': 'center', 'margin-top': '10px', 'margin-bottom': '30px'})
        ])


    ])


@app.callback(
    Output('modal-fs', 'is_open'),
    [
        Input('open-fs', 'n_clicks'),
        Input('close-fs', 'n_clicks'),
    ],
    [State('modal-fs', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-map', 'is_open'),
    [
        Input('open-body-scroll-map', 'n_clicks'),
        Input('close-body-scroll-map', 'n_clicks'),
    ],
    [State('modal-body-scroll-map', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-institution', 'is_open'),
    [
        Input('open-body-scroll-institution', 'n_clicks'),
        Input('close-body-scroll-institution', 'n_clicks'),
    ],
    [State('modal-body-scroll-institution', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-gender', 'is_open'),
    [
        Input('open-body-scroll-gender', 'n_clicks'),
        Input('close-body-scroll-gender', 'n_clicks'),
    ],
    [State('modal-body-scroll-gender', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-principle', 'is_open'),
    [
        Input('open-body-scroll-principle', 'n_clicks'),
        Input('close-body-scroll-principle', 'n_clicks'),
    ],
    [State('modal-body-scroll-principle', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-years', 'is_open'),
    [
        Input('open-body-scroll-years', 'n_clicks'),
        Input('close-body-scroll-years', 'n_clicks'),
    ],
    [State('modal-body-scroll-years', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-nature', 'is_open'),
    [
        Input('open-body-scroll-nature', 'n_clicks'),
        Input('close-body-scroll-nature', 'n_clicks'),
    ],
    [State('modal-body-scroll-nature', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-regulation', 'is_open'),
    [
        Input('open-body-scroll-regulation', 'n_clicks'),
        Input('close-body-scroll-regulation', 'n_clicks'),
    ],
    [State('modal-body-scroll-regulation', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-normative', 'is_open'),
    [
        Input('open-body-scroll-normative', 'n_clicks'),
        Input('close-body-scroll-normative', 'n_clicks'),
    ],
    [State('modal-body-scroll-normative', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-impact', 'is_open'),
    [
        Input('open-body-scroll-impact', 'n_clicks'),
        Input('close-body-scroll-impact', 'n_clicks'),
    ],
    [State('modal-body-scroll-impact', 'is_open')],
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
        'data_en.rar')


@app.callback(
    Output("download-html", "data"),
    Input("btn_html", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'html_files.rar')


@app.callback(
    Output("download-png", "data"),
    Input("btn_png", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'png_files.rar')


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
    Output('modal-body-scroll-divergence', 'is_open'),
    [
        Input('open-body-scroll-divergence', 'n_clicks'),
        Input('close-body-scroll-divergence', 'n_clicks'),
    ],
    [State('modal-body-scroll-divergence', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=False)
