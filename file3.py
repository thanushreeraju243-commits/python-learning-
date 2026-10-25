import csv
techniques = [
    {"name": "Technique A", "description": "Description of Technique A"},]

with open("techniques.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(techniques)
    print("CSV data written to techniques.csv")