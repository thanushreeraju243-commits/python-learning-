txt_data = "i love my k"
file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"Data written to {file_path}")
    