import csv
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

    def import_from_csv(self, filename):
        with open(filename, encoding = "utf-8-sig", newline = "") as csvfile:




#call get_key
