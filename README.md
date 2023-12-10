[![CI](https://github.com/NickStrauch13/IDS706-Individual-Project-4/actions/workflows/python-ci.yml/badge.svg)](https://github.com/NickStrauch13/IDS706-Individual-Project-4/actions/workflows/python-ci.yml)
# IDS706-Individual-Project-4

## Fix-It: The LLM Powered Home Repair Assistant
Watch the video walkthrough [here](https://youtu.be/n6USH_QwT1k).

This project is a home repair assistant that utilizes ChatGPT 3.5 Turbo alongside Retrieval Augmented Generation (RAG) to provide a an interface for users to ask questions about home repair. Fix-It aims to improve two of the most common sources of home repair information: YouTube and ChatGPT. By using RAG, Fix-It is able to provide more specific answers to questions than ChatGPT alone. Additionally, Fix-It is able to provide answers more efficiently than YouTube videos, which are often long drawn-out. Fix-It is able to provide answers to questions such as "How do I fix a leaky faucet?" or "How do I fix a broken window?", giving the user a step-by-step guide to fixing the problem, a difficulty rating, youtube tutorial, and more.

The project is built using a Flask server for the backend and a React frontend. The project is [deployed](https://fixit-ai.azurewebsites.net) on Azure, and has auto-scaling capabilites.

## Use

To use the project, either naviagate to [https://fixit-ai.azurewebsites.net](https://fixit-ai.azurewebsites.net), for follow the steps below to run locally.

The project dependencies are in `backend/requirements.txt` and `frontend/package.json`.

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

## Project Structure

The "Fix-It" home repair assistant project is structured with a modern and efficient architecture, comprising a Flask backend server and a React frontend. This bifurcated setup allows for a seamless division of concerns, where the backend handles API interactions and data processing, while the frontend is responsible for presenting a user-friendly interface. Both the Flask and React components are containerized using Docker, ensuring consistency in the development and deployment environments, and are separately hosted on Azure, providing robust and scalable cloud infrastructure.

The Flask backend is designed with multiple endpoints, each serving a specific function. The /generate_steps endpoint processes user queries to generate step-by-step repair instructions and corresponding YouTube links. The /get_difficulty endpoint retrieves and provides details about the difficulty, time, and cost associated with a repair task. Another crucial endpoint, /elaborate_step, allows for further elaboration on specific repair steps upon user request. These endpoints are equipped with CORS (Cross-Origin Resource Sharing) support, enabling secure and flexible interaction with the React frontend. The Flask application's configuration ensures that responses are properly handled and formatted in JSON, facilitating easy data exchange and integration with the frontend. The entire backend operation is geared towards efficient data handling and rapid response delivery, crucial for a responsive user experience in the interactive web application.

## Data-Driven Reccomendations for Future Improvement

The current state of the Fix-It home repair assistant project indicates areas for significant improvement. Notably, almost 10% of the YouTube videos suggested by the system are irrelevant, highlighting the need for enhanced filtering mechanisms in the backend before presenting these videos to users. While the backend endpoints demonstrate impressive efficiency with an average response time of just 7.5ms, the overall performance is hampered by the lengthy duration of nearly 8000ms required for completing the chain of OpenAI and YouTube API calls, which is a critical factor affecting the user experience. This discrepancy suggests that enhancements in server performance, such as those related to Azure, are unlikely to yield substantial benefits. Instead, the focus should be shifted towards optimizing the efficiency of API calls. Additionally, considering the minimal data transfer involved, approximately 1kB, the system appears to be data-efficient, but this aspect could be further leveraged to streamline operations and reduce response times.