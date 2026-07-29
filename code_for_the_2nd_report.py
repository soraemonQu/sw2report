# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。
def find_top_student(students):
    max_total = 0
    best_student = ""
    for student in students:
        grades = students[student]
        total, average = summarize_student(grades)
        if total > max_total:
            max_total = total
            best_student = student
        print(f"Student: {student}, Total: {total}, Average: {average}")
    return best_student, max_total


def summarize_student(grades) -> tuple[int, float]:
    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1
    if count == 0:
        return 0, 0.0
    average = total / count
    return total, average


students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = find_top_student(students)
print(f"Best student: {top_student} with total score: {top_score}")