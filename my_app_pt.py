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

dff = pd.read_excel('arxiv_submissions_data_pt.xlsx',
                    'Arxiv').set_index('Date')

fig = go.Figure(layout={'template': 'plotly_dark'})
for column in dff.columns:
    fig.add_trace(go.Scatter(x=dff.index, y=dff[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='Nº de Submissões (' +
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

dff = pd.read_excel('arxiv_submissions_data_pt.xlsx',
                    'Arxiv(CS)').set_index('Date')

fig1 = go.Figure(layout={'template': 'plotly_dark'})
for column in dff.columns:
    fig1.add_trace(go.Scatter(x=dff.index, y=dff[column],
                              line=dict(width=3), name=column, mode='lines',
                              hoverlabel=dict(namelength=-1),
                              hovertemplate='Nº de Submissões (' +
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
        dbc.Button(['Artigo ', html.I(className="bi bi-file-text-fill")],
                   id='open-fs', outline=False, color=OPEN_BUTTON),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Worldwide AI Ethics: a review of *200* guidelines and recommendations for AI governance  🌐', ), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Desde o final do nosso último *“inverno da IA",* 1987 – 1993, a pesquisa em IA e sua indústria têm visto um crescimento maciço, seja em tecnologias desenvolvidas, investimentos, atenção da mídia ou novas tarefas que sistemas autônomos são hoje, capazes de realizar. Se olharmos para a história das submissões no ArXiv ([entre 2009 e 2021](https://arxiv.org/about/reports/submission_category_by_year)), um repositório de preprints e publicações eletrônicas de acesso aberto, a partir de 2018, **trabalhos relacionados à Ciência da Computação têm sido o tipo mais comum de material submetido.**', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_sub', figure=fig), html.Br(),
                    dcc.Markdown('Além disso, quando examinamos apenas a categoria de Ciências da Computação, **" Visão Computacional e Reconhecimento de Padrões", "Aprendizagem de Máquina",** e **"Computação e Linguagem"** são os tipos de subcategorias mais apresentados. **Note que todas estas são áreas onde a aprendizagem de máquina se encontra estabelecida como seu paradigma atual.**', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_CS', figure=fig1), html.Br(),
                    dcc.Markdown('Além do número de publicações sendo produzidos, nunca tivemos mais capital sendo investido em empresas e startups, seja por governos ou fundos de *venture capital*. **( mais de 90 bilhões de USD$ em 2021 só nos EUA)**, e patentes relacionadas à IA sendo registradas (Zhang et al., [2022](https://aiindex.stanford.edu/report/)). Esta rápida expansão do campo/indústria da IA também veio com outro boom, o *"boom da ética da IA",* onde uma exigência nunca antes vista de regulamentação e orientação normativa de tais tecnologias foi manifestada. Baseando-se no trabalho realizado por outros meta-analistas do campo, **este estudo apresenta uma revisão sistemática de 200 documentos relacionados à ética e governança da IA.** Nós apresentamos uma coleção de **tipologias usadas para classificar nossa amostra**, tudo condensado em uma ferramenta on-line **interativa e de acesso aberto**, juntamente com uma análise crítica daquilo que *"está sendo dito"* e *"quem o está dizendo"* em nosso panorama global da ética da IA.', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('### Citar como 🤗'),
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
                            dbc.Badge([html.I(className="bi bi-envelope"), "  Contate-nos"], href="mailto:airespucrs@airespucrs.org",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-bar-chart-fill"), "  Power BI Version"], href="https://www.airespucrs.org/worldwide-ai-ethics",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-file-pdf-fill"), "  Artigo Completo"], href="https://doi.org/10.48550/arXiv.2206.11922",
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_text')

names = []
for i in range(len(dff['Document Title'])):
    x, y = dff['Document Title'][i], dff['Document URL'][i]
    names.append(f'[{x}]({y})')

df = pd.DataFrame({
    'Documentos': names,
    'Abstract': list(dff['Abstract'])
})

table = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c, 'presentation': 'markdown'}
             for c in ['Documentos']],
    tooltip_data=[{
        'Documentos': {'value': row['Abstract'], 'type': 'markdown'},
    } for row in df.to_dict('records')],
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color: #272b30; color: white; bottom: auto;'
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
        'fontSize': 22
    },
)

dff = pd.read_excel('meta_pt.xlsx', 'meta_countries')

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
            ['Publicações por País ', html.I(className="bi bi-flag-fill")], id='open-body-scroll-map', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Publicações por País 🏳️‍🌈'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Olhando para a distribuição entre regiões do mundo (agregadas por continente), vemos que a maior parte dos documentos produzidos vem da **Europa, América do Norte e Ásia**, enquanto regiões como **América do Sul, África e Oceania representam menos de 4,5% de toda a nossa amostra**. Se não fosse pela **participação significativa de Organizações Intergovernamentais,** como a OTAN, NU, UNESCO, **que representam 6% de nossa amostra (13 documentos),** outras regiões/países do mundo estariam ainda mais sub representadas.', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('77% do tamanho total de nossa amostra é composta por 13 países, **Estados Unidos da América, Reino Unido, Alemanha, Canadá, China, Japão, França, Finlândia, Holanda, Suíça, Bélgica, Brasil e Coréia do Sul,** enquanto uma miríade de **24 países (12,5%) representam o restante de nossa amostra**, juntamente com organizações intergovernamentais, como a União Europeia (9 = 4,5%) e as NU (6 = 3%).', style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_institutions')

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
            ['Instituições ', html.I(className="bi bi-building")], id='open-body-scroll-institution', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo de Instituição 🏢'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Com exceção de instituições como **IBM (5)**, **Microsoft (4)**, e **UNESCO (3)**, **a maioria das outras instituições não têm mais do que dois documentos publicados**. Observamos também que **a maior parte de nossa amostra foi produzida por instituições governamentais e corporações privadas (48%)**,  seguidas por **ONGs (17%)**, **Organizações Sem Fins Lucrativos (16%)**, e **Instituições Acadêmicas (12,5%)**. ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("No entanto, **esta tendência só se segue se olharmos para a totalidade de nossa amostra**. Se olharmos para os documentos produzidos por **continentes**,  vemos que, por exemplo, na **América do Norte (69), corporações privadas (24 = 34,7%) e organizações sem fins lucrativos (18 = 26%) produziram o maior número de documentos**, seguidas de instituições governamentais (12 = 17,4%). Ao mesmo tempo, quando olhamos para **Europa**, a **tendência global é restaurada**. ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Uma análise aprofundada **segmentada por países** mostra que o **engajamento** de certos tipos de **AI stakeholders** (i.e., tipos de instituições) **difere por países.** Por exemplo, na **China (11),  a maioria dos documentos foram produzidos por instituições acadêmicas (5 = 45,4%), enquanto que na Alemanha (20), a maioria dos documentos de nossa amostra foram produzidas por corporações privadas (6 = 30%), e NGOs (4 = 20%).** Outros insights podem ser encontrados em nosso [Power BI dashboard](https://www.airespucrs.org/worldwide-ai-ethics).", style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_gender')

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
            ['Gênero ', html.I(className="bi bi-gender-ambiguous"),
             html.I(className="bi bi-gender-female"),
             html.I(className="bi bi-gender-male"),
             html.I(className="bi bi-gender-trans")], id='open-body-scroll-gender', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Autores por Gênero 🧍‍♂️ ♂ ☿ ♀ 💃'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Ao remover documentos com autores não especificados, contamos um total de **561 autores homens (66,6%)** e **281 autoras mulheres (33,3%).** A predominância do gênero masculino é **uma tendência que pode ser encontrada em praticamente todas as regiões e países do mundo, independentemente do tipo de instituição.**', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('O gênero dos autores foi determinado pela busca de seus nomes e imagens de perfil em diferentes tipos de plataformas (e.g.,, *LinkedIn, Researchgate, sites universitários, sites pessoais, etc.*) através de motores de busca.', style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_principles')

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

dff = pd.read_excel('meta_pt.xlsx', 'Accountability_gram')

figa = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figa.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Beneficence_gram')

figb = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figb.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Children_gram')

figc = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figc.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Dignity_gram')

figd = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figd.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Diversity_gram')

fige = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
fige.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Freedom_gram')

figf = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figf.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Formation_gram')

figg = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figg.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Centeredness_gram')

figh = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figh.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Property_gram')

figi = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figi.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Justice_gram')

figj = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figj.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Labor_gram')

figk = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figk.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)

dff = pd.read_excel('meta_pt.xlsx', 'Open_gram')

figl = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figl.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Privacy_gram')

figm = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figm.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Reliability_gram')

fign = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
fign.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Sustainability_gram')

figo = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figo.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Transparency_gram')

figp = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
figp.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


dff = pd.read_excel('meta_pt.xlsx', 'Truthfulness_gram')

figq = px.bar(dff, x='Top four-grams', y='Contagem de palavras',
              color='Contagem de palavras', color_continuous_scale='oryel')
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
            ['Citações por Princípio ', html.I(className="bi bi-search")], id='open-body-scroll-principle', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Citações por Princípio 🔍'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Os **cinco principais princípios** defendidos nos documentos de nossa amostra são semelhantes aos resultados obtidos por Jobin et al. ([2019](https://www.nature.com/articles/s42256-019-0088-2)) e Hagendorff ([2020](https://link.springer.com/article/10.1007/s11023-020-09517-8)), **com o acréscimo de Confiabilidade/Segurança/Confiança/Fiabilidade (78%)**, que também são citados como um dos cinco principais na metanálise de Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)) **(80%)**. Como cada documento apresenta sua própria passagem sobre cada princípio, se existiam, por exemplo, 134 documentos que citam o princípio de privacidade, coletamos 134 definições/recomendações diferentes envolvendo este princípio. Todos sendo acessíveis em nosso [Power BI dashboard](https://www.airespucrs.org/worldwide-ai-ethics).", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Olhando para a **distribuição de princípios filtrada por continente**, **os cinco principais princípios continuam os mesmos** tanto na **América do Norte** como **Europa**. Já no **continente asático** é introduzido o princípio de **Beneficência/Não-maleficência como o 5º (74%) princípio mais citado**, colocando Responsabilidade/Responsabilização em 6º lugar (70%). **Filtrando nossos resultados por país**, não vemos **nenhuma mudança nos cinco principais princípios ** quando comparado aos **EUA** e **RU**. Entretanto, olhando **além dos cinco mais citados princípios**, nós começamos a ver **diferenças**, como **Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica (38%)** e  **Beneficência/Não-maleficência (34,4%)** sendo o **6º** e **7º princípios mais citados nos EUA**, e **Código aberto/Concorrência Justa/Cooperação (45,8%)** e **Diversidade/Inclusão/Pluralismo/Acesbilidade (41,6%)** sendo o **6º** e **7º princípios mais citados no UK**.", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Ao examinar a **distribuição de princípios filtrados por tipo de instituição**, podemos chegar a vários insights. Por exemplo, olhando para nossa amostra total, percebe-se que a **maior preocupação de instituições governamentais** (em todo o mundo) e a necessidade de **sistemas transparentes (89,5%)**, **corporações privadas** defendem principalmente **Confiabilidade e Segurança (87,5%)**, enquanto que **Organizações sem fins lucrativos e ONGs** defendem principalmente a **Jusiça (88,2%)**. ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Para criar uma **definição geral** de cada princípio/grupo de princípios, utilizamos uma técnica de **[mineração de texto](https://en.wikipedia.org/wiki/Text_mining)** chamada de **[análise de n-gramas](https://en.wikipedia.org/wiki/N-gram)**, onde contamos a repetição sucessiva de palavras (e grupos de palavras) em cada princípio encontrado nos documentos de nossa amostra. Assim, as definições abaixo foram criadas para contemplar os temas recorrentes que encontramos. *Abaixo também apresentamos gráficos de contagem de quatro-gramas de cada princípio.*", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("- **Responsabilidade/Responsabilização:** responsabilidade refere-se à ideia de que os desenvolvedores e implementadores de tecnologias de IA devem estar em conformidade com os órgãos reguladores, o que também significa que tais atores devem ser responsáveis por suas ações e pelos impactos causados por suas tecnologias;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}),
                    dcc.Graph(id='account',
                              figure=figa), html.Br(),
                    dcc.Markdown("- **Beneficência/Não-maleficência:** beneficência e não-maleficência são conceitos que oriundos da bioética e da ética médica. Na ética da IA, esses princípios afirmam que o bem-estar humano (e a aversão ao dano) devem ser o objetivo deste tipo de tecnologia. Algumas vezes, este princípio também está ligado à ideia de Sustentabilidade, afirmando que a IA deve ser benéfica não apenas para a civilização humana, mas para nosso meio ambiente e outros seres vivos; ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}),
                    dcc.Graph(id='benef', figure=figb), html.Br(),
                    dcc.Markdown("- **Direitos da Criança e do Adolescente:** a ideia de que os direitos das crianças e adolescentes devem ser respeitados por tecnologias que utilizam de IA. AI stakeholders devem salvaguardar, respeitar e estar cientes das fragilidades associadas aos jovens;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Graph(id='child', figure=figc), html.Br(),
                    dcc.Markdown("- **Dignidade/Direitos Humanos:** este princípio se baseia na ideia de que todos os indivíduos merecem tratamento adequado, dignidade e respeito. Na ética da IA, o respeito à dignidade humana está frequentemente ligado aos direitos humanos (i.e., a Declaração Universal dos Direitos Humanos); ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}),
                    dcc.Graph(id='digni', figure=figd), html.Br(),
                    dcc.Markdown("- **Diversidade/Inclusão/Pluralismo/Acessibilidade:** este conjunto de princípios defende a ideia de que o desenvolvimento e o uso das tecnologias de IA devem ser feitos de forma inclusiva e acessível, respeitando as diferentes formas que a entidade humana pode vir a se expressar (gênero, etnia, raça, orientação sexual, deficiências, etc.). Este grupo de princípios está fortemente ligado a outro conjunto de princípios: Justiça/Equidade/Igualdade/Não-discriminação; ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}),
                    dcc.Graph(id='diver', figure=fige), html.Br(),
                    dcc.Markdown("- **Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica:** este conjunto de princípios defende a ideia de que a autonomia da tomada de decisão humana deve ser preservada durante as interações humano-IA, quer essa escolha seja individual ou conjunta, como a inviolabilidade dos direitos e valores democráticos, estando também ligada à auto-suficiência tecnológica das Nações/Estados;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}),
                    dcc.Graph(id='free', figure=figf), html.Br(),
                    dcc.Markdown("- **Educação/Formação Humana:** tais princípios defendem a ideia de que a formação e educação humana deve ser priorizada em nossos avanços tecnológicos. Tecnologias que utilizam de IA exigem um nível considerável de especialização para serem produzidas e operadas, e tal conhecimento deve ser acessível a todos. Este princípio parece estar fortemente ligado aos Direitos Trabalhistas. A grande maioria dos documentos relativos aos trabalhadores e à vida profissional apontam para a necessidade de reeducar e requalificar a força de trabalho como uma estratégia de mitigação do desemprego tecnológico;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                    dcc.Graph(id='educa', figure=figg), html.Br(),
                    dcc.Markdown("- **Centrado no Ser Humano/Alinhamento:** tais princípios defendem a ideia de que os sistemas de IA devem ser centrados e alinhados com valores humanos. Tecnologias que utilizam de IA devem ser adaptadas para se alinharem com nossos valores (e. g., design sensível a valores). Este princípio também é usado como uma categoria 'coringa', muitas vezes sendo definido como um conjunto de 'princípios que são valorizados pelos humanos' (e. g., liberdade, privacidade, não-discriminação, etc.);", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}),
                    dcc.Graph(id='align', figure=figh), html.Br(),
                    dcc.Markdown("- **Propriedade Intelectual:** este princípio procura fundamentar os direitos de propriedade sobre produtos e/ou processos de conhecimento gerado por indivíduos, sejam eles tangíveis ou intangíveis;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Graph(id='intellec',
                              figure=figi), html.Br(),
                    dcc.Markdown("- **Justiça/Equidade/Igualdade/Não-discriminação:** este conjunto de princípios sustenta a ideia de não-discriminação e mitigação de preconceitos (sistemas de IA podem estar sujeitos a preconceitos algorítmicos discriminatórios). Aqui também se defende a ideia de que, independentemente dos diferentes atributos sensíveis que possam caracterizar um indivíduo, todos devem ser tratados 'justamente';", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Graph(id='justice',
                              figure=figj), html.Br(),
                    dcc.Markdown("- **Direitos Trabalhistas:** Os direitos trabalhistas são direitos legais e humanos relacionados às relações de trabalho entre trabalhadores e empregadores. Na ética da IA, este princípio enfatiza que os direitos dos trabalhadores devem ser preservados, independentemente de que as relações de trabalho estejam ou não sendo mediadas por tecnologias que utilizam de IA. Uma das principais preocupações apontadas quando este princípio é apresentado é a mitigação do desemprego tecnológico (e. g., , através da Educação/Formação Humana);", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Graph(id='labor', figure=figk), html.Br(),
                    dcc.Markdown("- **Código Aberto/Concorrência Justa/Cooperação:** este conjunto de princípios defende diferentes meios pelos quais ações conjuntas podem ser estabelecidas e cultivadas entre AI stakeholders para alcançar objetivos comuns. Também defende-se o intercâmbio livre e aberto de ativos valiosos para a IA (e. g., dados, conhecimento, direitos de patente, recursos humanos) para mitigar possíveis monopólios tecnológicos;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Graph(id='open', figure=figl), html.Br(),
                    dcc.Markdown("- **Privacidade:** a ideia de privacidade pode ser definida como o direito do indivíduo de 'expor-se voluntariamente, e na medida do desejado, ao mundo'. Na ética da IA, este princípio sustenta o direito de uma pessoa a controlar a exposição e disponibilidade de informações pessoais quando extraídas como dados de treinamento para sistemas de IA. Este princípio também está relacionado a conceitos tais como minimização de dados, anonimato, consentimento informado e outros conceitos relacionados à proteção de dados; ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}),
                    dcc.Graph(id='privacy',
                              figure=figm), html.Br(),
                    dcc.Markdown("- **Confiabilidade/Segurança/Confiança/Fiabilidade:** este conjunto de princípios sustenta a ideia de que as tecnologias de IA devem ser confiáveis, no sentido de que seu uso pode ser comprovadamente atestado como seguro e robusto, promovendo a confiança do usuário e uma melhor aceitação das tecnologias de IA; ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                    dcc.Graph(id='reliab', figure=fign), html.Br(),
                    dcc.Markdown("- **Sustentabilidade:** este princípio pode ser entendido como uma forma de 'justiça intergeracional', onde o bem-estar das gerações futuras também deve ser considerado durante o desenvolvimento da IA. Na ética da IA, sustentabilidade se refere à ideia de que o desenvolvimento de tecnologias de IA deve ser realizado com consciência de suas implicações a longo prazo, tais como custos ambientais e preservação/bem estar da vida não-humana;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                    dcc.Graph(id='sustaina',
                              figure=figo), html.Br(),
                    dcc.Markdown("- **Transparência/Explicabilidade/Auditoria:** este conjunto de princípios apoia a ideia de que o uso e desenvolvimento da IA deve ser feito de forma transparente para todos stakeholders. A transparência pode estar relacionada com 'a transparência de uma organização' ou 'a transparência de um algoritmo'. Este conjunto de princípios também está relacionado à ideia de que tais informações devem ser compreensíveis para não especialistas, e, quando necessário, sujeitas a auditoria;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Graph(id='trans', figure=figp), html.Br(),
                    dcc.Markdown("- **Veracidade:** este princípio sustenta a ideia de que a IA deve fornecer informações verdadeiras. Está também relacionado à ideia de que as pessoas não devem ser enganadas quando interagem com sistemas de IA. Este princípio está fortemente relacionado com a mitigação de meios automatizados de desinformação.", style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_year')

fig6 = go.Figure(data=go.Scatter(x=list(dff['Years']), y=list(dff['Nº of Published Documents']), mode='lines+markers',
                                 name='',
                                 line=dict(color=COLOR_GRAPHS_HEX, width=6),
                                 marker=dict(size=12),
                                 connectgaps=True,
                                 hovertemplate='<b>Nº de Publicações</b>: %{y} <extra></extra>'
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
            ['Nº de Publicações por Ano ', html.I(className="bi bi-calendar-fill")], id='open-body-scroll-years', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Ano 📅'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Com respeito ao ano de publicação dos documentos de nossa amostra, **vemos que a maioria dos documentos (129 = 64,5%) foram publicados entre os anos 2017 e 2019.** O que podemos chamar de *"boom da ética da IA"* trata-se da **produção significativa de documentos no ano 2018**, o que representa **30,5% (61)** de toda a nossa amostra.', style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('**Nota:** documentos com datas de publicação **não especificadas (27 = 13,5%)** também são bastante **prevalentes** em nossa amostra.', style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_nature')

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
            ['Natureza/Conteúdo ', html.I(className="bi bi-file-earmark-text-fill")], id='open-body-scroll-nature', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Natureza/Conteúdo) 📝'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado com a natureza/conteúdo do documento, e **três categorias** foram definidas (essas categorias *não foram definidas como mutuamente exclusivas*):", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                       'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("- **Descritivo:** Os documentos descritivos tomam o esforço de apresentar definições factuais relacionadas à IA. Estas definições servem para contextualizar 'o que queremos dizer' quando falamos de IA, e como o vocabulário utilizado neste campo pode ser compreendido;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Normativo:** documentos normativos apresentam normas, princípios éticos, recomendações e afirmações imperativas sobre como tais tecnologias devem ou não ser utilizadas/desenvolvidas;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                      'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Prático:** documentos práticos apresentam ferramentas de desenvolvimento para implementar princípios e normas éticas, sejam elas qualitativas (e. g., pesquisas de auto-avaliação) ou quantitativas (e. g., *Algoritmos de Debiasing* para modelos de ML).", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("A maior parte da nossa amostra é composta de **amostras normativas (96%)**, sendo que  **um terço desta amostra também apresenta conteúdo descritivo (55,5%)**, e mais **raramente**, implementações **práticas (27%)**.", style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_regulation')

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
            ['Regulação ', html.I(className="bi bi-rulers")], id='open-body-scroll-regulation', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Regulação) 📏'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado com a forma de regulamentação que o documento propõe. Para isso, foram definidas **três categorias** (estas categorias foram *definidas como mutuamente exclusivas*):", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("- **Regulamentação Governamental:** esta categoria foi definida para abranger estritamente documentos feitos por instituições governamentais, com o fim de regular o uso e desenvolvimento da IA, rigorosamente (regulamentos juridicamente vinculativos) ou suavemente (diretrizes juridicamente não vinculativas);", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Auto-regulamentação/Auto-regulamentação Voluntária:** esta categoria foi definida para englobar documentos feitos por organizações privadas e outros órgãos que defendem uma forma de auto-regulamentação governada pela própria indústria da IA. Ela também abrange o auto-compromisso voluntário feito por organizações independentes (ONGs, Associações Profissionais, etc.);", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Recomendação:** esta categoria foi definida para englobar documentos que apenas sugerem possíveis formas de governança e princípios éticos que devem orientar as organizações que buscam usar, desenvolver ou regular as tecnologias de IA.", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Quando analisamos a forma de regulamentação proposta pelos documentos de nossa amostra, **mais da metade (56%) são apenas recomendações** para diferentes stakeholders, enquanto que **24% dos documentos analisados foram enquadrados na categoria auto-regulamentação/auto-regulamentação voluntária**, e somente **20%** propuseram uma **forma de regulação administrada por um dado estado/país**.", style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_normative')

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
            ['Força Normativa ', html.I(className="bi bi-lightning-fill")], id='open-body-scroll-normative', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Força Normativa) ⚡'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado à força normativa do mecanismo de regulamentação proposto pelo documento. Para isso, foram definidas **duas categorias** (estas categorias *não foram definidas como mutuamente exclusivas*):", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("- **Diretivas juridicamente não vinculativas:** estes documentos propõem uma abordagem que entrelaça princípios éticos com práticas recomendadas para empresas e outras entidades (i. e., soluções jurídicas não vinculativas);", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Regulamentos juridicamente vinculativos:** estes documentos propõem uma abordagem que se concentra na regulamentação de usos específicos da IA em regulamentos juridicamente vinculativos, como exigências e proibições obrigatórias.", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("A falta de convergência para uma forma de regulamentação mais **'baseada no governo'** se reflete na força normativa dos documentos analisados, onde a **vasta maioria (98%) serve apenas como 'leis brandas'**, ou seja, tais diretrizes não implicam qualquer forma de obrigação legal, enquanto **somente 4,5% apresentam formas mais rígidas de regulamentação.** Uma vez que apenas as instituições governamentais podem apresentar normas legalmente vinculativas (outras formas de instituições não possuem tal poder), e **instituições governamentais produziram apenas 24% de nossa amostra**, alguns podem argumentar que esse desequilíbrio reside nesse fato.", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Entretanto, **filtrando** somente os documentos produzidos por **instituições governamentais**, a **desproporção não desaparece**, com **somente 18,7% dos documentos propondo formas de regulamentação juridicamente vinculativas**. Os países que parecem estar à frente desta, ainda fraca, tendência são **Canadá**, **Alemanha**, e o **Reino Unido**, com a Austrália, Noruega, e os EUA vindo logo atrás.", style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'meta_impact')

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
            ['Escopo de Impacto ', html.I(className="bi bi-asterisk")], id='open-body-scroll-impact', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Escopo de Impacto) 💥'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado com o escopo de impacto que motiva o documento. Com escopo de impacto, nos referimos aos riscos e benefícios relacionados ao uso da IA que motivam o tipo de regulamentação sugerida pelo documento. Para isso, **três categorias** foram definidas (estas categorias foram *definidas como mutuamente exclusivas*):", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("- **Short-Termism:** esta categoria foi definida para englobar documentos nos quais o escopo do impacto e da preocupação se concentra principalmente em problemas de curto prazo, ou seja, problemas que estamos enfrentando com as atuais tecnologias de IA (e. g., discriminação algorítmica, opacidade algorítmica, privacidade, responsabilidade legal);  ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Long-Termism:** esta categoria foi definida para englobar documentos nos quais o escopo do impacto e da preocupação se concentra principalmente em problemas de longo prazo, ou seja, problemas que podemos vir a enfrentar com futuros sistemas de IA. Como tais tecnologias ainda não são uma realidade, tais riscos podem ser classificados como hipotéticos ou, na melhor das hipóteses, incertos (e. g, IA senciente, AGI desalinhada, IA super inteligente, riscos existenciais relacionados à IA);", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}),
                    dcc.Markdown("- **Short-Termism & Long-Termism:** esta categoria foi projetada para englobar documentos nos quais o escopo do impacto é tanto de curto como de longo prazo, ou seja, eles apresentam um escopo de 'médio prazo' de preocupação. Estes documentos abordam questões relacionadas à categoria de curto prazo, ao mesmo tempo em que apontam os impactos de longo prazo de nossa atual adoção da IA (e. g., interferência da IA nos processos democráticos, armas autônomas, riscos existenciais, sustentabilidade ambiental, deslocamento de mão-de-obra, a necessidade de atualizar nossos sistemas educacionais).", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Olhando para a totalidade de nossa amostra, vemos claramente que **curto (47%)** e **'médio prazo' (i.e., Short-Termism & Long-Termism = 52%)** prevalecem sobre **preocupações a longo prazo (2%)**. Quando filtramos nossa amostra por **escopo de impacto a tipo de instituição** nós vemos que **corporações privadas pensam sobre os impactos relacionados a IA mais a curto prazo(33%)**, enquanto que **instituições governamentais tendem a focar no médio prazo (28%)**, e **instituições acadêmicas (66%) e organizações sem fins lucrativos (33%) são as que mais levantam questões definidas como long-term.**", style={'font-size': FONT_SIZE,
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

dff = pd.read_excel('meta_pt.xlsx', 'principle_by_principle')

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
                    title="Responsabilidade 👩🏾‍⚖️",
                ),
                dbc.AccordionItem(
                    beneficence,
                    title="Beneficência ⚕️",
                ),
                dbc.AccordionItem(
                    children,
                    title="Direitos da Criança 👶",
                ),
                dbc.AccordionItem(
                    dignity,
                    title="Direitos Humanos ✊🏿",
                ),
                dbc.AccordionItem(
                    diversity,
                    title="Diversidade 🌈",
                ),
                dbc.AccordionItem(
                    freedom,
                    title="Autonomia 🕊️",
                ),
                dbc.AccordionItem(
                    education,
                    title="Formação Humana 📚",
                ),
                dbc.AccordionItem(
                    alignment,
                    title="Centrado no Ser Humano 👨‍👨‍👦‍👦",
                ),
                dbc.AccordionItem(
                    intellectual,
                    title="Propriedade Intelectual 🧠",
                ),
                dbc.AccordionItem(
                    justice,
                    title="Não-discriminação ⚖️",
                ),
                dbc.AccordionItem(
                    labor,
                    title="Direitos Trabalhistas 👷",
                ),
                dbc.AccordionItem(
                    openess,
                    title="Cooperação 🤝",
                ),
                dbc.AccordionItem(
                    privacy,
                    title="Privacidade 🔒",
                ),
                dbc.AccordionItem(
                    reliability,
                    title="Confiabilidade 💪",
                ),
                dbc.AccordionItem(
                    sustainability,
                    title="Sustentabilidade ♻️",
                ),
                dbc.AccordionItem(
                    transparency,
                    title="Transparência 🕵",
                ),
                dbc.AccordionItem(
                    truth,
                    title="Veracidade 🤥",
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
            ['Divergências ', html.I(className="bi bi-arrow-left-right")], id='open-body-scroll-divergence', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Divergências nas Definições 🤔**'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Aqui podemos ver casos de *'divergência na definição de princípios'*, ou seja, **formas divergentes de definição de princípios éticos**. A título de exemplo, vejamos nosso princípio mais citado: **Transparência/Explicabilidade/Auditoria.**", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Ao examinar a definição proposta em '[ARCC: An Ethical Framework for Artificial Intelligence](https://www.tisi.org/13747):' ", style={'font-size': FONT_SIZE,
                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Markdown("- *'Promover a transparência algorítmica e a auditoria algorítmica, para alcançar sistemas de IA compreensíveis e explicáveis. Explicar as decisões assistidas/feitas por sistemas de IA, quando apropriado. Assegurar o direito dos indivíduos de conhecer e fornecer aos usuários informações suficientes sobre o propósito, função, limitação e impacto do sistema de IA.'* ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Em comparação com a definição fornecida em '[A practical guide to Responsible Artificial Intelligence (AI)](https://www.pwc.com/gx/en/issues/data-and-analytics/artificial-intelligence/what-is-responsible-ai/responsible-ai-practical-guide.pdf):'", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Markdown("- *'Para incutir confiança nos sistemas de IA, as pessoas devem ser habilitadas a olhar sob o capô de seus modelos subjacentes, explorar os dados usados para treiná-los, expor o raciocínio por trás de cada decisão e fornecer prontamente explicações coerentes a todos stakeholders. Estas explicações devem ser adaptadas às diferentes partes interessadas, incluindo reguladores, cientistas de dados, patrocinadores de negócios e consumidores finais.'*", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Ambas as definições são similares, porém *' the AI-devil is in the details.'* Somente a **primeira definição implica o conceito de auditoria,** o que significa (em algumas interpretações) uma revisão do sistema em questão por terceiros. Além disso, enquanto o primeiro documento menciona que *'é preciso explicar',* *'garantir o certo',* e *'prover informações suficientes para as pessoas',* impondo claramente a ideia de um *'dever de explicar'* (**sem especificar quem deve explicar**), junto com o *'direito de saber'*,  o segundo documento menciona que pessoas *'tem de ser capaz de olhar além'* (**também sem especificar quem deve poder olhar além**), sem trazer a ideia de direito ou dever. Ao mesmo tempo, **apenas o segundo propõe que este conhecimento seja adaptado e acessível a diferentes tipos de stakeholders**, já que uma explicação adequada para um engenheiro de aprendizagem de máquina pode não ser adequada para um consumidor leigo.", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Tendo em mente que o conceito de **transparência/interpretabilidade é uma ideia/conceito fundamental na Ética da IA** (especialmente em pesquisas de aprendizagem de máquina), estando ainda sujeito a divergências em sua interpretação/aplicação, que tipos de diferenças podem ocorrer quando olhamos para *'princípios não tão bem definidos'*, como **centrado no ser-humano**", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Em 'Data, Responsibly (Vol. 1) Mirror, Mirror', (Khan & Stoyanovich, [2020](https://dataresponsibly.github.io/comics/)), encontramos a seguinte recomentação:", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                         'text-justify': 'inter-word'}),
                    dcc.Markdown("- *'Talvez o que precisamos, ao invés disso, seja fundamentar o projeto de sistemas de IA nas pessoas. Usando os dados das pessoas, coletados e implantados com uma metodologia equitativa, conforme determinado pelas pessoas, para criar tecnologia que seja benéfica para as pessoas.'*", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Enquanto que em '[Everyday Ethics for Artificial Intelligence](https://www.ibm.com/watson/assets/duo/pdf/everydayethics.pdf).' a seguinte norma foi sugerida:", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                         'text-justify': 'inter-word'}),
                    dcc.Markdown("- *'AI deve ser projetado para se alinhar com as normas e valores de seu grupo de usuários em mente.'*", style={'font-size': FONT_SIZE,
                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                  'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("O primeiro documento menciona ideias como *'o uso de uma metodologia equitativa'* e *'tecnologia que seja benéfica para as pessoas'*. Esta ideia de *'pessoas'* parece se referir a um grande e diversificado  grupo (talvez 'todas as pessoas'). Enquanto isso, o segundo declara especificamente *'seu grupo de usuários em mente'*, o que poderia significar *'um pequeno e seleto grupo de pessoas'*, se é isso que os designers têm em mente como *'seus usuários'*.", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Muitas outras diferenças podem ser encontradas em nossa amostra, por exemplo: ", style={'font-size': FONT_SIZE,
                                                                                                                          'text-align': 'justify',
                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("- '[Tieto's AI ethics guidelines](https://www.tietoevry.com/en/newsroom/all-news-and-releases/press-releases/2018/10/tieto-strengthens-commitment-to-ethical-use-of-ai/)' assume uma outra postura de explicabilidade, dizendo que seus sistemas *'podem ser explicados e se explicam'*, colocando parte da responsabilidade de explicabilidade no próprio sistema **AI**, tornando-o um 'stakeholder' na cadeia de responsabilidade (uma abordagem curiosa); ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Markdown("- '[The Toronto Declaration](https://www.torontodeclaration.org/declaration-text/english/)' dá uma definição extensa e não exaustiva do que *'discriminação'* significa segundo as leis internacionais, enquanto a maioria dos outros documentos resumem-se a apenas citar o conceito, deixando em aberto a interpretação dos tipos de *'discriminação que são permitids'*;", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'}),
                    dcc.Markdown("- Em '[Artificial Intelligence and Machine Learning: Policy Paper](https://www.internetsociety.org/resources/doc/2017/artificial-intelligence-and-machine-learning-policy-paper/)', a justiça está relacionada à ideia de *'a IA proporciona oportunidades sócio-econômicas para todos'* (**benefícios**), e em '[Trustworthy AI in Aotearoa: AI Principles](https://aiforum.org.nz/wp-content/uploads/2020/03/Trustworthy-AI-in-Aotearoa-March-2020.pdf)' justiça é definida como *'sistemas de IA não prejudicam injustamente'* (**impactos**), o que podemos relacionar com a **diferença entre certas noções de justiça algorítmica** (paridade preditiva versus probabilidades equalizadas); ", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Markdown("- Enquanto alguns documentos (e.g., '[Telefónica's Approach to the Responsible Use of AI](https://www.telefonica.com/en/wp-content/uploads/sites/5/2021/08/ia-responsible-governance.pdf)') afirmam como a privacidade e a segurança são essenciais para o desenvolvimento de sistemas de IA, apenas alguns (e.g., '[Big Data, Artificial Intelligence, Machine Learning, and Data Protection](https://ico.org.uk/media/for-organisations/documents/2013559/big-data-ai-ml-and-data-protection.pdf)') especificam o que *'bons critérios de privacidade'* são (e.g., **data minimization**).", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Markdown("- Enquanto a maioria dos documentos interpreta Responsabilidade/Responsabilização como *'desenvolvedores sendo responsáveis por seus projetos '*(e.g., '[Declaration of Ethical Principles for AI in Latin America](https://ia-latam.com/etica-ia-latam/)'), **alguns documentos também colocam esta responsabilidade sobre os usuários**, e até mesmo os 'próprios algoritmos' (e.g., '[The Ethics of Code: Developing AI for Business with Five Core Principles](https://www.sage.com/~/media/group/files/business-builders/business-builders-ethics-of-code.pdf?la=en)').", style={'font-size': FONT_SIZE,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Além das comparações mencionadas acima, muitas outras podem ser feitas utilizando nosso conjunto de dados (disponível para download no final desta página).", style={'font-size': FONT_SIZE,
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
            ['Princípios Éticos ', html.I(className="bi bi-search-heart")], id='open-offcanvas', outline=False, color=OPEN_BUTTON, n_clicks=0
        ),
        dbc.Offcanvas(
            [modal_divergence, accordion],
            id="offcanvas",
            scrollable=True,
            title="Princípios Éticos 🌈👨‍👨‍👦‍👦🕊️✊🏿👷♻️",
            placement='end',
            is_open=False,
        ),
    ], style={'display': 'inline-block', 'margin-left': '15px'}
)

badges = html.Span([
    dbc.Badge([html.I(className="bi bi-heart-fill"), "  Open-Source"], href="https://github.com/Nkluge-correa/worldwide_AI-ethics",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
    dbc.Badge([html.I(className="bi bi-robot"), "  AIRES na PUCRS"], href="https://en.airespucrs.org/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
    dbc.Badge([html.I(className="bi bi-filetype-py"), "  Made with Python"], href="https://www.python.org/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
    dbc.Badge([html.I(className="bi bi-github"), "  Made by Nkluge-correa"], href="https://nkluge-correa.github.io/",
              color="dark", className="text-decoration-none", style={'margin-right': '5px'})
])

download_data = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  Dados'], id='btn_data',
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
        'data_pt.rar')


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
