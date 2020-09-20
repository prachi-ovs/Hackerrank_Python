def studentsWithSecondLargestScore(student_records):
    all_scores = student_records.values()
    second_lowest_score = sorted(list(set(all_scores)))[1]
    student_names = [n for n, s in records.items() if s == second_lowest_score]
    student_names.sort()
    for name in student_names:
        print(name)

if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
    #print(records)

    studentsWithSecondLargestScore(records)
