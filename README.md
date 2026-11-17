<p align="center">
  <a href="https://github.com/dse-club-kfupm"><img src=".github/assets/logo.svg" alt="Data Engineering &amp; Science Club, KFUPM" width="150"></a>
</p>

<h1 align="center">Exoplanet Signal Vetting</h1>

<p align="center">
  <b>Classifying Kepler transit signals as confirmed planets or false positives</b><br>
  A term 262 applied project of the <a href="https://github.com/dse-club-kfupm">Data Engineering &amp; Science Club, KFUPM</a>
</p>

<p align="center">
  <a href="https://docs.python.org/3/tutorial/"><img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="https://jupyter.org"><img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-notebooks-F37626?logo=jupyter&logoColor=white"></a>
  <a href="https://pandas.pydata.org"><img alt="pandas" src="https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white"></a>
  <a href="https://scikit-learn.org"><img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?logo=scikitlearn&logoColor=white"></a>
  <a href="https://matplotlib.org"><img alt="Matplotlib and seaborn" src="https://img.shields.io/badge/charts-matplotlib%20%C2%B7%20seaborn-11557C"></a>
  <a href="https://www.manim.community"><img alt="Manim" src="https://img.shields.io/badge/animation-Manim-0E1E3A"></a>
</p>

<p align="center">
  <a href="https://github.com/dse-club-kfupm"><img alt="Term 262" src="https://img.shields.io/badge/term-262-1D3A6B"></a>
  <img alt="Astronomy" src="https://img.shields.io/badge/field-Astronomy-47ABD6">
  <a href="#evaluation"><img alt="Metric" src="https://img.shields.io/badge/metric-balanced%20accuracy-3DD2A8"></a>
  <a href="data/README.md"><img alt="Data licence" src="https://img.shields.io/badge/data-NASA%20Exoplanet%20Archive-16A34A"></a>
  <a href="LICENSE"><img alt="Code licence" src="https://img.shields.io/badge/code-MIT-6B7280"></a>
  <a href="https://github.com/dse-club-kfupm/262-exoplanet-vetting/actions/workflows/format-check.yml"><img alt="Format check" src="https://github.com/dse-club-kfupm/262-exoplanet-vetting/actions/workflows/format-check.yml/badge.svg"></a>
</p>

<p align="center">
  <a href="#overview"><b>Overview</b></a> ·
  <a href="#dataset"><b>Dataset</b></a> ·
  <a href="#learning-path"><b>Learning path</b></a> ·
  <a href="#getting-started"><b>Getting started</b></a> ·
  <a href="#workflow"><b>Workflow</b></a> ·
  <a href="#deliverables"><b>Deliverables</b></a> ·
  <a href="#evaluation"><b>Evaluation</b></a> ·
  <a href="#rules"><b>Rules</b></a>
</p>

## Overview

NASA's Kepler space telescope spent four years measuring the brightness of stars, looking for the small, regular dips that occur when a planet passes in front of its star. Every candidate signal was catalogued as a Kepler Object of Interest (KOI). Many of these signals proved to be something else: two stars eclipsing each other, light from a background star, or instrument noise.

In this project you build a classifier that separates confirmed planets from false positives using only the measured properties of each signal and its host star.

> [!NOTE]
> This is a case study. You will not process telescope images or light curves. You work with one table that the NASA Exoplanet Archive has already derived from them, and show how the data science workflow (understanding, cleaning, exploring, modelling and communicating) answers the question on that table.

### Project summary

|  |  |
| --- | --- |
| **Stakeholder** | An exoplanet research team that must decide which candidate signals deserve scarce follow-up telescope time |
| **Question** | Does a transit signal come from a real planet, or is it a false positive? |
| **Target** | `is_planet`: 1 for a confirmed planet, 0 for a false positive |
| **Evaluation** | Balanced accuracy on a hidden test set ([details](#evaluation)) |
| **Training data** | 6,069 signals × 14 columns in `data/train.csv` |
| **Level** | Introductory: DATA 211, Introduction to Data Science |
| **Assessment** | 100 points: 50 for the prediction, 50 for charts, slides and an animation |

## Dataset

`data/train.csv` holds 6,069 KOIs whose status is settled (CONFIRMED or FALSE POSITIVE), about 80% of them. The committee keeps the other 20% as the hidden test set. Rows still marked CANDIDATE were removed, because their true class is not yet known.

| Column | Description | Unit |
| --- | --- | --- |
| `kepoi_name` | KOI identifier; not a feature | text |
| `koi_period` | Time between two transits (orbital period) | days |
| `koi_impact` | How close to the star's centre the planet crosses (impact parameter) | dimensionless |
| `koi_duration` | Length of one transit | hours |
| `koi_depth` | How much the star dims during the transit | parts per million |
| `koi_prad` | Estimated planet radius | Earth radii |
| `koi_teq` | Estimated planet temperature (equilibrium temperature) | kelvin |
| `koi_insol` | Energy received from the star (insolation flux) | relative to Earth |
| `koi_model_snr` | Strength of the transit signal against the noise | ratio |
| `koi_tce_plnt_num` | Order of this signal among the star's detected signals | count |
| `koi_steff` | Star's surface temperature | kelvin |
| `koi_slogg` | Star's surface gravity | log10(cm/s²) |
| `koi_srad` | Star's radius | solar radii |
| `is_planet` | **Target:** 1 confirmed planet, 0 false positive | label |

Test rows contain every column except `is_planet`.

### Data considerations

- **Leakage removed on purpose.** The archive's disposition score, the four false-positive flags, the pipeline disposition and the planet name (which only confirmed planets have) would reveal the answer, so they are not in the table. Recognising this kind of leakage is part of real data work.
- **Class balance.** About 36% of rows are confirmed planets and 64% are false positives.
- **Wide ranges.** `koi_period` runs from a quarter of a day to over 1,000 days, and `koi_depth` and `koi_insol` span several orders of magnitude. A log scale helps both charts and models.
- **Missing values.** About 200 rows (3%) have no value in most of the measured columns.

**Source.** NASA Exoplanet Archive, Kepler Objects of Interest cumulative table, DOI [10.26133/NEA4](https://doi.org/10.26133/NEA4). <https://exoplanetarchive.ipac.caltech.edu>

> [!IMPORTANT]
> Keep this acknowledgement in the README, the slides and any write-up:
>
> “This dataset or service is made available by the NASA Exoplanet Science Institute at IPAC, which is operated by the California Institute of Technology under contract with the National Aeronautics and Space Administration.”

## Learning path

The project assumes the level of DATA 211, Introduction to Data Science. If you have completed it, review the list and open only the topics you are unsure about. Each topic is needed by a specific milestone, so you can learn it just before that milestone. Most Kaggle Learn courses take a few hours and run in the browser.

| When | Topic | Why it is needed | Start with | Go further |
| --- | --- | --- | --- | --- |
| Before you start | Git and GitHub | Every change reaches `main` through a reviewed pull request | [Introduction to GitHub](https://github.com/skills/introduction-to-github) · GitHub Skills | [Pro Git](https://git-scm.com/book/en/v2), chapters 1 to 3 |
| Before you start | Python | The notebooks and `predict.py` are written in Python | [Python](https://www.kaggle.com/learn/python) · Kaggle Learn | [The Python Tutorial](https://docs.python.org/3/tutorial/) · python.org |
| Before you start | Environments | Install the project's packages in isolation | [Virtual environments and packages](https://docs.python.org/3/tutorial/venv.html) · python.org |  |
| Milestone 1 | pandas | Load, inspect and reshape the table | [Pandas](https://www.kaggle.com/learn/pandas) · Kaggle Learn | [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · pandas docs |
| Milestone 1 | Data cleaning | Handle missing and unusual values | [Data Cleaning](https://www.kaggle.com/learn/data-cleaning) · Kaggle Learn | [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) · pandas docs |
| Milestone 1 | Domain background | Understand what each column measures | [KOI column definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html) · NASA Exoplanet Archive |  |
| Milestone 2 | Visualisation | Show how the features relate to the target | [Data Visualization](https://www.kaggle.com/learn/data-visualization) · Kaggle Learn | [Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833) · PLOS |
| Milestone 3 | Modelling | Train a first model and compare it with the baseline | [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) · Kaggle Learn | [Getting started](https://scikit-learn.org/stable/getting_started.html) · scikit-learn |
| Milestone 3 | Better models | Pipelines, categorical features, missing values and leakage | [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) · Kaggle Learn | [Feature Engineering](https://www.kaggle.com/learn/feature-engineering) · Kaggle Learn |
| Milestone 3 | Evaluation | Balanced accuracy and a stratified validation split | [Balanced accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#balanced-accuracy-score) · scikit-learn | [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) · scikit-learn |
| Milestone 4 | Animation | Explain the result in motion, in up to 2 minutes | [Quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html) · Manim | [Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html) · Matplotlib |
| Milestone 4 | Presentation | Take the stakeholder from the question to the answer in 5 to 7 slides | [Ten Simple Rules for Making Good Oral Presentations](https://doi.org/10.1371/journal.pcbi.0030077) · PLOS |  |

## Getting started

You need Python 3.10 or newer and Git.

```bash
git clone https://github.com/dse-club-kfupm/262-exoplanet-vetting.git
cd 262-exoplanet-vetting
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then open `notebooks/01_data_understanding.ipynb` and work through its questions.

- **No local setup?** Google Colab also works: upload `data/train.csv`, and commit your notebooks back to this repository.
- **Preparing the animation?** Install Manim separately with `pip install manim`, after the system packages listed in the [Manim installation guide](https://docs.manim.community/en/stable/installation.html).
- **Questions?** Ask in the organization's [Discussions](https://github.com/orgs/dse-club-kfupm/discussions) or open an issue with the Question template.

## Workflow

The work is divided into four milestones. Each milestone has its own issues in the [Issues tab](https://github.com/dse-club-kfupm/262-exoplanet-vetting/issues) and is complete when all of them are closed.

| Milestone | Complete when |
| --- | --- |
| 1. Data understanding | Notebook 01 and the cleaning functions in `src/features.py` are merged |
| 2. Exploration | Notebook 02, with charts and written findings, is merged |
| 3. Prediction submission | Notebook 03 and `src/predict.py` are merged and pass the format check |
| 4. Visual communication | The slides and the animation or video are merged |

For every change:

1. Choose an open issue and assign yourself to it.
2. Create a branch for it: `git switch -c short-description`.
3. Commit in small steps with clear messages, then push the branch.
4. Open a pull request into `main` and write `Closes #<issue number>` in its description.
5. A teammate reviews it. Once it is approved and the format check has passed, merge it.

Files in `data/`, `tests/` and `.github/` are owned by the committee: a pull request that changes them also needs a committee review.

**Validation guidance for milestone 3.** Hold out a random 20% of the rows, keeping the same share of planets in both parts (`train_test_split` with `stratify`).

## Deliverables

**Part A · Prediction (50 points)**

- [ ] `src/predict.py` with a function `predict(df)`. It receives a table with the test columns and returns 1 (confirmed planet) or 0 (false positive) for each row, in the same order as the rows of `df`.
- [ ] Notebooks 01 to 03, run from top to bottom, documenting how the model was developed.
- [ ] A passing format check. Run `python tests/check_submission.py` from the repository root before the final pull request; the same check runs automatically on every pull request.

**Part B · Visual communication (50 points)**

- [ ] Clear, labelled charts in the notebooks.
- [ ] 5 to 7 slides that take the stakeholder from the question to the answer, saved as PDF in `visuals/slides/`.
- [ ] An animation or a short video of up to 2 minutes made with Python (Manim or matplotlib), with its source code and the rendered file in `visuals/animation/`. A suggested subject: a planet crossing its star and the dip it causes in the star's brightness, or how a real transit differs from an eclipsing pair of stars.

## Evaluation

`predict.py` is run once on the hidden test set after the submission deadline. A team receives the points of the highest level it reaches; the levels are not added together.

| Level | Requirement | Points |
| --- | --- | --- |
| Runs | Returns a valid prediction for every test row | 10 |
| Bronze | Balanced accuracy above the baseline's 50.0% (the baseline always predicts the more common class) | 30 |
| Silver | Balanced accuracy of at least 71.2% | 40 |
| Gold | Balanced accuracy of at least 92.5%, the committee's reference model | 50 |

Balanced accuracy is the average of two percentages: the share of real planets the model finds, and the share of false positives it correctly rejects. A model that always gives the same answer scores 50%.

| Part B | Missing | Basic | Good | Excellent |
| --- | --- | --- | --- | --- |
| Charts in the notebooks | 0 | 5 | 10 | 15 |
| Slides, 5 to 7, as PDF | 0 | 5 | 10 | 15 |
| Animation or video, made with Python, up to 2 minutes | 0 | 7 | 14 | 20 |

> [!IMPORTANT]
> Any team member may be asked to explain any part of the work. If no one can, the Part A points do not count.

## Rules

- Train only on `data/train.csv`.
- Using the full KOI table, or any list of known planets, for training or prediction is not allowed.
- Every change reaches `main` through a pull request reviewed by a teammate.
- `predict.py` may use only pandas, NumPy and scikit-learn, so that it runs in the grading environment. Notebooks and visuals may also use matplotlib, seaborn, plotly and Manim.
- AI tools are allowed if they are declared in the Credits section, and every member must be able to explain the work.
- Follow the organization's [code of conduct](https://github.com/dse-club-kfupm/.github/blob/main/CODE_OF_CONDUCT.md).

## Repository structure

```text
262-exoplanet-vetting/
├── README.md
├── LICENSE                     MIT licence for the code
├── requirements.txt
├── data/
│   ├── train.csv
│   └── README.md               source and licence of the data
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_cleaning_and_exploration.ipynb
│   └── 03_modelling.ipynb
├── src/
│   ├── features.py             cleaning and feature functions
│   └── predict.py              submission entry point
├── models/                     saved model, if predict.py loads one
├── tests/
│   └── check_submission.py     format check, run before submitting
└── visuals/
    ├── slides/                 presentation as PDF
    └── animation/              animation source code and rendered video
```

## Credits

- **Project leads:** Name (@github), Name (@github)
- **Contributors:** Name (@github)
- **Organized by:** Applied Projects Committee, Data Engineering & Science Club, KFUPM
- **Data:** NASA Exoplanet Archive, Kepler Objects of Interest cumulative table, DOI 10.26133/NEA4.
- **AI tools used:** none, or name the tool and what it was used for
- **Licence:** the code is released under the [MIT licence](LICENSE); the data keeps its own licence, described in [data/README.md](data/README.md).

---

<p align="center">
  <sub>Applied Projects Committee · <a href="https://github.com/dse-club-kfupm">Data Engineering &amp; Science Club, KFUPM</a> · نادي هندسة وعلوم البيانات</sub>
</p>
