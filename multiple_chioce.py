from question import question

question_banks = [
    "your name is?\n(a) bola\n(b) tade\n", 
    "your second name is?\n(a) laolu\n(b) wale \n "
]

questions = [
    question(question_banks[0], "a"),
    question(question_banks[1], "b")
]

def exam(questions):
    score = 0
    for question in questions:
        answer = input(questions)
        if answer == questions.answer:
            score += 1

exam(questions)

