grades = [
    [85, 90, 78],   
    [92, 88, 82],   
    [75, 80, 85]    
]

for row in grades:
    for grade in row:
        print(grade, end=' ' )
    print()

print(grades[2][1])  

update_grade[0][3] = 555
