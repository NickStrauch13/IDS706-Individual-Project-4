[![CI](https://github.com/NickStrauch13/IDS706-Individual-Project-4/actions/workflows/python-ci.yml/badge.svg)](https://github.com/NickStrauch13/IDS706-Individual-Project-4/actions/workflows/python-ci.yml)
# IDS706-Individual-Project-4

## Fix-It: The LLM Powered Home Repair Assistant
This project is a home repair assistant that utilizes ChatGPT 3.5 Turbo alongside Retrieval Augmented Generation (RAG) to provide a an interface for users to ask questions about home repair. The project is built using a Flask server for the backend and a React frontend. The project is deployed on Azure and can be accessed at [https://fixit-ai.azurewebsites.net](https://fixit-ai.azurewebsites.net).

## Use

To use the project, either naviagate to [https://fixit-ai.azurewebsites.net](https://fixit-ai.azurewebsites.net), for follow the steps below to run locally.

### Local Setup

1. Build and run the docker image for the Flask backend server:
```
cd backend
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
2. Build and run the docker image for the React frontend server:
```
cd frontend
docker build -t react-app .
docker run -p 3000:3000 react-app
```
3. *IMPORTANT* Define the following environment variables:
```
OPENAI_API_KEY=<your openai api key>
GOOGLE_API_KEY=<your google api key>
```

