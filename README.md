# Employee Management System (EMS)

A web-based Employee Management System built using **Python, Django, HTML, CSS and JavaScript**.

The project aims to simplify employee data management through a centralized dashboard with a clean and user-friendly interface.

## Project Overview

The Employee Management System is designed to help organizations manage employee information and related administrative activities.

The application currently includes a dashboard and an employee management interface. Additional modules are planned as development progresses.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Current Features

- Dashboard with employee statistics
- Employee listing
- Employee search interface
- Department information display
- Employee management interface

## Planned Features

- Employee registration and profile management
- Department management
- Attendance tracking
- Leave management
- Salary management
- Reports and analytics
- User authentication and profile management

## Project Structure

```text
Employee_Management_System/
│
├── accounts/
├── attendance/
├── departments/
├── employees/
├── leave_management/
├── salary/
├── reports/
├── EMS/
├── static/
├── templates/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AdeebaMultani/Employee-Management-System.git
```

### 2. Navigate to the project directory

```bash
cd Employee-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```bash
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## Development Status

**Status:** Currently under development.

New features, UI improvements and additional modules will be added progressively.

## Author

**Adeeba Multani**

GitHub: [@AdeebaMultani](https://github.com/AdeebaMultani)

---

*This project is being developed as a practical learning project to improve my skills in Python, Django and full-stack web development.*
