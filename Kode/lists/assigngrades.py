#Et program som tar i mot poengsummer fra bruker separert av mellomrom 
#og returnerer karakterer basert på disse

def main():
    scores = get_scores()

    students = 0
    for score in scores:
        grade = assign_grade_to_score(score, scores)
        print(f"Student {students} score is {score} and grade is {grade}")
        students += 1

def get_scores(scores = input("Enter scores: ") ):
    scores = scores.split(" ")
    scores = [int(score) for score in scores]
    return scores

def assign_grade_to_score(score, scores):
    best_score = max(scores)
    score_requirement_for_A = best_score - 10
    score_requirement_for_B = best_score - 20
    score_requirement_for_C = best_score - 30
    score_requirement_for_D = best_score - 40

    if score >= score_requirement_for_A:
        grade = "A"
    elif score >= score_requirement_for_B:
        grade = "B"
    elif score >= score_requirement_for_C:
        grade = "C"
    elif score >= score_requirement_for_D:
        grade = "D"
    else: 
        grade = "F"

    return grade


main()