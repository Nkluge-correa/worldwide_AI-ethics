from dash import Dash, dcc, html, Output, Input, State, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
import dash
import warnings
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = dash.Dash(__name__,
                meta_tags=[
                    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                external_stylesheets=[dbc.themes.DARKLY])

server = app.server
app.title = 'Worldwide AI Ethics 🌐'


df = pd.read_excel('meta_pt.xlsx', 'meta_countries')

fig = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['Nº of Publications'],
    text=df['Countries'],
    colorscale='inferno',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
))

fig.update_layout(
    font_color='white',
    hoverlabel=dict(font_size=20),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='rgba(0,0,0,0)'
    ),
    margin={'r': 0, 't': 10, 'l': 0, 'b': 0},
    legend=dict(font_size=18),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

df10 = pd.read_excel('meta_pt.xlsx', 'meta_gender')
x_tick_text = list(df10['Authors'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig10 = go.Figure(go.Bar(
    x=x_tick_text,
    y=df10['Nº'],
    text=df10['Nº'],
    width=[0.8, 0.8],
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig10.update_traces(textposition='outside')
fig10.update_yaxes(showgrid=False, visible=True,
                   showticklabels=True, tickfont=dict(size=16))
fig10.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(size=16))
fig10.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    uniformtext_mode='hide',
    barmode='group',
    bargroupgap=0.8
)

df5 = pd.read_excel('meta_pt.xlsx', 'meta_year')
labels = '<i>Documentos</br>publicados<br>em 2014</i>'
colors = '#ff8800'
mode_size = 16
line_size = 6
x_data = list(df5['Years'])
y_data = list(df5['Nº of Published Documents'])

fig5 = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='lines+markers',
                                 name='',
                                 line=dict(color=colors, width=line_size),
                                 marker=dict(size=12),
                                 connectgaps=True,
                                 hovertemplate='<b>Nº de Publicações</b>: %{y} <extra></extra>'
                                 ))
fig5.add_trace(go.Scatter(
    x=[x_data[0], x_data[-1]],
    y=[y_data[0], y_data[-1]],
    mode='markers',
    marker=dict(color=colors, size=mode_size),
    hoverinfo='skip'
))
fig5.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='#ff8800',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            size=16,
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
            size=16,
            color='white',
        ),
    ),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=20),
)
annotations = []
annotations.append(dict(xref='paper', x=0.05, y=y_data[0],
                        xanchor='right', yanchor='middle',
                        text=labels,
                        font=dict(size=14),
                        showarrow=False))
annotations.append(dict(xref='paper', x=0.95, y=y_data[-1],
                        xanchor='left', yanchor='middle',
                        text='',
                        font=dict(size=14),
                        showarrow=False))
fig5.update_layout(annotations=annotations,
                   font_color='white',
                   hovermode='x',
                   hoverlabel=dict(font_size=20),
                   margin={'r': 20, 't': 20, 'l': 20, 'b': 20})


df4 = pd.read_excel('meta_pt.xlsx', 'meta_principles')
y_tick_text = list(df4['Principles'])
y_tick_text = ['<b>'+elem+'</b>' for elem in y_tick_text]
fig4 = go.Figure(go.Bar(
    x=df4['Nº of Citations'],
    y=y_tick_text,
    text=df4['Nº of Citations'],
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig4.update_traces(textposition='outside')
fig4.update_yaxes(tickfont=dict(size=16))
fig4.update_xaxes(visible=True, tickfont=dict(size=16))
fig4.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
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

    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)

df3 = pd.read_excel('meta_pt.xlsx', 'meta_institutions')
y_tick_text = list(df3['Institution Type'])
y_tick_text = ['<b>'+elem+'</b>' for elem in y_tick_text]
fig3 = go.Figure(go.Bar(
    x=df3['Nº of Publications'],
    y=y_tick_text,
    text=df3['Nº of Publications'],
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig3.update_traces(textposition='outside')
fig3.update_yaxes(tickfont=dict(size=16))
fig3.update_xaxes(visible=True, tickfont=dict(size=16))
fig3.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
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

    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)

df6 = pd.read_excel('meta_pt.xlsx', 'meta_nature')
x_tick_text = list(df6['Documents Nature/Content'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig6 = go.Figure(go.Bar(
    x=x_tick_text,
    y=df6['Nº of Documents'],
    text=df6['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig6.update_traces(textposition='outside')
fig6.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig6.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig6.update_layout(

    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    barmode='group',
    bargroupgap=0.8
)

df8 = pd.read_excel('meta_pt.xlsx', 'meta_regulation')
x_tick_text = list(df8['Documents Form of Regulation'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig8 = go.Figure(go.Bar(
    x=x_tick_text,
    y=df8['Nº of Documents'],
    text=df8['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig8.update_traces(textposition='outside')
fig8.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig8.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig8.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    barmode='group',
    bargroupgap=0.8
)

df9 = pd.read_excel('meta_pt.xlsx', 'meta_impact')
x_tick_text = list(df9['Documents Impact Scope'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig9 = go.Figure(go.Bar(
    x=x_tick_text,
    y=df9['Nº of Documents'],
    text=df9['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig9.update_traces(textposition='outside')
fig9.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig9.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig9.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    barmode='group',
    bargroupgap=0.8
)

df7 = pd.read_excel('meta_pt.xlsx', 'meta_normative')
x_tick_text = list(df7['Documents Normative Strength'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig7 = go.Figure(go.Bar(
    x=x_tick_text,
    y=df7['Nº of Documents'],
    text=df7['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(255, 136, 0, 0.8)',
        line=dict(
            color='rgba(255, 136, 0, 1.0)',
            width=1))))
fig7.update_traces(textposition='outside')
fig7.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig7.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(size=16))
fig7.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    margin=dict(l=20, r=20, t=30, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    barmode='group',
    bargroupgap=0.8
)

df2 = pd.read_excel('meta_pt.xlsx', 'meta_names')
names = []
for i in range(0, len(df2['Document Title'])):
    x = df2['Document Title'][i]
    y = df2['Document URL'][i]
    text = f'[{x}]({y})'
    names.append(text)

abstract = list(df2['Abstract'])

df_table = pd.DataFrame({
    'Publicações': names,
    'Abstract': abstract
})

table = html.Div(children=[

    dash_table.DataTable(
        data=df_table.to_dict(orient='records'),
        columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x ==
                 'Publicações' else {'id': x, 'name': x} for x in df_table.columns],
        style_table={'text-align': 'justify', 'text-justify': 'inter-word',
                     'height': '400px', 'overflowY': 'scroll'},
        page_current=0,
        page_size=50,
        style_cell={
            'text-align': 'justify', 'text-justify': 'inter-word', 'fontSize': 16, 'padding': '10px',
            'backgroundColor': '#222222'
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        style_header={
            'backgroundColor': '#222222',
            'fontWeight': 'bold',
            'text-align': 'left',
            'fontSize': 16
        },
    ),

], style={'margin-left': '15px', 'margin-right': '20px', 'margin-top': '10px'})

df2_table = pd.read_excel('meta_pt.xlsx', 'meta_principles_definitions_2')

table_2 = html.Div(children=[

    dash_table.DataTable(
        data=df2_table.to_dict(orient='records'),
        columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x ==
                 'Título do documento' else {'id': x, 'name': x} for x in df2_table.columns],
        style_table={'text-align': 'justify', 'text-justify': 'inter-word',
                     'height': '400px', 'overflowY': 'scroll'},
        page_current=0,
        page_size=50,
        style_cell={
            'text-align': 'justify', 'text-justify': 'inter-word', 'fontSize': 16, 'padding': '10px',
            'backgroundColor': '#222222'
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        style_header={
            'backgroundColor': '#222222',
            'fontWeight': 'bold',
            'text-align': 'left',
            'fontSize': 16
        },
    ),

], style={'margin-left': '15px', 'margin-right': '20px', 'margin-top': '10px'})

df11 = pd.read_excel('arxiv_submissions_data_pt.xlsx', 'Arxiv')
df11 = df11.set_index('Date')
fig11 = go.Figure(layout={'template': 'plotly_dark'})
for column in df11.columns:
    fig11.add_trace(go.Scatter(x=df11.index, y=df11[column],
                               line=dict(width=3), name=column, mode='lines',
                               hoverlabel=dict(namelength=-1),
                               hovertemplate='Nº de Submissões (' +
                               column + '): %{y} <extra></extra>',
                               showlegend=True))
fig11.update_yaxes(showgrid=True, gridcolor='lightgray',
                   showticklabels=True, tickfont=dict(size=12))
fig11.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(size=12))
fig11.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        tickangle=45,
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
    title='Nº de Submissões no Arxiv por Categoria',
    font_color='white',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)

df12 = pd.read_excel('arxiv_submissions_data_pt.xlsx', 'Arxiv(CS)')
df12 = df12.set_index('Date')
fig12 = go.Figure(layout={'template': 'plotly_dark'})
for column in df12.columns:
    fig12.add_trace(go.Scatter(x=df12.index, y=df12[column],
                               line=dict(width=3), name=column, mode='lines',
                               hoverlabel=dict(namelength=-1),
                               hovertemplate='Nº de Submissões (' +
                               column + '): %{y} <extra></extra>',
                               showlegend=True))
fig12.update_yaxes(showgrid=True, gridcolor='lightgray',
                   showticklabels=True, tickfont=dict(size=12))
fig12.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(size=12))
fig12.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        tickangle=45,
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
    title='Nº de Submissões no Arxiv em Ciências da Computação',
    font_color='white',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)

df13 = pd.read_excel('meta_pt.xlsx', 'Accountability_gram')

fig13 = px.bar(df13, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Responsabilidade/Responsabilização',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig13.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df14 = pd.read_excel('meta_pt.xlsx', 'Beneficence_gram')

fig14 = px.bar(df14, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Beneficência/Não-maleficência',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig14.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df15 = pd.read_excel('meta_pt.xlsx', 'Children_gram')

fig15 = px.bar(df15, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Direitos da Criança e do Adolescente',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig15.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df16 = pd.read_excel('meta_pt.xlsx', 'Dignity_gram')

fig16 = px.bar(df15, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Dignidade/Direitos Humanos',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig16.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df17 = pd.read_excel('meta_pt.xlsx', 'Diversity_gram')

fig17 = px.bar(df17, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Diversidade/Inclusão/Pluralismo/Acessibilidade',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig17.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df18 = pd.read_excel('meta_pt.xlsx', 'Freedom_gram')

fig18 = px.bar(df18, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig18.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df19 = pd.read_excel('meta_pt.xlsx', 'Formation_gram')

fig19 = px.bar(df19, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Educação/Formação Humana',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig19.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df21 = pd.read_excel('meta_pt.xlsx', 'Centeredness_gram')

fig21 = px.bar(df21, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Centrado no Ser Humano/Alinhamento',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig21.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df22 = pd.read_excel('meta_pt.xlsx', 'Property_gram')

fig22 = px.bar(df22, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Propriedade Intelectual',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig22.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df23 = pd.read_excel('meta_pt.xlsx', 'Justice_gram')

fig23 = px.bar(df23, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Justiça/Equidade/Igualdade/Não-discriminação',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig23.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df24 = pd.read_excel('meta_pt.xlsx', 'Labor_gram')

fig24 = px.bar(df24, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Direitos Trabalhistas',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig24.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df25 = pd.read_excel('meta_pt.xlsx', 'Open_gram')

fig25 = px.bar(df25, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Código Aberto/Concorrência Justa/Cooperação',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig25.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df26 = pd.read_excel('meta_pt.xlsx', 'Privacy_gram')

fig26 = px.bar(df26, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Privacidade',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig26.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df27 = pd.read_excel('meta_pt.xlsx', 'Reliability_gram')

fig27 = px.bar(df27, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Confiabilidade/Segurança/Confiança/Fiabilidade',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig27.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df28 = pd.read_excel('meta_pt.xlsx', 'Sustainability_gram')

fig28 = px.bar(df28, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Sustentabilidade',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig28.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df29 = pd.read_excel('meta_pt.xlsx', 'Transparency_gram')

fig29 = px.bar(df29, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Transparência/Explicabilidade/Auditoria',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig29.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df30 = pd.read_excel('meta_pt.xlsx', 'Truthfulness_gram')

fig30 = px.bar(df30, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Veracidade',
               color='Contagem de palavras', color_continuous_scale='inferno')
fig30.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


modal_abstract = html.Div(
    [
        dbc.Button('Abstract', id='open-fs', outline=True, color='warning'),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Worldwide AI Ethics: uma revisão de 200 diretrizes e recomendações para a governança da IA ⚖️'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Desde o final do nosso último *“inverno da IA",* 1987 – 1993, a pesquisa em IA e sua indústria têm visto um crescimento maciço, seja em tecnologias desenvolvidas, investimentos, atenção da mídia ou novas tarefas que sistemas autônomos são hoje, capazes de realizar. Se olharmos para a história das submissões no ArXiv ([entre 2009 e 2021](https://arxiv.org/about/reports/submission_category_by_year)), um repositório de preprints e publicações eletrônicas de acesso aberto, a partir de 2018, **trabalhos relacionados à Ciência da Computação têm sido o tipo mais comum de material submetido.**', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_sub', figure=fig11), html.Br(),
                    dcc.Markdown('Além disso, quando examinamos apenas a categoria de Ciências da Computação, **" Visão Computacional e Reconhecimento de Padrões", "Aprendizagem de Máquina",** e **"Computação e Linguagem"** são os tipos de subcategorias mais apresentados. **Note que todas estas são áreas onde a aprendizagem de máquina se encontra estabelecida como seu paradigma atual.**', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_CS', figure=fig12), html.Br(),
                    dcc.Markdown('Além do número de publicações sendo produzidos, nunca tivemos mais capital sendo investido em empresas e startups, seja por governos ou fundos de *venture capital*. **( mais de 90 bilhões de USD$ em 2021 só nos EUA)**, e patentes relacionadas à IA sendo registradas (Zhang et al., [2022](https://aiindex.stanford.edu/report/)). Esta rápida expansão do campo/indústria da IA também veio com outro boom, o *"boom da ética da IA",* onde uma exigência nunca antes vista de regulamentação e orientação normativa de tais tecnologias foi manifestada. Baseando-se no trabalho realizado por outros meta-analistas do campo, **este estudo apresenta uma revisão sistemática de 200 documentos relacionados à ética e governança da IA.** Nós apresentamos uma coleção de **tipologias usadas para classificar nossa amostra**, tudo condensado em uma ferramenta on-line **interativa e de acesso aberto**, juntamente com uma análise crítica daquilo que *"está sendo dito"* e *"quem o está dizendo"* em nosso panorama global da ética da IA.', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'}),
                    html.Hr(),
                    dcc.Markdown('### Como citar: 🤗'),
                    dcc.Markdown('''

                    ````bash

                    @article{correa2022worldwide,
                        title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
                        author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, 
                                Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, 
                                Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund},
                        journal={arXiv preprint arXiv:2206.11922},
                        year={2022}
                    }
                    ````
                    ''', style={'font-size': 18,
                                'text-align': 'justify',
                                'text-justify': 'inter-word'}),
                    html.Hr(),
                    dcc.Markdown('- Para mais informações, contate [airespucrs@airespucrs.org](mailto:airespucrs@airespucrs.org).',
                                 style={'text-decoration': 'none',
                                        'font-size': 18,
                                        'text-align': 'justify',
                                        'text-justify': 'inter-word'}),
                    dcc.Markdown('- Acesse o Dash completo (versão em Power BI) [aqui](https://www.airespucrs.org/worldwide-ai-ethics).',
                                 style={'text-decoration': 'none',
                                        'font-size': 18,
                                        'text-align': 'justify',
                                        'text-justify': 'inter-word'}),
                    dcc.Markdown('- Acesse o artigo completo (preprint) [aqui](https://doi.org/10.48550/arXiv.2206.11922).',
                                 style={'text-decoration': 'none',
                                        'font-size': 18,
                                        'text-align': 'justify',
                                        'text-justify': 'inter-word'}),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Close',
                        id='close-fs',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-fs',
            fullscreen=True,
        ),
    ], style={
        'margin-left': '15px',
        'margin-bottom': '10px',
        'display': 'inline-block',
    },
)
modal_map = html.Div(
    [
        dbc.Button(
            'Publicações por País 🏳️‍🌈', id='open-body-scroll', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Publicações por País 🏳️‍🌈'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Olhando para a distribuição entre regiões do mundo (agregadas por continente), vemos que a maior parte dos documentos produzidos vem da **Europa, América do Norte e Ásia**, enquanto regiões como **América do Sul, África e Oceania representam menos de 4,5% de toda a nossa amostra**. Se não fosse pela **participação significativa de Organizações Intergovernamentais,** como a OTAN, NU, UNESCO, **que representam 6% de nossa amostra (13 documentos),** outras regiões/países do mundo estariam ainda mais sub representadas.', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('77% do tamanho total de nossa amostra é composta por 13 países, **Estados Unidos da América, Reino Unido, Alemanha, Canadá, China, Japão, França, Finlândia, Holanda, Suíça, Bélgica, Brasil e Coréia do Sul,** enquanto uma miríade de **24 países (12,5%) representam o restante de nossa amostra**, juntamente com organizações intergovernamentais, como a União Europeia (9 = 4,5%) e as NU (6 = 3%).', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll',
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

modal_gender = html.Div(
    [
        dbc.Button(
            'Gênero 🧍‍♂️ ♂ ☿ ♀ 💃', id='open-body-scroll-1', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Autores por Gênero 🧍‍♂️ ♂ ☿ ♀ 💃'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Ao remover documentos com autores não especificados, contamos um total de **561 autores homens (66,6%)** e **281 autoras mulheres (33,3%).** A predominância do gênero masculino é **uma tendência que pode ser encontrada em praticamente todas as regiões e países do mundo, independentemente do tipo de instituição.**', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('O gênero dos autores foi determinado pela busca de seus nomes e imagens de perfil em diferentes tipos de plataformas (e.g.,, *LinkedIn, Researchgate, sites universitários, sites pessoais, etc.*) através de motores de busca.', style={'font-size': 18,
                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-1',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-1',
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

modal_years = html.Div(
    [
        dbc.Button(
            'Publicações por Ano ⌛', id='open-body-scroll-2', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Ano ⌛'), style={})),
                dbc.ModalBody([
                    dcc.Markdown('Com respeito ao ano de publicação dos documentos de nossa amostra, **vemos que a maioria dos documentos (129 = 64,5%) foram publicados entre os anos 2017 e 2019.** O que podemos chamar de *"boom da ética da IA"* trata-se da **produção significativa de documentos no ano 2018**, o que representa **30,5% (61)** de toda a nossa amostra.', style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown('**Nota:** documentos com datas de publicação **não especificadas (27 = 13,5%)** também são bastante **prevalentes** em nossa amostra.', style={'font-size': 18,
                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                 'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-2',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-2',
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

modal_principles = html.Div(
    [
        dbc.Button(
            'Citações por Princípio ⚖️', id='open-body-scroll-3', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Citações por Princípio ⚖️'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Os **cinco principais princípios** defendidos nos documentos de nossa amostra são semelhantes aos resultados obtidos por Jobin et al. ([2019](https://www.nature.com/articles/s42256-019-0088-2)) e Hagendorff ([2020](https://link.springer.com/article/10.1007/s11023-020-09517-8)), **com o acréscimo de Confiabilidade/Segurança/Confiança/Fiabilidade (78%)**, que também são citados como um dos cinco principais na metanálise de Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)) **(80%)**. Como cada documento apresenta sua própria passagem sobre cada princípio, se existiam, por exemplo, 134 documentos que citam o princípio de privacidade, coletamos 134 definições/recomendações diferentes envolvendo este princípio. Todos sendo acessíveis em nosso [Power BI dashboard](https://www.airespucrs.org/worldwide-ai-ethics).", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Olhando para a **distribuição de princípios filtrada por continente**, **os cinco principais princípios continuam os mesmos** tanto na **América do Norte** como **Europa**. Já no **continente asático** é introduzido o princípio de **Beneficência/Não-maleficência como o 5º (74%) princípio mais citado**, colocando Responsabilidade/Responsabilização em 6º lugar (70%). **Filtrando nossos resultados por país**, não vemos **nenhuma mudança nos cinco principais princípios ** quando comparado aos **EUA** e **RU**. Entretanto, olhando **além dos cinco mais citados princípios**, nós começamos a ver **diferenças**, como **Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica (38%)** e  **Beneficência/Não-maleficência (34,4%)** sendo o **6º** e **7º princípios mais citados nos EUA**, e **Código aberto/Concorrência Justa/Cooperação (45,8%)** e **Diversidade/Inclusão/Pluralismo/Acesbilidade (41,6%)** sendo o **6º** e **7º princípios mais citados no UK**.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Ao examinar a **distribuição de princípios filtrados por tipo de instituição**, podemos chegar a vários insights. Por exemplo, olhando para nossa amostra total, percebe-se que a **maior preocupação de instituições governamentais** (em todo o mundo) e a necessidade de **sistemas transparentes (89,5%)**, **corporações privadas** defendem principalmente **Confiabilidade e Segurança (87,5%)**, enquanto que **Organizações sem fins lucrativos e ONGs** defendem principalmente a **Jusiça (88,2%)**. ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Para criar uma **definição geral** de cada princípio/grupo de princípios, utilizamos uma técnica de **[mineração de texto](https://en.wikipedia.org/wiki/Text_mining)** chamada de **[análise de n-gramas](https://en.wikipedia.org/wiki/N-gram)**, onde contamos a repetição sucessiva de palavras (e grupos de palavras) em cada princípio encontrado nos documentos de nossa amostra. Assim, as definições abaixo foram criadas para contemplar os temas recorrentes que encontramos. *Abaixo também apresentamos gráficos de contagem de quatro-gramas de cada princípio.*", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("**Responsabilidade/Responsabilização:** responsabilidade refere-se à ideia de que os desenvolvedores e implementadores de tecnologias de IA devem estar em conformidade com os órgãos reguladores, o que também significa que tais atores devem ser responsáveis por suas ações e pelos impactos causados por suas tecnologias;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}),
                    dcc.Graph(id='account',
                              figure=fig13), html.Br(),
                    dcc.Markdown("**Beneficência/Não-maleficência:** beneficência e não-maleficência são conceitos que oriundos da bioética e da ética médica. Na ética da IA, esses princípios afirmam que o bem-estar humano (e a aversão ao dano) devem ser o objetivo deste tipo de tecnologia. Algumas vezes, este princípio também está ligado à ideia de Sustentabilidade, afirmando que a IA deve ser benéfica não apenas para a civilização humana, mas para nosso meio ambiente e outros seres vivos; ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'text-justify': 'inter-word'}),
                    dcc.Graph(id='benef', figure=fig14), html.Br(),
                    dcc.Markdown("**Direitos da Criança e do Adolescente:** a ideia de que os direitos das crianças e adolescentes devem ser respeitados por tecnologias que utilizam de IA. AI stakeholders devem salvaguardar, respeitar e estar cientes das fragilidades associadas aos jovens;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}),
                    dcc.Graph(id='child', figure=fig15), html.Br(),
                    dcc.Markdown("**Dignidade/Direitos Humanos:** este princípio se baseia na ideia de que todos os indivíduos merecem tratamento adequado, dignidade e respeito. Na ética da IA, o respeito à dignidade humana está frequentemente ligado aos direitos humanos (i.e., a Declaração Universal dos Direitos Humanos); ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}),
                    dcc.Graph(id='digni', figure=fig16), html.Br(),
                    dcc.Markdown("**Diversidade/Inclusão/Pluralismo/Acessibilidade:** este conjunto de princípios defende a ideia de que o desenvolvimento e o uso das tecnologias de IA devem ser feitos de forma inclusiva e acessível, respeitando as diferentes formas que a entidade humana pode vir a se expressar (gênero, etnia, raça, orientação sexual, deficiências, etc.). Este grupo de princípios está fortemente ligado a outro conjunto de princípios: Justiça/Equidade/Igualdade/Não-discriminação; ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}),
                    dcc.Graph(id='diver', figure=fig17), html.Br(),
                    dcc.Markdown("**Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica:** este conjunto de princípios defende a ideia de que a autonomia da tomada de decisão humana deve ser preservada durante as interações humano-IA, quer essa escolha seja individual ou conjunta, como a inviolabilidade dos direitos e valores democráticos, estando também ligada à auto-suficiência tecnológica das Nações/Estados;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}),
                    dcc.Graph(id='free', figure=fig18), html.Br(),
                    dcc.Markdown("**Educação/Formação Humana:** tais princípios defendem a ideia de que a formação e educação humana deve ser priorizada em nossos avanços tecnológicos. Tecnologias que utilizam de IA exigem um nível considerável de especialização para serem produzidas e operadas, e tal conhecimento deve ser acessível a todos. Este princípio parece estar fortemente ligado aos Direitos Trabalhistas. A grande maioria dos documentos relativos aos trabalhadores e à vida profissional apontam para a necessidade de reeducar e requalificar a força de trabalho como uma estratégia de mitigação do desemprego tecnológico;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Graph(id='educa', figure=fig19), html.Br(),
                    dcc.Markdown("**Centrado no Ser Humano/Alinhamento:** tais princípios defendem a ideia de que os sistemas de IA devem ser centrados e alinhados com valores humanos. Tecnologias que utilizam de IA devem ser adaptadas para se alinharem com nossos valores (e. g., design sensível a valores). Este princípio também é usado como uma categoria 'coringa', muitas vezes sendo definido como um conjunto de 'princípios que são valorizados pelos humanos' (e. g., liberdade, privacidade, não-discriminação, etc.);", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}),
                    dcc.Graph(id='align', figure=fig21), html.Br(),
                    dcc.Markdown("**Propriedade Intelectual:** este princípio procura fundamentar os direitos de propriedade sobre produtos e/ou processos de conhecimento gerado por indivíduos, sejam eles tangíveis ou intangíveis;", style={'font-size': 18,
                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Graph(id='intellec',
                              figure=fig22), html.Br(),
                    dcc.Markdown("**Justiça/Equidade/Igualdade/Não-discriminação:** este conjunto de princípios sustenta a ideia de não-discriminação e mitigação de preconceitos (sistemas de IA podem estar sujeitos a preconceitos algorítmicos discriminatórios). Aqui também se defende a ideia de que, independentemente dos diferentes atributos sensíveis que possam caracterizar um indivíduo, todos devem ser tratados 'justamente';", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Graph(id='justice',
                              figure=fig23), html.Br(),
                    dcc.Markdown("**Direitos Trabalhistas:** Os direitos trabalhistas são direitos legais e humanos relacionados às relações de trabalho entre trabalhadores e empregadores. Na ética da IA, este princípio enfatiza que os direitos dos trabalhadores devem ser preservados, independentemente de que as relações de trabalho estejam ou não sendo mediadas por tecnologias que utilizam de IA. Uma das principais preocupações apontadas quando este princípio é apresentado é a mitigação do desemprego tecnológico (e. g., , através da Educação/Formação Humana);", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Graph(id='labor', figure=fig24), html.Br(),
                    dcc.Markdown("**Código Aberto/Concorrência Justa/Cooperação:** este conjunto de princípios defende diferentes meios pelos quais ações conjuntas podem ser estabelecidas e cultivadas entre AI stakeholders para alcançar objetivos comuns. Também defende-se o intercâmbio livre e aberto de ativos valiosos para a IA (e. g., dados, conhecimento, direitos de patente, recursos humanos) para mitigar possíveis monopólios tecnológicos;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Graph(id='open', figure=fig25), html.Br(),
                    dcc.Markdown("**Privacidade:** a ideia de privacidade pode ser definida como o direito do indivíduo de 'expor-se voluntariamente, e na medida do desejado, ao mundo'. Na ética da IA, este princípio sustenta o direito de uma pessoa a controlar a exposição e disponibilidade de informações pessoais quando extraídas como dados de treinamento para sistemas de IA. Este princípio também está relacionado a conceitos tais como minimização de dados, anonimato, consentimento informado e outros conceitos relacionados à proteção de dados; ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}),
                    dcc.Graph(id='privacy',
                              figure=fig26), html.Br(),
                    dcc.Markdown("**Confiabilidade/Segurança/Confiança/Fiabilidade:** este conjunto de princípios sustenta a ideia de que as tecnologias de IA devem ser confiáveis, no sentido de que seu uso pode ser comprovadamente atestado como seguro e robusto, promovendo a confiança do usuário e uma melhor aceitação das tecnologias de IA; ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Graph(id='reliab', figure=fig27), html.Br(),
                    dcc.Markdown("**Sustentabilidade:** este princípio pode ser entendido como uma forma de 'justiça intergeracional', onde o bem-estar das gerações futuras também deve ser considerado durante o desenvolvimento da IA. Na ética da IA, sustentabilidade se refere à ideia de que o desenvolvimento de tecnologias de IA deve ser realizado com consciência de suas implicações a longo prazo, tais como custos ambientais e preservação/bem estar da vida não-humana;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'text-justify': 'inter-word'}),
                    dcc.Graph(id='sustaina',
                              figure=fig28), html.Br(),
                    dcc.Markdown("**Transparência/Explicabilidade/Auditoria:** este conjunto de princípios apoia a ideia de que o uso e desenvolvimento da IA deve ser feito de forma transparente para todos stakeholders. A transparência pode estar relacionada com 'a transparência de uma organização' ou 'a transparência de um algoritmo'. Este conjunto de princípios também está relacionado à ideia de que tais informações devem ser compreensíveis para não especialistas, e, quando necessário, sujeitas a auditoria;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}),
                    dcc.Graph(id='trans', figure=fig29), html.Br(),
                    dcc.Markdown("**Veracidade:** este princípio sustenta a ideia de que a IA deve fornecer informações verdadeiras. Está também relacionado à ideia de que as pessoas não devem ser enganadas quando interagem com sistemas de IA. Este princípio está fortemente relacionado com a mitigação de meios automatizados de desinformação.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}),
                    dcc.Graph(id='truth', figure=fig30), html.Br(),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-3',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-3',
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

modal_institution = html.Div(
    [
        dbc.Button(
            'Tipo de Instituição 👩‍💼', id='open-body-scroll-4', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo de Instituição 👩‍💼'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Com exceção de instituições como **IBM (5)**, **Microsoft (4)**, e **UNESCO (3)**, **a maioria das outras instituições não têm mais do que dois documentos publicados**. Observamos também que **a maior parte de nossa amostra foi produzida por instituições governamentais e corporações privadas (48%)**,  seguidas por **ONGs (17%)**, **Organizações Sem Fins Lucrativos (16%)**, e **Instituições Acadêmicas (12,5%)**. ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("No entanto, **esta tendência só se segue se olharmos para a totalidade de nossa amostra**. Se olharmos para os documentos produzidos por **continentes**,  vemos que, por exemplo, na **América do Norte (69), corporações privadas (24 = 34,7%) e organizações sem fins lucrativos (18 = 26%) produziram o maior número de documentos**, seguidas de instituições governamentais (12 = 17,4%). Ao mesmo tempo, quando olhamos para **Europa**, a **tendência global é restaurada**. ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Uma análise aprofundada **segmentada por países** mostra que o **engajamento** de certos tipos de **AI stakeholders** (i.e., tipos de instituições) **difere por países.** Por exemplo, na **China (11),  a maioria dos documentos foram produzidos por instituições acadêmicas (5 = 45,4%), enquanto que na Alemanha (20), a maioria dos documentos de nossa amostra foram produzidas por corporações privadas (6 = 30%), e NGOs (4 = 20%).** Outros insights podem ser encontrados em nosso [Power BI dashboard](https://www.airespucrs.org/worldwide-ai-ethics).", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-4',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-4',
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

modal_nature = html.Div(
    [
        dbc.Button(
            'Natureza/Conteúdo 📝', id='open-body-scroll-5', size='lg', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Natureza/Conteúdo) 📝'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado com a natureza/conteúdo do documento, e **três categorias** foram definidas (essas categorias *não foram definidas como mutuamente exclusivas*):", style={'font-size': 18,
                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                       'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("**Descritivo:** Os documentos descritivos tomam o esforço de apresentar definições factuais relacionadas à IA. Estas definições servem para contextualizar 'o que queremos dizer' quando falamos de IA, e como o vocabulário utilizado neste campo pode ser compreendido;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}),
                    dcc.Markdown("**Normativo:** documentos normativos apresentam normas, princípios éticos, recomendações e afirmações imperativas sobre como tais tecnologias devem ou não ser utilizadas/desenvolvidas;", style={'font-size': 18,
                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                    'text-justify': 'inter-word'}),
                    dcc.Markdown("**Prático:** documentos práticos apresentam ferramentas de desenvolvimento para implementar princípios e normas éticas, sejam elas qualitativas (e. g., pesquisas de auto-avaliação) ou quantitativas (e. g., *Algoritmos de Debiasing* para modelos de ML).", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("A maior parte da nossa amostra é composta de **amostras normativas (96%)**, sendo que  **um terço desta amostra também apresenta conteúdo descritivo (55,5%)**, e mais **raramente**, implementações **práticas (27%)**.", style={'font-size': 18,
                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-5',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-5',
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

modal_regulation = html.Div(
    [
        dbc.Button(
            'Forma de Regulação 👩‍⚖️', id='open-body-scroll-6', size='lg', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Forma de Regulação) 👩‍⚖️'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado com a forma de regulamentação que o documento propõe. Para isso, foram definidas **três categorias** (estas categorias foram *definidas como mutuamente exclusivas*):", style={'font-size': 18,
                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("**Regulamentação Governamental:** esta categoria foi definida para abranger estritamente documentos feitos por instituições governamentais, com o fim de regular o uso e desenvolvimento da IA, rigorosamente (regulamentos juridicamente vinculativos) ou suavemente (diretrizes juridicamente não vinculativas);", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Markdown("**Auto-regulamentação/Auto-regulamentação Voluntária:** esta categoria foi definida para englobar documentos feitos por organizações privadas e outros órgãos que defendem uma forma de auto-regulamentação governada pela própria indústria da IA. Ela também abrange o auto-compromisso voluntário feito por organizações independentes (ONGs, Associações Profissionais, etc.);", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                              'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                              'text-justify': 'inter-word'}),
                    dcc.Markdown("**Recomendação:** esta categoria foi definida para englobar documentos que apenas sugerem possíveis formas de governança e princípios éticos que devem orientar as organizações que buscam usar, desenvolver ou regular as tecnologias de IA.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Quando analisamos a forma de regulamentação proposta pelos documentos de nossa amostra, **mais da metade (56%) são apenas recomendações** para diferentes stakeholders, enquanto que **24% dos documentos analisados foram enquadrados na categoria auto-regulamentação/auto-regulamentação voluntária**, e somente **20%** propuseram uma **forma de regulação administrada por um dado estado/país**.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-6',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-6',
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

modal_impact = html.Div(
    [
        dbc.Button(
            'Escopo de Impacto 💥', id='open-body-scroll-7', size='lg', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Escopo de Impacto) 💥'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado com o escopo de impacto que motiva o documento. Com escopo de impacto, nos referimos aos riscos e benefícios relacionados ao uso da IA que motivam o tipo de regulamentação sugerida pelo documento. Para isso, **três categorias** foram definidas (estas categorias foram *definidas como mutuamente exclusivas*):", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("**Short-Termism:** esta categoria foi definida para englobar documentos nos quais o escopo do impacto e da preocupação se concentra principalmente em problemas de curto prazo, ou seja, problemas que estamos enfrentando com as atuais tecnologias de IA (e. g., discriminação algorítmica, opacidade algorítmica, privacidade, responsabilidade legal);  ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Markdown("**Long-Termism:** esta categoria foi definida para englobar documentos nos quais o escopo do impacto e da preocupação se concentra principalmente em problemas de longo prazo, ou seja, problemas que podemos vir a enfrentar com futuros sistemas de IA. Como tais tecnologias ainda não são uma realidade, tais riscos podem ser classificados como hipotéticos ou, na melhor das hipóteses, incertos (e. g, IA senciente, AGI desalinhada, IA super inteligente, riscos existenciais relacionados à IA);", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'text-justify': 'inter-word'}),
                    dcc.Markdown("**Short-Termism & Long-Termism:** esta categoria foi projetada para englobar documentos nos quais o escopo do impacto é tanto de curto como de longo prazo, ou seja, eles apresentam um escopo de 'médio prazo' de preocupação. Estes documentos abordam questões relacionadas à categoria de curto prazo, ao mesmo tempo em que apontam os impactos de longo prazo de nossa atual adoção da IA (e. g., interferência da IA nos processos democráticos, armas autônomas, riscos existenciais, sustentabilidade ambiental, deslocamento de mão-de-obra, a necessidade de atualizar nossos sistemas educacionais).", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Olhando para a totalidade de nossa amostra, vemos claramente que **curto (47%)** e **'médio prazo' (i.e., Short-Termism & Long-Termism = 52%)** prevalecem sobre **preocupações a longo prazo (2%)**. Quando filtramos nossa amostra por **escopo de impacto a tipo de instituição** nós vemos que **corporações privadas pensam sobre os impactos relacionados a IA mais a curto prazo(33%)**, enquanto que **instituições governamentais tendem a focar no médio prazo (28%)**, e **instituições acadêmicas (66%) e organizações sem fins lucrativos (33%) são as que mais levantam questões definidas como long-term.**", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-7',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-7',
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

modal_normative = html.Div(
    [
        dbc.Button(
            'Força Normativa 💪', id='open-body-scroll-8', size='lg', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Nº de Publicações por Tipo (Força Normativa) 💪'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Este tipo está relacionado à força normativa do mecanismo de regulamentação proposto pelo documento. Para isso, foram definidas **duas categorias** (estas categorias *não foram definidas como mutuamente exclusivas*):", style={'font-size': 18,
                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("**Diretivas juridicamente não vinculativas:** estes documentos propõem uma abordagem que entrelaça princípios éticos com práticas recomendadas para empresas e outras entidades (i. e., soluções jurídicas não vinculativas);", style={'font-size': 18,
                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}),
                    dcc.Markdown("**Regulamentos juridicamente vinculativos:** estes documentos propõem uma abordagem que se concentra na regulamentação de usos específicos da IA em regulamentos juridicamente vinculativos, como exigências e proibições obrigatórias.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                   'text-align': 'justify',
                                                                                                                                                                                                                                                                                   'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("A falta de convergência para uma forma de regulamentação mais **'baseada no governo'** se reflete na força normativa dos documentos analisados, onde a **vasta maioria (98%) serve apenas como 'leis brandas'**, ou seja, tais diretrizes não implicam qualquer forma de obrigação legal, enquanto **somente 4,5% apresentam formas mais rígidas de regulamentação.** Uma vez que apenas as instituições governamentais podem apresentar normas legalmente vinculativas (outras formas de instituições não possuem tal poder), e **instituições governamentais produziram apenas 24% de nossa amostra**, alguns podem argumentar que esse desequilíbrio reside nesse fato.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Entretanto, **filtrando** somente os documentos produzidos por **instituições governamentais**, a **desproporção não desaparece**, com **somente 18,7% dos documentos propondo formas de regulamentação juridicamente vinculativas**. Os países que parecem estar à frente desta, ainda fraca, tendência são **Canadá**, **Alemanha**, e o **Reino Unido**, com a Austrália, Noruega, e os EUA vindo logo atrás.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-8',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-8',
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

modal_table = html.Div(
    [
        dbc.Button(
            'URL & Abstract 🌐📝', id='open-body-scroll-9', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### URL & Abstract 🌐📝'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Como uma contribuição final, para cada documento de nossa amostra, foi escrito um breve resumo, permitindo ao leitor ter uma rápida visão do conteúdo de cada documento. Cada documento também foi vinculado a sua URL. Em nosso [Power BI dashboard](https://www.airespucrs.org/worldwide-ai-ethics), também é possível encontrar os websites da instituição de origem, e outros documentos importantes anexados e citados na publicação original.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'})
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-9',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-9',
            scrollable=True,
            is_open=False,
        ),
    ], style={
        'margin-left': '10px',
        'margin-top': '10px',
        'margin-bottom': '5px',
        'display': 'inline-block'},

)

modal_definition = html.Div(
    [
        dbc.Button(
            'Princípios Éticos ⚖️🧭🤔 📙🧠⚕️', id='open-body-scroll-10', outline=True, color='warning', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### Publicações (Definição dos Princípios) ⚖️🧭🤔 📙🧠⚕️'), style={})),
                dbc.ModalBody([
                    dcc.Markdown("Aqui podemos ver casos de *'divergência na definição de princípios'*, ou seja, **formas divergentes de definição de princípios éticos**. A título de exemplo, vejamos nosso princípio mais citado: **Transparência/Explicabilidade/Auditoria.**", style={'font-size': 18,
                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Ao examinar a definição proposta em '[ARCC: An Ethical Framework for Artificial Intelligence](https://www.tisi.org/13747):' ", style={'font-size': 18,
                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Markdown("*'Promover a transparência algorítmica e a auditoria algorítmica, para alcançar sistemas de IA compreensíveis e explicáveis. Explicar as decisões assistidas/feitas por sistemas de IA, quando apropriado. Assegurar o direito dos indivíduos de conhecer e fornecer aos usuários informações suficientes sobre o propósito, função, limitação e impacto do sistema de IA.'* ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                         'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Em comparação com a definição fornecida em '[A practical guide to Responsible Artificial Intelligence (AI)](https://www.pwc.com/gx/en/issues/data-and-analytics/artificial-intelligence/what-is-responsible-ai/responsible-ai-practical-guide.pdf):'", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                'text-align': 'justify',
                                                                                                                                                                                                                                                                                                'text-justify': 'inter-word'}),
                    dcc.Markdown("*'Para incutir confiança nos sistemas de IA, as pessoas devem ser habilitadas a olhar sob o capô de seus modelos subjacentes, explorar os dados usados para treiná-los, expor o raciocínio por trás de cada decisão e fornecer prontamente explicações coerentes a todos stakeholders. Estas explicações devem ser adaptadas às diferentes partes interessadas, incluindo reguladores, cientistas de dados, patrocinadores de negócios e consumidores finais.'*", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Ambas as definições são similares, porém *' the AI-devil is in the details.'* Somente a **primeira definição implica o conceito de auditoria,** o que significa (em algumas interpretações) uma revisão do sistema em questão por terceiros. Além disso, enquanto o primeiro documento menciona que *'é preciso explicar',* *'garantir o certo',* e *'prover informações suficientes para as pessoas',* impondo claramente a ideia de um *'dever de explicar'* (**sem especificar quem deve explicar**), junto com o *'direito de saber'*,  o segundo documento menciona que pessoas *'tem de ser capaz de olhar além'* (**também sem especificar quem deve poder olhar além**), sem trazer a ideia de direito ou dever. Ao mesmo tempo, **apenas o segundo propõe que este conhecimento seja adaptado e acessível a diferentes tipos de stakeholders**, já que uma explicação adequada para um engenheiro de aprendizagem de máquina pode não ser adequada para um consumidor leigo.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Tendo em mente que o conceito de **transparência/interpretabilidade é uma ideia/conceito fundamental na Ética da IA** (especialmente em pesquisas de aprendizagem de máquina), estando ainda sujeito a divergências em sua interpretação/aplicação, que tipos de diferenças podem ocorrer quando olhamos para *'princípios não tão bem definidos'*, como **centrado no ser-humano**", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                               'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Em 'Data, Responsibly (Vol. 1) Mirror, Mirror', (Khan & Stoyanovich, [2020](https://dataresponsibly.github.io/comics/)), encontramos a seguinte recomentação:", style={'font-size': 18,
                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                         'text-justify': 'inter-word'}),
                    dcc.Markdown("*'Talvez o que precisamos, ao invés disso, seja fundamentar o projeto de sistemas de IA nas pessoas. Usando os dados das pessoas, coletados e implantados com uma metodologia equitativa, conforme determinado pelas pessoas, para criar tecnologia que seja benéfica para as pessoas.'*", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                    'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                    'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Enquanto que em '[Everyday Ethics for Artificial Intelligence](https://www.ibm.com/watson/assets/duo/pdf/everydayethics.pdf).' a seguinte norma foi sugerida:", style={'font-size': 18,
                                                                                                                                                                                                         'text-align': 'justify',
                                                                                                                                                                                                         'text-justify': 'inter-word'}),
                    dcc.Markdown("*'AI deve ser projetado para se alinhar com as normas e valores de seu grupo de usuários em mente.'*", style={'font-size': 18,
                                                                                                                                                'text-align': 'justify',
                                                                                                                                                'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("O primeiro documento menciona ideias como *'o uso de uma metodologia equitativa'* e *'tecnologia que seja benéfica para as pessoas'*. Esta ideia de *'pessoas'* parece se referir a um grande e diversificado  grupo (talvez 'todas as pessoas'). Enquanto isso, o segundo declara especificamente *'seu grupo de usuários em mente'*, o que poderia significar *'um pequeno e seleto grupo de pessoas'*, se é isso que os designers têm em mente como *'seus usuários'*.", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Muitas outras diferenças podem ser encontradas em nossa amostra, por exemplo: ", style={'font-size': 18,
                                                                                                                          'text-align': 'justify',
                                                                                                                          'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("'[Tieto’s AI ethics guidelines](https://www.tietoevry.com/en/newsroom/all-news-and-releases/press-releases/2018/10/tieto-strengthens-commitment-to-ethical-use-of-ai/)' assume uma outra postura de explicabilidade, dizendo que seus sistemas *'podem ser explicados e se explicam'*, colocando parte da responsabilidade de explicabilidade no próprio sistema **AI**, tornando-o um 'stakeholder' na cadeia de responsabilidade (uma abordagem curiosa); ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'text-justify': 'inter-word'}),
                    dcc.Markdown("'[The Toronto Declaration](https://www.torontodeclaration.org/declaration-text/english/)' dá uma definição extensa e não exaustiva do que *'discriminação'* significa segundo as leis internacionais, enquanto a maioria dos outros documentos resumem-se a apenas citar o conceito, deixando em aberto a interpretação dos tipos de *'discriminação que são permitids'*;", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                     'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                     'text-justify': 'inter-word'}),
                    dcc.Markdown("Em '[Artificial Intelligence and Machine Learning: Policy Paper](https://www.internetsociety.org/resources/doc/2017/artificial-intelligence-and-machine-learning-policy-paper/)', a justiça está relacionada à ideia de *'a IA proporciona oportunidades sócio-econômicas para todos'* (**benefícios**), e em '[Trustworthy AI in Aotearoa: AI Principles](https://aiforum.org.nz/wp-content/uploads/2020/03/Trustworthy-AI-in-Aotearoa-March-2020.pdf)' justiça é definida como *'sistemas de IA não prejudicam injustamente'* (**impactos**), o que podemos relacionar com a **diferença entre certas noções de justiça algorítmica** (paridade preditiva versus probabilidades equalizadas); ", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'text-justify': 'inter-word'}),
                    dcc.Markdown("Enquanto alguns documentos (e.g., '[Telefónica´s Approach to the Responsible Use of AI](https://www.telefonica.com/en/wp-content/uploads/sites/5/2021/08/ia-responsible-governance.pdf)') afirmam como a privacidade e a segurança são essenciais para o desenvolvimento de sistemas de IA, apenas alguns (e.g., '[Big Data, Artificial Intelligence, Machine Learning, and Data Protection](https://ico.org.uk/media/for-organisations/documents/2013559/big-data-ai-ml-and-data-protection.pdf)') especificam o que *'bons critérios de privacidade'* são (e.g., **data minimization**).", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}),
                    dcc.Markdown("Enquanto a maioria dos documentos interpreta Responsabilidade/Responsabilização como *'desenvolvedores sendo responsáveis por seus projetos '*(e.g., '[Declaration of Ethical Principles for AI in Latin America](https://ia-latam.com/etica-ia-latam/)'), **alguns documentos também colocam esta responsabilidade sobre os usuários**, e até mesmo os 'próprios algoritmos' (e.g., '[The Ethics of Code: Developing AI for Business with Five Core Principles](https://www.sage.com/~/media/group/files/business-builders/business-builders-ethics-of-code.pdf?la=en)').", style={'font-size': 18,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-align': 'justify',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text-justify': 'inter-word'}), html.Br(),
                    dcc.Markdown("Além das comparações mencionadas acima, muitas outras podem ser feitas utilizando nosso conjunto de dados (disponível para download no final desta página).", style={'font-size': 18,
                                                                                                                                                                                                       'text-align': 'justify',
                                                                                                                                                                                                       'text-justify': 'inter-word'}),
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-10',
                        className='ms-auto',
                        n_clicks=0,
                        color='warning'
                    )
                ),
            ],
            id='modal-body-scroll-10',
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

download_data = html.Div([
    dbc.Button('Download dos Dados', id='btn_data',
               outline=False, color='secondary'),
    dcc.Download(id="download-data")
], style={
    'margin-left': '25px',
    'margin-top': '10px',
    'margin-bottom': '5px',
    'display': 'inline-block'})

download_html = html.Div([
    dbc.Button('Download dos arquivos HTML', id='btn_html',
               outline=False, color='secondary'),
    dcc.Download(id="download-html")
], style={
    'margin-left': '10px',
    'margin-top': '10px',
    'margin-bottom': '5px',
    'display': 'inline-block'})

download_png = html.Div([
    dbc.Button('Download dos arquivos PNG', id='btn_png',
               outline=False, color='secondary'),
    dcc.Download(id="download-png")
], style={
    'margin-left': '10px',
    'margin-top': '10px',
    'margin-bottom': '5px',
    'display': 'inline-block'})


img_3 = html.Div([html.Img(id='img_3', src=app.get_asset_url('aireslogo.png'), height=512,
                 width=512, style={'height': '6%', 'width': '6%'})], style={'margin-left': '70px'})
aires_link = html.A(
    href='https://www.airespucrs.org/',
    children=[img_3]
)

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.H1('Worldwide AI Ethics ⚖️', style={'margin-top': '15px',
                                                 'margin-left': '15px',
                                                 'display': 'inline-block'}),
        html.Div([modal_abstract], style={
                 'display': 'inline-block', 'float': 'right', 'margin-top': '35px'}),

        html.Hr(),
        dbc.Row([
            dbc.Col([
                modal_map,
                dcc.Loading(id='loading', type='default', children=[
                    dcc.Graph(id='map', figure=fig)
                ])
            ], md=8),
            dbc.Col([
                modal_gender,
                dcc.Loading(id='loading_2', type='default', children=[
                    dcc.Graph(id='gender', figure=fig10)
                ])
            ], md=4),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                modal_principles,
                dcc.Loading(id='loading_3', type='default', children=[
                    dcc.Graph(id='principles', figure=fig4)
                ])
            ], md=7),
            dbc.Col([
                modal_institution,
                dcc.Loading(id='loading_4', type='default', children=[
                    dcc.Graph(id='institutions', figure=fig3)
                ])
            ], md=5),
        ], style={'margin-top': '10px'}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                modal_definition,
                dcc.Loading(id='loading_11', type='default', children=[
                    table_2
                ])
            ], md=12, style={'margin-top': '10px'})
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                modal_years,
                dcc.Loading(id='loading_5', type='default', children=[
                    dcc.Graph(id='years', figure=fig5)
                ])
            ], md=12, style={'margin-top': '10px'})
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                modal_nature,
                dcc.Loading(id='loading_6', type='default', children=[
                    dcc.Graph(id='nature', figure=fig6)
                ])
            ], md=3),
            dbc.Col([
                modal_regulation,
                dcc.Loading(id='loading_7', type='default', children=[
                    dcc.Graph(id='regulation', figure=fig8)
                ])
            ], md=3),
            dbc.Col([
                modal_normative,
                dcc.Loading(id='loading_9', type='default', children=[
                    dcc.Graph(id='normative', figure=fig7)
                ])
            ], md=3),
            dbc.Col([
                modal_impact,
                dcc.Loading(id='loading_8', type='default', children=[
                    dcc.Graph(id='impact', figure=fig9)
                ])
            ], md=3),
        ], style={'margin-top': '10px'}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                modal_table,
                dcc.Loading(id='loading_10', type='default', children=[
                    table
                ])
            ], md=12, style={'margin-top': '10px'})
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                aires_link, download_data, download_html, download_png
            ], md=12, style={'margin-top': '10px', 'margin-bottom': '30px'})
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
    Output('modal-body-scroll', 'is_open'),
    [
        Input('open-body-scroll', 'n_clicks'),
        Input('close-body-scroll', 'n_clicks'),
    ],
    [State('modal-body-scroll', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-1', 'is_open'),
    [
        Input('open-body-scroll-1', 'n_clicks'),
        Input('close-body-scroll-1', 'n_clicks'),
    ],
    [State('modal-body-scroll-1', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-2', 'is_open'),
    [
        Input('open-body-scroll-2', 'n_clicks'),
        Input('close-body-scroll-2', 'n_clicks'),
    ],
    [State('modal-body-scroll-2', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-3', 'is_open'),
    [
        Input('open-body-scroll-3', 'n_clicks'),
        Input('close-body-scroll-3', 'n_clicks'),
    ],
    [State('modal-body-scroll-3', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-4', 'is_open'),
    [
        Input('open-body-scroll-4', 'n_clicks'),
        Input('close-body-scroll-4', 'n_clicks'),
    ],
    [State('modal-body-scroll-4', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-5', 'is_open'),
    [
        Input('open-body-scroll-5', 'n_clicks'),
        Input('close-body-scroll-5', 'n_clicks'),
    ],
    [State('modal-body-scroll-5', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-6', 'is_open'),
    [
        Input('open-body-scroll-6', 'n_clicks'),
        Input('close-body-scroll-6', 'n_clicks'),
    ],
    [State('modal-body-scroll-6', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-7', 'is_open'),
    [
        Input('open-body-scroll-7', 'n_clicks'),
        Input('close-body-scroll-7', 'n_clicks'),
    ],
    [State('modal-body-scroll-7', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-8', 'is_open'),
    [
        Input('open-body-scroll-8', 'n_clicks'),
        Input('close-body-scroll-8', 'n_clicks'),
    ],
    [State('modal-body-scroll-8', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-9', 'is_open'),
    [
        Input('open-body-scroll-9', 'n_clicks'),
        Input('close-body-scroll-9', 'n_clicks'),
    ],
    [State('modal-body-scroll-9', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-10', 'is_open'),
    [
        Input('open-body-scroll-10', 'n_clicks'),
        Input('close-body-scroll-10', 'n_clicks'),
    ],
    [State('modal-body-scroll-10', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('modal-body-scroll-11', 'is_open'),
    [
        Input('open-body-scroll-11', 'n_clicks'),
        Input('close-body-scroll-11', 'n_clicks'),
    ],
    [State('modal-body-scroll-11', 'is_open')],
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
        'data(pt).rar')


@app.callback(
    Output("download-html", "data"),
    Input("btn_html", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'html_files(pt).rar')


@app.callback(
    Output("download-png", "data"),
    Input("btn_png", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        'png_files(pt).rar')


if __name__ == '__main__':
    app.run_server(debug=False)
