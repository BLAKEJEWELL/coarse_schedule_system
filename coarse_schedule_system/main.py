from schedule import Schedule



def main():
    filename = "STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv"
    schedule = Schedule()
    schedule.import_from_csv(filename)
    
    while True:
        print("\nCourse Schedule System Menu")
        print("1. Display all")
        print("Search by subject")
        print("Search by subject/catalog")
        print("Search by instuctor")
        print("Quit")

        choice = input("\nEnter choice:")

        if choice == "1":
            schedule.print()
