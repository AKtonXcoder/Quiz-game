import csv
def load_quiz_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        quiz_data = list(reader)
    return quiz_data

def display_question(question):
    print(question["question"])
    print("Options:")
    print("a. " + question["optiona"])
    print("b. " + question["optionb"])
    print("c. " + question["optionc"])
    print("d. " + question["optiond"])

def collect_answer():
    while True:
        answer = input("Your answer (Enter the option number): ")
        if answer in ["a", "b", "c", "d"]:
            break
        print("Invalid input. Please enter a valid option number (a, b, c, or d).")
    return answer

def calculate_score(quiz_data, user_answers):
    score = 0
    for i in range(len(quiz_data)):
        if user_answers[i] == quiz_data[i]["correct_option"]:
            score += 1
    return score

def main():
    file_path ="D:\PY\CSV\quiz_data.csv"
    quiz_data = load_quiz_data(file_path)

    total_questions = len(quiz_data)
    user_answers = []

    for question in quiz_data:
        display_question(question)
        answer = collect_answer()
        user_answers.append(answer)

    score = calculate_score(quiz_data, user_answers)

    print("Quiz completed!")
    print("Your score:", score, "/", total_questions)

if __name__ == "__main__":
    main()

