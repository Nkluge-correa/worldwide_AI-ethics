<h2 style="text-align:center"> Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance </h2>

The utilization of artificial intelligence (AI) applications has experienced tremendous growth in recent years, bringing forth numerous benefits and conveniences. However, this expansion has also provoked ethical concerns, such as privacy breaches, algorithmic discrimination, security and reliability issues, transparency, and other unintended consequences. To determine whether a global consensus exists regarding the ethical principles that should govern AI applications and to contribute to the formation of future regulations, this paper conducts a meta-analysis of 200 governance policies and ethical guidelines for AI usage published by public bodies, academic institutions, private companies, and civil society organizations worldwide. **We identified at least 17 resonating principles prevalent in the policies and guidelines of our dataset, released as an open-source database and tool**. We present the limitations of performing a global scale analysis study paired with a critical analysis of our findings, presenting areas of consensus that should be incorporated into future regulatory efforts.

<p style="text-align: center;">
<a href="https://doi.org/10.1016/j.patter.2023.100857" target="_blank">Full article here.</a>
</p>

### Dash Template 🐱‍💻

Here you can find the source code used to create our _Worldwide AI Ethics_ dashboard. This panel was created using the [Dash](https://dash.plotly.com/dash-enterprise) library. All the tables that feed our dashboard (`data_en.rar`), images (`png_files.rar`), and HTML-Plotly graphs (`html_files.rar`) are available in the `data` folder (in `csv` and `parquet`). Auxiliary notebooks for creating the graphs (`make_graphs.ipynb`) and processing the text data(`principle_mining.ipynb`) are also available. We also make available the notebook we used to infer the gender of all authors in our sample (`gender_infer.ipynb`), and the notebook to create the `geojson` file that sets the boundaries of the polygons on the `Mapbox`. To render the dash app in your browser, simply run the `worldwide.py` script.

### Worldwide AI Ethics Embeddings: _visualizing normative principles in vector space_

In the `waie-embeddings`, you can find one of the first spin-offs of our study.

After curating a dataset with 1400+ definitions across 17 ethical principles in AI (the Worldwide AI Ethics dataset), we leverage OpenAI's `text-embedding-ada-002` to perform a different kind of analysis. In short, we have transformed these definitions into vectors so we can visualize them in 3D space using PCA and t-SNE.

The generated plots are available on our [website](https://nkluge-correa.github.io/worldwide_AI-ethics/).

## Cite as 🤗

```latex
@article{correa2023worldwide,
  author={Corr{\^e}a, Nicholas Kluge and Galv{\~a}o, Camila and Santos, James William and Del Pino, Carolina and Pinto, Edson Pontes and Barbosa, Camila and Massmann, Diogo and Mambrini, Rodrigo and Galv{\~a}o, Luiza and Terem, Edmund and Oliveira, Nythamar},
  title={Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance},
  journal={Patterns},
  year={2023},
  month={October},
  volume={4},
  number={10},
  doi={10.1016/j.patter.2023.100857}
}
```
