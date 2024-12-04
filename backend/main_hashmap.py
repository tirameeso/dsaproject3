from hashtable import HashTable, InvertedIndex, build_data_structures
import pandas as pd
def load_csv_file(file_path):
    data = pd.read_csv("maxai-excel-to-csv-converted.csv")
    data.dropna(subset=["perfume"], inplace=True)
    data["notes"] = data["notes"].str.split(",")
    perfume_data = data[["brand", "perfume", "notes"]].values.tolist()
    return perfume_data

def searchEng(hash_table, notes):
    """
    Search for perfumes that match ALL the given notes in the hash table.

    Args:
    hash_table (HashTable): The hash table containing perfumes.
    notes (list): The list of notes to search for.

    Returns:
    list: A list of perfumes that match all the notes.
    """
    if not notes:
        print("Error: No notes provided for search.")
        return []

    matchingPerfumes = []

    for bucket in hash_table.table:
        if bucket:
            for _, value in bucket:
                brand, perfume, perfume_notes = value
                # Convert notes to lowercase for case-insensitive comparison
                perfume_notes_lower = [note.lower() for note in perfume_notes]
                if all(note in perfume_notes_lower for note in notes):
                    matchingPerfumes.append((brand, perfume, perfume_notes))

    return matchingPerfumes

def main():
    # load dataset
    #file_path = "maxai-excel-to-csv-converted.csv"
    perfume_data = load_csv_file("maxai-excel-to-csv-converted.csv")

    # create and populate the hash table
    table_size = 100  # Adjust size as needed
    hash_table = HashTable(table_size)
    for brand, perfume, notes in perfume_data:
        hash_table.insert(perfume, (brand, perfume, notes))

    # get search input
    search_input = input("Please enter desired notes to find a fragrance (comma-separated): ")
    search_notes = [note.strip().lower() for note in search_input.split(',')]

    if not search_notes:
        print("Error: No notes entered. Please enter at least one note.")
        return

    # search for matching perfumes
    matching_perfumes = searchEng(hash_table, search_notes)

    # display results
    if not matching_perfumes:
        print(f"No fragrances found matching ALL notes ({', '.join(search_notes)}).")
    else:
        print(f"\n{len(matching_perfumes)} Fragrances Found matching ALL notes ({', '.join(search_notes)}):")
        for brand, perfume, notes in matching_perfumes:
            print(f"{perfume} by {brand} with notes of: {', '.join(notes)}")

if __name__ == "__main__":
    main()

        # Example Usage: Add your snippet here
    file_path = "maxai-excel-to-csv-converted.csv"
    perfume_table, inverted_index = build_data_structures(file_path)

    # Retrieve a perfume by name
    perfume_name = "Chanel No.5".lower()
    perfume = perfume_table.get(perfume_name)
    if perfume:
        print(f"Perfume Found: {perfume}")
    else:
        print(f"Perfume '{perfume_name}' not found.")

    # Search for perfumes by a note
    note = "jasmine"
    perfumes_with_note = inverted_index.get(note)
    if perfumes_with_note:
        print(f"\nPerfumes with note '{note}':")
        for p in perfumes_with_note:
            print(f"{p.name} by {p.brand} - Notes: {', '.join(p.notes)}")
    else:
        print(f"No perfumes found with note '{note}'.")