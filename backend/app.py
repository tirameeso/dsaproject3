from fastapi import FastAPI
import pandas as pd
from collections import defaultdict

app = FastAPI()

# Load dataset
data = pd.read_csv("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")

# Create hash maps; might not need this
perfume_map = {row["perfume"]: {"brand": row["brand"], "notes": row["notes"]} for _, row in data.iterrows()}
note_map = defaultdict(list)
for _, row in data.iterrows():
    for note in row["notes"]:
        note_map[note].append(row["perfume"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Fragrance Finder API!"}

# Search perfumes by note
@app.get("/search_by_note/")
def search_by_note(note: str):
    perfumes = note_map.get(note, [])
    return {"note": note, "perfumes": perfumes}

# Sort perfumes by brand
@app.get("/sort_by_brand/")
def sort_by_brand():
    sorted_data = sorted(perfume_map.items(), key=lambda x: x[1]["brand"])
    return {"sorted_perfumes": sorted_data}


print(data["notes"].head())