# Task Management API

This API allows users to create tasks, assign them to users, and retrieve assigned tasks.

# Features

- User Registration API

- Task Creation API

- Assigning Tasks to Users

- Retrieving Tasks for a Specific User

---

## Installation

1. Clone the repository:
   ```sh
   git clone "https://github.com/RohitSingh-04/task_assinger.git"
   ```
2. Navigate to task_asigner directory
   ```
   cd task_asigner
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the server:
   ```sh
   python manage.py runserver
   ```

---

## API Endpoints

### 1. Create a User
- **Endpoint:** `POST /api/create-user/`
- **Description:** Creates a new user.
- **Request Body:**
  ```json
  {
    "username": "rohiyaa",
    "first_name": "Rohit",
    "last_name": "Singh",
    "email": "rsingh.py@gmail.com",
    "password": "securepassword123"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "username": "rohiyaa",
    "email": "rsingh.py@gmail.com",
    "tasks": []
  }
  ```

---

### 2. Create a Task
- **Endpoint:** `POST /api/tasks/`
- **Description:** Creates a new task.
- **Request Body:**
  ```json
  {
    "name": "Complete Django Project",
    "description": "Finish the project by the deadline",
    "task_type": "development",
    "status": "pending"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Complete Django Project",
    "description": "Finish the project by the deadline",
    "task_type": "development",
    "created_at": "2025-03-25T12:00:00Z",
    "status": "pending",
    "assignee": [],
    "completed_at": null
  }
  ```

---

### 3. Assign a Task to a User
- **Endpoint:** `POST /api/tasks/{task_id}/assign/`
- **Description:** Assigns one or more users to a task.
- **Path Parameter:**
  - `task_id` (integer): ID of the task to be assigned.
- **Request Body:**
  ```json
  {
    "assignee": [1, 2]
  }
  ```
- **Response:**
  ```json
  {
    "message": "user assigned successfully"
  }
  ```

---

### 4. Get Tasks Assigned to a User
- **Endpoint:** `GET /api/users/{user_id}/tasks/`
- **Description:** Fetches all tasks assigned to a particular user.
- **Path Parameter:**
  - `user_id` (integer): ID of the user.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Complete Django Project",
      "description": "Finish the project by the deadline",
      "task_type": "development",
      "created_at": "2025-03-25T12:00:00Z",
      "status": "pending",
      "assignee": [1],
      "completed_at": null
    }
  ]
  ```

---

## Notes
- Ensure to create users before assigning tasks.
- The API uses `PrimaryKeyRelatedField` for `assignee`, so user IDs must be provided when assigning tasks.
- Tasks can have multiple assignees.
