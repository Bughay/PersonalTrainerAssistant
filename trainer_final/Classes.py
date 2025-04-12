from typing import Optional, List
from pydantic import BaseModel, Field, computed_field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class Food(BaseModel):
    """Information about a Food."""

    name: str = Field(description="What is the name of the food eaten? It must be one item, e.g(Banana, Apple,Salmon,Chicken breast")
    calories_per_100: int = Field(description="How many calories are in 100g serving",default=0)
    total_serving_size: int = Field(description="What is the total weight in g of the food eaten? e.g(I ate 270g of icecream)",default=0)
    
    # Macronutrients (per 100g)
    protein_g: float = Field(description="Protein content in grams per 100g serving")
    carbohydrates_g: float = Field(description="Carbohydrates content in grams per 100g serving")
    fat_g: float = Field(description="Fat content in grams per 100g serving")
    fiber_g: Optional[float] = Field(None, description="Dietary fiber content in grams per 100g serving")
    sugar_g: Optional[float] = Field(None, description="Sugar content in grams per 100g serving")
    

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
    reps_in_reserve: int = Field(description='How many reps where left in reserve? how many could i have done more?',default=None)
    

   


class Data_Exercise(BaseModel):
    """Extracted data about Exercises."""

    # Creates a model so that we can extract multiple entities.
    people: List[Exercise]
