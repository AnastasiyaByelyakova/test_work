# Project Setup

This project uses Poetry for dependency management.

### 1. Project Setup

To set up the project, navigate to the project's root directory and run the following commands. 

1) To nstall poetry dependency management package
  
```bash
pip install poetry
```

2) To create a virtual environment and install the dependencies:

```bash
poetry install
```

### 2. Activating the Environment

Once the dependencies are installed, activate the virtual environment with the following command:

```bash
poetry env activate
```

### 3. Running the Service

To run the FastAPI service, execute the following command from the project's root directory:

```bash
python main.py
```

The service will be available at `http://localhost:8000`.

### 4. Using the Service

You can use any HTTP client to interact with the service. Here's an example using `curl` to get 5 items:

```bash
curl "http://localhost:8000/process-items/?limit=5"
```
