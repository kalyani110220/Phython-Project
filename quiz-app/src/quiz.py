# Simple Python Quiz App

questions = [
    {
        "question": "1. What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Rome", "d) Berlin"],
        "answer": "a"
    },
    {
        "question": "2. Who wrote 'Harry Potter'?",
        "options": ["a) J.K. Rowling", "b) Charles Dickens", "c) Mark Twain", "d) Jane Austen"],
        "answer": "a"
    },
    {
        "question": "3. What is 5 + 7?",
        "options": ["a) 10", "b) 11", "c) 12", "d) 13"],
        "answer": "c"
    }
]

score = 0

print("🎉 Welcome to the Quiz Game! 🎉\n")

# Loop through each question
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    if user_answer == q["answer"]:
        print("✔ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!")
        print(f"Correct answer: {q['answer']}\n")

# Final Score
print(f"🎯 Your final score: {score}/{len(questions)}")
if score == len(questions):
    print("🏆 Excellent! Perfect score!")
elif score >= len(questions)//2:
    print("👍 Good job!")
else:
    print("📘 Keep practicing!")
