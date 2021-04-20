from Question import Question
question_prompts=[
    "What color are apple?\n(a) red\n(b) purple\n(c) orange\n\n",
    "What color are banana?\n(a) red\n(b) purple\n(c) yellow\n\n",
    "What color are strawberries?\n(a) red\n(b) magenta\n(c) orange\n\n"
]

questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
         score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
