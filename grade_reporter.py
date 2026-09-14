# Grade Reporter - Week 3 Assignment

scores = [72, 45, 90, 61, 38]

pass_count = 0
fail_count = 0
total_sum = 0

for s in scores:
    if s >= 80:
        result = "A"
    elif s >= 70:
        result = "B"
    elif s >= 50:
        result = "C"
    else:
        result = "F"

    print(f"{s} -> {result}")

    if s >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

    total_sum = total_sum + s

avg = total_sum / len(scores)
print("Passed:", pass_count)
print("Failed:", fail_count)
print("Average:", round(avg, 1))