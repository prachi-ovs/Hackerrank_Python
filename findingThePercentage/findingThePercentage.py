def averageScore(student_name):
    all_scores = student_marks[student_name]
    avg_score = sum(all_scores) / len(all_scores)
    #print(round(avg_score,2))
    print("{:.2f}".format(avg_score))    #to print the score to two decimal places

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()    # * operator next to line indicates unassigned/mulitple number of variables to store the split values in
        scores = list(map(float, line))  #applies the float function to the iterable object which is line here
        student_marks[name] = scores
    query_name = input()
    averageScore(query_name)