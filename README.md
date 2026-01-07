# Portfolio API using FastAPI

This project is a **personal portfolio backend API** built using **FastAPI**.  
It exposes structured information about my **technical profile, skills, social links, and projects** following clean backend architecture principles.

The goal of this project is to demonstrate:
- Backend API design
- Clean code structure
- Router–Service separation
- Readable and scalable REST APIs

---

## 🚀 Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- REST API Architecture

---

Purpose of This Project

This project was built to:

Practice backend development using FastAPI

Learn clean API design and structure

Build a portfolio-ready backend project

Prepare for backend / DevOps roles

## INTERVIEW PREP QUESTIONS 
1. What problem does your Portfolio API solve?

Answer:
My Portfolio API provides a structured and programmatic way to showcase my technical profile, skills, and projects. Instead of static information, this API acts as proof that I can design, build, and structure a backend application using FastAPI. Anyone can access my skills and projects through API endpoints, which demonstrates both my technical knowledge and practical implementation.

2. Why did you choose FastAPI for this project?

Answer:
I chose FastAPI because it is a high-performance Python framework that is easy to use and understand. It provides automatic Swagger documentation, fast request handling, and clean API development. FastAPI also encourages best practices like type hints and modular code structure.

3. Explain the architecture of your project.

Answer:
My project follows a layered architecture. The router layer handles HTTP requests and API endpoints, the service layer contains the business logic and data handling, and the main application file initializes FastAPI and includes routers. This separation improves readability, maintainability, and scalability.

4. Why did you separate router and service layers instead of writing everything in one file?

Answer:
I separated the router and service layers to improve readability and maintainability. The router layer is responsible only for handling HTTP requests, while the service layer contains the business logic. This approach keeps the code clean and makes it easier to scale or modify in the future.

5. Why is it bad practice to write business logic directly inside the router?

Answer:
Writing business logic inside the router mixes responsibilities and makes the code harder to maintain and test. The router should only manage HTTP requests and responses, while the service layer should handle logic. Separating them follows best practices and improves scalability.

6. If you want to add a database (PostgreSQL or MongoDB), where would you add it and why?

Answer:
I would add database operations in the service layer because database actions such as insert, update, delete, and fetch are part of business logic. Keeping database logic in the service layer maintains separation of concerns and allows future changes without affecting the API routes.

7. Why did you return projects as a list instead of using keys like project1, project2?

Answer:
I returned projects as a list because lists are scalable and predictable. New projects can be added easily without changing the API structure or hard-coding new keys. This approach is also frontend-friendly and works well with databases.

8. Why should API response keys avoid spaces?

Answer:
API response keys should avoid spaces because they make the data harder to use across different clients. Keys without spaces are easier to access in JavaScript and other languages. Using snake_case improves readability, consistency, and maintainability.

9. What is APIRouter in FastAPI and why did you use multiple routers?

Answer:
APIRouter is used to organize API endpoints into separate modules. I used multiple routers to separate concerns—one router handles technical profile information and another handles project details. This makes the code modular and easier to manage.

10. What is the purpose of app.include_router()?

Answer:
app.include_router() registers routes from an APIRouter into the main FastAPI application. Without including the router, the endpoints will not be available or visible in Swagger documentation.


