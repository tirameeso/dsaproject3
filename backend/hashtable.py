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