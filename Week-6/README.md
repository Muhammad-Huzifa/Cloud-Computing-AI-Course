# Week 6: Laptop-Price Regression with Pipelines

Combine numeric scaling, categorical encoding, and linear regression in one scikit-learn pipeline. Use the saved pipeline in a Streamlit laptop-price application.

## Available materials

| Material | Purpose |
| --- | --- |
| [multiple-linear-regression.ipynb](code/multiple-linear-regression.ipynb) | Load the dataset, split the data, build the pipeline, train, evaluate, and export |
| [Laptop_price.csv](code/Laptop_price.csv) | Laptop specifications and prices |
| [app.py](code/app.py) | Streamlit application for entering laptop specifications |
| [multiple_linear_regression.pkl](code/multiple_linear_regression.pkl) | Saved preprocessing and regression pipeline |

A Week 6 PDF slide deck has not been added yet.

## What the pipeline does

| Step | Component | Purpose |
| --- | --- | --- |
| Scale numbers | `StandardScaler` | Scale processor speed, RAM, storage, screen size, and weight |
| Encode brands | `OneHotEncoder` | Convert the brand column into numeric features |
| Combine preprocessing | `ColumnTransformer` | Apply the appropriate transformation to each column group |
| Predict price | `LinearRegression` | Learn the relationship between the processed features and price |
| Keep the steps together | `Pipeline` | Apply the same fitted preprocessing during training and prediction |

The input columns are `Brand`, `Processor_Speed`, `RAM_Size`, `Storage_Capacity`, `Screen_Size`, and `Weight`. The target column is `Price`.

## Prepare the notebook

1. Complete the [course setup](../README.md#getting-started).
2. Open the notebook in `Week-6/code/`.
3. Replace the Windows CSV path in its loading cell with:

```python
data = pd.read_csv("Laptop_price.csv")
```

Run the training cells through the model-export cell. The pipeline is saved as `multiple_linear_regression.pkl` in the notebook's working directory.

### Evaluation and practice notes

The current evaluation cell passes the R² arguments in reverse order. Use the true values first:

```python
r2 = r2_score(y_test, prediction)
```

The final DataFrame practice cell uses `ram = 32,`, which creates a tuple. Use `ram = 32` for a numeric RAM value when preparing a prediction example.

## Run the application

In [app.py](code/app.py), replace the instructor's Windows model path with the filename in this folder:

```python
model = joblib.load("multiple_linear_regression.pkl")
```

Then, from the repository root with the course environment activated:

```bash
cd Week-6/code
python -m streamlit run app.py
```

Keep the model file in this folder and open the local URL printed by Streamlit. The saved pipeline handles scaling and brand encoding when the application calls `predict`.

Regenerate the pipeline from the notebook when you need a model compatible with your installed package versions.

[Course home](../README.md) · [Previous: Week 5](../Week-5/README.md) · [Course roadmap](../docs/ROADMAP.md)
