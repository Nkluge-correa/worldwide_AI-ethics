import os
import pandas as pd
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_excel('meta_en.xlsx', 'meta_countries')

fig = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['Nº of Publications'],
    text=df['Countries'],
    colorscale='ylorrd',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar=dict(tickfont=dict(size=40))
))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='rgba(0,0,0,0)'
    ),
    margin={'r': 0, 't': 60, 'l': 0, 'b': 0},
    legend=dict(title_font_family='Lato', font_size=40),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
py.plot(fig, filename='Mapa')

df = pd.read_excel('meta_en.xlsx', 'meta_gender')
x_tick_text = list(df['Authors'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig = go.Figure(go.Bar(
    x=x_tick_text,
    y=df['Nº'],
    text=df['Nº'],
    width=[0.8, 0.8],
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color='rgba((255, 136, 0, 0.8)',
        line=dict(
            color='rgba((255, 136, 0, 1.0)',
            width=2))))
fig.update_traces(textposition='inside')
fig.update_yaxes(showgrid=True, gridcolor='lightgray', visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=40,
    uniformtext_mode='hide',
    barmode='group',
    bargroupgap=0.8
)
py.plot(fig, filename='Gênero')


df = pd.read_excel('meta_en.xlsx', 'meta_year')
labels = '<i>Documents</br>published<br>in 2014</i>'
colors = 'rgb(183,69,0)'
mode_size = 16
line_size = 6
x_data = list(df['Years'])
y_data = list(df['Nº of Published Documents'])

fig = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='lines+markers',
                                name='',
                                line=dict(color=colors, width=line_size),
                                marker=dict(size=12),
                                connectgaps=True,
                                hovertemplate='<b>Nº of Publications</b>: %{y} <extra></extra>'
                                ))
fig.add_trace(go.Scatter(
    x=[x_data[0], x_data[-1]],
    y=[y_data[0], y_data[-1]],
    mode='markers',
    marker=dict(color=colors, size=mode_size),
    hoverinfo='skip'
))
fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Lato',
            size=40,
            color='black',
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
            size=40,
            color='black',
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
                                  size=20),
                        showarrow=False))
fig.update_layout(annotations=annotations,
                  font=dict(family='Lato'),
                  font_color='black',
                  hovermode='x',
                  hoverlabel=dict(font_family='Lato', font_size=20),
                  margin={'r': 20, 't': 70, 'l': 20, 'b': 20})
py.plot(fig, filename='Ano')


df = pd.read_excel('meta_en.xlsx', 'meta_principles')
y_tick_text = list(df['Principles'])
y_tick_text = ['<b>'+elem+'</b>' for elem in y_tick_text]
fig = go.Figure(go.Bar(
    x=df['Nº of Citations'],
    y=y_tick_text,
    text=df['Nº of Citations'],
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
                color='rgba(183,69,0, 0.8)',
                line=dict(
                    color='rgba(255,207,3, 1.0)',
                    width=4))))
fig.update_traces(textposition='outside', textfont_size=25)
fig.update_xaxes(showgrid=True, gridcolor='lightgray', visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=25))
fig.update_yaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=25))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
)
py.plot(fig, filename='Princípios')

df = pd.read_excel('meta_en.xlsx', 'meta_institutions')
y_tick_text = list(df['Institution Type'])
y_tick_text = ['<b>'+elem+'</b>' for elem in y_tick_text]
fig = go.Figure(go.Bar(
    x=df['Nº of Publications'],
    y=y_tick_text,
    text=df['Nº of Publications'],
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
                color='rgba(183,69,0, 0.8)',
                line=dict(
                    color='rgba(255,207,3, 1.0)',
                    width=4))))
fig.update_traces(textposition='inside', textfont_size=30)
fig.update_yaxes(tickfont=dict(family='Lato', size=30))
fig.update_xaxes(visible=True, tickfont=dict(family='Lato', size=30))
fig.update_layout(
    font_family='Lato',
    font_color='black',
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
        showgrid=True,
        gridcolor='lightgray'
    ),

    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext=dict(minsize=20),
)
py.plot(fig, filename='Instituições')


df = pd.read_excel('meta_en.xlsx', 'meta_nature')
x_tick_text = list(df['Documents Nature/Content'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig = go.Figure(go.Bar(
    x=x_tick_text,
    y=df['Nº of Documents'],
    text=df['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(183,69,0, 0.8)',
        line=dict(
            color='rgba(255,207,3, 1.0)',
            width=4))))
fig.update_traces(textposition='inside', textfont_size=40)
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=40,
    barmode='group',
    bargroupgap=0.8
)
py.plot(fig, filename='Tipo I')


df = pd.read_excel('meta_en.xlsx', 'meta_regulation')
x_tick_text = list(df['Documents Form of Regulation'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig = go.Figure(go.Bar(
    x=x_tick_text,
    y=df['Nº of Documents'],
    text=df['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(183,69,0, 0.8)',
        line=dict(
            color='rgba(255,207,3, 1.0)',
            width=4))))
fig.update_traces(textposition='inside', textfont_size=40)
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)
py.plot(fig, filename='Tipo II')


df = pd.read_excel('meta_en.xlsx', 'meta_impact')
x_tick_text = list(df['Documents Impact Scope'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig = go.Figure(go.Bar(
    x=x_tick_text,
    y=df['Nº of Documents'],
    text=df['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(183,69,0, 0.8)',
        line=dict(
            color='rgba(255,207,3, 1.0)',
            width=4))))
fig.update_traces(textposition='auto', textfont_size=40)
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=40,
    barmode='group',
    bargroupgap=0.8
)
py.plot(fig, filename='Tipo IV')


df = pd.read_excel('meta_en.xlsx', 'meta_normative')
x_tick_text = list(df['Documents Normative Strength'])
x_tick_text = ['<b>'+elem+'</b>' for elem in x_tick_text]
fig = go.Figure(go.Bar(
    x=x_tick_text,
    y=df['Nº of Documents'],
    text=df['Nº of Documents'],
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=[0.5, 0.5, 0.5],
    marker=dict(
        color='rgba(183,69,0, 0.8)',
        line=dict(
            color='rgba(255,207,3, 1.0)',
            width=4))))
fig.update_traces(textposition='auto', textfont_size=40)
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=40))
fig.update_layout(
    font_family='Lato',
    font_color='black',
    hoverlabel=dict(font_family='Lato', font_size=20),
    margin=dict(l=20, r=20, t=70, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)
py.plot(fig, filename='Tipo III')


df = pd.read_excel('arxiv_submissions_data_en.xlsx', 'Arxiv')
df = df.set_index('Date')
fig = go.Figure(layout={'template': 'plotly_dark'})
for column in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='Nº of Submissions (' +
                             column + '): %{y} <extra></extra>',
                             showlegend=True))
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(family='Lato', size=20))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=14))
fig.update_layout(
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
            size=14,
            color='black',
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
            size=20,
            color='black',
        ),
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_family='Lato', font_size=20),
    font_family='Lato',
    font_color='black',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)
py.plot(fig, filename='Arxiv(sub)')

df = pd.read_excel('arxiv_submissions_data_en.xlsx', 'Arxiv(CS)')
df = df.set_index('Date')
fig = go.Figure(layout={'template': 'plotly_dark'})
for column in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='Nº of Submissions (' +
                             column + '): %{y} <extra></extra>',
                             showlegend=True))
fig.update_yaxes(showgrid=True, gridcolor='lightgray',
                 showticklabels=True, tickfont=dict(family='Lato', size=20))
fig.update_xaxes(showgrid=False, showline=False, visible=True,
                 showticklabels=True, tickfont=dict(family='Lato', size=20))
fig.update_layout(
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
            size=20,
            color='black',
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
            size=20,
            color='black',
        ),
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_family='Lato', font_size=20),
    font_family='Lato',
    font_color='black',
    hovermode='x',
    margin={'r': 20, 't': 70, 'l': 20, 'b': 20}
)
py.plot(fig, filename='Arxiv(CS)')

# N-grams

# ---------------------------------------------------------------------------------------------------------------# en

df = pd.read_excel('meta_en.xlsx', 'Accountability_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Accountability/Liability',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Beneficence_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Beneficence/Non-Maleficence',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Children_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Children & Adolescents Rights',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Dignity_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Dignity/Human Rights',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Diversity_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Diversity/Inclusion/Pluralism/Accessibility',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Freedom_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Freedom/Autonomy/Democratic Values/Technological Sovereignty',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Formation_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Human Formation/Education',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Centeredness_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Human-Centeredness/Alignment',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Property_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Intellectual Property',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Justice_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Justice/Equity/Fairness/Non-discrimination',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Labor_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Labor Rights',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Open_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Open source/Fair Competition/Cooperation',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Privacy_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Privacy',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Reliability_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Reliability/Safety/Security/Trustworthiness',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Sustainability_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Sustainability',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_en.xlsx', 'Transparency_gram')

fig = px.bar(df, x='Top four-grams', y='Word Count',
             title=f'Top-20 Words (four-grams) in principle: Transparency/Explainability/Auditability',
             color='Word Count', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df0 = pd.read_excel('meta_en.xlsx', 'Truthfulness_gram')

fig0 = px.bar(df0, x='Top four-grams', y='Word Count',
              title=f'Top-20 Words (four-grams) in principle: Truthfulness',
              color='Word Count', color_continuous_scale='deep')
fig0.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


# ---------------------------------------------------------------------------------------------------------------# pt

df = pd.read_excel('meta_pt.xlsx', 'Accountability_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Responsabilidade/Responsabilização',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Beneficence_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Beneficência/Não-maleficência',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Children_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Direitos da Criança e do Adolescente',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Dignity_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Dignidade/Direitos Humanos',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Diversity_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Diversidade/Inclusão/Pluralismo/Acessibilidade',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Freedom_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Liberdade/Autonomia/Valores Democráticos/Soberania Tecnológica',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Formation_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Educação/Formação Humana',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Centeredness_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Centrado no Ser Humano/Alinhamento',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Property_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Propriedade Intelectual',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Justice_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Justiça/Equidade/Igualdade/Não-discriminação',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Labor_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Direitos Trabalhistas',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Open_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Código Aberto/Concorrência Justa/Cooperação',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Privacy_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Privacidade',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Reliability_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Confiabilidade/Segurança/Confiança/Fiabilidade',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Sustainability_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Sustentabilidade',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df = pd.read_excel('meta_pt.xlsx', 'Transparency_gram')

fig = px.bar(df, x='Top four-grams', y='Contagem de palavras',
             title=f'Top-20 Palavras (four-grams) do princípio: Transparência/Explicabilidade/Auditoria',
             color='Contagem de palavras', color_continuous_scale='deep')
fig.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)


df0 = pd.read_excel('meta_pt.xlsx', 'Truthfulness_gram')

fig0 = px.bar(df0, x='Top four-grams', y='Contagem de palavras',
              title=f'Top-20 Palavras (four-grams) do princípio: Veracidade',
              color='Contagem de palavras', color_continuous_scale='deep')
fig0.update_layout(
    font_family='Lato',
    template='plotly_white',
    hoverlabel=dict(font_family='Lato', font_size=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
)
