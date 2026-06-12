import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/creditcard.csv")

# ---------------- FEATURES (30 SAFE) ----------------
X = df.drop("Class", axis=1)
y = df["Class"]

# ---------------- TRAIN TEST SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ----------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------------- SAVE MODEL ----------------
joblib.dump(model, "models/fraud_model.pkl")

print("✅ Model trained successfully with 30 features")