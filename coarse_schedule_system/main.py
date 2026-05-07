from schedule import Schedule



def main():
    filename = "STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv"
    schedule = Schedule()
    schedule.import_from_csv(filename)
    