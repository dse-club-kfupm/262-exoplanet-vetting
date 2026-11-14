# Planet Hunters: Real Planet or False Signal?

Data Engineering & Science Club, Applied Projects Committee, KFUPM. Term 262. Prediction case study.

NASA's Kepler telescope spent four years measuring the brightness of stars, looking for the small, regular dips that occur when a planet passes in front of its star. Every dip it flagged became a Kepler Object of Interest (KOI). Many of these signals turned out to be something else: two stars eclipsing each other, light from a background star, or instrument noise.

In this project you build a model that predicts whether a KOI is a confirmed planet or a false positive, using only the measured properties of the signal and its host star.

## Scope

This is a case study. You will not process telescope images or brightness curves. You work with one table that the NASA Exoplanet Archive has already derived from them, and you show how the data science workflow (understanding, cleaning, exploring, modelling and communicating) answers the question on that table.

## The client and the question

| Item | Description |
| --- | --- |
| Client | An analyst at a space agency with more candidate signals than follow-up telescope time |
| Question | Is this signal a real planet or a false positive? |
| Prediction | `is_planet`: 1 for a confirmed planet, 0 for a false positive |
| Score | Balanced accuracy on the hidden test set (see Grading) |

## The data

`data/train.csv` contains about 80% of the KOIs whose status is settled (CONFIRMED or FALSE POSITIVE). The committee holds the remaining 20% as the hidden test set; it is used only for grading. Rows still marked CANDIDATE were removed, because their true class is not yet known.

Columns that would give the answer away were also removed: the archive's disposition score, the four false-positive flags, the pipeline disposition, and the planet name, which exists only for confirmed planets. Recognising this kind of leakage is part of real data work.

| Column | Meaning | Unit |
| --- | --- | --- |
| `kepoi_name` | KOI identifier, not used as a feature | text |
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
| `is_planet` | Target: 1 confirmed planet, 0 false positive | label |

Test rows contain every column except `is_planet`.

Source: NASA Exoplanet Archive, Kepler Objects of Interest cumulative table, DOI 10.26133/NEA4. <https://exoplanetarchive.ipac.caltech.edu>

Keep this acknowledgement in the README, the slides and any write-up: "This dataset or service is made available by the NASA Exoplanet Science Institute at IPAC, which is operated by the California Institute of Technology under contract with the National Aeronautics and Space Administration."

## Prerequisites

Learn these before you start. Each row gives one source to start with and one to go further.

| Skill | Start with | Go further |
| --- | --- | --- |
| Git and GitHub | [Introduction to GitHub](https://github.com/skills/introduction-to-github), GitHub Skills | [Pro Git](https://git-scm.com/book/en/v2), chapters 1 to 3 |
| Python | [Python](https://www.kaggle.com/learn/python), Kaggle Learn | [The Python Tutorial](https://docs.python.org/3/tutorial/) |
| pandas | [Pandas](https://www.kaggle.com/learn/pandas), Kaggle Learn | [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) |
| Data cleaning | [Data Cleaning](https://www.kaggle.com/learn/data-cleaning), Kaggle Learn | [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) |
| Charts | [Data Visualization](https://www.kaggle.com/learn/data-visualization), Kaggle Learn | [Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833) |
| Prediction | [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning), Kaggle Learn | [scikit-learn: Getting started](https://scikit-learn.org/stable/getting_started.html) |
| Animation | [Manim Community quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html) | [Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html) |
| Slides | [Ten Simple Rules for Making Good Oral Presentations](https://doi.org/10.1371/journal.pcbi.0030077) |  |

Background on the data: the [KOI column definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html) published by the archive.

## Getting started

```bash
git clone https://github.com/dse-club-kfupm/262-planet-hunters.git
cd 262-planet-hunters
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Open `notebooks/01_data_understanding.ipynb`. Google Colab is also acceptable; upload `data/train.csv` and keep your notebooks in the repository.

## Repository structure

```text
262-planet-hunters/
├── README.md
├── requirements.txt
├── data/
│   ├── train.csv
│   └── README.md               source and licence
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_cleaning_and_exploration.ipynb
│   └── 03_modelling.ipynb
├── src/
│   ├── features.py             cleaning and feature functions
│   └── predict.py              submission entry point
├── models/                     saved model, if predict.py loads one
├── tests/
│   └── check_submission.py     run before submitting
└── visuals/
    ├── slides/                 presentation as PDF
    └── animation/              animation source code and rendered video
```

## What you submit

Part A, prediction (50 points)

- `src/predict.py` containing a function `predict(df)`. It receives a table with the test columns described above and returns 1 (confirmed planet) or 0 (false positive) per row, in the same order.
- The three notebooks showing how you reached the model.
- Run `python tests/check_submission.py` before your final pull request. It confirms that `predict.py` loads and returns predictions in the right format.

Part B, visual communication (50 points)

- Clear, labelled charts in the notebooks.
- Slides: 5 to 7 slides that take the client from the question to the answer, saved as PDF in `visuals/slides/`.
- An animation or a short video of up to 2 minutes made with Python (Manim or matplotlib), with its source code and the rendered file in `visuals/animation/`. A good subject: a planet crossing its star and the dip it causes in the star's brightness, or how a real transit differs from an eclipsing pair of stars.

## Grading

Your `predict.py` is run once on the hidden test set after the submission deadline.

| Level | Requirement | Points |
| --- | --- | --- |
| Runs | Returns a valid prediction for every test row | 10 |
| Bronze | Scores above the baseline, which always predicts the more common class: 50.0% | 30 |
| Silver | Balanced accuracy of at least 71.2% | 40 |
| Gold | Balanced accuracy of at least 92.5%, the committee's reference model | 50 |

Balanced accuracy is the average of two percentages: the share of real planets your model finds, and the share of false positives it correctly rejects. A model that always gives the same answer scores 50%.

| Part B | Missing | Basic | Good | Excellent |
| --- | --- | --- | --- | --- |
| Charts in the notebooks | 0 | 5 | 10 | 15 |
| Slides, 5 to 7, as PDF | 0 | 5 | 10 | 15 |
| Animation or video, made with Python, up to 2 minutes | 0 | 7 | 14 | 20 |

Any team member may be asked to explain any part of the work. If no one can, the Part A points do not count.

## Milestones

Progress is tracked with four milestones, each with its own issues.

| Milestone | Complete when |
| --- | --- |
| 1. Data understanding | Notebook 01 and the cleaning functions are merged |
| 2. Exploration | Notebook 02, with charts and written findings, is merged |
| 3. Prediction submission | Notebook 03 and `src/predict.py` are merged and pass the format check |
| 4. Visual communication | The slides and the animation or video are merged |

## Rules

- Train only on `data/train.csv`.
- Using the full KOI table, or any list of known planets, for training or prediction is not allowed.
- Every change reaches `main` through a pull request reviewed by a teammate.
- AI tools are allowed if declared in the Credits section, and every member must be able to explain the work.
- `predict.py` may use only pandas, NumPy and scikit-learn, so that it runs in the grading environment. Notebooks and visuals may also use matplotlib, seaborn, plotly and Manim.

## Credits

- Project Leads: Name (@github), Name (@github)
- Contributors: Name (@github)
- Organized by: Applied Projects Committee, Data Engineering & Science Club, KFUPM
- Data: NASA Exoplanet Archive, Kepler Objects of Interest cumulative table, DOI 10.26133/NEA4.
- AI tools used: none, or name the tool and what it was used for
