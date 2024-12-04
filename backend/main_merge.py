# the main file we'll be using for merge sort
from dataTest import load_csv_file
from mergesort import mergeSort

def searchEng(frag, notes):
    fragList = []
    for f in frag:
        found = False
        for n in f[2]:
            for note in notes:

                if note in n.lower():
                   found = True
                   break

            if found:
               fragList.append(f)
               break

    return fragList

def main():
    dataSet = load_csv_file("maxai-excel-to-csv-converted.csv")

    dataCopy = dataSet.copy()
    mergeSort(dataCopy, 1)

    searchInput = input("Please enter desired notes to find a fragrance:")
    searchNotes = [note.strip().lower() for note in searchInput.split(',')]
    searchResults = searchEng(dataCopy, searchNotes)

    print(f"{len(searchResults)} Fragrances Found:")
    for fragrances in searchResults:
        print(f"{fragrances[1]} by {fragrances[0]} with Notes: {', '.join(fragrances[2])}")


if __name__ == "__main__":
    main()

