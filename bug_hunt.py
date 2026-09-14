count = 1
total = 0

# BUG: The condition was < 5, so the loop stopped at 4 and never added 5. Changed to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer and cannot be concatenated to a string. Used str(total) to convert it.
print("Sum of 1 to 5 is: " + str(total))