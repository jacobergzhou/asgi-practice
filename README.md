# ASGI Practice Project

A learning project exploring ASGI (Asynchronous Server Gateway Interface) concepts through both raw ASGI implementation and FastAPI framework comparison.

## Project Overview

This repository demonstrates the progression from low-level ASGI protocol handling to high-level FastAPI framework usage, helping understand the underlying concepts that make modern async Python web frameworks possible.

## Files Description

### `raw_asgi.py`
A minimal ASGI application implementation that:
- Directly implements the ASGI interface without any framework
- Manually handles the ASGI message flow: `receive` → `process` → `send`
- Demonstrates low-level HTTP request body reading and response construction
- Returns a simple "Hello ASGI!" message for all requests

### `fastapi_version.py`
A FastAPI implementation featuring:
- **GET `/`**: Simple root endpoint
- **GET `/users`**: Endpoint with query parameters (`page`, `limit`)
- **POST `/echo`**: Endpoint accepting JSON request body using Pydantic validation
- Demonstrates async/await pattern, request validation, and automatic API documentation

### `CLAUDE.md`
Project-specific instructions for AI assistants working with this codebase.

## Prerequisites

- Python 3.7+
- Anaconda or Miniconda

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd ASGIPractice
```

2. Create and activate conda environment:
```bash
# Create new conda environment
conda create -n asgi-practice python=3.9

# Activate the environment
conda activate asgi-practice
```

3. Install dependencies:
```bash
# For FastAPI version
conda install -c conda-forge fastapi uvicorn

# Or using pip within conda environment
pip install fastapi uvicorn

# Alternative ASGI servers (optional)
pip install hypercorn  # or
pip install daphne
```

## Running the Applications

### Raw ASGI Application

```bash
# Using uvicorn
uvicorn raw_asgi:app --reload

# Using hypercorn
hypercorn raw_asgi:app --reload

# Using daphne
daphne raw_asgi:app
```

Access at: `http://localhost:8000`

### FastAPI Application

```bash
uvicorn fastapi_version:app --reload
```

Access at:
- **Application**: `http://localhost:8000`
- **Interactive API Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`

## API Endpoints (FastAPI Version)

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/` | Root endpoint | None |
| GET | `/users` | Get users list | `page` (int, default: 1), `limit` (int, default: 10) |
| POST | `/echo` | Echo request data | JSON body: `{"name": "string", "age": integer}` |

## Example Usage

### Testing the FastAPI endpoints:

```bash
# GET request with query parameters
curl "http://localhost:8000/users?page=2&limit=5"

# POST request with JSON body
curl -X POST "http://localhost:8000/echo" \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "age": 25}'
```

## Learning Objectives

This project illustrates:

1. **Raw ASGI**: Understanding the foundational ASGI protocol
2. **FastAPI Magic**: How frameworks abstract away ASGI complexity
3. **Async Programming**: Proper use of `async`/`await` in web applications
4. **Request Validation**: Pydantic models for type safety and validation
5. **Automatic Documentation**: FastAPI's built-in API documentation generation

## Key Differences

| Aspect | Raw ASGI | FastAPI |
|--------|----------|---------|
| Code Complexity | Manual message handling | Decorator-based routing |
| Request Parsing | Manual body reading | Automatic with Pydantic |
| Validation | None | Built-in with type hints |
| Documentation | None | Auto-generated |
| Error Handling | Manual | Automatic HTTP status codes |