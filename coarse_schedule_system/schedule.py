import csv
from operator import itemgetter
from schedule_item import Schedule_Item

class Schedule:
    def __init__(self):
        self.inputs = {}

    def print_h(self):
        print(
            f"{'subject':<8}"
            f"{'Catalog':<8}"
            f"{'Section':<8}"
            f"{'Component':<8}"
            f"{'Session':<8}"
            f"{'Units':<8}"
            f"{'TotEnrl':<8}"
            f"{'CapEnrl':<8}"
            f"{'Instructor':<8}"
            
            )

    def print_e(self):
        self.print_h()
        for item in self.entries.values():
            item.print()

    def add_entries(self, item):
        self.entries[item.get_key()] = item

    def import_from_csv(self, filename):
        with open(filename, encoding = "utf-8-sig", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                item = Schedule_Item(
                    subject = row["Subject"],
                    catalog = row["Catalog"],
                    section = row["Section"],
                    component = row["Compnonent"],
                    session = row["Session"],
                    units = row["Units"],
                    totenrl = row["TotEnrl"],
                    capenrl= ["CapEnrl"],
                    instructor = row["Instructor"]
                    )
                self.add_enetries(item)

    def find_subject(self, subject):
        return [
            item
            for item in self.entries.values()
            if self.item.subject.upper() == subject.upper()
            find_subject function to schedule.py
            ]
                





