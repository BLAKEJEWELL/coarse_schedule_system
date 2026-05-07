from schedule import Schedule

def print_results(results):
    if not results:
        print("\nNo matching results.\n")
        return

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
    for item in results:
        item.print()

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
        elif choice == "2":
            subject = input("Enter subject")
            results = schedule.find_subject(subject)
        elif choice == "3":
            subject = input("Enter subject")
            catalog = input("Enter catalog #")
            results = schedule.find_subject_catalog(subject, catalog)
            print_results(results)
