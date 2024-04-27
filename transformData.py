import json
import pandas as pd
from IPython.display import display
from datetime import datetime
import math
import numpy as np
import matplotlib.pyplot as plt


with open('EuronextOslo.json') as json_file:
    data = json.load(json_file)
    print(data.keys())
    eq = data["equinor"]
    pdDF = pd.DataFrame(eq)
    stockValues = pdDF["last"].iloc[0:(math.floor(len(pdDF)/12))]



