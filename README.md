# Django Task Management Application

## Overview

This Django application is a task management tool that allows users to create, manage, and track tasks. It includes an authentication system to ensure that only authorized users can create and manage their tasks.

## Features
- *CREATE* : Authenticated users can create a TASK with due Date.
- *UPDATE* : ''  users can update the previous Tasks.
- *DELETE* : '' users can delete when logged in to their profiles
- *STATUS*: '' users can mark the task as *completed* or not *completed*
- "ABOUTPAGE* : most important route

##SETUP
- run python3 install requirements.txt
- if no database is created ```run python3 manage.py makemigrations``` followed by ```migrate```
- after successfull DB initialization run python manage.py runserver and hop on to the ```127.0.0.1```
- run test.py  by using ```python3 manage.py app test``` if you want to check for any flaws related to the request and functionality used client of django to test api "POST" and "GET"


### User Authentication

- **Registration**: New users can register for an account.
- **Login**: Registered users can log in to their accounts.
- **Logout**: Users can log out of their accounts.

### Task Management

- **Create Tasks**: Users can create new tasks with a title, description, due date, and author.
- **View Tasks**: Users can view a list of their tasks, with details such as overdue status.
- **Update Tasks**: Users can edit existing tasks.
- **Delete Tasks**: Users can delete tasks they no longer need.

### Validation

- **Title Length Validation**: Task titles are validated to ensure they do not exceed a specified length.
- **Due Date Validation**: The due date must always be greater than or equal to the task's published date.

### Test Suite

The project includes a test suite located in `tests.py`, which covers the following functionalities:

- **Task Model Tests**: Tests for creating tasks, validation for title lengths, and due date checks.
- **View Tests**: Tests for checking the functionality of list and detail views.

To run the tests, use the following command:

```bash
python manage.py test
