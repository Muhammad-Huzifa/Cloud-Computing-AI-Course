# Week 5: Linear Regression and Streamlit

Practise simple and multiple linear regression, save models, and connect them to Streamlit applications.

## Lessons, slides, and practice

| Material | Purpose |
| --- | --- |
| [Week 5 slides](slides/Huawei_HCCDA_AI_W05.pdf) | PDF slide deck |
| [sklearnLR.ipynb](code/sklearnLR.ipynb) | Regression, evaluation, scaling, and model saving |
| [slearn.ipynb](code/slearn.ipynb) | Additional house-price regression practice |
| [multiple-linear-regression.ipynb](code/multiple-linear-regression.ipynb) | Laptop-price regression using numeric scaling, brand encoding, and a pipeline |
| [Practice notebook](student_task/sklearnLR.ipynb) | A copy of the scikit-learn regression notebook for classroom practice |
| [Laptop_price.csv](code/Laptop_price.csv) | Dataset for the laptop regression notebook |
| [Housing.csv](dataset/Houses/Housing.csv) | Additional housing-data practice |

## Applications

| Application | Training material | Streamlit entry point |
| --- | --- | --- |
| Simple house-price prediction | [train.py](code/House_Size_Prediction_APP/train.py) and [dataset](code/House_Size_Prediction_APP/house_price_dataset.csv) | [app.py](code/House_Size_Prediction_APP/app.py) |
| House-price prediction with five features | [ml_regression.py](code/House_Size_Prediction_APP/Multiple_Linear_Regression/ml_regression.py) and [Housing.csv](code/House_Size_Prediction_APP/Multiple_Linear_Regression/Housing.csv) | [app.py](code/House_Size_Prediction_APP/Multiple_Linear_Regression/app.py) |
| Alternative simple house-price example | [Application/slearn.ipynb](code/Application/slearn.ipynb) | [Application/app.py](code/Application/app.py) |
| Laptop-price prediction | [multiple-linear-regression.ipynb](code/multiple-linear-regression.ipynb) | [applaptop.py](code/applaptop.py) |
| Introductory UI with fixed coefficients | Coefficients are written in the example | [streamlit.py](code/streamlit.py) |

### Simple house-price application

Complete the [course setup](../README.md#getting-started), then run these commands from the repository root:

```bash
cd Week-5/code/House_Size_Prediction_APP
python train.py
python -m streamlit run app.py
```

Training reads the bundled `house_price_dataset.csv` and creates `house_price_model.pkl` and `house_price_scaler.pkl`. Keep the terminal in this application folder when starting Streamlit.

### Multiple-regression house application

From the repository root, with the course environment activated:

```bash
cd Week-5/code/House_Size_Prediction_APP/Multiple_Linear_Regression
python ml_regression.py
python -m streamlit run app.py
```

The model uses area, bedrooms, bathrooms, stories, and parking. Training creates `ml-regression-model.pkl` and `ml-regression-scaler.pkl` in this folder.

### Alternative house-price application

Open [Application/slearn.ipynb](code/Application/slearn.ipynb), update its CSV path as shown below, and run its training and export cells. It saves `house_price_model.pkl` and `house_price_scale.pkl`; this example uses `scale` in the filename.

Then, from the repository root:

```bash
cd Week-5/code/Application
python -m streamlit run app.py
```

### Laptop application

Run the completed training and export cells in the [laptop notebook](code/multiple-linear-regression.ipynb) to regenerate `laptop_price.pkl` for your environment. Complete the unfinished practice cell before using Run All.

From the repository root:

```bash
cd Week-5/code
streamlit run applaptop.py
```

Use the `streamlit` command in this folder: `python -m streamlit` would select the local `streamlit.py` example instead of the installed package.

## Notebook paths and practice

Some data-loading cells still use the instructor's Windows paths. Use these relative paths when the kernel runs from the notebook's own directory:

| Notebook | CSV path |
| --- | --- |
| `code/sklearnLR.ipynb` | `../../Week-4/dataset/House_Price/house_price_dataset.csv` |
| `student_task/sklearnLR.ipynb` | `../../Week-4/dataset/House_Price/house_price_dataset.csv` |
| `code/slearn.ipynb` | `House_Size_Prediction_APP/house_price_dataset.csv` |
| `code/Application/slearn.ipynb` | `../House_Size_Prediction_APP/house_price_dataset.csv` |
| `code/multiple-linear-regression.ipynb` | `Laptop_price.csv` |

The laptop notebook contains an unfinished classroom cell with `numerical =` and `catagorie =`. Fill in those feature lists before running that cell, or work through the completed teaching cells individually. The [Week 6 guide](../Week-6/README.md) explains the complete preprocessing pipeline.

Run the training material again when you need model files compatible with your installed package versions.

[Course home](../README.md) · [Previous: Week 4](../Week-4/README.md) · [Next: Week 6](../Week-6/README.md)
