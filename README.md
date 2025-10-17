Task Management API
 Built with:

Django & Django REST Framework

SQLite (default)

PythonAnywhere (for deployment)

 Project Overview

This is a Task Management API that allows users to manage their personal tasks.
Each user can:

Register and log in

Create, read, update, and delete tasks

Mark tasks as complete or incomplete

 Features

 User authentication
 Task CRUD operations
 Mark complete/incomplete endpoints
 Uses Django ORM
 RESTful API structure

 API Endpoints
Method	Endpoint	Description
GET	/api/tasks/	List all tasks for user
POST	/api/tasks/	Create new task
GET	/api/tasks/<id>/	Retrieve task
PUT/PATCH	/api/tasks/<id>/	Update task
DELETE	/api/tasks/<id>/	Delete task
PATCH	/api/tasks/<id>/complete/	Mark task complete
PATCH	/api/tasks/<id>/incomplete/	Mark task incomplete