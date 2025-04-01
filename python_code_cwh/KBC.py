# Define questions with options and the correct answer
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Chennai", "D) Kolkata"],
        "answer": "B"
    },
    {
        "question": "Who is the CEO of Tesla?",
        "options": ["A) Jeff Bezos", "B) Bill Gates", "C) Elon Musk", "D) Mark Zuckerberg"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "Which language is known as the mother of programming languages?",
        "options": ["A) C", "B) Assembly", "C) Python", "D) Fortran"],
        "answer": "D"
    },
    {
        "question": "What is 10 + 20?",
        "options": ["A) 20", "B) 30", "C) 40", "D) 50"],
        "answer": "B"
    }
]

# Function to ask questions
def ask_questions(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        # Get the user's answer
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        
        # Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.")
    
    # Print final score
    print(f"\nYour final score is {score} out of {len(questions)}.")

# Run the quiz
ask_questions(questions)
