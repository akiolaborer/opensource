import pandas
import numpy

import matplotlib.pyplot as plot
import japanize_matplotlib

FILE_NAME = r""
dataset = pandas.read_csv(FILE_NAME)

print(dataset.head(1))
print("Len:", len(dataset))

print("Info:", dataset.info())
print("Shape:", dataset.shape)

print(dataset["表層系"])
print(dataset[["表層系","品詞"]].head(5))
print(dataset[0:5])

pos = dataset[dataset["品詞"] == "名詞"]
pos.head(5)
np = pos["原形"].head(5).values
print(np)

print(pos["表層系"].value_counts())
print(pos["表層系"].value_counts().index[0])

print(pos["表層系"].value_counts().iat[0])
print(pos["表層系"].nunique())

tf = pos["表層系"].value_counts().iat[0] / pos["表層系"].nunique()
print("TF:", tf)

idf = numpy.log(pos["表層系"].nunique() / pos["表層系"].value_counts().iat[0] ) + 1
print("IDF:", idf)

tfidf = tf * idf
print("TF-IDF:", tfidf)

pos["表層系"].value_counts().plot(kind="bar")
plot.show()
