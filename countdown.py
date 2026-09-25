import time
n = int(input("Enter the number of seconds for the countdown: "))
while n > 0:
    print(f"Time remaining: {n} seconds")
    time.sleep(1)
    n -= 1
print("Countdown finished!")