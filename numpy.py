import numpy as np
import pandas as pd  # CSVを読み込むために使用

# =============================================
# データの読み込み
# =============================================
df = pd.read_csv('sample.csv')

# Pandasで読み込んだデータをNumPy配列に変換する
smartphone = df['スマホ使用時間'].values
sleep      = df['睡眠時間'].values
height     = df['身長'].values
weight     = df['体重'].values

# ここから書いてみよう↓
