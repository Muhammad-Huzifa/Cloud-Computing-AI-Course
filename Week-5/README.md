# Week 5: Linear Regression and Streamlit

Train a simple house-price regression model, save the model and scaler, and use them in a Streamlit prediction application.

## Available materials

| Material | Purpose |
| --- | --- |
| [sklearnLR.ipynb](code/sklearnLR.ipynb) | scikit-learn regression, evaluation, and model saving |
| [train.py](code/House_Size_Prediction_APP/train.py) | Train the application model from the bundled size/price CSV |
| [app.py](code/House_Size_Prediction_APP/app.py) | Predict a price from a user-entered house size |
| [Application dataset](code/House_Size_Prediction_APP/house_price_dataset.csv) | Size and price values used by the training script |
| [streamlit.py](code/streamlit.py) | Separate introductory UI example using fixed prediction coefficients |
| [MLRegressioj.py](code/House_Size_Prediction_APP/Multiple_Linear_Regression/MLRegressioj.py) | Initial data-loading exercise for multiple regression |
| [Multiple-regression dataset](code/House_Size_Prediction_APP/Multiple_Linear_Regression/Housing.csv) | Dataset for the data-loading exercise |
| [Housing.csv](dataset/Houses/Housing.csv) | Additional housing-data practice |

A Week 5 PDF slide deck and a separate student-task notebook have not been added yet.

## Run the prediction application

First follow the [course setup instructions](../README.md#getting-started). Then, from the repository root:

```bash
cd Week-5/code/House_Size_Prediction_APP
python train.py
python -m streamlit run app.py
```

The training script reads `house_price_dataset.csv` from the application folder and saves `house_price_model.pkl` and `house_price_scaler.pkl` there. Run the application from the same folder and open the local URL shown in the terminal.

Use the training script to regenerate the model files for your installed package versions.

## Notebook and practice paths

The regression notebook currently refers to the instructor's Windows copy of the Week 4 dataset. When its kernel runs from `Week-5/code/`, replace that path with:

```python
dataset = pd.read_csv("../../Week-4/dataset/House_Price/house_price_dataset.csv")
```

The multiple-regression script currently loads a dataset and displays its shape; it does not yet train a multiple-regression model. When running it from its own folder, replace its Windows CSV path with `Housing.csv`.

[Course home](../README.md) · [Previous: Week 4](../Week-4/README.md) · [Course roadmap](../docs/ROADMAP.md)
