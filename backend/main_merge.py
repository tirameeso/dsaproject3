# # the main file we'll be using for merge sort
# from dataTest import load_csv_file
# from mergesort import mergeSort
#
# def searchEng(frag, notes):
#     # list to hold all perfumes that have ALL notes in common
#     allNotes = []
#     #dictionary to hold individual fragrances
#     noteResults = {note: [] for note in notes}
#     for f in frag:
#         # crating a set for all matching notes
#         matchingNotes = set()
#         # boolean to keep track of no perfume matching all notes (edge case)
#         found = False
#         for n in f[2]:
#             for note in notes:
#                 if note in n.lower():
#                    found = True
#                    matchingNotes.add(note)
#         for matchedNote in matchingNotes:
#             noteResults[matchedNote].append(f)
#
#         if found:
#             allNotes.append(f)
#
#     return allNotes, noteResults
#
# def main():
#     dataSet = load_csv_file("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")
#     dataCopy = dataSet.copy()
#     mergeSort(dataCopy, 1)
#
#     searchInput = input("Please enter desired notes to find a fragrance:")
#     searchNotes = [note.strip().lower() for note in searchInput.split(',')]
#     allNotes, noteResults = searchEng(dataCopy, searchInput)
#     print(f"\n{len(allNotes)} Fragrances Found with ALL notes:")
#     for fragrances in allNotes:
#          # Flatten notes before joining
#          flattened_notes = [item for sublist in fragrances[2] for item in
#                             (sublist if isinstance(sublist, list) else [sublist])]
#          print(f"{fragrances[1]} by {fragrances[0]} with notes of {', '.join(flattened_notes)}")
#
#     #Print perfumes matching individual notes
#     for note, perfumes in noteResults.items():
#         print(f"\n{len(perfumes)} Fragrances Found with the note '{note}':")
#         for fragrances in perfumes:
#             # Flatten notes before joining
#             flattened_notes = [item for sublist in fragrances[2] for item in
#                                (sublist if isinstance(sublist, list) else [sublist])]
#             print(f"{fragrances[1]} by {fragrances[0]} with Notes: {', '.join(flattened_notes)}")
#
#     print(f"{len(searchResults)} Fragrances Found:")
#     for fragrances in searchResults:
#         print(f"{fragrances[1]} by {fragrances[0]} with Notes: {', '.join(fragrances[2])}")
#
# # damn I forgot about this shit -angie
# if __name__ == "__main__":
#     main()
#
# the main file we'll be using for merge sort
from dataTest import load_csv_file
from mergesort import mergeSort

def searchEng(frag, notes):
    # List to hold all perfumes that match ALL notes
    allNotes = []

    # Dictionary to hold fragrances for individual notes
    noteResults = {note: [] for note in notes}

    for f in frag:
        # Track which notes this fragrance matches
        matchingNotes = set()

        for n in f[2]:  # Iterate over the fragrance's notes
            for note in notes:
                if note in n.lower():
                    matchingNotes.add(note)

        # If the fragrance matches all notes, add it to `allNotes`
        if len(matchingNotes) == len(notes):
            allNotes.append(f)

        # Add the fragrance to the dictionary for each matched note
        for matchedNote in matchingNotes:
            noteResults[matchedNote].append(f)

    return allNotes, noteResults

def main():
    # Load dataset
    dataSet = load_csv_file("/Users/angielaptop/PycharmProjects/dsaproject3/maxai-excel-to-csv-converted.csv")
    dataCopy = dataSet.copy()

    # Sort the dataset by the second column (index 1)
    mergeSort(dataCopy, 1)

    # Get search input
    searchInput = input("Please enter desired notes to find a fragrance (comma-separated): ")
    searchNotes = [note.strip().lower() for note in searchInput.split(',')]

    # Search for fragrances matching the notes
    allNotes, noteResults = searchEng(dataCopy, searchNotes)

    # Print perfumes matching ALL notes
    print(f"\n{len(allNotes)} Fragrances Found with ALL notes:")
    for fragrances in allNotes:
        flattened_notes = [item for sublist in fragrances[2] for item in (sublist if isinstance(sublist, list) else [sublist])]
        print(f"{fragrances[1]} by {fragrances[0]} with Notes: {', '.join(flattened_notes)}")

    # Print perfumes matching individual notes
    for note, perfumes in noteResults.items():
        print(f"\n{len(perfumes)} Fragrances Found with the note '{note}':")
        for fragrances in perfumes:
            flattened_notes = [item for sublist in fragrances[2] for item in (sublist if isinstance(sublist, list) else [sublist])]
            print(f"{fragrances[1]} by {fragrances[0]} with Notes: {', '.join(flattened_notes)}")

if __name__ == "__main__":
    main()
