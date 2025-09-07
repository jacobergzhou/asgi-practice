# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimal ASGI (Asynchronous Server Gateway Interface) practice project containing a raw ASGI application implementation. The project demonstrates low-level ASGI concepts without using frameworks like FastAPI or Django.

## Architecture

- **raw_asgi.py**: Contains a basic ASGI application that handles HTTP requests directly using the ASGI protocol. The app reads request body, sends HTTP response headers, and returns a simple "Hello ASGI!" message.

## Running the Application

Since this is a raw ASGI application, it needs an ASGI server to run:

```bash
# Install an ASGI server (uvicorn is commonly used)
pip install uvicorn

# Run the application
uvicorn raw_asgi:app --reload
```

Alternatively with other ASGI servers:
```bash
# With hypercorn
pip install hypercorn
hypercorn raw_asgi:app --reload

# With daphne
pip install daphne
daphne raw_asgi:app
```

## Development Notes

- The application directly implements the ASGI interface without using any web framework
- It demonstrates the basic ASGI message flow: receive → process → send
- The code shows manual HTTP request body reading and response construction
- No dependencies are currently defined in the project