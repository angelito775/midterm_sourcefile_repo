scores = [90, 89, 78, 99, 81]

print("Student scores:")

for x in scores:
    print(x)

print()

passed= 0
failed = 0

total_score = sum(scores)
avg_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

for index in range(len(scores)):
    x = scores[index]

    if x >= 75:
        if x >= 90:
            remark = "Excellent"
        elif x >= 80:
            remark = "Very Good"
        else:
            remark = "Good"

        print(f"Student {index + 1}: {x} - {remark} - Passed")
        passed += 1
    else:
        print(f"Student {index + 1}: {x} - Failed")
        failed += 1

print()

print(f"Total Score: {total_score}")
print(f"Average Score: {avg_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")