# Worldwide AI Ethics: a review of _200_ guidelines and recommendations for AI governance 🌐

In the last decade, a great number of organizations have produced documents intended to standardize, in the normative sense, and promote guidance to our recent and rapid AI development. However, _the full content and divergence of ideas presented in these documents have not yet been analyzed, except for a few meta-analyses and critical reviews of the field._ In this work, we seek to expand on the work done by past researchers and create a **tool for better data visualization of the contents and nature of these documents.** We also provide our critical analysis of the results acquired by the application of our tool into a sample size of _200_ documents.

_[Full article here.](https://arxiv.org/abs/2206.11922)_

## Dash Template 🐱‍💻

![demo-dash-app](assets/gif_demo.gif)

Here you can find the source code used to create our _Worldwide AI Ethics_ dashboard. This panel was created using the [Dash](https://dash.plotly.com/dash-enterprise) library. All the tables that feed our dashboard (`data_en.rar`), images (`png_files.rar`), and HTML-plotly graphs (`html_files.rar`) are available in the `data` folder (in `csv` and `parquet`). Auxiliary notebooks for creating the graphs (`make_graphs.ipynb`) and processing the text data(`principle_mining.ipynb`) are also available. We also make available the notebook we used to infer the gender of all authors in our sample (`gender_infer.ipynb`). To render the dashes in your browser, simply run the `worldwide.py` script.

## Requirements 🛠️

```bash

dash
pandas
plotly
urllib3
unidecode
scikit-learn
dash-bootstrap-components

```

## Cite as 🤗

```latex
@article{correa2022worldwide,
  title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
  author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund},
  journal={arXiv preprint arXiv:2206.11922},
  year={2022}
}
```
