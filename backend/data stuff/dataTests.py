import pandas as pd

from faker import Faker
import random

faker = Faker()
new_data = []

# Generate 100 random fragrances
for _ in range(17,000):
    new_data.append({
        'name': faker.word().capitalize(),
        'notes': ', '.join(faker.words(3)),
        'rating': round(random.uniform(1, 5), 1),
    })

# Convert to DataFrame and save
new_df = pd.DataFrame(new_data)
new_df.to_csv('synthetic_fragrances.csv', index=False)
