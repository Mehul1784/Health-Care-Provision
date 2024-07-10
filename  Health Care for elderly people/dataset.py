import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Sample dataset
data = {
    "Symptom1": [1, 0, 1, 0, 1, 1, 0],
    "Symptom2": [0, 1, 1, 1, 0, 1, 0],
    "Symptom3": [1, 1, 0, 1, 1, 0, 1],
    "Disease": ["Diabetes", "Heart Problems", "Respiratory Ailments", "Cancer", "Depression", "Alzheimer's", "Diabetes"]
}

df = pd.DataFrame(data)

# Encode labels
label_encoder = LabelEncoder()
df['Disease'] = label_encoder.fit_transform(df['Disease'])

# Split data
X = df.drop('Disease', axis=1)
y = df['Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model and label encoder
with open('disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)
with open('label_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoder, file)