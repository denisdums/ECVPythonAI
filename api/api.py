from typing import Union
from fastapi import FastAPI, Request
import pandas as pd
import xgboost as xg

app = FastAPI()

@app.post("/")
def read_root(request: Request):
    regressor = xg.XGBRegressor()
    regressor.load_model("../resources/xgb.json")

    energy = request.query_params.get("energy")
    if energy is "":
        energy = 0
    else:
        energy = float(energy)

    valence = request.query_params.get("valence")
    if valence is "":
        valence = 0
    else:
        valence = float(valence)

    acousticness = request.query_params.get("acousticness")
    if acousticness is "":
        acousticness = 0
    else:
        acousticness = float(acousticness)

    liveness = request.query_params.get("liveness")
    if liveness is "":
        liveness = 0
    else:
        liveness = float(liveness)

    x = [[energy, valence, acousticness, liveness]]

    data = pd.DataFrame(x, columns=['energy', 'valence', 'acousticness', 'liveness'])
    prediction = regressor.predict(data).tolist()[0]

    return {"prediction": prediction}
