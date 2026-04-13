# ACM API Workshop Demo

This repository contains a full-stack Python web application designed as a demonstration for the **UChicago ACM (Association for Computing Machinery)** API workshop. 

The primary goal of this demo is to showcase how **REST APIs** work in practice, how to connect a frontend client to a backend server, and how to dynamically pull structured data and visualize it on a webpage without manually creating an HTML file statically. 

## Features

- **Custom Flask Backend (`server.py`)**: A backend application that serves structured data from a simulated dictionary-based database (`data.json`).
- **RESTful Endpoints**: Specifically highlights REST design by fetching diverse resources across multiple routes instead of one monolithic endpoint:
  - `GET /api/names`: Retrieves a list of all board member names.
  - `GET /api/roles/<name>`: Dynamically accepts a board member's name and fetches their specific role.
  - `GET /api/hobbies/<name>`: Dynamically accepts a board member's name and fetches their hobbies/bio.
- **Dynamic Client (`client.py`)**: A second Flask server representing a consumer application. It aggregates data by actively querying the backend APIs using the `requests` library and constructs Python dictionary objects.
- **Dynamic HTML Generation (`frontend.py`)**: Demonstrates decoupling frontend styling and component structure by defining HTML visually in Python functions that render data.

## Getting Started

Follow these steps to boot up the project locally.

### 1. Install Prerequisites

Ensure you have Python installed. You'll need to install the project dependencies, specifically the `Flask` framework and the `requests` library to manage HTTP logic. 

Open your terminal and run:
```bash
pip install Flask requests
```

### 2. Boot up the Backend Server (API)

Open a terminal in the project directory. Run the backend server, which will act as our "database" and API provider and listen cleanly on port 5000:
```bash
python server.py
```
*(Leave this terminal window running)*

### 3. Boot up the Frontend Client

Open a **second, separate terminal** in the same project directory. Boot up the user interface client, which will ping your backend server and render the HTML interface on port 5001:
```bash
python client.py
```
*(Leave this terminal window running too)*

### 4. View the App

Open any web browser and navigate to:
```text
http://127.0.0.1:5001
```
You will instantly see the dynamic board member profiles loaded securely from your backend server API!