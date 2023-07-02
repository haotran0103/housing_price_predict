import os 
import sys

import numpy as np
import pandas as pd
import dill
from src.exception import CusException


def save_objects(path, objects):
    try:
        dir = os.path.dirname(path)
        os.makedirs(dir, exist_ok=True)
        with open(path , 'wb') as f:
            dill.dump(objects, f)
    except Exception as e:
        raise CusException(e, sys)