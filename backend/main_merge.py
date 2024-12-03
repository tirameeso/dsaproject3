# the main file we'll be using for merge sort
from backend import load_csv_file
from mergesort import mergeSort

'''
file_path = "maxai-excel-to-csv-converted.csv"
dataSet = load_csv_file(file_path)
mergeSort(dataSet, 1)

def searchEng(frag, notes):
    fragList = []
    for i in frag:
        if notes.lower() in [j.lower() for j in i[2]]:
            fragList.append(i)
    return fragList

searchInput = input("Please enter a note to find a fragrance!").strip()
searchResults = searchEng(dataSet, searchInput)

if searchResults:
    print(f"Fragrance(s) featuring notes of '{searchInput}':")
    for s in searchResults:
        print(f"Brand: {s[0]}, Fragrance: {s[1]}, All Notes: {','.join(searchResults[2])}")
    else:
        print(f"There are no perfumes found featuring this note.") '''