def ask_question():
    user_question = input("What is your question?")
    return user_question

from random import randrange

def answer():
    answer_list = ["It is certain", "It is decidedly so", "Without a doubt",
    "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely",
    "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
    "Ask again later", "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it", "My reply is no",
    "My sources say no", "Outlook not so good", "Very doubtful"]
    choose_num = randrange(19)
    return answer_list[choose_num]

def check_question(user_q):
    if user_q[-1] == "?":
        return True
    else:
        print ("I'm sorry, I can only answer questions.")
        return False


magic_eight_ques = ask_question()
while (magic_eight_ques != "quit"):
    if (check_question(magic_eight_ques) == True):
        print (answer())
    magic_eight_ques = ask_question()
