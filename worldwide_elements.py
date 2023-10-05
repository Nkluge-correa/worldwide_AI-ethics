import pickle
import pandas as pd
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

from graphs import fig, fig1, fig_a

STYLE_BUTTON = {'border': 0, 'font-weight': 'bold'}
CLOSE_BUTTON = 'primary'
DOWNLOAD_BUTTON = {'margin-right': '5px',
                   'margin-left': '5px',
                   'display': 'inline-block'}
FONT_SIZE = '1rem'
FONT_SIZE_HEADER = '1.5rem'
STYLE_BUTTON = {'border': 0, 'font-weight': 'bold'}
CLOSE_BUTTON = 'primary'
FONT_SIZE_HEADER = '1.5rem'

documents_dive = pd.read_parquet('data/documents_dive.parquet')

modal_article = html.Div(
    [
        html.A(['Article ', html.I(className='bi bi-file-text')],
               id="open-body-abstract", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '## Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance ⚖️', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown(
                        '''Since the last period of reduced interest in AI, the "AI winter" from 1987-1993, the field of AI research and industry has witnessed significant growth. This growth encompasses various aspects, including the development of new technologies, increased investment, greater media attention, and expanded capabilities of autonomous systems. A study analyzing the submission history on [ArXiv from 2009 to 2021](https://arxiv.org/about/reports/submission_category_by_year) reveals that computer science-related articles have become the most prevalent type of material submitted, increasing tenfold starting in 2018.''', className='modal-body-text-style'), html.Br(),
                    dcc.Graph(id='arxiv_sub', className='hidden-mobile', config={'displayModeBar': False},
                              figure=fig), html.Br(),
                    dcc.Markdown('''Furthermore, within the broad scope of Computer Science, the most frequently submitted sub-categories for publications are "_Computer Vision and Pattern Recognition_," "_Machine Learning_," and "_Computation and Language_", i.e., areas where Machine Learning (a sub-field of AI Research) has established itself as the reigning paradigm.''',
                                 className='modal-body-text-style'), html.Br(),
                    dcc.Graph(id='arxiv_CS', className='hidden-mobile', config={'displayModeBar': False},
                              figure=fig1), html.Br(),
                    dcc.Markdown(
                        '''Moreover, investment in AI-related companies and startups has reached unprecedented levels, with governments and venture capital firms investing over 90 billion (USD) in the United States alone in 2021, accompanied by a surge in the registration of AI-related patents (Zhang et al. [2022](https://aiindex.stanford.edu/report/)). While these money-field advancements have brought numerous benefits, they also introduce risks and side effects that promoted several ethical concerns, like risks to user privacy, the potential for increased surveillance, the environmental cost of the industry, and the amplification of prejudices and discrimination on a large scale, which can disproportionately harm vulnerable groups. Consequently, the expansion of the AI industry has given rise to what we refer to as the "_AI ethics boom_," i.e., a period marked by an unprecedented demand for regulation and normative guidance in this field.''', className='modal-body-text-style'), html.Br(),
                    dcc.Markdown(
                        '''One of the central questions surrounding this boom is the determination of what ethical premises should guide the development of AI technologies. And to answer this question, a plethora of principles and guidelines have been proposed by many stakeholders. However, the consensus and divergences in these varied discourses have yet to be extensively accessed. For instance, do Silicon Valley-based companies follow the same precautions as major Chinese technology firms? Are these concerns relevant to end-users in countries with diverse cultural and social norms? Establishing a consensus to support the global regulations currently under discussion is of paramount importance in both a practical and theoretical sense.''', className='modal-body-text-style'), html.Br(),
                    dcc.Markdown(
                        '''To address these questions, we draw inspiration from previous works by meta-analysts and meticulously survey a wide array of available ethical guidelines related to AI development. These sources include governance policies of private companies, academic institutions, and governmental and non-governmental organizations, as well as ethical guidelines for AI usage. By analyzing 200 documents in five different languages, we gathered information on what ethical principles are the most popular, how they are described, where they come from, their intrinsic characteristics, and much else. Our primary goal was to identify the most advocated ethical principles, examine their global distribution, and assess if there is a consistent understanding of these principles. Ultimately, this analysis aims to determine whether a consensus exists regarding the normative discourse presented in ethical guidelines surrounding AI development.''', className='modal-body-text-style'), html.Br(),
                    dcc.Markdown('## Limitations ⚠️', className='title-style'), html.Br(),
                    dcc.Markdown(
                        '''As in past works, this analysis also suffers from a small sample. Our work represents a mere fraction of what our true global landscape on this matter is. Some of the main limitations we encountered during our work are:''', className='modal-body-text-style'), html.Br(),
                    dcc.Markdown(
                        '''
                        - The limited scope of languages we could interpret represents a language bias, potentially excluding relevant perspectives.
                        - Publication bias is also a concern, as the focus on published guidelines may overlook valuable insights from ongoing discussions in other forms of media.
                        - The "guideline" scope excludes the academic work done worldwide (i.e., we did not consider academic papers on AI Ethics).
                        - The study's time window limits our understanding of past dynamics and trends in AI ethics that predate our window of analysis.
                        - Methodological limitations, such as data collection techniques and analysis frameworks, can influence the results and interpretations.
                        - The study may lack contextual information, failing to address the deeper social, cultural, and political aspects surrounding AI ethics.
                        - While name-based analyses are generally considered sound practices, gender prediction methods still exhibit an error rate that we were unable to address. These are also limited in capturing non-binary gender accounts and fail to cover cases of self-declaration (e.g., genderfluid, queer, or transgender).
                        ''', className='modal-body-text-style'), html.Br(),                    
                    dcc.Markdown(
                        '## Explore the Worldwide Dataset 🔬', className='title-style'), html.Br(),
                    dcc.Dropdown(id='documents',
                                 options=tuple(documents_dive.index),
                                 value=documents_dive.index[0], clearable=False,
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
                    dcc.Markdown('## Cite as 🤗', className='title-style'), html.Br(),
                    dcc.Clipboard(target_id="cite_worldwide",
                                  style={"fontSize": 20}),
                    dcc.Markdown('''

                    ````markdown

                    @article{correa2022worldwide,
                        title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
                        author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund and Oliveira, Nythamar},
                        journal={arXiv preprint arXiv:2206.11922},
                        year={2022}
                    }
                    ````
                    ''', id="cite_worldwide", className='modal-body-text-style'), html.Br(),
                    html.Div([
                        html.H4([
                            dbc.Badge([html.I(className="bi bi-heart-fill"), "  Open-Source"], href="https://github.com/Nkluge-correa/worldwide_AI-ethics",
                                      color="dark", className="text-decoration-none", style={'margin-right': '5px'}),
                            dbc.Badge([html.I(className="bi bi-bar-chart-fill"), "  Power BI Version"], href="https://nkluge-correa.github.io/worldwide_AI-ethics/",
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
    ],
)

df = pd.read_parquet('data/titles_abstracts.parquet')

df = pd.DataFrame({
    'Documents': tuple([f'[{df.document_title[i]}]({df.document_url[i]})' for i in range(len(df.document_title))]),
    'Abstract': tuple(df.abstract)
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
    style_table={'height': '2550px', 'overflow-y': 'scroll'},
    page_current=0,
    page_size=200,
    style_cell={
        'text-align': 'justify', 'text-justify': 'inter-word',
        'font-size': FONT_SIZE, 'padding': '10px',
        'background-color': '#272b30'
    },
    style_data={
        'white-space': 'normal',
        'height': 'auto',
        'border': '1px solid #696b6f'
    },
    style_header={
        'background-color': '#272b30',
        'font-weight': 'bold',
        'text-align': 'center',
        'font-size': FONT_SIZE_HEADER,
        'border': 'none'
    },
    style_as_list_view=True,
)

modal_map = html.Div(
    [
        html.A([html.I(className='bi bi-info-circle')],
               id="open-body-map", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Publications by Country 🏳️‍🌈', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''Looking at the distribution among world regions (aggregated by continent), we see that the bulk of produced documents come from Europe (especially countries from Western Europe, 63 = 31.5%, like the United Kingdom, 24 = 12%, and Germany, 20 = 10%), North America (United States of America, 58 = 29%, and Canada, 11 = 5.5%), that together represent a third of our sample size, and Asia (mostly represented by East Asian countries, 23 = 11.5%, like China, 11 = 5.5%, and Japan, 8 = 4%), while South America, Africa, and Oceania represent less than 4.5% of our sample, with countries like Brazil (3 = 1.5%) spearheading this portion of our distribution (Latin America, 7 = 3.5%). If it was not for the significant participation of Intergovernmental Organizations, like NATO, UN, and UNESCO, which represent 6% of our sample size (13 documents), other world regions/countries would be even more underrepresented. However, this still excludes States like the Holy See/Vatican City and Palestine.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''When we examine our sample through a "country" level of granularity, we see that the bulk (13 countries = 77%) of our total sample size is represented by the United States of America, the United Kingdom, (England, Scotland, Wales, and Northern Ireland has been considered as a country unit, even though technically this is not the case) Germany, Canada, China, Japan, France, Finland, Netherlands, Switzerland, Belgium, Brazil, and South Korea, while a myriad of 24 countries (12.5%) represents the remainder of our sample, along with Intergovernmental organizations, like the EU (9 = 4.5%) and the UN (6 = 3%).''',
                                 className='modal-body-text-style')
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
    ], className='info-graph-buttons'
)

modal_institution = html.Div(
    [
        html.A([html.I(className='bi bi-info-circle')],
               id="open-body-institution", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Publications by Institutions 🏢', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''Switching our gaze to institution types, except for institutions like IBM (5), Microsoft (4), and UNESCO (3), most other institutions do not have more than two published documents. We can also see that the bulk of our sample was produced by governmental institutions and private corporations (48), followed by CSO/NGO (17), non-profit organizations (16), and academic institutions (12.5). However, this trend only follows if we look at the totality of our sample size. If we look at documents produced by continents, for example, in North America (69), private corporations (24 = 34.7) and non-profit organizations (18 = 26) produced most documents, followed by governmental institutions (12 = 17.4). Meanwhile, when we look at Europe, the global trend is restored.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''An in-depth analysis segmented by countries shows that the engagement of particular AI stakeholders (i.e., institution types) differs between countries. For example, in China (11), the majority of documents are produced by academic institutions (5 = 45,4), while in Germany (20), most samples came from private corporations (6 = 30) and CSO/NGO (4 = 20). Also, the only document produced by a religious institution in our sample is the "_[Rome Call for AI Ethics](https://www.romecall.org/)_," produced by the Pontifical Academy for Life (Vatican City).''',
                                 className='modal-body-text-style'),
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
    ], className='info-graph-buttons'
)

modal_gender = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-gender", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Authors by Gender ♂ ☿ ♀ ', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''To infer the gender of the authors responsible for the documents in our sample, we performed an analysis based on the names of each author. Given the variety/diversity that names can possess, it was necessary to use automation.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''To make an accurate inference, it was also necessary to extract (in addition to each author's name) the most likely nationality associated with each name. For this, we used (in addition to the country/origin of each document) [nationalize.io](https://nationalize.io/), an API service that predicts the nationality of a person given their name. After that, we grouped the names of authors who had the same origin/nationality associated with their names.''', className='modal-body-text-style'),
                    dcc.Markdown('''Finally, we used the API services of the [genderize.io](https://genderize.io/) platform to infer the gender of each name. Each request was made by providing the name to be inferred and the ISO-2 code of the nationality associated with that name. In the end, 830 names were extracted from the 200 documents analyzed. From those names, 558 unique names were found, each associated with one of 36 different nationalities.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''The final count shows that 66% of the sample (132 documents) do not identify the authors. The distribution of authors with "_male_" names was favorable for the remainder of our dataset (549 = 66%). 34% (281) of these names were inferred as "_female_."''',
                                 className='modal-body-text-style')
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
    ], className='info-graph-buttons'
)

with open('data/principles_definition_dict.pickle', 'rb') as fp:
    principles_definition_dict = pickle.load(fp)
    fp.close()

with open('data/principles_dict.pickle', 'rb') as fp:
    principles_dict = pickle.load(fp)
    fp.close()

modal_principles = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-principle", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Citations by Principle 🔍', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''The top five principles advocated in the documents of our sample are similar to the results shown by Jobin et al. ([2019](https://www.nature.com/articles/s42256-019-0088-2)) and Hagendorff ([2020](https://link.springer.com/article/10.1007/s11023-020-09517-8)), with the addition of Reliability/Safety/Security/Trustworthiness (78%), which was also cited as top five in Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)) meta analysis (80%).''', className='modal-body-text-style'),
                    dcc.Markdown('''Looking at principle distribution filtered by continent, the top five principles remain the same in both North America and Europe, but the Asian continent introduces the principle of Beneficence/Non-Maleficence as is 5th (74%) most cited principle, putting Accountability/Liability in the 6th place (70%). Filtering our results by country, we see no change in the top five principles when comparing EUA and the UK. However, looking under the top five principles, we begin to see differences, like Freedom/Autonomy/Democratic Values/Technological Sovereignty (38%) and Beneficence/Non-Maleficence (34.4%) being the 6th and 7th most cited principles in the EUA, and Cooperation/Fair Competition/Open source (45.8%) and Diversity/Inclusion/Pluralism/Accessibility (41.6%) being 6th and 7th most cited principles in the UK.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''When examining principle distribution filtered by institution type, we also can find many insights. For example, looking at our total sample, we notice that the main preoccupation of governmental institutions (worldwide) is the need for transparent systems (89.5%), private corporations mainly advocate for Reliability ($87.5%), and CSO/NGOs primarily defend the principle of fairness (88.2%).''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''To create an "_overall definition_" of each principle/group of principles, we utilize a [text mining](https://en.wikipedia.org/wiki/Text_mining) technique called [n-gram analysis](https://en.wikipedia.org/wiki/N-gram), were we counted the successive repetition of words (and groups of words) in every principle found in the documents of our sample. Thus, the bellow definitions were created to contemplate the recurring themes we encountered. Below we also present count charts for four-grams of each principle.''', className='modal-body-text-style'), html.Br(),
                    dcc.Markdown(
                        '''## Explore the Worldwide Principles 🔬''', className='title-style'), html.Br(),
                    dcc.Dropdown(id='principle',
                                 options=tuple(principles_dict.keys()),
                                 value=tuple(principles_dict.keys())[
                                     0], clearable=False,
                                 style={'margin-top': '10px'}
                                 ), html.Br(),
                    dcc.Loading(type='circle', color='#dc3d87', children=[
                        dcc.Markdown(''' ''', className='modal-body-text-style', id='four-gram-definiton'),
                        dcc.Graph(id='four-gram-graph', className='hidden-mobile', config={'displayModeBar': False},
                                  figure=fig_a)]), html.Br(),
                    dcc.Markdown(
                        '## Divergence in Definitions 🤔', className='title-style'), html.Br(),
                    dcc.Markdown('''Another point we would like to bring attention to, as done by Jobin et al. ([2019](https://www.nature.com/articles/s42256-019-0088-2)) and Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)), is the divergence concerning how these principles are defined. Our tools bring all definitions given by each document to the mentioned principles, which allows for a more diverse comparison of how these abstract objects are presented. Here, we bring some cases that most sparked curiosity, reminding us that this analysis is partial to our subjective interpretation of how the discourse surrounding these principles varies. The reader may well find other more intriguing discrepancies by searching our tool.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''For example, when examining Transparency/Explainability/Auditability, the definition proposed in "_[ARCC: An Ethical Framework for Artificial Intelligence](https://www.tisi.org/13747)_":''', className='modal-body-text-style'),
                    dcc.Markdown('''- "_Promote algorithmic transparency and algorithmic audit, to achieve understandable and explainable AI systems. Explain the decisions assisted/made by AI systems when appropriate. Ensure individuals' right to know, and provide users with sufficient information concerning the AI system's purpose, function, limitation, and impact._"''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''In comparison with the one provided in "_[A practical guide to Responsible Artificial Intelligence (AI)](https://www.pwc.com/gx/en/issues/data-and-analytics/artificial-intelligence/what-is-responsible-ai/responsible-ai-practical-guide.pdf)_":''', className='modal-body-text-style'),
                    dcc.Markdown('''- "_To instill trust in AI systems, people must be enabled to look under the hood at their underlying models, explore the data used to train them, expose the reasoning behind each decision, and provide coherent explanations to all stakeholders promptly. These explanations should be tailored to the different stakeholders, including regulators, data scientists, business sponsors, and end consumers_."''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''If we take a look at Human-Centeredness/Alignment, in "_Data, Responsibly (Vol. 1) Mirror, Mirror_," (Khan & Stoyanovich, [2020](https://dataresponsibly.github.io/comics/)), we find the following recommendation:''', className='modal-body-text-style'),
                    dcc.Markdown('''- "_Maybe what we need instead is to ground the design of AI systems in people. Using the data of the people, collected and deployed with an equitable methodology as determined by the people, to create technology that is beneficial for the people._"''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''While in "_[Everyday Ethics for Artificial Intelligence](https://www.ibm.com/watson/assets/duo/pdf/everydayethics.pdf)_",the following norm is suggested:''', className='modal-body-text-style'),
                    dcc.Markdown('''- "_AI should be designed to align with the norms and values of your user group in mind_."''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''Many other differences can be found in our sample, for example:''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''- "_[Tieto's AI ethics guidelines](https://www.tietoevry.com/en/newsroom/all-news-and-releases/press-releases/2018/10/tieto-strengthens-commitment-to-ethical-use-of-ai/)_" takes a different take on explainability, saying its systems "_can be explained and explain itself_", potting some of the responsibility of explainability in the AI system itself, making it a "_stakeholder_" in the accountability chain.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''- "_[The Toronto Declaration](https://www.torontodeclaration.org/declaration-text/english/)_" gives an extensive and nonexhaustive definition of what "_discrimination_" means under international laws, while most other documents resume themselves in only citing the concept, leaving open to interpretation the types of "_discrimination that is permissible_".''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''- In "_[Artificial Intelligence and Machine Learning: Policy Paper](https://www.internetsociety.org/resources/doc/2017/artificial-intelligence-and-machine-learning-policy-paper/)_", fairness is related to the idea of "_AI provides socio-economic opportunities for all_" (benefits), in "_[Trustworthy AI in Aotearoa: AI Principles](https://aiforum.org.nz/wp-content/uploads/2020/03/Trustworthy-AI-in-Aotearoa-March-2020.pdf)_" fairness is also defined as "_AI systems do not unjustly harm_" (impacts), which we can relate to the difference between certain notions of algorithmic fairness (predictive parity vs equalized odds).''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''- While some documents (e.g., "_[Telefónica's Approach to the Responsible Use of AI](https://www.telefonica.com/en/wp-content/uploads/sites/5/2021/08/ia-responsible-governance.pdf)_") state how privacy and security are essential for AI systems developments, only some (e.g., "_[Big Data, Artificial Intelligence, Machine Learning, and Data Protection](https://ico.org.uk/media/for-organisations/documents/2013559/big-data-ai-ml-and-data-protection.pdf)_") specify what "_good privacy criteria_" are (e.g., data minimization).''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''- While most documents interpret accountability/liability as "_developers being responsible for their projects_" (e.g., "_[Declaration of Ethical Principles for AI in Latin America](https://ia-latam.com/etica-ia-latam/)_"), some documents also put this responsibility on users, and even algorithms "_themselves_" (e.g., "_[The Ethics of Code: Developing AI for Business with Five Core Principles](https://www.sage.com/~/media/group/files/business-builders/business-builders-ethics-of-code.pdf?la=en)_").''', className='modal-body-text-style'),
                    dcc.Markdown(
                        '''Besides the ones mentioned above, many other forms of comparisons can be made using our dataset (available for download at the bottom of this page).''', className='modal-body-text-style'),
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
    ],
    style={'display': 'inline-block'},
)

modal_years = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-years", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Publications Timeline 📅', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown(
                        '''Concerning the year of publication of the documents from our sample, one can see that the majority (129 = 64.5%) was published between 2017 and 2019. What we call the "_AI ethics boom_" constitutes the significant production of documents in the year 2018, which represents 30.5% (61) of our entire sample.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown(
                        '''The fact that almost a third of our sample (30.5%) got published in 2018 (64.5% if extended from 2017 to 2019) is worth contextualizing. The AI Index report also points to this trend, where since 2014, we had a five-time increase in publications related to AI Ethics, where topics like algorithmic fairness have stopped being only academic objects of research and actual AI industry areas of R&D. ''', className='modal-body-text-style'),
                    dcc.Markdown(
                        '''It is also interesting to see the shift of interest during the timeline we analyzed. In 2014, the top-cited principles were Fairness, Reliability, and Dignity (Transparency was not even in the top 10 at this time), and in 2016, Accountability, Beneficence, and Privacy received more attention (Accountability being the number one concern of documents published in 2017). But in 2018, Transparency (Explainable AI/XAI, Mechanistic Interpretability) became the dominant topic of concern.''', className='modal-body-text-style')
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
    ],
)

modal_nature = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-nature", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Nature/Content 📝', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the nature/content of the document, and three categories were defined (these categories were _defined as mutually inclusive_):''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Descriptive 
                    
                    - "_Descriptive documents take the effort of presenting definitions related to AI technologies. These definitions serve to contextualize "what we mean" when we talk about AI._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Normative 
                    
                    - "_Normative documents present norms, ethical principles, recommendations, and imperative affirmations about what such technologies should be used/developed for._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Practical 
                    
                    - "_Practical documents present development tools to implement ethical principles and norms._"''', className='modal-body-text-style'),
                    dcc.Markdown('''Regarding the previously defined typological categories, when looking at the document's Nature/Content, we found that the majority of our sample is from the normative type (96%), which a third of the time also presents descriptive contents (55.5%), and more rarely, practical implementations (2%).''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''It is a curious phenomenon that only a little more than half of the documents define their subject of interest. More so if we acknowledge that there is no consensual definition of what "_Artificial Intelligence_" is and what is not. There are many interpretations and contesting definitions, which may prove to be a challenge for regulating organizations. For example, if you choose to define AI as only "_systems that can learn_," you will leave outside your scope of regulation an entire family of systems that do not learn (rule-based systems) but can still act "intelligently" and autonomously.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''Meanwhile, as already stated by Fjeld et al. ([2020](https://dash.harvard.edu/handle/1/42160420)) work, there is a gap between established principles and their actual application. In our sample, most of the documents only prescribe normative claims without the means to achieve them, while the effectiveness of more practical methodologies, in the majority of cases, remains extra empirical. With this, we see a field with a significant lack of practical implementations ([check our tutorails](https://github.com/Nkluge-correa/teeny-tiny_castle)) that could support its normative claims.''',
                                 className='modal-body-text-style'),
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
    ],
)

modal_regulation = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-regulation", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Form of Regulation 📏', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the form of regulation that the document proposes. For this, three categories were defined (these categories were _defined as mutually exclusive_):''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Government-Regulation
                     
                    - "_We designed this category to encompass documents made by governmental institutions. These documents propose that States should regulate the use and development of AI strictly (Legally binding horizontal regulations) or softly (Legally non-binding guidelines)._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Self-Regulation/Voluntary Self-Commitment 
                    
                    - "_We designed this category to encompass documents made by private organizations and other bodies. These documents defend a form of Self-Regulation governed by the AI industry itself. It also encompasses voluntary self-commitment made by independent organizations._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Recommendation 
                    
                    - "_We designed this category to encompass documents that only suggest possible forms of governance and ethical principles that should guide organizations seeking to use, develop, or regulate AI technologies._"''', className='modal-body-text-style'),
                    dcc.Markdown('''When we look at the form of regulation proposed by the documents of our sample, more than half (56%) are only recommendations to different AI stakeholders, while 24% possess self-regulatory/voluntary self-commitment style guidelines and only 20% propose a form of regulation administered by a given state/country.''',
                                 className='modal-body-text-style'),
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
    ],
)

modal_normative = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-normative", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Normative Strength ⚡', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the normative strength of the regulation mechanism proposed by the document. For this, two categories were defined (these categories were _not defined as mutually exclusive_):''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Legally non-binding guidelines 
                    
                    - "_These documents propose an approach that intertwines AI principles with recommended practices for companies and other entities._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Legally binding horizontal regulations
                    
                    - "_These documents propose an approach that focuses on regulating specific uses of AI through legally binding regulations, such as mandatory requirements and prohibitions._"''', className='modal-body-text-style'),
                    dcc.Markdown('''When we look at the form of regulation proposed by the documents of our sample, more than half (56%) are only recommendations to different AI stakeholders, while 24% possess self-regulatory/voluntary self-commitment style guidelines and only 20% propose a form of regulation administered by a given state/country.''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''This lack of convergence to a more "government-based" form of regulation reflects in the normative strength of these documents, where the vast majority (98%) only serve as "soft laws," i.e., guidelines that do not entail any form of a legal obligation, while only 4.5% propose stricter regulation. Since only governmental institutions can create legally binding norms (other institutions lack this power), and they produced only 24% of our sample, some may argue that this imbalance lies in this fact. However, by filtering only the documents produced by governmental institutions, the disproportion does not go away, with only 18.7% of samples proposing legally binding forms of regulation. The countries on the front of this still weak trend are Canada, Germany, and the United Kingdom, with Australia, Norway, and the USA coming right behind. ''',
                                 className='modal-body-text-style')
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
    ],
)

modal_impact = html.Div(
    [
        html.A([html.I(className="bi bi-info-circle")],
               id="open-body-impact", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Impact Scope 💥', className='title-style'))),
                dbc.ModalBody([
                    dcc.Markdown('''This type relates to the impact scope that motivates the document. With impact scope, we mean the related risks and benefits regarding the use of AI that motivate the type of regulation suggested by the document. For this, three categories were defined (these categories were _defined as mutually exclusive_):''',
                                 className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Short-Termism 
                    
                    - "_We designed this category to encompass documents in which the scope of impact and preoccupation focus mainly on current/short-term problems, like algorithmic discrimination, algorithmic opacity, privacy, legal accountability, etc._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Long-Termism 
                    
                    - "_We designed this category to encompass documents in which the scope of impact and preoccupation focus mainly on future/long-term problems, like problems we may face with future AI systems. Since such technologies are not yet a reality, we can classify these risks as hypothetical or, at best, uncertain._"''', className='modal-body-text-style'),
                    dcc.Markdown('''
                    ### Short-Termism & Long-Termism 
                    
                    - "_We designed this category to encompass documents in which the scope of impact is short and long-term, i.e., they present a "mid-term" scope of preoccupation. These documents address issues related to the Short-Termism category while also pointing out the mid/long-term impacts of our current AI adoption (e.g., AI interfering in democratic processes, autonomous weapons, existential risks, environmental sustainability, labor displacement, and the need for updating our educational systems)._"''', className='modal-body-text-style'),
                    dcc.Markdown('''Looking at the totality of our sample size, we see that short-term (47%) and "_mid-term_" (i.e., short-term & long-term = 52%) prevail over more long-term preoccupations (2%). When we filter our sample by impact scope and institution type, it seems to us that private corporations think more about the short-term (33%), governmental institutions about the short/long-term (28%), and academic (66%) and non-profit organizations (33%) with the long-term impacts of AI technologies.''',
                                 className='modal-body-text-style')
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
    ],
)


df = pd.read_parquet('data/principle_definition.parquet')

accordion = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.accountability.dropna(axis=0)]),
                    title="Accountability 👩🏾‍⚖️",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.beneficence.dropna(axis=0)]),
                    title="Beneficence ⚕️",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.children_rights.dropna(axis=0)]),
                    title="Children's Rights 👶",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.dignity.dropna(axis=0)]),
                    title="Human Rights ✊🏿",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.diversity.dropna(axis=0)]),
                    title="Diversity 🌈",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.autonomy.dropna(axis=0)]),
                    title="Autonomy 🕊️",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.human_formation.dropna(axis=0)]),
                    title="Human Formation 📚",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.human_centeredness.dropna(axis=0)]),
                    title="Human-Centeredness 👨‍👨‍👦‍👦",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.intellectual_property.dropna(axis=0)]),
                    title="Intellectual Property 🧠",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.fairness.dropna(axis=0)]),
                    title="Fairness ⚖️",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.labor_rights.dropna(axis=0)]),
                    title="Labor Rights 👷",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.cooperation.dropna(axis=0)]),
                    title="Cooperation 🤝",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.privacy.dropna(axis=0)]),
                    title="Privacy 🔒",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.reliability.dropna(axis=0)]),
                    title="Reliability 💪",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.sustainability.dropna(axis=0)]),
                    title="Sustainability ♻️",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.transparency.dropna(axis=0)]),
                    title="Transparency 🕵",
                ),
                dbc.AccordionItem(
                    tuple([dcc.Markdown(f"{x}", className='modal-body-text-style')
                           for x in df.truthfulness.dropna(axis=0)]),
                    title="Truthfulness 🤥",
                ),
            ],
            id="accordion",
            start_collapsed=True,
        ),
    ]
)

offcanvas_principles = html.Div(
    [
        html.A([html.I(className="bi bi-search-heart")],
               id="open-body-all-principles", n_clicks=0, className="icon-button", style={'font-size': 20}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown(
                    '# Ethical Principles ✊🏿', className='title-style'))),
                dbc.ModalBody([accordion]),
                dbc.ModalFooter(
                    dbc.Button(
                        html.I(className="bi bi-x-circle-fill"),
                        id='close-body-all-principles',
                        className='ms-auto',
                        outline=True,
                        size='xl',
                        n_clicks=0,
                        color=CLOSE_BUTTON,
                        style=STYLE_BUTTON
                    )
                ),
            ],
            id='body-all-principles',
            fullscreen=True,
        ),
    ], style={'display': 'inline-block', 'margin-left': '10px'}
)

download_data = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  Data'], id='btn_data',
               outline=True, color='light', style={'font-weight': 'bold'}),
    dcc.Download(id="download-data")
], style=DOWNLOAD_BUTTON)

download_html = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  HTML'], id='btn_html',
               outline=True, color='light', style={'font-weight': 'bold'}),
    dcc.Download(id="download-html")
], style=DOWNLOAD_BUTTON)

download_png = html.Div([
    dbc.Button([html.I(className="bi bi-download"), '  PNG'], id='btn_png',
               outline=True, color='light', style={'font-weight': 'bold'}),
    dcc.Download(id="download-png")
], style=DOWNLOAD_BUTTON)
