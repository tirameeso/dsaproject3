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

# Importing necessary modules
from dataTest import load_csv_file
from mergesort import mergeSort


def searchEng(frag, notes):
    """
    Search for perfumes that match ALL the given notes.

    Args:
    frag (list): The list of all perfumes.
    notes (list): The list of notes to search for.

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

    # Sort the dataset by the second column (index 1)
    mergeSort(dataCopy, 1)

    # Get search input
    searchInput = input("Please enter desired notes to find a fragrance (comma-separated): ")
    searchNotes = [note.strip().lower() for note in searchInput.split(',')]

    # Get matching perfumes
    matchingPerfumes = searchEng(dataCopy, searchNotes)

    # Display results
    print(f"\n{len(matchingPerfumes)} Fragrances Found matching ALL notes ({', '.join(searchNotes)}):")
    for fragrances in matchingPerfumes:
        print(f"{fragrances[1]} by {fragrances[0]} with Notes: {', '.join(fragrances[2])}")


if __name__ == "__main__":
    main()

