import csv

class Reader():
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()
        self.records = len(self.data)

    def load_data(self):
        with open(self.file_path, "r") as f:
            data = list(csv.DictReader(f))
        return data
    
    def get_column(self, key: str | None = None):
        if key is None:
            return "Please provide a key"
        try:
            line = line[key]
        except KeyError:
            return "Please provide a VALID key"
        
        new_list = []
        for line in self.data:
            try:
                line = int(line[key])
                new_list.append(line)
            except ValueError:
                try:
                    line = float(line[key])
                    new_list.append(line)
                except ValueError:
                    new_list.append(line[key])
        return new_list

    def max_item(self, list: list):
        return max(list)

    def min_item(self, list: list):
        return min(list)

    def average_val(self, list: list, n_digits: int | None = None):
        return round(sum(list)/len(list), n_digits)
    
if __name__ == "__main__":
    reader = Reader("example.csv")
    names = reader.get_column("name")
    ages = reader.get_column("age")
    print(f"Number of records {reader.records}")
    print(f"Average age: {reader.average_val(ages, 1)}")
    print(f"Youngest: {reader.min_item(ages)}")
    print(f"Oldest: {reader.max_item(ages)}")