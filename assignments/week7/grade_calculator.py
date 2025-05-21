import csv
import random
import os
import time
students_data = []


all_possible_weeks = [f"Week {i}" for i in range(1, 14)]
valid_score_weeks = [week for week in all_possible_weeks if week != "Week 6"] #since there is no week 6 it's removed from the count


def read_csv_data(filename):
    global students_data
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_data = list(reader)
            time.sleep(1)
        print(f"Successfully read data from '{filename}'.")
        time.sleep(1.5)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure the path is correct.")
        exit(1)

def adding_missing_scores():
    print("Generating missing scores...")
    time.sleep(1.5)
    for row in students_data:
        for week in valid_score_weeks: # Checking if the week column exists and if its value is empty or not a digit
            current_score = row.get(week)
            if not current_score or not str(current_score).strip().isdigit():
                random_score = random.randint(0, 3)
                row[week] = str(random_score)  # Score as string
    print("Missing scores populated.")
    time.sleep(1.5)

def calculate_all_student_metrics():
    print("Calculating total and average points...")
    time.sleep(1)
    for row in students_data:
        scores = []
        for week in valid_score_weeks:
            score_value = row.get(week)
            if score_value is not None and str(score_value).strip().isdigit():
                scores.append(int(str(score_value).strip()))
        row["Total Points"] = calculate_total_points(scores)
        row["Average Points"] = calculate_average_points(scores)
    print("Calculations complete.")


def calculate_total_points(scores):
    if len(scores) >= 10:
        top_scores = sorted(scores, reverse=True)[:10]
        return sum(top_scores)
    else:
        return "###"

def calculate_average_points(scores):
    return sum(scores) / 12



def write_updated_csv(filename):
    output_fieldnames = ["Name"] + valid_score_weeks + ["Total Points", "Average Points"]

    try: # this segment is AI generated
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=output_fieldnames)
            writer.writeheader()  # Write the header row with the defined order
            for row in students_data:
                clean_row = {key: row.get(key, "") for key in output_fieldnames}
                writer.writerow(clean_row)
        print(f"Updated data successfully written to:")
        time.sleep(1.5)
        print(f"  {os.path.abspath(filename)}")  # Print the absolute path for clarity
    except Exception as e:
        print(f"An error occurred while writing the CSV file: {e}")


if __name__ == "__main__":
    # <<<<<<<<<<<< those may be changed >>>>>>>>>>>>>
    input_directory_path = r"C:\Users\schmi\OneDrive\Dokumente\!Uni\2 Semester\TechBasics 1"

    input_csv_base_filename = "Technical Basics I_2025 - Sheet1.csv"

    input_csv_filename = os.path.join(input_directory_path, input_csv_base_filename)

    # Replace with your name or a descriptive identifier for the output file
    user_identifier = "MyAnalysis"

    print(f"\nStarting processing for file: '{input_csv_filename}'")

    # Step 1: Reads the CSV file
    read_csv_data(input_csv_filename)

    # Step 2: adds missing scores
    adding_missing_scores()

    # Step 3: Calculates total and average scores
    calculate_all_student_metrics()

    # Constructs the new output filename. It will be saved in the same directory.
    base_name_without_ext = os.path.splitext(input_csv_base_filename)[0]
    output_csv_filename = os.path.join(input_directory_path,
                                       f"{base_name_without_ext}_calculated_by_{user_identifier}.csv")

    # Step 4: Writes the updated data to a new CSV file with specified column order
    write_updated_csv(output_csv_filename)


    print("\nScript execution finished.")