<div align="center">

# Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance

[Dashboard](https://nkluge-correa.github.io/worldwide_AI-ethics/dashboard.html) | [Paper](https://doi.org/10.1016/j.patter.2023.100857) | [Embeddings](https://nkluge-correa.github.io/worldwide_AI-ethics/tsne.html)

</div>

The utilization of artificial intelligence (AI) applications has experienced tremendous growth in recent years, bringing forth numerous benefits and conveniences. However, this expansion has also provoked ethical concerns, such as privacy breaches, algorithmic discrimination, security and reliability issues, transparency, and other unintended consequences. To determine whether a global consensus exists regarding the ethical principles that should govern AI applications and to contribute to the formation of future regulations, this paper conducts a meta-analysis of 200 governance policies and ethical guidelines for AI usage published by public bodies, academic institutions, private companies, and civil society organizations worldwide. **We identified at least 17 resonating principles prevalent in the policies and guidelines of our dataset, released as an open-source database and tool**. We present the limitations of performing a global scale analysis study paired with a critical analysis of our findings, presenting areas of consensus that should be incorporated into future regulatory efforts.

## Dash Template

Here, you can find the source code for the [Dash](https://dash.plotly.com/dash-enterprise) version of our WAIE dashboard. All the sources that feed our dashboard (`data.rar`), images (`png_files.rar`), and HTML-Plotly graphs (`html_files.rar`) are available in the [`data`](data) folder.

To render the dash app in your browser, install the [requirements](requirements.txt) and run the `app.py` script.

Auxiliary notebooks and scripts for processing the text data are:

- `parse-raw-data.py`: This script pareses the raw table ([`data_raw.parquet`](data/data_raw.parquet)) into a formated json file. This is used to feed most of the graphs and functionalities of the dashboard.
- `principle_mining.ipynb`: This notebook processes the principles and creates the n-gram plots. All n-gram tables are in [`data/n-grams`](data/n-grams).

## Worldwide AI Ethics Embeddings: visualizing normative principles in vector space

In the `waie-embeddings`, you can find one of the first spin-offs of our study.

After curating a dataset with 1400+ definitions across 17 ethical principles in AI (the Worldwide AI Ethics dataset), we leverage OpenAI's `text-embedding-ada-002` to perform a different analysis. In short, we have transformed these definitions into vectors to visualize them in 3D space using PCA and t-SNE. You can find the notebook we used to run this analysis [here](waie-embeddings/evaluate_embbedings.ipynb) (embedding data can be found in the [`waie-embeddings/data`](waie-embeddings/data) folder).

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

## Funding

This research was funded by RAIES ([Rede de Inteligência Artificial Ética e Segura](https://www.raies.org/)). RAIES is a project supported by FAPERGS ([Fundação de Amparo à Pesquisa do Estado do Rio Grande do Sul](https://fapergs.rs.gov.br/inicial)) and CNPq ([Conselho Nacional de Desenvolvimento Científico e Tecnológico](https://www.gov.br/cnpq/)).

## License

Worldwide AI Ethics is licensed under the CC-BY-NC license, Version 4.0. See the [LICENSE](LICENSE) file for more details.
