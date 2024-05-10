import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return ttest_ind(x, y, equal_var=False)[1] < 0.06
