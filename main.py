from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
#
# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Dense, InputLayer

iris = load_iris(as_frame=True).frame

# model = Sequential(
#     layers=[
#         InputLayer(),
#         Dense(32, activation="relu"),
#         Dense(3)
#     ]
# )
#model.compile(optimizer='adam',          metrics=['accuracy'])

model = LogisticRegression()
