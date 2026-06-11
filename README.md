Weather app in Python

A full-stack Python web application built using the Django framework that delivers real-time weather analytics and multi-day forecasts. This project highlights a migration from a terminal-based script to a secure, multi-user web platform featuring user authentication and a relational database backend.

🚀 Key Features
Live Weather Engine: Fetches real-time current weather metrics and a 5-day forecast using third-party REST APIs.

User Authentication Suite: Includes secure, encrypted user registration, login, and session-managed logout states.

Interactive Comments Platform: Features a restricted database-backed comment section where authenticated users can leave feedback.

Dynamic Environment Switching: Configured to instantly toggle between local SQLite storage for development and production-grade SQL databases on cloud deployments.

📈 Project Evolution & Background
This application is adapted and scaled from a final project requirement in the SheCodes Python curriculum.

The Original Architecture
The initial scope of the course project focused on core Python fundamentals inside a command-line interface (CLI). It utilized terminal input() prompts, basic string formatting, standard if/else logic, and basic requests blocks to print raw JSON payloads into the console.

The Full-Stack Upgrade
To challenge myself and demonstrate the cross-stack evolution of my skills (moving from vanilla JavaScript to React and now into Python frameworks), I decoupled the terminal script and rebuilt it as a full-featured web app.

🛠️ Tech Stack & Tools
Backend Framework: Python 3.12, Django 5.2

Database Management: SQLite (Local Dev) / PostgreSQL Compatibility 

Environment Security: Python-Decouple (.env)

Static Assets: WhiteNoise (Production caching and compression)


