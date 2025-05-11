# Python Microservices

This repository contains a collection of Python microservices designed to demonstrate best practices in microservice architecture. The project focuses on building independent, scalable services using Python, implementing API communication, and integrating Playwright for end-to-end testing.

## Features

* Independent microservices architecture
* API communication between services
* End-to-end testing with Playwright
* Error handling and logging
* Modular and reusable components

## Technologies

* FastAPI
* Playwright
* Docker
* Redis
* PostgreSQL

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/metju29/python-microservices.git
   cd python-microservices
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the services:

   ```bash
   docker-compose up --build
   ```
