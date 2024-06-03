import pandas as pd

# Example ID
id_number = "1990051512345678"

# Function to extract information from the ID
def extract_id_info(id_number):
    # Extracting year, month, day
    year = id_number[0:4]
    month = id_number[4:6]
    day = id_number[6:8]
    
    # Assuming the unique identifier is the next three digits (if needed)
    unique_id = id_number[8:11]
    
    # Extracting nationality and gender
    nationality_code = id_number[11:14]
    gender_code = id_number[14:15]
    
    # Mapping gender code to actual gender
    gender = "Male" if gender_code == "1" else "Female"
    
    # Assuming a predefined mapping for nationality codes
    nationality_dict = {
        "001": "American",
        "002": "Canadian",
        "003": "British",
        # Add other mappings as needed
    }
    
    nationality = nationality_dict.get(nationality_code, "Unknown")
    
    return {
        "Year": year,
        "Month": month,
        "Day": day,
        "Gender": gender,
        "Nationality": nationality
    }

# Example usage
info = extract_id_info(id_number)
print(info)

