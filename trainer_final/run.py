import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_deepseek import ChatDeepSeek
from functions import *

load_dotenv()

diet_training = input('do you want to log your diet or training?(answer diet or training) ')

if diet_training == 'diet':
    text = input('Tell us what you have eaten ')

    check = extract_food(text)
    with open('pantik_fooddd.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in check:
            print(item)
            send_sheets(item,diet_training)
            writer.writerow(item)

elif diet_training == 'training':
    text = input('describe your training or exercise you wana log ')
    check = extract_exercise(text)

    with open('pantik_exercise.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in check:
            print(item)
            send_sheets(item,diet_training)
            writer.writerow(item)
else:
    print('you can only choose to log training or data')


