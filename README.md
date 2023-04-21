# ECVPythonAI

## Installation
### Get model
Run [Notebook-XGBoost](notebooks/Notebook-XGBoost.ipynb). then `resources/xgb.json` will be created.

### Run api
```bash
    cd api

    uvicorn api:app --reload
```

### Run front
```bash
    cd front

    python manage.py runserver 8080
```

## Analysis
For learn the analysis, please read the [Notebook-DataAnalyse](notebooks/Notebook-DataAnalyse.ipynb).
