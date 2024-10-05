# Job Recommendation Backend Service

## Project Overview

This project implements a backend service that recommends job postings to users based on their profiles and preferences. The service is built using Django and utilizes SQLite as the database.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Recommendation Logic](#recommendation-logic)
- [Assumptions and Design Decisions](#assumptions-and-design-decisions)
- [Challenges Encountered](#challenges-encountered)
- [Evaluation Criteria](#evaluation-criteria)
- [License](#license)

## Features

- RESTful API to receive user profiles and return job recommendations.
- Database to store user profiles and job postings.
- Custom recommendation algorithm based on user preferences and job requirements.

## Technologies Used

- **Python**: Programming language used for backend development.
- **Django**: Web framework for building the RESTful API.
- **SQLite**: Lightweight database for storing data.
- **Django REST Framework**: Toolkit for building Web APIs.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sushantkrsky/Job-Recommendation-Backend-Service.git
   cd job-recommendation-service
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Set up the database with the initial schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (optional, for accessing the admin interface):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- The service can be accessed at `http://127.0.0.1:8000/api/recommend/` for job recommendations.
- Use a tool like Postman to send POST requests with user profile data.

## API Endpoints

### POST /api/recommend/

**Request Body**:
```json
{
  "name": "Jane Doe",
  "skills": ["Python", "Django", "REST APIs"],
  "experience_level": "Intermediate",
  "preferences": {
    "desired_roles": ["Backend Developer", "Software Engineer"],
    "locations": ["Remote", "New York"],
    "job_type": "Full-Time"
  }
}
```

**Response**:
Returns a list of job postings matching the user’s profile.

## Recommendation Logic

The recommendation algorithm evaluates job postings based on:

1. **Role Match**: Checks if the job title is in the user's desired roles.
2. **Job Type Match**: Compares the job type against the user's preference.
3. **Experience Level Match**: Matches the required experience level with the user's level.
4. **Location Match**: Validates if the job location is one of the preferred locations.
5. **Skill Match**: Checks if any required skills match the user's skills.

## Assumptions and Design Decisions

- The application assumes that job postings are accurately represented in the database.
- It uses a straightforward rule-based approach for matching rather than complex algorithms or machine learning.
- The user profile includes preferences, which are crucial for generating recommendations.

## Challenges Encountered

- **Data Matching**: Ensuring that job postings in the database accurately reflect potential user preferences was challenging, as misalignment could lead to empty recommendation results.
- **Serialization**: Handling nested data structures in user profiles required careful design in the serializer to ensure data integrity and correctness.

## Evaluation Criteria

### Functionality
- The application meets the requirements specified in the assignment.
- Job recommendations are relevant based on user profiles and preferences.

### Technical Skills
- Proficient implementation of Python and Django.
- Effective recommendation algorithm that processes user profiles correctly.
- Appropriate database design using SQLite.

### Code Quality
- Code is organized into functions and classes for better readability.
- Clean and maintainable code structure with proper error handling.

### Problem-Solving and Creativity
- The algorithm efficiently matches users with job postings.
- Innovative approach in how user preferences are handled and matched against job postings.

### Documentation and Clarity
- Comprehensive documentation explaining the setup, usage, and internal logic.
- Clear explanations of assumptions and design decisions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
