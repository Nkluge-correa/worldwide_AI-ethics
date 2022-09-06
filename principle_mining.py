
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

accountability = []
beneficence = []
children = []
dignity = []
diversity = []
freedom = []
education = []
alignment = []
intellectual = []
justice = []
labor = []
openess = []
privacy = []
reliability = []
sustainability = []
transparency = []
truth = []

columns_names = [

    'Accountability/Liability',
    'Beneficence/Non-Maleficence',
    'Children & Adolescents Rights',
    'Dignity/Human Rights',
    'Diversity/Inclusion/Pluralism/Accessibility',
    'Freedom/Autonomy/Democratic Values/Technological Sovereignty',
    'Human Formation/Education',
    'Human-Centeredness/Alignment',
    'Intellectual Property',
    'Justice/Equity/Fairness/Non-discrimination',
    'Labor Rights',
    'Open source/Fair Competition/Cooperation',
    'Privacy',
    'Reliability/Safety/Security/Trustworthiness',
    'Sustainability',
    'Transparency/Explainability/Auditability',
    'Truthfulness'
]

df = pd.read_excel('meta_en.xlsx', 'meta_names')

names = []
for i in range(len(df['Document Title'])):
    x = df['Document Title'][i]
    y = df['Document URL'][i]
    text = f'[{x}]({y})'
    names.append(text)

dff = pd.DataFrame(columns=columns_names, index=names)

df3 = pd.read_excel('meta_en.xlsx', 'meta_principles_definitions')

for i in range(len(df3['Principles Definition'])):

    text = df3['Principles Definition'][i]
    words = text.split('#')
    for word in words:

        if "Accountability/Liability:" in word:
            word = word.replace("Accountability/Liability:", "")
            accountability.append(word)
            dff['Accountability/Liability'][i] = word
        elif "Beneficence/Non-Maleficence:" in word:
            word = word.replace("Beneficence/Non-Maleficence:", "")
            beneficence.append(word)
            dff['Beneficence/Non-Maleficence'][i] = word
        elif "Children & Adolescents Rights:" in word:
            word = word.replace("Children & Adolescents Rights:", "")
            children.append(word)
            dff['Children & Adolescents Rights'][i] = word
        elif "Dignity/Human Rights:" in word:
            word = word.replace("Dignity/Human Rights:", "")
            dignity.append(word)
            dff['Children & Adolescents Rights'][i] = word
        elif "Diversity/Inclusion/Pluralism/Accessibility:" in word:
            word = word.replace(
                "Diversity/Inclusion/Pluralism/Accessibility:", "")
            diversity.append(word)
            dff['Diversity/Inclusion/Pluralism/Accessibility'][i] = word
        elif "Freedom/Autonomy/Democratic Values/Technological Sovereignty:" in word:
            word = word.replace(
                "Freedom/Autonomy/Democratic Values/Technological Sovereignty:", "")
            freedom.append(word)
            dff['Freedom/Autonomy/Democratic Values/Technological Sovereignty'][i] = word
        elif "Human Formation/Education:" in word:
            word = word.replace("Human Formation/Education:", "")
            education.append(word)
            dff['Human Formation/Education'][i] = word
        elif "Human-Centeredness/Alignment:" in word:
            word = word.replace("Human-Centeredness/Alignment:", "")
            alignment.append(word)
            dff['Human-Centeredness/Alignment'][i] = word
        elif "Intellectual Property:" in word:
            word = word.replace("Intellectual Property:", "")
            intellectual.append(word)
            dff['Intellectual Property'][i] = word
        elif "Justice/Equity/Fairness/Non-discrimination:" in word:
            word = word.replace(
                "Justice/Equity/Fairness/Non-discrimination:", "")
            justice.append(word)
            dff['Justice/Equity/Fairness/Non-discrimination'][i] = word
        elif "Labor Rights:" in word:
            word = word.replace("Labor Rights:", "")
            labor.append(word)
            dff['Labor Rights'][i] = word
        elif "Open source/Fair Competition/Cooperation:" in word:
            word = word.replace(
                "Open source/Fair Competition/Cooperation:", "")
            openess.append(word)
            dff['Open source/Fair Competition/Cooperation'][i] = word
        elif "Privacy:" in word:
            word = word.replace("Privacy:", "")
            privacy.append(word)
            dff['Privacy'][i] = word
        elif "Reliability/Safety/Security/Trustworthiness:" in word:
            word = word.replace(
                "Reliability/Safety/Security/Trustworthiness:", "")
            reliability.append(word)
            dff['Reliability/Safety/Security/Trustworthiness'][i] = word
        elif "Sustainability:" in word:
            word = word.replace("Sustainability:", "")
            sustainability.append(word)
            dff['Sustainability'][i] = word
        elif "Transparency/Explainability/Auditability:" in word:
            word = word.replace(
                "Transparency/Explainability/Auditability:", "")
            transparency.append(word)
            dff['Transparency/Explainability/Auditability'][i] = word
        elif "Truthfulness:" in word:
            word = word.replace("Truthfulness:", "")
            truth.append(word)
            dff['Truthfulness'][i] = word

dff = dff.fillna('Principle not cited.')
dff = dff.reset_index()
dff = dff.rename({'index': 'Document Title'}, axis=1)
dff.set_index('Document Title', inplace=True)
# dff.to_excel('temp.xlsx')

principles = []
principles.append(accountability)
principles.append(beneficence)
principles.append(children)
principles.append(dignity)
principles.append(diversity)
principles.append(freedom)
principles.append(education)
principles.append(alignment)
principles.append(intellectual)
principles.append(justice)
principles.append(labor)
principles.append(openess)
principles.append(privacy)
principles.append(reliability)
principles.append(sustainability)
principles.append(transparency)
principles.append(truth)


def get_top_n_words(corpus, n=None):
    vec = CountVectorizer(stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


def get_top_n_bigrams(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


def get_top_n_trigrams(corpus, n=None):
    vec = CountVectorizer(ngram_range=(3, 3), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


columns_namess = [

    'Accountability',
    'Beneficence',
    'Children & Adolescents Rights',
    'Dignity',
    'Diversity',
    'Freedom',
    'Human Formation',
    'Human Centeredness',
    'Intellectual Property',
    'Justice',
    'Labor Rights',
    'Open source',
    'Privacy',
    'Reliability',
    'Sustainability',
    'Transparency',
    'Truthfulness'
]

for i in range(len(principles)):
    # ----------------------------------------------------------------------------------------#

    common_words = get_top_n_words(principles[i], 20)

    df = pd.DataFrame(common_words, columns=['principles_words', 'count'])

    fig = px.bar(df, x='principles_words', y='count',
                 title=f'Top-20 Words (unigrams) in principle: {columns_names[i]}',
                 color='count', color_continuous_scale='reds')
    fig.update_layout(template='plotly_white'
                      )
    fig.show()
    py.plot(
        fig, filename=f'Top-20 Words (unigrams) in principle - {columns_namess[i]}.html', auto_open=False)

# ----------------------------------------------------------------------------------------#

    common_bigrams = get_top_n_bigrams(principles[i], 20)

    df = pd.DataFrame(common_bigrams, columns=['principles_words', 'count'])

    fig = px.bar(df, x='principles_words', y='count',
                 title=f'Top-20 Words (bigrams) in principle: {columns_names[i]}',
                 color='count', color_continuous_scale='reds')
    fig.update_layout(template='plotly_white'
                      )
    fig.show()
    py.plot(
        fig, filename=f'Top-20 Words (bigrams) in principle - {columns_namess[i]}.html', auto_open=False)

# ----------------------------------------------------------------------------------------#

    common_trigrams = get_top_n_trigrams(principles[i], 20)

    df = pd.DataFrame(common_trigrams, columns=['principles_words', 'count'])

    fig = px.bar(df, x='principles_words', y='count',
                 title=f'Top-20 Words (trigrams) in principle: {columns_names[i]}',
                 color='count', color_continuous_scale='reds')
    fig.update_layout(template='plotly_white'
                      )
    fig.show()
    py.plot(
        fig, filename=f'Top-20 Words (trigrams) in principle - {columns_namess[i]}.html', auto_open=False)
