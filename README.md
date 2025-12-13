# Mini-RAG

A minimal implementation of a Retrieval-Augmented Generation (RAG) model for question answering.

## Requirements

- Python **3.12.10**

## Installation

### 1. Install Python

Download and install Python from the official website:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Install the required packages

```bash
$ pip install -r requirements.txt
```

### 4. Setup the enviornment variables

```bash
$ cp .env.example --> .env
```

Set your environment variable in the `.env` file. Like `OPENAI_API_KEY` value.

### 5. Run the FastAPI Server

```
uvicorn main:app --reload --host 0.0.0.0 --port 3000
```
