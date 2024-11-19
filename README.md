# Text-to-SQL LLM App

## Table of Contents
1. [Project Title](#project-title)
2. [Project Description](#project-description)
3. [Key Features](#key-features)
4. [Tech Stack](#tech-stack)
5. [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
6. [Usage](#usage)
7. [File Structure](#file-structure)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)
10. [Contributors](#contributors)
11. [Acknowledgments](#acknowledgments)

---

## Project Title
**Text-to-SQL App Powered by Google Gemini Pro**

---

## Project Description
This application allows users to input questions in plain English, which are converted into SQL queries using Google's **Gemini Pro** large language model (LLM). The generated SQL query is executed on a local SQLite database, and the results are displayed on the Streamlit interface. It provides an intuitive way for users to interact with databases without writing SQL queries manually.

---

## Key Features
1. **Natural Language to SQL Conversion**:
   - Converts user questions into SQL queries using Google Gemini Pro LLM.
   - Example: "How many students are in the database?" is converted to `SELECT COUNT(*) FROM STUDENT`.

2. **Database Query Execution**:
   - Executes the generated SQL query on a local SQLite database.

3. **Dynamic Results Display**:
   - Fetches and displays query results directly on the Streamlit app.

4. **Predefined Prompt**:
   - Utilizes a predefined prompt to guide the LLM for accurate SQL generation.

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite
- **AI Model**: Google Gemini Pro
- **Libraries**:
  - `dotenv` (for managing API keys)
  - `sqlite3` (for database interaction)
  - `google.generativeai` (for LLM integration)

---

## Setup Instructions

### Prerequisites
1. Install Python 3.8 or later.
2. Obtain a **Google API Key** for accessing Gemini Pro.
3. Ensure the following Python libraries are installed:
   - `streamlit`
   - `sqlite3`
   - `google-generativeai`
   - `python-dotenv`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-to-sql.git
   cd text-to-sql
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

4. Set up the SQLite database:
   - Create a file named `student.tb`.
   - Define the `STUDENT` table with the following schema:
     ```sql
     CREATE TABLE STUDENT (
         NAME TEXT,
         CLASS TEXT,
         SECTION TEXT
     );
     ```
   - Populate the table with sample data as required.

5. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. **Start the Application**:
   - Launch the app using Streamlit.
   - Open the provided local server URL in your browser.

2. **Ask a Question**:
   - Input a natural language question in the text box (e.g., *"List all students in Data Science class"*).
   - Click the **Ask the question** button.

3. **View Results**:
   - The app generates a SQL query, executes it on the database, and displays the results below.

---

## File Structure
```
├── app.py                # Main application script
├── student.tb            # SQLite database file
├── requirements.txt      # Required libraries
├── .env                  # Environment variables (Google API Key)
├── README.md             # Project documentation
```

---

## Future Enhancements
1. **Dynamic Database Schema**:
   - Automatically adapt to changes in database schema without hardcoding column names.

2. **Multi-Language Support**:
   - Extend natural language inputs to other languages.

3. **Integration with Cloud Databases**:
   - Enable querying remote or cloud-hosted databases.

4. **Enhanced UI**:
   - Provide dropdowns for database selection and schema visualization.

---

## Contributors
- **Rishikesh**  
- LinkedIn: www.linkedin.com/in/rishikesh-a12090285
- Email: rishikesh23@kgpian.iitkgp.ac.in
  
---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
