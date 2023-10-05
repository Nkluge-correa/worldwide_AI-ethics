import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

COLOR_GRAPH_RGB = 'rgba(172, 50, 75, 1.0)'
COLOR_GRAPHS_HEX = '#923146'
LARGE_FONT_SIZE = 18
FONT_SIZE = '1rem'

df = pd.read_parquet('data/arxiv_submissions.parquet')

fig = go.Figure()
for column in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate=column + ': %{y} <extra></extra>',
                             showlegend=True))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        tickangle=45,
        ticks='inside',
        tickfont=dict(
            size=12,
            color='white',
        ),
        fixedrange=True,
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
        fixedrange=True,
    ),
    title='<b><i>Arxiv Submissions History (2009 to 2021)</i><b>',
    template='plotly_dark',
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=LARGE_FONT_SIZE),
    font_color='white',
    hovermode='x',
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0}
)

df = pd.read_parquet('data/arxiv_submissions_cs.parquet')

fig1 = go.Figure()
for column in df.columns:
    fig1.add_trace(go.Scatter(x=df.index, y=df[column],
                              line=dict(width=3), name=column, mode='lines',
                              hoverlabel=dict(namelength=-1),
                              hovertemplate=column + ': %{y} <extra></extra>',
                              showlegend=True))

fig1.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        tickangle=45,
        ticks='inside',
        tickfont=dict(
            size=12,
            color='white',
        ),
        fixedrange=True,
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
        fixedrange=True,
    ),
    title='<b><i>Arxiv Submissions History in CS (2009 to 2021)</i><b>',
    template='plotly_dark',
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=LARGE_FONT_SIZE),
    font_color='white',
    hovermode='x',
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0}
)

df = pd.read_parquet('data/countries.parquet')


fig2 = go.Figure(data=go.Choropleth(
    locations=tuple(df.code),
    z=tuple(df.n_of_publications),
    text=tuple(df.countries),
    colorscale='oryel',
    showscale=False,
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar=dict(tickfont=dict(size=40))
))

fig2.update_layout(
    title="<b><i>Publications by Country</i></b>",
    template='plotly_dark',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='rgba(0,0,0,0)'
    ),
    margin=dict(l=0, r=0, b=0, t=30,),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    dragmode=False
)

df = pd.read_parquet('data/institutions.parquet')

fig3 = go.Figure(go.Bar(
    x=tuple(df.n_of_publications),
    y=tuple(['<b>'+elem+'</b>' for elem in df.institution_type]),
    text=tuple(df.n_of_publications),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
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

df = pd.read_parquet('data/gender.parquet')

fig4 = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in df.authors]),
    y=tuple(df.number_of_authors),
    text=tuple(df.number_of_authors),
    width=(0.8, 0.8),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

df = pd.read_parquet('data/principles.parquet')

fig5 = go.Figure(go.Bar(
    x=tuple(df.n_of_citations),
    y=tuple(['<b>'+elem+'</b>' for elem in df.principles]),
    text=tuple(df.n_of_citations),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    margin=dict(l=0, r=0, b=0, t=30,),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

df = pd.read_parquet('data/Accountability_gram.parquet')

fig_a = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')

fig_a.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=LARGE_FONT_SIZE),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=LARGE_FONT_SIZE,
    xaxis_title=None,
    yaxis_title=None
)

df = pd.read_parquet('data/time_line.parquet')

fig6 = go.Figure(data=go.Bar(x=tuple(df.years), y=tuple(df.n_of_published_documents),
                             text=tuple(df.n_of_published_documents),
                             marker=dict(color=COLOR_GRAPHS_HEX), name=" ",
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='<extra></extra>', showlegend=False))

fig6.update_traces(textposition='outside')

fig6.add_trace(go.Scatter(x=df.years, y=df.n_of_published_documents, mode='lines+markers',
                                name='',
                                line=dict(color='rgba(172, 50, 75, 0.5)'),
                                connectgaps=True,
                                hovertemplate='<extra></extra>', showlegend=False))

fig6.update_layout(
    title="<b><i>Publication Timeline</i></b>",
    template='plotly_dark',
    margin=dict(l=0, r=0, b=0, t=30,),
    xaxis=dict(
        showline=False,
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        tickfont=dict(
            size=12,
        ),
        fixedrange=True,
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
        fixedrange=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(font_size=14),
)

df = pd.read_parquet('data/document_nature.parquet')

fig7 = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in df.document_nature]),
    y=tuple(df.n_of_documents),
    text=tuple(df.n_of_documents),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

df = pd.read_parquet('data/document_regulation.parquet')

fig8 = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in df.document_regulation]),
    y=tuple(df.n_of_documents),
    text=tuple(df.n_of_documents),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

df = pd.read_parquet('data/document_normative.parquet')

fig9 = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in df.document_normative]),
    y=tuple(df.n_of_documents),
    text=tuple(df.n_of_documents),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)

df = pd.read_parquet('data/document_impact.parquet')

fig10 = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in df.document_impact]),
    y=tuple(df.n_of_documents),
    text=tuple(df.n_of_documents),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
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
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    xaxis=dict(
        visible=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        tickfont=dict(size=12),
        fixedrange=True,
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    bargroupgap=0.8
)
