grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = list(students)
students_sort.sort()  # Нашел метод в интернете, так как сортировку вы не объясняли (циклы тоже нельзя)

res_students_grades = {}

# print(students_sort)
#
# sum_grades = sum(grades[0])
# count_grades = len(grades[0])
#
# print(sum_grades)
# print(count_grades)
# print(sum_grades / count_grades)

res_students_grades[students_sort[0]] = sum(grades[0]) / len(grades[0])
res_students_grades[students_sort[1]] = sum(grades[1]) / len(grades[1])
res_students_grades[students_sort[2]] = sum(grades[2]) / len(grades[2])
res_students_grades[students_sort[3]] = sum(grades[3]) / len(grades[3])
res_students_grades[students_sort[4]] = sum(grades[4]) / len(grades[4])


print(res_students_grades)