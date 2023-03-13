import random

# Generate a random phone number and answer the call.
caller_id = random.randint(1000000000, 9999999999)
print("Incoming call from:", caller_id)

# If the call is urgent, tell the user to press 0.
is_urgent = input("Is this an urgent call? (y/n): ")
if is_urgent == "y":
    answer = input("Press 0 to answer the call: ")
else:
    answer = input("Press any key to ignore the call: ")

# Check the user-entered response.
if answer == "0":
    print("Connecting you to the caller.")
else:
    print("Call ignored.")
