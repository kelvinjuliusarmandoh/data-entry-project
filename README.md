# Data Entry Project

## Overview
This project is a data entry application built using Python's Tkinter library. The application allows users to input personal and job information, and save the data either to an Excel file or an SQLite database.

## Features
- User can input their personal information including first name, second name, last name, age, gender, and nationality.
- User can input job-related information including job role, job status, and years of experience.
- Data can be saved to an Excel file or an SQLite database.
- Option to switch between light and dark themes.

## Requirements
- Python 3.x
- Tkinter
- Openpyxl (for Excel operations)
- SQLite3 (for database operations)

## File Structure
```
data-entry-project/
├── app.py
├── data.py
├── nationalities.txt
├── role.txt
├── README.md
└── main.py
```


## Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```sh
    cd data-entry-project
    ```
3. Install the required packages:
    ```sh
    pip install openpyxl
    ```

## Usage
1. Ensure the `nationalities.txt` and `role.txt` files are present in the project directory. These files should contain the list of nationalities and job roles respectively, each on a new line.
2. Run the application:
    ```sh
    python main.py
    ```

## Components
- `app.py`: Contains the `App` class which defines the layout and functionality of the application.
- `data.py`: Contains the data lists for nationalities and job roles.
- `main.py`: The entry point of the application.
- `nationalities.txt`: A text file containing a list of nationalities.
- `role.txt`: A text file containing a list of job roles.

## Functionality
- **Data Entry Form**: Users can enter their personal and job information in the provided fields.
- **Submit to Excel**: Saves the entered data to an Excel file. If the file does not exist, it creates a new one with the appropriate headers.
- **Submit to SQLite**: Saves the entered data to an SQLite database. If the database does not exist, it creates a new one with the appropriate table structure.
- **Settings**: Allows the user to switch between light and dark themes.




