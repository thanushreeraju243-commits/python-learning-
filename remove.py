numbers = [1, 2, 3, 4, 5]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print(unique_numbers)