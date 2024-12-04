from mergesort import mergeSort
from hashtable import *
import pandas as pd
import time

def load_csv_file(file_path):
    data = pd.read_csv("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")
    # dropping data that doesn't have value (3 perfume names not included)
    data.dropna(subset=["perfume"], inplace=True)
    data["notes"] = data["notes"].str.split(", ")
    perfume_data = data[["brand", "perfume", "notes"]].values.tolist()
    data["notes"] = data["notes"].str.split(", ")
    # for testing whether notes are split up accurately
    return perfume_data

def searchEng(frag, notes):
    """
    Search for perfumes that match ALL the given notes.

    Args:
    frag (list): list of all perfumes
    notes (list): list of notes to search for

    Returns:
    list: A list of perfumes that match all the notes.
    """
    matchingPerfumes = []
    for f in frag:
        perfumeNotes = [n.lower() for n in f[2]]  # Convert notes to lowercase
        # Check if all search notes are in the perfume's notes
        if all(note in perfumeNotes for note in notes):
            matchingPerfumes.append(f)
    return matchingPerfumes


def main():
    # Load dataset
    dataSet = load_csv_file("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")
    dataCopy = dataSet.copy()
    running = True
    initialInput = input("Welcome to Fragrance Note Finder! Please enter 'c' to continue or 'x' to exit the program.")
    while True:
        if initialInput == "c":
                DSAoptionInput = input("Do you want to use a hash table or merge sort to sort the data for this query? Enter 'h' or 'm'.")
                if DSAoptionInput == "m":
                    # Sort the dataset by the second column (index 1)
                    startTime = time.time()
                    mergeSort(dataCopy, 1)
                    endTime = time.time()

                    # Get search input
                    searchInput = input("Please enter desired notes to find a fragrance (comma-separated): ")
                    searchNotes = [note.strip().lower() for note in searchInput.split(',')]

                    # Get matching perfumes
                    matchingPerfumes = searchEng(dataCopy, searchNotes)

                    if not searchNotes:
                        print("Error: No notes entered. Please enter at least one note.")
                        return

                    if not matchingPerfumes:
                        print(f"No fragrances found matching ALL notes ({', '.join(searchNotes)}).")

                    # Display results
                    print(f"\n{len(matchingPerfumes)} Fragrances Found matching ALL notes ({', '.join(searchNotes)}):")
                    for fragrances in matchingPerfumes:
                        print(f"{fragrances[1]} by {fragrances[0]} with notes of: {', '.join(fragrances[2])}")

                    # compute time it took
                    totalTime = endTime - startTime
                    print(f"Merge sort completed in {totalTime:.6f} seconds.")
                elif DSAoptionInput ==  "h":
                    # implementation for hash table search
                    print("work in progress")
                else:
                    print("Not a valid input. Please start over.")
                    continue
        elif initialInput == "x":
            print("Thank you for using Fragrance Note Finder! Goodbye.")
            running = False
            break

if __name__ == "__main__":
    main()

