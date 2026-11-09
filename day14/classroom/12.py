'''
Example 12 — Pickle Serialization and Security
'''
import pickle
from pathlib import Path

data = {
    "model": "LinearRegression",
    "features": ["age", "salary"],
    "coefficients": [0.25, 0.75]
}

path = Path("model_metadata.pkl")

with path.open("wb") as file:
    pickle.dump(
        data,
        file,
        protocol=pickle.HIGHEST_PROTOCOL
    )

# Load only files created by trusted sources.
with path.open("rb") as file:
    restored = pickle.load(file)

print(restored)
print(restored == data)