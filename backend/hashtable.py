# using a generator function that will load the perfume data one at a time so it won't load into memory at once
def load_perfumes_data(whatever_files_path_we_choose):
    # r allows it to open in read mode only and the with will allow it to close once all the data is processed
    with open(whatever_files_path_we_choose, "r", encoding = "utf-8") as file:
        # if there is a header, this next line of code will skip it and omit it from the data, IF NO HEADER IS PRESENT, delete the following line of code
        next(file)
        for line in file:
            # parse each line into a perfume object
            perfume = parse_perfume_line(line)
            if perfume:
                yield perfume
            else:
                continue # will skip lines that cannot be parsed

# parsing each line of code, assuming we are using a CSV file (which we are):
def parse_perfume_line(line):
    import csv
    from collections import namedtuple

    perfumeRecord = namedtuple("PerfumeRecord", ["name", "brand", "notes"])

    # using CSV reader to handle any commas within the fields (adjust as needed)
    # this will help adjust indicies based on our CVS structure
    # these will retireieve the list of fields from the parsed line and read the data
    # strip function will remove any trailing or leading whitespace
    reader = csv.reader([line])
    try:
        fields = next(reader)
        name = fields[0].strip()
        brand = fields[1].strip()
        notes_field = fields[2].strip()

        # since notes are within quotes and seperated by commas, we just need to split the notes field into a list
        notes = [note.strip() for note in notes_field.split(",")]

        return perfumeRecord(name=name, brand=brand, notes=notes)
    except (IndexError, ValueError) as e:
        print("Error parsing line: {e}")
        return None


class HashTable:
    def __init__(self, size = 131071):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
            
        return None
    
class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add(self, note, perfume):
        note = note.lower()
        if note in self.index:
            self.index[note].append(perfume)
        else:
            self.index[note] = [perfume]

    def get(self, note):
        return self.index.get(note.lower(), [])
    
def build_data_structures(file_path):
    perfume_table = HashTable()
    inverted_index = InvertedIndex()
    perfume_generator = load_perfumes_data(file_path)

    for perfume in perfume_generator:
        key = perfume.name.lower()
        perfume_table.insert(key, perfume)

        for note in perfume.notes:
            inverted_index.add(note, perfume)

    return perfume_table, inverted_index