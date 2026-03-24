# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement modern REST APIs using the FastAPI framework. You'll create a web service with multiple endpoints, implement proper request validation, and understand the basics of API development including routing, request handling, and response management.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Server

#### Description
Create a basic FastAPI application with proper project structure. Initialize the development environment, install required dependencies, and set up a main application file that will serve as the foundation for your API.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn using pip
- Create a main application file that initializes a FastAPI app instance
- Set up at least one basic GET endpoint that returns a welcome message
- Run the development server successfully


### 🛠️ Task 2: Implement CRUD Endpoints

#### Description
Build out a complete set of CRUD (Create, Read, Update, Delete) endpoints for a resource of your choice (e.g., tasks, books, students, or products). Use proper HTTP methods (GET, POST, PUT, DELETE) and implement request/response models.

#### Requirements
Completed program should:

- Define a data model using Pydantic for request/response validation
- Implement GET endpoint to retrieve all items
- Implement GET endpoint with path parameter to retrieve a single item by ID
- Implement POST endpoint to create new items
- Implement PUT/PATCH endpoint to update existing items
- Implement DELETE endpoint to remove items


### 🛠️ Task 3: Add Error Handling and Validation

#### Description
Enhance your API with proper error handling, input validation, and meaningful HTTP status codes. Validate incoming data and provide clear error messages to API consumers.

#### Requirements
Completed program should:

- Use Pydantic models for automatic request validation
- Return appropriate HTTP status codes (200, 201, 400, 404, 500)
- Handle cases where requested items don't exist with proper error responses
- Validate data types and required fields in request bodies
- Provide meaningful error messages in responses
