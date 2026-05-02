# Deceptive Cookies: Consent by Design - A Mixed Method Study

## About

This repository contains the code used to quantitatively analyse the data in the article *Deceptive Cookies: Consent by Design - a Mixed Method Study*.

The raw data from the study is not shared, it is only presented in aggregated forms found in the tables and figures.

## Structure

The main file is `main.py`, which can be run with `python main.py`. The python packages can be found in `requirements.txt`, run `pip install -r requirements.txt` to install. It is generally recommended to use a Python virtual environment, for example with [`uv`](https://github.com/astral-sh/uv). The tools `flake8`, `autopep8` and `isort` were used to format the code.

The main file reads and processes the data, runs the hypothesis tests and creates LaTeX tables with the results. Note due to the nature of the data, it will not be made publically available, so it will not be possible to reproduce the results. However, the code for running the analysis is here and is possible to examine. The tables (in LaTeX syntax) and plots are included in this repository (in `latex_tables/` and `plots/`).

The source code can be found in `src/`, with separate files for loading and processing data, making well-formed paths, performing hypothesis tests, making LaTeX tables and more. Some constants, such as folder names, filenames and column names of the data, can be found in `constants.yaml`.

This repository contains statistics, tests and tables for more that was included in the final study. As noted in the article, multiple hypothesis tests were performed without adjusting the p-value for this, so the p-values should be interpreted with care. This was because the motivation of the study was to explore a wide variety of possible connections rather than arriving at conclusive evidence.

The raw data was saved in files in `data/`. The answers from the survey was saved as an `xlsx` file with the questions and answers. The results from the usability test, such as responses to the cookie consent banners, the time spent interacting with them and utterances from the participants when doing so was manually saved in structured `yaml` files, one per participant.

![gif should be here :)](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmk1anhsaDl1b2tpdnRvYjF3bTQ0MmZodGVrbXU2emVjd3U0cjd3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ov2S60rDmVTMc/giphy.gif)
