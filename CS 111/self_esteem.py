#my working code
questions = ["I feel that I am a person of worth, at least on an equal plane with others. ",
             "I feel that I have a number of good qualities. ",
             "All in all, I am inclined to feel that I am a failure. ",
             "I am able to do things as well as most other people. ",
             "I feel I do not have much to be proud of. ",
             "I take a positive attitude toward myself. ",
             "On the whole, I am satisfied with myself. ",
             "I wish I could have more respect for myself. ",
             "I certainly feel useless at times. ",
             "At times I think I am no good at all. "]

def get_str_input(prompt):
    user_input=""
    while True:
        user_input = input(prompt + "\n").strip().lower()
        if user_input in ('a','b','c','d'):
            return user_input
        else:
            print("please input A,B,C, or D")

def score_answer(answer, which_q):
    score = 0
    if which_q in (0,1,3,5,6):
        if answer == 'a':
            score = 3
        elif answer == 'b':
            score = 2
        elif answer == 'c':
            score = 1
        return score
    elif which_q in (2,4,7,8,9):
        if answer == 'd':
            score = 3
        elif answer == 'c':
            score = 2
        elif answer == 'b':
            score = 1
    return score

def get_total_score ():
    total_score = 0
    for i in range(len(questions)):
        question = questions[i]
        answer = get_str_input(question)
        individual_score = score_answer(answer, i)
        total_score = total_score + individual_score
    return total_score

def main():
    print("This program is an implementation of the Rosenberg " \
        "Self-Esteem Scale. This program will show you ten" \
        " statements that you could possibly apply to yourself." \
        " Please rate how much you agree with each of the" \
        " statements by responding with one of these four letters: " \
        "\nA means you strongly agree with the statement" \
        "\nB means you agree with the statement" \
        "\nC means you disagree with the statement" \
        "\nD means you strongly disagree with the statement")
    
    user_score = get_total_score()

    print(f"\nYour score is {user_score}")
    print("A score below 15 may indicate problematic low self-esteem.")
    
main()
    