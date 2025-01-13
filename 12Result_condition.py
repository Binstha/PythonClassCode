# >90 : Exellent
# >80 and <90 : Good
# >70 and <= 80 : Satisfactory
# <=70 : Need Improvement

maths = 75
science = 80
english = 80
nepali = 90
social = a0

total = (maths + science + english + nepali + social)

total_max_marks = 500

percentage = (total / total_max_marks) * 100

print(f"Total Grade obtained = {total} \nPercentage = {percentage:.1f}%")

if percentage> 90:
    print("Excellent")

elif percentage > 80:
    print("Good")
elif percentage >70:
    print("Satisfactory")
elif percentage <=70:
    print("Need Improvement")
else:
    print("Input wrong")
    