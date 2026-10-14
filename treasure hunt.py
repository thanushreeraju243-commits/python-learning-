def hunt(round1, round2):
    total_points = sum(round1) + sum(round2)
    return total_points
print(hunt([10, 20, 30], [5, 15, 25])) 
num = int(input("Enter the number of points for round 1: ")) # Example usage
if hunt([10, 20, 30], [5, 15, 25]) >= 100:
    print("Congratulations! You have won the treasure hunt.")
elif hunt([10, 20, 30], [5, 15, 25]) >= 50:
    print("Good job! You have completed the treasure hunt.")
else:
    print("Keep trying! You can do better in the treasure hunt.")
print("round 1 completed.")
print("round 2 started.")
num2 = int(input("Enter the number of points for round 2: ")) # Example usage
if hunt([8, 12, 15], [10, 20, 30]) >= 100:
    print("Congratulations! You have won the treasure hunt.")
elif hunt([8, 12, 15], [10, 20, 30]) >= 50:
    print("Good job! You have completed the treasure hunt.")
else:
    print("Keep trying! You can do better in the treasure hunt.")
print("round 2 completed.")

