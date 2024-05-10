import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 386300009 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t_stat, p_val = ttest_ind(x, y, equal_var=False) < 0.06
    return p_val < 0.06
