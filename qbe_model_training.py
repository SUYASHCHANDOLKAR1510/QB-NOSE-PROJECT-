# Quantum Bioelectronic Nose - TinyML Training Script
# Trains a model to classify gases using 3 sensor values

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Load your dataset
# CSV should have columns: ['mq3', 'mq135', 'graphene', 'label']
data = pd.read_csv('gas_sensor_dataset.csv')

# Features and Labels
X = data[['mq3', 'mq135', 'graphene']]
y = to_categorical(data['label'])  # Example: 0 = Clean, 1 = Alcohol, etc.

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential([
    Dense(16, activation='relu', input_shape=(3,)),
    Dense(16, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))

# Save model
model.save('qbe_model.h5')
