from typing import Optional, List
from pydantic import BaseModel, Field, computed_field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from datetime import datetime
import os

from dotenv import load_dotenv
from typing import Optional, List
from pydantic import BaseModel, Field, computed_field
from langchain_deepseek import ChatDeepSeek

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


load_dotenv()
deep_seek_api_key = os.getenv("DEEPSEEK_API_KEY")

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=2000,
    timeout=None,
    max_retries=2,
    api_key=deep_seek_api_key
)

current_time = str(datetime.now())



class Date(BaseModel):
    
    """Information about the date"""
    day: int = Field(description='What is the day of mentioned in number?',
               enum=[1,2,3,4,5,6,7])
    month: int = Field(description='what is the month mentioned ?e.g(december is 12 and january is 1)',
                     enum=[1,2,3,4,5,6,7,8,9,10,11,12])
    year: int = Field(description='what is the year mentioned?',default=2024)


class Food(BaseModel):
    """Information about a Food."""

    name: str = Field(description="What is the name of the food eaten? It must be one item, e.g(Banana, Apple,Salmon,Chicken breast")
    calories_per_100: int = Field(description="How many calories are in 100g serving")
    total_serving_size: int = Field(description="What is the total weight in g of the food eaten? e.g(I ate 270g of icecream)")
    
    # Macronutrients (per 100g)
    protein_g: float = Field(description="Protein content in grams per 100g serving")
    carbohydrates_g: float = Field(description="Carbohydrates content in grams per 100g serving")
    fat_g: float = Field(description="Fat content in grams per 100g serving")
 
    

    # Computed fields for total amounts based on serving size
    @computed_field(description="Automatically calculated total calories")
    def total_calories(self) -> float:
        return (self.calories_per_100 * self.total_serving_size) / 100

    @computed_field(description="Total protein in grams for the serving size")
    def total_protein_g(self) -> float:
        return (self.protein_g * self.total_serving_size) / 100

    @computed_field(description="Total carbohydrates in grams for the serving size")
    def total_carbohydrates_g(self) -> float:
        return (self.carbohydrates_g * self.total_serving_size) / 100

    @computed_field(description="Total fat in grams for the serving size")
    def total_fat_g(self) -> float:
        return (self.fat_g * self.total_serving_size) / 100

   


class Data_Food(BaseModel):
    """Extracted data about Food."""

    # Creates a model so that we can extract multiple entities.
    people: List[Food]

class Exercise(BaseModel):
    """Information about a Food."""

    name: str = Field(description="How is the exercise called? It must be one exercise, e.g(benchpress, pullups,squat,deadlift,paused squat, 2ct deadlift")
    weight: Optional[int] = Field(description="what was the weight lifted in kilos",default=None)
    repetitions: int = Field(description="How many repetitions have been done")
    reps_in_reserve: Optional[int] = Field(description='How many reps where left in reserve? how many could i have done more?',default=None)
    

class Cardio(BaseModel):
    """Information about Cardio""" 

    name: str = Field(description="What type of cardiovascular excercise did you perform? e.g(runing, cycling, swimming etc)")
    distance: float = Field(description="How many meters have you performed cardio for?")
    time: int = Field(description="how many seconds did it take to complete the distance?")

class Data_Cardio(BaseModel):
    """Extracted data about cardio."""

    # Creates a model so that we can extract multiple entities.
    people: List[Cardio]


class Data_Exercise(BaseModel):
    """Extracted data about Food."""

    # Creates a model so that we can extract multiple entities.
    people: List[Exercise]



class Date(BaseModel):
    
    """Information about the date"""
    day: int = Field(description='What is the day of mentioned in number?',
               enum=[1,2,3,4,5,6,7])
    month: int = Field(description='what is the month mentioned ?e.g(december is 12 and january is 1)',
                     enum=[1,2,3,4,5,6,7,8,9,10,11,12])
    year: int = Field(description='what is the year mentioned?',default=2024)

class Data_Date(BaseModel):
    """Extracts the date"""

    people: List[Date]

    
class Classification(BaseModel):
    diet_training_cardio: str = Field(
        description="Analyze the given text and classify it based on its content. "
                   "Determine if the text is primarily about:\n"
                   "1. A training program (workout routine, strength training, exercise regimen)\n"
                   "2. A diet (nutrition plan, eating habits, meal planning)\n"
                   "3. A cardio session (aerobic exercise, running, cycling, swimming)\n"
                   "4. Non of the above, they are asking about analytics, they want their data for a specific date",





                   
        enum=['analytics','diet', 'training', 'cardio'])
    