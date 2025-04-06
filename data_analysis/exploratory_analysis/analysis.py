from google.colab import drive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
%matplotlib inline
drive.mount('/content/drive')
file_path = '/content/drive/My Drive/data/listings.csv'
df = pd.read_csv(file_path)

missing = df.isnull().mean().sort_values(ascending=False)
df = df.drop(columns=missing[missing > 0.5].index)
df = df.dropna(subset=["price", "latitude", "longitude"])
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="longitude", y="latitude", hue="room_type", alpha=0.4)
plt.title("Distribuição Geográfica dos Imóveis por Tipo de Quarto")

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="room_type", y="price")
plt.ylim(0, 1000)  # limitar outliers
plt.title("Distribuição de Preços por Tipo de Quarto")

sns.scatterplot(data=df, x="review_scores_rating", y="price", alpha=0.5)
plt.title("Relação entre Avaliação e Preço")

top_bairros = df['neighbourhood'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_bairros.values, y=top_bairros.index)
plt.title("Top 10 Bairros com Mais Anúncios")

drive.flush_and_unmount()