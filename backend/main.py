from mergesort import mergeSort
from hashtable import *
import pandas as pd
import time

def load_csv_file(file_path):
    data = pd.read_csv("maxai-excel-to-csv-converted.csv")
    # dropping data that doesn't have value (3 perfume names not included)
    data.dropna(subset=["perfume"], inplace=True)
    data["notes"] = data["notes"].str.split(", ")
    perfume_data = data[["brand", "perfume", "notes"]].values.tolist()
    data["notes"] = data["notes"].str.split(", ")
    # for testing whether notes are split up accurately
    return perfume_data

def searchEng(frag, notes):
    matchingPerfumes = []
    for f in frag:
        perfumeNotes = [n.lower() for n in f[2]]
        if all(note in perfumeNotes for note in notes):
            matchingPerfumes.append(f)
    return matchingPerfumes


def main():
    # Load dataset
    dataSet = load_csv_file("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")
    dataCopy = dataSet.copy()
    running = True

    print("========================================================")
    print("⊹₊ ˚‧︵‿₊୨ Welcome to Fragrance Note Finder ୧₊‿︵‧ ˚ ₊⊹")
    print("========================================================")
    
    while running:
        print("\n┌─────────── ⋆⋅☆⋅⋆ ───────────┐")
        print("  Menu:")
        print("  1. Search for desired notes")
        print("  2. Exit")
        print("└─────────── ⋆⋅☆⋅⋆ ───────────┘")
        initialInput = input("Please enter an option from the menu above! (1 or 2):\n")

        if initialInput == "1":
                DSAoptionInput = input("Do you want to use a hash table or merge sort to sort the data for this query? Enter 'h' or 'm'.\n" )
                
                if DSAoptionInput == "m":
                    # begin recording time
                    startTimeMerge = time.perf_counter_ns()
                    mergeSort(dataCopy, 1)
                    endTimeMerge = time.perf_counter_ns()

                    # prompt for user input (notes)
                    searchInput = input("Please enter desired notes to find a fragrance (comma-separated): ")
                    # put the user input into list
                    searchNotes = [note.strip().lower() for note in searchInput.split(',')]

                    # call search engine function
                    matchingPerfumes = searchEng(dataCopy, searchNotes)

                    # edge cases: no notes entered OR note entered DNE
                    # if triggered, reprompt menu (restart while loop)
                    if not searchNotes:
                        print("Error: No notes entered. Please enter at least one note.")
                        continue

                    if not matchingPerfumes:
                        print(f"No fragrances found matching ALL notes ({', '.join(searchNotes)}).")
                        continue

                    # display results
                    print(f"\n{len(matchingPerfumes)} Fragrances Found matching ALL notes ({', '.join(searchNotes)}):")
                    for fragrances in matchingPerfumes:
                        print(f"{fragrances[1]} by {fragrances[0]} with notes of: {', '.join(fragrances[2])}")

                    # compute time it took for the merge sort to sort data
                    totalTimeMerge = endTimeMerge - startTimeMerge
                    print(f"Merge sort completed in {totalTimeMerge:.6f} seconds.")

                elif DSAoptionInput ==  "h":
                    # create and populate the hash table
                    startTimeHash = time.perf_counter_ns()
                    table_size = 100
                    hash_table = HashTable(table_size)

                    for brand, perfume, notes in dataCopy:
                        hash_table.insert(perfume, (brand, perfume, notes))

                    endTimeHash = time.perf_counter_ns()
                    searchInput = input("Please enter desired notes to find a fragrance (comma-separated): ")
                    searchNotes = [note.strip().lower() for note in searchInput.split(',')]

                    # Get matching perfumes
                    matchingPerfumes = searchEng(dataCopy, searchNotes)

                    if not searchNotes:
                        print("Error: No notes entered. Please enter at least one note.")
                        continue

                    if not matchingPerfumes:
                        print(f"No fragrances found matching ALL notes ({', '.join(searchNotes)}).")
                        continue

                    # prints out results
                    print(
                        f"\n{len(matchingPerfumes)} Fragrances Found matching ALL notes ({', '.join(searchNotes)}):")
                    for fragrances in matchingPerfumes:
                        print(f"{fragrances[1]} by {fragrances[0]} with notes of: {', '.join(fragrances[2])}")

                    # compute time it took; come to this in a second
                    totalTimeHash = endTimeHash - startTimeHash
                    print(f"Hash table completed in {totalTimeHash:.6f} nanoseconds.")

                else:
                    print("Not a valid input. Please start over.")
                    continue
                
        elif initialInput == "2":
            print("Thank you for using Fragrance Note Finder! Goodbye.")
            running = False
            break

if __name__ == "__main__":
    main()