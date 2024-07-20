import numpy as np
import pandas as pd

# Данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Средние значения
mean_zp = np.mean(zp)
mean_ks = np.mean(ks)

# Ковариация с помощью numpy
cov_matrix = np.cov(zp, ks, ddof=1)
cov_numpy = cov_matrix[0, 1]
print(f"Ковариация (numpy): {cov_numpy}")

# Коэффициент корреляции Пирсона с помощью numpy
corr_numpy = np.corrcoef(zp, ks)[0, 1]
print(f"Коэффициент корреляции Пирсона (numpy): {corr_numpy}")

# Коэффициент корреляции Пирсона с помощью pandas
df = pd.DataFrame({'zp': zp, 'ks': ks})
corr_pandas = df.corr().iloc[0, 1]
print(f"Коэффициент корреляции Пирсона (pandas): {corr_pandas}")
