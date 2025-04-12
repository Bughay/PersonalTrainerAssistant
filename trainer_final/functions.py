import os
from dotenv import load_dotenv
from typing import Optional, List
from pydantic import BaseModel, Field, computed_field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from Classes import *
import csv
from langchain_deepseek import ChatDeepSeek
from datetime import datetime
import gspread
from google.oauth2 import service_account



current_time = str(datetime.now())

load_dotenv()


def send_sheets(item,diet_training):
    credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']
            )
    gc = gspread.authorize(credentials)
    SPREADSHEET_ID = '18AOpHu6CnB-qQiqQW-Exto1HSTECCidAl_QXXGpbDdU'  # Replace with your actual ID
    if diet_training == 'diet':
    
        sheet = gc.open_by_key(SPREADSHEET_ID).sheet1
        next_row = len(sheet.col_values(1)) + 1  # Count rows in Column A
        
        sheet.update(f'A{next_row}', [item])  # Wrap item in list to make it a row
        
        print(f"Data appended to row {next_row}")  
    elif diet_training == 'training':
        sheet = gc.open_by_key(SPREADSHEET_ID).worksheet("Sheet2")
        next_row = len(sheet.col_values(1)) + 1  # Count rows in Column A
        
        sheet.update(f'A{next_row}', [item])  # Wrap item in list to make it a row
        
        print(f"Data appended to row {next_row}") 

deep_seek_api_key = os.getenv("DEEPSEEK_API_KEY")

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=1000,
    timeout=None,
    max_retries=2,
    api_key=deep_seek_api_key
)



def extract_food(text):
    
    return_list = []
    prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "You will extract food found in the text"
            "If you do not know the value of an attribute asked to extract, "
            "return 0 for the attribute's value.",
        ),
    
        ("human", "{text}"),
    ]
)

    structured_llm = llm.with_structured_output(schema=Data_Food)
    prompt = prompt_template.invoke({"text": text})
    df = structured_llm.invoke(prompt)

    for i in range(len(df.people)):
        food = df.people[i]

        values_list = [
        current_time,
        food.name,
        food.calories_per_100,
        food.total_serving_size,
        food.protein_g,
        food.carbohydrates_g,
        food.fat_g,
        food.fiber_g,
        food.sugar_g,
        food.total_calories,
        food.total_protein_g,
        food.total_carbohydrates_g,
        food.total_fat_g,
                            ]
        return_list.append(values_list)
    return return_list

def extract_exercise(text):
    return_list = []
    prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "I may perform multiple sets of the same exercise, in that case create a seperate item for each single set"
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
    
        ("human", "{text}"),
    ]
)

    structured_llm = llm.with_structured_output(schema=Data_Exercise)
    prompt = prompt_template.invoke({"text": text})
    df = structured_llm.invoke(prompt)
    for i in range(len(df.people)):
        exercise = df.people[i]  
        values_list = [current_time,exercise.name, exercise.weight, exercise.repetitions, exercise.reps_in_reserve]
        return_list.append(values_list)  
    return return_list
            

