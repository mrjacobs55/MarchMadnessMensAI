from keras.models import Sequential
from keras.layers import Dense


model = Sequential()
model.add(Dense(32, activation='relu', input_dim=33))
model.add(Dense(30, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(2, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])


