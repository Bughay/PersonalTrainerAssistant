CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    weight REAL,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL ,
    type_food TEXT NOT NULL,
    serving_g REAL,
    calories REAL,
    protein REAL,
    carbs REAL,
    fats REAL,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE INDEX idx_food_user ON food(user_id);
CREATE INDEX idx_food_user_date ON food(user_id, date_added);

CREATE TABLE exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    exercise_name TEXT NOT NULL,
    weight_total REAL,
    reps INTEGER,
    rpe INTEGER CHECK(rpe BETWEEN 1 AND 10),
    fatigue INTEGER CHECK(fatigue BETWEEN 1 AND 10),
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE INDEX idx_exercises_user ON exercises(user_id);
CREATE INDEX idx_exercises_user_date ON exercises(user_id, date_added);

CREATE TABLE Cardio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    cardio_name TEXT NOT NULL,
    distance_m INTEGER,
    time_sec INTEGER,
    speed REAL GENERATED ALWAYS AS (
        CASE WHEN time_sec > 0 
             THEN distance_m / (time_sec / 3600.0)  
             ELSE NULL 
        END
    ) VIRTUAL,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE INDEX idx_cardio_user ON Cardio(user_id);
CREATE INDEX idx_cardio_user_date ON Cardio(user_id, date_added);
