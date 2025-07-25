# mini project on Quiz App (List of Questions + Answers)

questions = [
    ["What is the capital of Nepal?", "kathmandu"],
    ["What is 5 + 7?", "12"],
    ["Python is ___ language?", "interpreted"]
]

score = 0
for q in questions:
    ans = input(q[0] + " ")
    if ans.lower() == q[1].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! Correct answer: {q[1]}\n")

print(f"🎯 Your score: {score}/{len(questions)}")
