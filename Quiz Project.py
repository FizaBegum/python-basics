class Question:

    def __init__(self, prompt, answer):

        self.prompt = prompt

        self.answer = answer

 

def run_quiz(questions):

    score = 0

    total_questions = len(questions)

    for question in questions:

        user_answer = input(question.prompt + " ")

        if user_answer.lower() == question.answer.lower():

            score += 1

    print("Quiz completed!")

    print("Your score:", score, "/", total_questions)

 

# Create a list of questions

questions = [

    Question("What is the capital of France?", "Paris"),

    Question("What is the largest planet in our solar system?", "Jupiter"),

    Question("Who painted the Mona Lisa?", "Leonardo da Vinci"),

    Question("Who wrote “Romeo and Juliet”?","William Shakespeare"),

    Question("Who was the first woman to win a Nobel Prize?"," Marie Curie"),

    Question("Who is known as the “Father of Modern Physics”?","Albert Einstein"),

    Question("Which continent is known as the “Dark Continent”?","Africa")

]

 

# Run the quiz

run_quiz(questions)
