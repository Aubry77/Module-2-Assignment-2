"""_summary_list transformation task 1
"""

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the list in descending order
grades.sort(reverse=True)

# Print the sorted list
print("Sorted grades:", grades)

# task 2 cal avg grade

average_grade = sum(grades) / len(grades)
print("average grade:",average_grade)
