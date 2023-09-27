# Worldwide AI Ethics: a review of _200_ guidelines and recommendations for AI governance 🌐

[![DOI](https://zenodo.org/badge/533441174.svg)](https://zenodo.org/badge/latestdoi/533441174)

The utilization of artificial intelligence (AI) applications has experienced tremendous growth in recent years, bringing forth numerous benefits and conveniences. However, this expansion has also provoked ethical concerns, such as privacy breaches, algorithmic discrimination, security and reliability issues, transparency, and other unintended consequences. To determine whether a global consensus exists regarding the ethical principles that should govern AI applications and to contribute to the formation of future regulations, this paper conducts a meta-analysis of 200 governance policies and ethical guidelines for AI usage published by public bodies, academic institutions, private companies, and civil society organizations worldwide. **We identified at least 17 resonating principles prevalent in the policies and guidelines of our dataset, released as an open-source database and tool**. We present the limitations of performing a global scale analysis study paired with a critical analysis of our findings, presenting areas of consensus that should be incorporated into future regulatory efforts.

_[Full article here.](https://arxiv.org/abs/2206.11922)_

## Dash Template 🐱‍💻

<img src="assets/globe.gif" width=300 >

Here you can find the source code used to create our _Worldwide AI Ethics_ dashboard. This panel was created using the [Dash](https://dash.plotly.com/dash-enterprise) library. All the tables that feed our dashboard (`data_en.rar`), images (`png_files.rar`), and HTML-Plotly graphs (`html_files.rar`) are available in the `data` folder (in `csv` and `parquet`). Auxiliary notebooks for creating the graphs (`make_graphs.ipynb`) and processing the text data(`principle_mining.ipynb`) are also available. We also make available the notebook we used to infer the gender of all authors in our sample (`gender_infer.ipynb`), and the notebook to create the `geojson` file that sets the boundaries of the polygons on the `Mapbox`. To render the dash app in your browser, simply run the `worldwide.py` script.

You can also find a Power BI version of our dashboard in [this link]().

## Requirements 🛠️

```bash

dash
pandas
urllib3
unidecode
scikit-learn
dash-bootstrap-components

```

## Cite as 🤗

```latex
@article{correa2022worldwide,
  title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
  author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund and Oliveira, Nythamar},
  journal={arXiv preprint arXiv:2206.11922},
  year={2022}
}
```
