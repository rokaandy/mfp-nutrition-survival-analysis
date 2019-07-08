import pickle
import pandas as pd
import numpy as np

def prediction(user_input, model):
    user_input = np.array((user_input))
    df = pd.DataFrame(user_input).T
    proba = model.predict_proba(df)
return proba