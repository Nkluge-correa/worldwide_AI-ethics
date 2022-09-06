
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dcc, html, Output, Input, State, dash_table


app = dash.Dash(__name__,
                meta_tags=[
                    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
                external_stylesheets=[dbc.themes.CYBORG])

server = app.server
app.title = 'Worldwide AI Ethics 🌐'

df = pd.read_excel('meta_pt.xlsx', 'meta_countries')

fig = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['Nº of Publications'],
    text=df['Countries'],
    colorscale='deep',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
))

fig.update_layout(
    font_family='Lato',
    font_color='white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='rgba(0,0,0,0)'
    ),
    margin={'r': 0, 't': 10, 'l': 0, 'b': 0},
    legend=dict(title_font_family='Lato', font_size=18),
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
        line=dict(
            width=1))))
fig10.update_traces(textposition='outside')
fig10.update_yaxes(showgrid=False, visible=True,
                   showticklabels=True, tickfont=dict(family='Lato', size=16))
fig10.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(family='Lato', size=16))
fig10.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
colors = '#636efa'
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
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Lato',
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
            family='Lato',
            size=16,
            color='white',
        ),
    ),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_family='Lato', font_size=20),
)
annotations = []
annotations.append(dict(xref='paper', x=0.05, y=y_data[0],
                        xanchor='right', yanchor='middle',
                        text=labels,
                        font=dict(family='Lato',
                                  size=16),
                        showarrow=False))
annotations.append(dict(xref='paper', x=0.95, y=y_data[-1],
                        xanchor='left', yanchor='middle',
                        text='',
                        font=dict(family='Lato',
                                  size=16),
                        showarrow=False))
fig5.update_layout(annotations=annotations,
                   font=dict(family='Lato'),
                   font_color='white',
                   hovermode='x',
                   hoverlabel=dict(font_family='Lato', font_size=20),
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
                line=dict(
                    width=1))))
fig4.update_traces(textposition='outside')
fig4.update_yaxes(tickfont=dict(family='Lato', size=16))
fig4.update_xaxes(visible=True, tickfont=dict(family='Lato', size=16))
fig4.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
                line=dict(
                    width=1))))
fig3.update_traces(textposition='outside')
fig3.update_yaxes(tickfont=dict(family='Lato', size=16))
fig3.update_xaxes(visible=True, tickfont=dict(family='Lato', size=16))
fig3.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
        line=dict(
            width=1))))
fig6.update_traces(textposition='outside')
fig6.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig6.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig6.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
        line=dict(
            width=1))))
fig8.update_traces(textposition='outside')
fig8.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig8.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig8.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
        line=dict(
            width=1))))
fig9.update_traces(textposition='outside')
fig9.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig9.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig9.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
        line=dict(
            width=1))))
fig7.update_traces(textposition='outside')
fig7.update_yaxes(showgrid=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig7.update_xaxes(showgrid=False, showline=False, visible=True,
                  showticklabels=True, tickfont=dict(family='Lato', size=16))
fig7.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
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
            'text-align': 'justify', 'text-justify': 'inter-word', 'font-family': 'Lato', 'fontSize': 16, 'padding': '10px',
            'backgroundColor': '#060606'
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        style_header={
            'backgroundColor': '#060606',
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
                     'height': '600px', 'overflowY': 'scroll'},
        page_current=0,
        page_size=50,
        style_cell={
            'text-align': 'justify', 'text-justify': 'inter-word', 'font-family': 'Lato', 'fontSize': 16, 'padding': '10px',
            'backgroundColor': '#060606'
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        style_header={
            'backgroundColor': '#060606',
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
                   showticklabels=True, tickfont=dict(family='Lato', size=12))
fig11.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(family='Lato', size=12))
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
            family='Lato',
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
            family='Lato',
            size=12,
            color='white',
        ),
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_family='Lato', font_size=20),
    title='Nº de Submissões no Arxiv por Categoria',
    font_family='Lato',
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
                   showticklabels=True, tickfont=dict(family='Lato', size=12))
fig12.update_xaxes(showgrid=False, showline=False, visible=True,
                   showticklabels=True, tickfont=dict(family='Lato', size=12))
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
            family='Lato',
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
            family='Lato',
            size=12,
            color='white',
        ),
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_family='Lato', font_size=20),
    title='Nº de Submissões no Arxiv em Ciências da Computação',
    font_family='Lato',
    font_color='white',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)

df13 = pd.read_excel('meta_pt.xlsx', 'Accountability_gram')

fig13 = px.bar(df13, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Responsabilidade/Responsabilização',
               color='Contagem de palavras', color_continuous_scale='deep')
fig13.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df14 = pd.read_excel('meta_pt.xlsx', 'Beneficence_gram')

fig14 = px.bar(df14, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Beneficência/Não-maleficência',
               color='Contagem de palavras', color_continuous_scale='deep')
fig14.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df15 = pd.read_excel('meta_pt.xlsx', 'Children_gram')

fig15 = px.bar(df15, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Direitos da Criança e do Adolescente',
               color='Contagem de palavras', color_continuous_scale='deep')
fig15.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df16 = pd.read_excel('meta_pt.xlsx', 'Dignity_gram')

fig16 = px.bar(df15, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Dignidade/Direitos Humanos',
               color='Contagem de palavras', color_continuous_scale='deep')
fig16.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df17 = pd.read_excel('meta_pt.xlsx', 'Diversity_gram')

fig17 = px.bar(df17, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Diversidade/Inclusão/Pluralismo/Acessibilidade',
               color='Contagem de palavras', color_continuous_scale='deep')
fig17.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df18 = pd.read_excel('meta_pt.xlsx', 'Freedom_gram')

fig18 = px.bar(df18, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica',
               color='Contagem de palavras', color_continuous_scale='deep')
fig18.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df19 = pd.read_excel('meta_pt.xlsx', 'Formation_gram')

fig19 = px.bar(df19, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Educação/Formação Humana',
               color='Contagem de palavras', color_continuous_scale='deep')
fig19.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df21 = pd.read_excel('meta_pt.xlsx', 'Centeredness_gram')

fig21 = px.bar(df21, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Centrado no Ser Humano/Alinhamento',
               color='Contagem de palavras', color_continuous_scale='deep')
fig21.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df22 = pd.read_excel('meta_pt.xlsx', 'Property_gram')

fig22 = px.bar(df22, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Propriedade Intelectual',
               color='Contagem de palavras', color_continuous_scale='deep')
fig22.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df23 = pd.read_excel('meta_pt.xlsx', 'Justice_gram')

fig23 = px.bar(df23, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Justiça/Equidade/Igualdade/Não-discriminação',
               color='Contagem de palavras', color_continuous_scale='deep')
fig23.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df24 = pd.read_excel('meta_pt.xlsx', 'Labor_gram')

fig24 = px.bar(df24, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Direitos Trabalhistas',
               color='Contagem de palavras', color_continuous_scale='deep')
fig24.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df25 = pd.read_excel('meta_pt.xlsx', 'Open_gram')

fig25 = px.bar(df25, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Código Aberto/Concorrência Justa/Cooperação',
               color='Contagem de palavras', color_continuous_scale='deep')
fig25.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df26 = pd.read_excel('meta_pt.xlsx', 'Privacy_gram')

fig26 = px.bar(df26, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Privacidade',
               color='Contagem de palavras', color_continuous_scale='deep')
fig26.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df27 = pd.read_excel('meta_pt.xlsx', 'Reliability_gram')

fig27 = px.bar(df27, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Confiabilidade/Segurança/Confiança/Fiabilidade',
               color='Contagem de palavras', color_continuous_scale='deep')
fig27.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df28 = pd.read_excel('meta_pt.xlsx', 'Sustainability_gram')

fig28 = px.bar(df28, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Sustentabilidade',
               color='Contagem de palavras', color_continuous_scale='deep')
fig28.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df29 = pd.read_excel('meta_pt.xlsx', 'Transparency_gram')

fig29 = px.bar(df29, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Transparência/Explicabilidade/Auditoria',
               color='Contagem de palavras', color_continuous_scale='deep')
fig29.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df30 = pd.read_excel('meta_pt.xlsx', 'Truthfulness_gram')

fig30 = px.bar(df30, x='Top four-grams', y='Contagem de palavras',
               title=f'Top-20 Palavras (four-grams) do princípio: Veracidade',
               color='Contagem de palavras', color_continuous_scale='deep')
fig30.update_layout(
    font_family='Lato',
    template='plotly_dark',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)

with open('info_pt.txt', encoding='utf8') as file_in:
    info = []
    for line in file_in:
        info.append(line.strip())

modal_abstract = html.Div(
    [
        dbc.Button('Abstract', id='open-fs', outline=True, color='primary'),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## **Worldwide AI Ethics: uma revisão de 200 diretrizes e recomendações para a governança da IA**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([
                    html.Span([dcc.Markdown(info[0])], style={'font-family': 'Lato',
                                                              'font-size': 18,
                                                              'text-align': 'justify',
                                                              'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_sub', figure=fig11), html.Br(),
                    html.Span([dcc.Markdown(info[72])], style={'font-family': 'Lato',
                                                               'font-size': 18,
                                                               'text-align': 'justify',
                                                               'text-justify': 'inter-word'}), html.Br(),
                    dcc.Graph(id='arxiv_CS', figure=fig12), html.Br(),
                    html.Span([dcc.Markdown(info[73])], style={'font-family': 'Lato',
                                                               'font-size': 18,
                                                               'text-align': 'justify',
                                                               'text-justify': 'inter-word'}),
                    html.Hr(),
                    html.Span([dcc.Markdown('### **Cite as:**'), dcc.Markdown(info[1])], style={'font-family': 'Lato',
                                                                                                'font-style': 'bold',
                                                                                                'text-align': 'justify',
                                                                                                'text-justify': 'inter-word'}),
                    html.Hr(),
                    dcc.Markdown('Para mais informações, contate [airespucrs@airespucrs.org](mailto:airespucrs@airespucrs.org).',
                                 style={'text-decoration': 'none',
                                        'font-size': 18,
                                        'font-family': 'Lato',
                                        'text-align': 'justify',
                                        'text-justify': 'inter-word'}),
                    dcc.Markdown('Acesse o Dash completo (versão em Power BI) [aqui](https://www.airespucrs.org/worldwide-ai-ethics).',
                                 style={'text-decoration': 'none',
                                        'font-family': 'Lato',
                                        'font-size': 18,
                                        'text-align': 'justify',
                                        'text-justify': 'inter-word'}),
                    dcc.Markdown('Acesse o artigo completo (preprint) [aqui](https://doi.org/10.48550/arXiv.2206.11922).',
                                 style={'text-decoration': 'none',
                                        'font-family': 'Lato',
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
                        color='primary'
                    )
                ),
            ],
            id='modal-fs',
            fullscreen=True,
        ),
    ], style={
        'margin-left': '15px',
        'margin-bottom': '10px',
    },
)
modal_map = html.Div(
    [
        dbc.Button(
            'Publicações por País', id='open-body-scroll', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Publicações por País**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[2]), html.Br(), dcc.Markdown(info[3])], style={'font-family': 'Lato',
                                                                                                'text-align': 'justify',
                                                                                                'font-size': 18,
                                                                                                'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Autores por Gênero', id='open-body-scroll-1', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Autores por Gênero**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[4]), html.Br(), dcc.Markdown(info[5])], style={'font-family': 'Lato',
                                                                                                'text-align': 'justify',
                                                                                                'font-size': 18,
                                                                                                'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-1',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Publicações por Ano', id='open-body-scroll-2', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Publicações por Ano**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[6]), html.Br(), dcc.Markdown(info[7])], style={'font-family': 'Lato',
                                                                                                'text-align': 'justify',
                                                                                                'font-size': 18,
                                                                                                'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-2',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Citações por Princípio', id='open-body-scroll-3', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Citações por Princípio**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[8]), html.Br(),
                               dcc.Markdown(info[9]), html.Br(),
                               dcc.Markdown(info[10]), html.Br(),
                               dcc.Markdown(info[19]), html.Br(),
                               dcc.Markdown(info[20]),
                               dcc.Graph(id='account',
                                         figure=fig13), html.Br(),
                               dcc.Markdown(info[21]),
                               dcc.Graph(id='benef', figure=fig14), html.Br(),
                               dcc.Markdown(info[22]),
                               dcc.Graph(id='child', figure=fig15), html.Br(),
                               dcc.Markdown(info[23]),
                               dcc.Graph(id='digni', figure=fig16), html.Br(),
                               dcc.Markdown(info[24]),
                               dcc.Graph(id='diver', figure=fig17), html.Br(),
                               dcc.Markdown(info[25]),
                               dcc.Graph(id='free', figure=fig18), html.Br(),
                               dcc.Markdown(info[26]),
                               dcc.Graph(id='educa', figure=fig19), html.Br(),
                               dcc.Markdown(info[27]),
                               dcc.Graph(id='align', figure=fig21), html.Br(),
                               dcc.Markdown(info[28]),
                               dcc.Graph(id='intellec',
                                         figure=fig22), html.Br(),
                               dcc.Markdown(info[29]),
                               dcc.Graph(id='justice',
                                         figure=fig23), html.Br(),
                               dcc.Markdown(info[30]),
                               dcc.Graph(id='labor', figure=fig24), html.Br(),
                               dcc.Markdown(info[31]),
                               dcc.Graph(id='open', figure=fig25), html.Br(),
                               dcc.Markdown(info[32]),
                               dcc.Graph(id='privacy',
                                         figure=fig26), html.Br(),
                               dcc.Markdown(info[33]),
                               dcc.Graph(id='reliab', figure=fig27), html.Br(),
                               dcc.Markdown(info[34]),
                               dcc.Graph(id='sustaina',
                                         figure=fig28), html.Br(),
                               dcc.Markdown(info[35]),
                               dcc.Graph(id='trans', figure=fig29), html.Br(),
                               dcc.Markdown(info[36]),
                               dcc.Graph(id='truth', figure=fig30), html.Br(),
                               ], style={'font-family': 'Lato',
                                         'text-align': 'justify',
                                         'font-size': 18,
                                         'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-3',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Publicações por Tipo de Instituição', id='open-body-scroll-4', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Publicações por Tipo de Instituição**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[11]), html.Br(), dcc.Markdown(info[12]), html.Br(), dcc.Markdown(info[13])], style={'font-family': 'Lato',
                                                                                                                                     'text-align': 'justify',
                                                                                                                                     'font-size': 18,
                                                                                                                                     'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-4',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Publicações por Tipo (Natureza/Conteúdo)', id='open-body-scroll-5', size='lg', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Publicações por Tipo (Natureza/Conteúdo)**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[14]), html.Br(),
                               dcc.Markdown(info[15]),
                               dcc.Markdown(info[16]),
                               dcc.Markdown(info[17]), html.Br(),
                               dcc.Markdown(info[18])], style={'font-family': 'Lato',
                                                               'text-align': 'justify',
                                                               'font-size': 18,
                                                               'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-5',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Publicações por Tipo (Forma de Regulação)', id='open-body-scroll-6', size='lg', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Publicações por Tipo (Forma de Regulação)**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[37]), html.Br(),
                               dcc.Markdown(info[38]),
                               dcc.Markdown(info[39]),
                               dcc.Markdown(info[40]), html.Br(),
                               dcc.Markdown(info[41])], style={'font-family': 'Lato',
                                                               'font-size': 18,
                                                               'text-align': 'justify',
                                                               'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-6',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Publicações por Tipo (Escopo de Impacto)', id='open-body-scroll-7', size='lg', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Publicações por Tipo (Escopo de Impacto)**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[42]), html.Br(),
                               dcc.Markdown(info[43]),
                               dcc.Markdown(info[44]),
                               dcc.Markdown(info[45]), html.Br(),
                               dcc.Markdown(info[46])], style={'font-family': 'Lato',
                                                               'font-size': 18,
                                                               'text-align': 'justify',
                                                               'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-7',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Nº de Publicações por Tipo (Força Normativa)', id='open-body-scroll-8', size='lg', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Nº de Publicações por Tipo (Força Normativa)**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[47]), html.Br(),
                               dcc.Markdown(info[48]),
                               dcc.Markdown(info[49]), html.Br(),
                               dcc.Markdown(info[50]), html.Br(),
                               dcc.Markdown(info[51])], style={'font-family': 'Lato',
                                                               'text-align': 'justify',
                                                               'font-size': 18,
                                                               'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-8',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Publicações (URL & Abstract)', id='open-body-scroll-9', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Publicações (URL & Abstract)**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[52])], style={'font-family': 'Lato',
                                                               'text-align': 'justify',
                                                               'font-size': 18,
                                                               'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-9',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
            'Publicações (Definição dos Princípios)', id='open-body-scroll-10', outline=True, color='primary', n_clicks=0
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '### **Publicações (Definição dos Princípios)**'), style={'font-family': 'Lato'})),
                dbc.ModalBody([dcc.Markdown(info[53]), html.Br(),
                               dcc.Markdown(info[54]),
                               dcc.Markdown(info[55]), html.Br(),
                               dcc.Markdown(info[56]),
                               dcc.Markdown(info[57]), html.Br(),
                               dcc.Markdown(info[58]), html.Br(),
                               dcc.Markdown(info[59]), html.Br(),
                               dcc.Markdown(info[60]),
                               dcc.Markdown(info[61]), html.Br(),
                               dcc.Markdown(info[62]),
                               dcc.Markdown(info[63]), html.Br(),
                               dcc.Markdown(info[64]), html.Br(),
                               dcc.Markdown(info[65]), html.Br(),
                               dcc.Markdown(info[66]),
                               dcc.Markdown(info[67]),
                               dcc.Markdown(info[68]),
                               dcc.Markdown(info[69]),
                               dcc.Markdown(info[70]), html.Br(),
                               dcc.Markdown(info[71]), ], style={'font-family': 'Lato',
                                                                 'text-align': 'justify',
                                                                 'font-size': 18,
                                                                 'text-justify': 'inter-word'}),
                dbc.ModalFooter(
                    dbc.Button(
                        'Fechar',
                        id='close-body-scroll-10',
                        className='ms-auto',
                        n_clicks=0,
                        color='primary'
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
        html.H1('Worldwide AI Ethics 🌐', style={'font-style': 'bold',
                                                'margin-top': '15px',
                                                'margin-left': '15px',
                                                'display': 'inline-block'}),

        modal_abstract,
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
