# Student Hub
The Student Hub Application is a web-based platform designed to serve students and parents, providing access to academic results and other relevant information. Additionally, it offers an admin dashboard for centralized administrative tasks.

## User Interface for Students/Parents
The user interface for students/parents offers the following features:
* Viewing Results: Access academic performance and view detailed result information.
* Access Student Information: Obtain information related to education.

## Admin Dashboard
The admin dashboard provides administrators with the tools to manage various aspects of the system:

* Student Management: Add, edit, or delete student profiles.
* Class Management: Manage classes by adding, editing, or deleting class levels and sections.
* Subject Management: Add, edit, or delete subjects taught in different classes.
* Result Management: Record and manage student academic results, including subject-wise marks, and overall performance.

## Technologies

The Student Hub application uses the following technologies:
* Flask: used as the web framework for backend development, providing a lightweight and flexible environment.
* SQLAlchemy: serves as the Object-Relational Mapping (ORM) tool to interact with the application's database.
* HTML/CSS/JavaScript: Frontend development is done using HTML, CSS, and JavaScript to create an interactive user interface.
* Bootstrap: is utilized for responsive and mobile-first design elements.
* bcrypt: library used for secure password hashing and verification.
* MySQL: used as the relational database management system for storing application data.

## Installation and Usage
1. Clone the repository:
First, you need to clone the repository to your local machine using the following command:
`git clone https://github.com/hajarzaitouni/Student_Hub.git`

2. Set Up a Virtual Environment
Navigate to the project directory and create a virtual environment. You can do this using venv (for Python 3) or virtualenv. Here's an example using venv:

```
cd Student_Hub
python3 -m venv venv
```
which gonna create a virtual environment named venv in the project directory.

3. Activate the Virtual Environment
Activate the virtual environment which depends on your operating system:

* On macOS and Linux:
    ```
    source venv/bin/activate
    ````
* On Windows:
    ````
    venv\Scripts\activate
    ````
4. Install Dependencies
The virtual environement must be active and you install the required dependencies using `pip`:

`pip install -r requirements.txt`
5. Run the flask Application

`python run.py`
This will start the development server. By default, the application will be accessible at http://localhost:5000.

## Usage
* Log in as an administrator to access the dashboard.
* Navigate through different sections such as Student Management, Class Management, Subject Management, and Result Management to perform various tasks.
* Add, edit, or delete student profiles, classes, subjects, and academic results as needed.
* View Results: Students and parents can access the student interface and enter the student's roll number to view their academic results and other related informations.

## Contributors
Hajar ZAITOUNI [https://github.com/hajarzaitouni]
















