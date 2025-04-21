Input Processing:

    User provides natural language input (e.g., "Ate 150g of chicken breast with 100g rice")

    The system receives this text through the process_input() method

Text Classification:

    The input text is classified into one of four categories:

        'diet' (food/nutrition data)

        'training' (weight training exercises)

        'cardio' (cardiovascular exercises)

        'analytics' (data analysis requests)

Data Extraction:

    Based on the classification, the appropriate LLM extractor is used:

        For 'diet': extract_food() uses LLM to get food name, serving size, and macronutrients

        For 'training': extract_exercise() gets exercise name, weight, reps, and RIR

        For 'cardio': extract_cardio() extracts activity name, distance, and time

    The LLM uses structured output schemas (Data_Food, Data_Exercise, Data_Cardio)

Data Formatting:

    The raw extracted data is formatted for human-readable display:

        Food data shows calories and macros per serving

        Exercise data shows weight and reps

        Cardio data shows distance and speed calculations

    Emojis and bullet points are added for visual clarity

Data Persistence:

    The data is converted to dataclass objects (Food, Exercise, Cardio)

    Saved to a SQLite database via DatabaseManager:

        Food data goes to 'food' table

        Exercises to 'exercises' table

        Cardio to 'Cardio' table

    Also saved to Google Sheets (though the spreadsheet ID is currently placeholder)


    