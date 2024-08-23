def get_questions():
    questions = [
        {
            "question": "Which language is known as the 'Language of the Web'?",
            "options": ["Java", "Python", "JavaScript", "C#"],
            "answer": "JavaScript"
        },
        {
            "question": "What year was Python first released?",
            "options": ["1991", "1989", "2000", "1995"],
            "answer": "1991"
        },
        {
            "question": "Who developed the C programming language?",
            "options": ["Bjarne Stroustrup", "Dennis Ritchie", "James Gosling", "Guido van Rossum"],
            "answer": "Dennis Ritchie"
        }
    ]
    return questions
def ask_question(question_data):
    print("\n" + question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    
    try:
        user_choice = int(input("Your answer (choose the number): "))
        while user_choice < 1 or user_choice > len(question_data["options"]):
            user_choice = int(input("Invalid choice. Please choose a valid number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return False
    
    correct_answer = question_data["answer"]
    if question_data["options"][user_choice - 1] == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")
        return False
def run_quiz():
    questions = get_questions()
    score = 0
    
    print("Welcome to the Quiz Game!")
    
    for question_data in questions:
        if ask_question(question_data):
            score += 1
    
    print(f"\nYour final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    run_quiz()

