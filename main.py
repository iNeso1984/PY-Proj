from fastapi import FastAPI
from typing import Optional
import random

app = FastAPI()

# define a list of interesting and engaging questions for veterans
questions = [
    "What was your most memorable experience during your time in the military?",
    "What is one thing you learned in the military that you still apply to your everyday life?",
    "What was the biggest challenge you faced while serving, and how did you overcome it?",
    "What was your favorite duty station or deployment location?",
    "What advice would you give to someone who is about to join the military?",
    "How did serving in the military change your perspective on life?",
    "What is the funniest memory you have from your time in the military?",
    "What was your favorite thing about being in the military?",
    "What was the most valuable lesson you learned during your time in the military?",
    "What was your biggest accomplishment during your time in the military?",
    "What was the most difficult decision you had to make during your service, and how did you make it?",
    "How did you stay motivated during challenging times in the military?",
    "What did you miss the most about home while you were deployed?",
    "What was the most meaningful interaction you had with a fellow service member or veteran?",
    "What was the most important skill you learned while serving, and how has it helped you in your civilian life?",
    "Who is your favorite fictional character, and why?",
    "If you could be any fictional character for a day, who would you be and why?",
    "Which fictional character do you think you relate to the most, and why?",
    "Which fictional world would you most like to visit, and why?",
    "If you could have a superpower, which one would you choose, and why?",
    "Who is your favorite Marvel character, and why?",
    "If you could be any Marvel character for a day, who would you be and why?",
    "What is your favorite Marvel movie, and why?",
    "What is your favorite workout routine, and why?",
    "What is your favorite way to stay active, and why?",
    "What is your favorite hobby, and why?",
    "What is your favorite snack, and why?",
    "If you could only eat one snack for the rest of your life, what would it be, and why?",
    "What is your favorite bucket list item, and why?",
    "What is one thing you want to accomplish in the next year, and why?",
    "What is your favorite candy, and why?",
    "What is the most interesting audiobook you've ever listened to, and why?",
    "If you could only listen to one audiobook for the rest of your life, what would it be, and why?",
    "What is the most fascinating documentary you've ever watched, and why?",
    "What is your favorite way to relax after a long day, and why?",
    "If you could learn any skill in the world, what would it be, and why?",
    "What is the most important thing you've learned in the last year, and why?",
    "If you could have any job in the world, what would it be, and why?",
    "What is the best advice you've ever received, and who gave it to you?",
    "If you could have any pet, what would it be, and why?",
    "What is one thing you've always wanted to do but haven't yet, and why?",
    "What is your favorite way to spend a lazy day, and why?"
]

# define a function to generate a random question from the list
def generate_question() -> str:
    return random.choice(questions)

# define a route to return a random question
@app.get("/question")
async def get_question():
    return {"question": generate_question()}
