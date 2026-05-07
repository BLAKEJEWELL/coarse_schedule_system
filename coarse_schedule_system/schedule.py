import csv
from schedule_item import Schedule_Item

class Schedule:
    def __init__(self):
        self.inputs = {}

    def print_header(self):
        print(
            f"{'subject':<8}"
            f"{'Catalog':<10}"
            f"{'Section':<10}"
            f"{'Component':<11}"
            f"{'Session':<10}"
            f"{'Units':<7}"
            f"{'TotEnrl':<10}"
            f"{'CapEnrl':<10}"
            f"{'Instructor':<8}"
            
            )

    def print(self):
        self.print_header()
        for item in self.inputs.values():
            item.print()

    def add_entry(self, item):
        self.inputs[item.get_key()] = item

    def import_from_csv(self, filename):
        with open(filename, encoding = "utf-8-sig", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                item = Schedule_Item(
                    subject = row["Subject"],
                    catalog = row["Catalog"],
                    section = row["Section"],
                    component = row["Component"],
                    session = row["Session"],
                    units = int(row["Units"]),
                    totenrl = int(row["TotEnrl"]),
                    capenrl= int(row["CapEnrl"]),
                    instructor = row["Instructor"]
                    )
                self.add_entry(item)

    def find_by_subject(self, subject):
        return [
            item
            for item in self.inputs.values()
            if item.subject.upper() == subject.upper()
            ]
    def find_by_subject_catalog(self, subject, catalog):
        return[
            item
            for item in self.inputs.values()
            if item.subject.upper() ==subject.upper()
            and item.catalog == catalog
            ]
    def find_by_instructor_last_name(self, name):
        return[
            item
            for item in self.inputs.values()
            if item.instructor.split(",")[0].upper() == name.upper()
            ]
                





