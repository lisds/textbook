""" Make one random sample from Havana mathematics results.
"""
from pathlib import Path

import numpy as np
import pandas as pd

data_dir = Path(__file__).parent
df = pd.read_csv(data_dir / 'havana_math_2019.csv').dropna()

# We need the result to be more or less 58.74 to match the text.
seed = 100
while True:
    rng = np.random.default_rng(seed)
    sample = df.sample(50, replace=False, random_state=rng)
    mean = sample['mark'].mean()
    if np.round(mean, 2) == 58.74:
        break
    seed += 1

print('Seed', seed)
print('Mean', mean)

sample.to_csv(data_dir / 'havana_math_2019_sample.csv', index=None)
