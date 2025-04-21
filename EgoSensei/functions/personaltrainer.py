from typing import List
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek
from sqlalchemy import create_engine, select, Table, MetaData, and_
from functions.models import *
import pandas as pd

def extract_analytics(text):
      
    return_list = []
    prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "You will extract analytics and dates found in the text"
            "If you do not know the value of an attribute asked to extract, "
            "return 0 for the attribute's value.",
        ),
    
        ("human", "{text}"),
    ]
    )
    structured_llm = llm.with_structured_output(schema=Data_Date)

    prompt = prompt_template.invoke({"text": text})
    df = structured_llm.invoke(prompt)

    for i in range(len(df.people)):
        if i == 0 :

            food = df.people[i]

            values_list = [
            food.day,food.month,food.year
                                ]
            return_list = values_list
            break
    return return_list



    

def extract_cardio(text):
    
    return_list = []
    prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "You will extract cardiovascular excercise data found in the text"
            "If you do not know the value of an attribute asked to extract, "
            "return 0 for the attribute's value.",
        ),
    
        ("human", "{text}"),
    ]
)

    structured_llm = llm.with_structured_output(schema=Data_Cardio)
    prompt = prompt_template.invoke({"text": text})
    df = structured_llm.invoke(prompt)

    for i in range(len(df.people)):
        cardio = df.people[i]

        values_list = [
        current_time,
        cardio.name,
        cardio.distance,
        cardio.time
                            ]
        return_list.append(values_list)
    return list(return_list)

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
        food.total_calories,
        food.total_protein_g,
        food.total_carbohydrates_g,
        food.total_fat_g,
                            ]
        return_list.append(values_list)
    return return_list

def extract_cardio(text):
    
    return_list = []
    prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "You will extract cardiovascular excercise data found in the text"
            "If you do not know the value of an attribute asked to extract, "
            "return 0 for the attribute's value.",
        ),
    
        ("human", "{text}"),
    ]
)

    structured_llm = llm.with_structured_output(schema=Data_Cardio)
    prompt = prompt_template.invoke({"text": text})
    df = structured_llm.invoke(prompt)

    for i in range(len(df.people)):
        cardio = df.people[i]

        values_list = [
        current_time,
        cardio.name,
        cardio.distance,
        cardio.time
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


    
def personal_trainer_log(text):
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=2000,
        timeout=None,
        max_retries=2,
        api_key=deep_seek_api_key
    )
    structured_llm = llm.with_structured_output(Classification)  
    tagging_prompt = ChatPromptTemplate.from_template(
    """
    Extract the desired information from the following passage.

    Only extract the properties mentioned in the 'Classification' function.

    Passage:
    {input}
    """
    )
    
      
    llm = llm.with_structured_output(
        Classification
    )
    prompt = tagging_prompt.invoke({'input':text})
    response = structured_llm.invoke(prompt)
    category = response.diet_training_cardio
    result = None
    if category == 'diet':
        result = extract_food(text)
    elif category == 'training':
        result = extract_exercise(text)
    else:
        result = extract_cardio(text)
    
    return result, category




