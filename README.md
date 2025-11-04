Task Management Web App (Django)

A simple, test-driven web application built with Django that allows users to create, edit, delete, and mark tasks as complete.
This project demonstrates the use of Test-Driven Development (TDD) principles and basic CRUD operations within a Django framework.


Features

Create new tasks with optional notes and due dates
Edit existing tasks
Delete tasks instantly
Mark tasks as complete or undo completion
Persistent storage using SQLite (local development)
Clean, minimal HTML interface
Fully covered by automated Django unit tests


Tech Stack
Component	Description
Language	Python 3.11
Framework	Django 5.2.6
Database	SQLite3 (development)
IDE	Visual Studio Code
Version Control	Git / GitHub
OS	Windows 11


Installation and Setup
1. Clone the repository
git clone https://github.com/eece-4081-fall-2025/drake_watters_todo.git
cd drake_watters_todo

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install django

4. Run migrations
python manage.py migrate

5. Start the development server
python manage.py runserver

Visit http://127.0.0.1:8000/
 to view the app.


Running Tests

This project was built using a Red-Green-Refactor workflow:
Red — Write failing tests before any implementation.
Green — Implement minimal code to make tests pass.
Refactor — Clean and improve code without breaking tests.

Run all tests:
python manage.py test

Tests are located in: five/tests.py


Test Summary
Test	Purpose
test_list_shows_tasks	Verifies that all saved tasks appear on the task list page.
test_create_task	Ensures a new task is saved and visible after submission.
test_edit_task	Confirms editing updates task details correctly.
test_delete_task	Checks that deleting removes the task from the list.
test_toggle_complete	Validates toggling a task’s completion status.


🧹 .gitignore Highlights
venv/
__pycache__/
db.sqlite3
*.log
*.pyc
*.pyo
*.pyd


Development Notes

Built following Django’s MTV (Model-Template-View) architecture.
Focused on clear function separation and simple test coverage.
Designed to be lightweight for local demonstration and grading.


Author

Drake Watters
University of Memphis — EECE 4081 (Fall 2025)
Task Management MVP built using Test-Driven Development.
