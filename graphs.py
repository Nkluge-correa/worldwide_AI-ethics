import json
import collections
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

COLOR_GRAPH_RGB = 'rgba(172, 50, 75, 1.0)'
COLOR_GRAPHS_HEX = '#923146'
LARGE_FONT_SIZE = 18
FONT_SIZE = '1rem'

# All countries in WAIE
countries_in_waie = {
    'Argentina': 'ARG',
    'Australia': 'AUS',
    'Austria': 'AUT',
    'Belgium': 'BEL',
    'Brazil': 'BRA',
    'Canada': 'CAN',
    'China': 'CHN',
    'Colombia': 'COL',
    'Denmark': 'DNK',
    'Finland': 'FIN',
    'France': 'FRA',
    'Germany': 'DEU',
    'Hungary': 'HUN',
    'Iceland': 'ISL',
    'India': 'IND',
    'Italy': 'ITA',
    'Japan': 'JPN',
    'Lithuania': 'LTU',
    'Luxembourg': 'LUX',
    'Netherlands': 'NLD',
    'New Zealand': 'NZL',
    'Norway': 'NOR',
    'Russia': 'RUS',
    'Singapore': 'SGP',
    'South Africa': 'ZAF',
    'South Korea': 'KOR',
    'Spain': 'ESP',
    'Sweden': 'SWE',
    'Switzerland': 'CHE',
    'Turkey': 'TUR',
    'United Arab Emirates': 'ARE',
    'United Kingdom': 'GBR',
    'United States of America': 'USA'
}

with open('data/data_processed.json') as f:
    data = json.load(f)

df = pd.read_parquet('data/arxiv_submissions.parquet')

arxiv = go.Figure()
for column in df.columns:
    arxiv.add_trace(go.Scatter(x=df.index, y=df[column],
                             line=dict(width=3), name=column, mode='lines',
                             hoverlabel=dict(namelength=-1),
                             hovertemplate=column + ': %{y} <extra></extra>',
                             showlegend=True))

arxiv.update_layout(
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

arxiv_cs = go.Figure()
for column in df.columns:
    arxiv_cs.add_trace(go.Scatter(x=df.index, y=df[column],
                              line=dict(width=3), name=column, mode='lines',
                              hoverlabel=dict(namelength=-1),
                              hovertemplate=column + ': %{y} <extra></extra>',
                              showlegend=True))

arxiv_cs.update_layout(
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

plot_data=collections.Counter(
    [item for sublist in [d['country'] if isinstance(d['country'], list) else [d['country']] for d in data] for item in sublist]
)

countries = go.Figure(data=go.Choropleth(
    locations=tuple(countries_in_waie.values()),
    z=tuple([plot_data[country] for country in countries_in_waie.keys()]),
    text=tuple(countries_in_waie.keys()),
    colorscale='oryel',
    showscale=False,
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar=dict(tickfont=dict(size=40))
))

countries.update_layout(
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

plot_data=collections.Counter(
    [item for sublist in [d['institution_type'] if isinstance(d['institution_type'], list) else [d['institution_type']] for d in data] for item in sublist]
)
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[1]))

institutions = go.Figure(go.Bar(
    x=tuple(plot_data.values()),
    y=tuple(['<b>'+elem+'</b>' for elem in plot_data.keys()]),
    text=tuple(plot_data.values()),
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

institutions.update_layout(
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

number_of_male_authors = [item for sublist in [d['number_of_male_authors'] if isinstance(d['number_of_male_authors'], list) else [d['number_of_male_authors']] for d in data] for item in sublist]
number_of_male_authors = sum([int(x) for x in number_of_male_authors if x != "Unspecified" and x != ""])
number_of_female_authors = [item for sublist in [d['number_of_female_authors'] if isinstance(d['number_of_female_authors'], list) else [d['number_of_female_authors']] for d in data] for item in sublist]
number_of_female_authors = sum([int(x) for x in number_of_female_authors if x != "Unspecified" and x != ""])

authors = go.Figure(go.Bar(
    x=tuple(["<b>Female Authors</b>", "<b>Male Authors</b>"]),
    y=tuple([number_of_female_authors, number_of_male_authors]),
    text=tuple([number_of_female_authors, number_of_male_authors]),
    width=(0.8, 0.8),
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

authors.update_layout(
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

plot_data = collections.Counter(
    principle for item in data for principle, value in item["principles"].items() if value
)
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[1]))

principles = go.Figure(go.Bar(
    x=tuple(plot_data.values()),
    y=tuple(['<b>'+elem+'</b>' for elem in plot_data.keys()]),
    text=tuple(plot_data.values()),
    orientation='h',
    hovertemplate="%{y}: %{x} <extra></extra>",
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

principles.update_layout(
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

df = pd.read_parquet('data/n-grams/Accountability_gram.parquet')

accountability_gram = px.bar(df, x='Top four-grams', y='Word Count',
               color='Word Count', color_continuous_scale='oryel')

accountability_gram.update_layout(
    template='plotly_dark',
    hoverlabel=dict(font_size=LARGE_FONT_SIZE),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=LARGE_FONT_SIZE,
    xaxis_title=None,
    yaxis_title=None
)

plot_data = collections.Counter(
    [item for sublist in [d['year_of_publication'] if isinstance(d['year_of_publication'], list) else [d['year_of_publication']] for d in data] for item in sublist]
)
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[0]))

timeline = go.Figure(data=go.Bar(x=tuple(plot_data.keys()), y=tuple(plot_data.values()),
                             text=tuple(plot_data.values()),
                             marker=dict(color=COLOR_GRAPHS_HEX), name=" ",
                             hoverlabel=dict(namelength=-1),
                             hovertemplate='<extra></extra>', showlegend=False))

timeline.update_traces(textposition='outside')

timeline.add_trace(go.Scatter(x=tuple(plot_data.keys()), y=tuple(plot_data.values()), mode='lines+markers',
                                name='',
                                line=dict(color='rgba(172, 50, 75, 0.5)'),
                                connectgaps=True,
                                hovertemplate='<extra></extra>', showlegend=False))

timeline.update_layout(
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

plot_data = collections.Counter(
    [item for sublist in [d['document_nature'] if isinstance(d['document_nature'], list) else [d['document_nature']] for d in data] for item in sublist]
)
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[1]))

nature = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in plot_data.keys()]),
    y=tuple(plot_data.values()),
    text=tuple(plot_data.values()),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

nature.update_layout(
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

plot_data = collections.Counter(
    [item for sublist in [d['document_regulation'] if isinstance(d['document_regulation'], list) else [d['document_regulation']] for d in data] for item in sublist]
)   
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[1]))

regulation = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in plot_data.keys()]),
    y=tuple(plot_data.values()),
    text=tuple(plot_data.values()),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

regulation.update_layout(
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

plot_data = collections.Counter(
    [item for sublist in [d['document_normative'] if isinstance(d['document_normative'], list) else [d['document_normative']] for d in data] for item in sublist]
)
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[1]))

normative = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in plot_data.keys()]),
    y=tuple(plot_data.values()),
    text=tuple(plot_data.values()),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

normative.update_layout(
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

plot_data = collections.Counter(
    [item for sublist in [d['document_impact'] if isinstance(d['document_impact'], list) else [d['document_impact']] for d in data] for item in sublist]
)
plot_data = dict(sorted(plot_data.items(), key=lambda item: item[1]))

impact = go.Figure(go.Bar(
    x=tuple(['<b>'+elem+'</b>' for elem in plot_data.keys()]),
    y=tuple(plot_data.values()),
    text=tuple(plot_data.values()),
    orientation='v',
    hovertemplate="%{x}: %{y} <extra></extra>",
    width=(0.5, 0.5, 0.5),
    marker=dict(
        color=COLOR_GRAPH_RGB,
        line=dict(
            color=COLOR_GRAPH_RGB,
            width=1))))

impact.update_layout(
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
