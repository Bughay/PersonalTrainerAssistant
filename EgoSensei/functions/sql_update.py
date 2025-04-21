from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, select, Table, MetaData


from sqlalchemy.sql import insert

db_path = 'db/trainer.db'
# Assuming you have SQLAlchemy models defined (better approach)
# Here's an alternative using Core API if you don't have models

def update_food(item):
    # Create engine and connect
    engine = create_engine(f'sqlite:///{db_path}')
    metadata = MetaData()
    
    # Reflect the tables
    food_table = Table('food', metadata, autoload_with=engine)                                                     
    
    user_id = 1
    name = item[1].title()
    serving = item[3]
    calories = (item[2] * serving) / 100
    protein = (item[4] * serving) / 100
    carbs = (item[5] * serving) / 100
    fat = (item[6] * serving) / 100
    
    with engine.connect() as conn:


        stmt = insert(food_table).values(
                        user_id=user_id,
                        type_food=name,
                        serving_g=serving,
                        calories=calories,
                        protein=protein,
                        carbs=carbs,
                        fats=fat,
                    )
        conn.execute(stmt)
        conn.commit()

def update_exercise(item):
    user_id = 1
    engine = create_engine(f'sqlite:///{db_path}')

    metadata = MetaData()
    
    # Reflect the tables
    exercises_table = Table('exercises', metadata, autoload_with=engine)
    with engine.connect() as conn:
  
        stmt = insert(exercises_table).values(
            user_id = user_id,
            exercise_name = item[1],
            weight_total = item[2],
            reps = item[3],
            rpe = item[4]
        )
        conn.execute(stmt)
        conn.commit()

def update_cardio(item):
    user_id = 1
    engine = create_engine(f'sqlite:///{db_path}')

    metadata = MetaData()
    
    # Reflect the tables
    exercises_table = Table('Cardio', metadata, autoload_with=engine)
    with engine.connect() as conn:
        stmt = insert(exercises_table).values(
            user_id = user_id,
            cardio_name = item[1],
            distance_m = item[2],
            time_sec = item[3],
        )
        conn.execute(stmt)
        conn.commit()


    
