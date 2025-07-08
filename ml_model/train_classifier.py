
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
import joblib

# Load CSV
df = pd.read_csv('results/perf_log.csv')

# Encode labels: Random = 1, Non-Random = 0
df['label'] = df['first_join_pattern'].apply(lambda x: 1 if x == 'Random' else 0)

# Features and target
X = df[['cache_misses', 'time_secs']].values
y = df['label'].values

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Model
clf = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=500, random_state=1)
clf.fit(X_train, y_train)

# Save model
joblib.dump(clf, 'access_pattern_model.pkl')

# Evaluation
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['Non-Random', 'Random']))
