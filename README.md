# Worldwide AI Ethics: a review of _200_ guidelines and recommendations for AI governance 🌐

In the last decade, a great number of organizations have produced documents intended to standardize, in the normative sense, and promote guidance to our recent and rapid AI development. However, _the full content and divergence of ideas presented in these documents have not yet been analyzed, except for a few meta-analyses and critical reviews of the field._ In this work, we seek to expand on the work done by past researchers and create a **tool for better data visualization of the contents and nature of these documents.** We also provide our critical analysis of the results acquired by the application of our tool into a sample size of _200_ documents.

_[Full article here.](https://arxiv.org/abs/2206.11922)_

## Dash Teamplate 🐱‍💻

![demo-dash-app](assets/gif_demo.gif)

Here you can find the source code used to create our _Worldwide AI Ethics_ dashboard. This panel was created using the [Dash](https://dash.plotly.com/dash-enterprise) library. All the tables that feed our dashboard (`data(en).rar`), images (`png_files(en).rar`), and HTML-plotly graphs (`html_files(en).rar`) are also available in two languages (_Portuguese and English_). Auxiliary notebooks for creating the graphs (`make_graphs.ipynb`) and processing the text in the tables (`principle_mining.ipynb`) are also available. To render the dashes in your browser, simply run the `my_app_en.py` (_english_) or the `my_app_pt.py` (_portuguese_) script.

## Requirements 🛠️

```python
plotly==5.7.0
dash==2.3.1
dash-bootstrap-components==1.1.0
dash-auth==1.4.1
dash-daq==0.5.0
dash-labs==1.0.4
gunicorn==20.1.0
unidecode==1.3.4
openpyxl==3.0.9
pandas==1.4.2
```

## How to cite this study😊

```latex
@article{correa2022worldwide,
  title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
  author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund},
  journal={arXiv preprint arXiv:2206.11922},
  year={2022}
}
```
