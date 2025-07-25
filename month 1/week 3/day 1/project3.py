#mini project on Simple Quiz Gam
score = 0
questions = {
    "Capital of Nepal?": "kathmandu",
    "2 + 2 = ?": "4",
    "Python's creator?": "guido"
}

for q, a in questions.items():
    user = input(q + " ").lower()
    if user == a:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")

print(f"Your score: {score}/{len(questions)}")
