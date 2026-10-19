# Cloud Computing and AI Course

**From ML to production AI deployment: training, pipelines, and cloud.**

Teaching materials for a twelve-week Huawei HCCDA-AI course, prepared by [Muhammad Huzifa](https://github.com/Muhammad-Huzifa). The course develops practical skills in Python, data analysis, machine learning, and model deployment.

Materials for **Weeks 1–6** are available below. Weeks 7–12 follow the [course roadmap](docs/ROADMAP.md) and will be added as teaching progresses.

## Course materials

| Week | Available code focus | Notebooks and code | PDF slides |
| --- | --- | --- | --- |
| [Week 1](Week-1/README.md) | Python foundations, collections, loops, functions, and classes | [Lessons and tasks](Week-1/Code/) | [Week 1 slides](Week-1/Slides/Huawei_HCCDA_AI_W01.pdf) |
| [Week 2](Week-2/README.md) | Python practice, matrix operations, and object-oriented programming | [Lessons and tasks](Week-2/Code/) | [Week 2 slides](Week-2/Slides/Huawei_HCCDA_AI_W02.pdf) |
| [Week 3](Week-3/README.md) | NumPy, Pandas DataFrames, and TensorFlow regression | [Lesson notebooks](Week-3/Code/) | [Week 3 slides](Week-3/Slides/Huawei_HCCDA_AI_W03.pdf) |
| [Week 4](Week-4/README.md) | Matplotlib and review of data analysis and regression | [Lesson notebooks](Week-4/Code/) | [Shared Week 3 deck](Week-4/Slides/Huawei_HCCDA_AI_W03.pdf) |
| [Week 5](Week-5/README.md) | Simple and multiple regression, model saving, and Streamlit applications | [Notebooks and applications](Week-5/code/) | [Week 5 slides](Week-5/slides/Huawei_HCCDA_AI_W05.pdf) |
| [Week 6](Week-6/README.md) | Laptop-price regression with preprocessing pipelines and Streamlit | [Notebook and application](Week-6/code/) | Not yet added |

Weeks 1 and 2 include `Live_Code.ipynb` and `Student_Tasks.ipynb`. Weeks 3–6 use topic-specific notebooks and scripts. Week 5 also includes a [practice copy of the regression notebook](Week-5/student_task/sklearnLR.ipynb). Week 4 currently reuses the Week 3 PDF deck.

## Getting started

Use Python 3.11 and run these commands from your terminal:

```bash
git clone https://github.com/Muhammad-Huzifa/Cloud-Computing-AI-Course.git
cd Cloud-Computing-AI-Course
python -m venv .venv
```

Activate the environment for your terminal:

| Terminal | Command |
| --- | --- |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Windows Git Bash | `source .venv/Scripts/activate` |
| Linux or macOS | `source .venv/bin/activate` |

Install the course packages and start JupyterLab:

```bash
python -m pip install -r requirements.txt
python -m jupyter lab
```

For the TensorFlow notebooks, also install:

```bash
python -m pip install -r requirements-tensorflow.txt
```

## How to use the lessons

1. Open the week's index and read its PDF slides when available.
2. Open a lesson notebook in JupyterLab and run its cells in order.
3. Complete `Student_Tasks.ipynb` where provided.
4. Use the accompanying CSV files for data analysis and regression.
5. Follow each application's week guide, update any local paths, and train or export its model before launching Streamlit.

### Dataset paths

Some notebooks still contain the instructor's original Windows paths. Replace `file_path`, or the path passed to `pd.read_csv(...)`, with the location on your computer.

When the notebook kernel runs from its `Code/` or `code/` directory, use:

| Notebook | CSV path |
| --- | --- |
| Week 3 or 4: `Housing_DataFrame_Basics.ipynb` | `../dataset/Houses/Housing.csv` |
| Week 3 or 4: `TensorFlow.ipynb` | `../dataset/House_Price/house_price_dataset.csv` |
| Week 5: `sklearnLR.ipynb`, including the practice copy | `../../Week-4/dataset/House_Price/house_price_dataset.csv` |
| Week 5 or 6: `multiple-linear-regression.ipynb` | `Laptop_price.csv` |

The NumPy notebooks also contain file-loading examples; check those paths before running the corresponding cells. The [Week 5 guide](Week-5/README.md#notebook-paths-and-practice) covers its additional house-price notebooks, and the [Week 6 guide](Week-6/README.md#prepare-the-notebook) explains the laptop dataset and model paths.

## Run the Week 5 application

From the repository root, with the environment activated:

```bash
cd Week-5/code/House_Size_Prediction_APP
python train.py
python -m streamlit run app.py
```

Training creates `house_price_model.pkl` and `house_price_scaler.pkl` in the application folder. Keep the terminal in that folder so the application can find both files. Open the local URL printed by Streamlit.

See the [Week 5 guide](Week-5/README.md) for the multiple-regression house application, laptop example, and classroom practice. The [Week 6 guide](Week-6/README.md) covers the laptop preprocessing pipeline and its Streamlit application.

## Repository guide

| Location | Contents |
| --- | --- |
| `Week-1/` and `Week-2/` | Live lesson notebooks, student tasks, and PDF slides |
| `Week-3/` and `Week-4/` | Topic notebooks, PDF slides, and datasets |
| [Week-5/](Week-5/README.md) | Regression notebooks, house and laptop applications, PDF slides, and a practice notebook |
| [Week-6/](Week-6/README.md) | Laptop-price notebook, dataset, saved pipeline, and Streamlit application |
| [requirements.txt](requirements.txt) | Packages for notebooks, classical ML, and Streamlit |
| [requirements-tensorflow.txt](requirements-tensorflow.txt) | Course packages plus TensorFlow |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Published topics and planned twelve-week sequence |

## Instructor

**Muhammad Huzifa**  
Research Assistant, DIP & AI Research Lab, Islamia College University Peshawar.

[GitHub](https://github.com/Muhammad-Huzifa) · [LinkedIn](https://www.linkedin.com/in/muhammad-huzifa3202/)
