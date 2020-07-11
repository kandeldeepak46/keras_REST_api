# Zero to Production

> It is not recommended to deploy your production models as shown here.
 This is just an end-to-end example to get started quickly.


This guide shows you how to:

- build a Deep Neural Network that predicts Airbnb prices in NYC (using scikit-learn and Keras)
- build a REST API that predicts prices based on the model (using Flask and gunicorn)


# Quick start

Requirements:

- Python 3.7



Install libraries:

```bash
pip install -r requirements.txt
```

## Start local server

```bash
flask run
```

## Make predictions
```bash
python test_api.py
```