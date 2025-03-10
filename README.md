# Code Similarity Checker

## Overview

This project compares two code snippets and detects similarities using efficient string-matching algorithms.

## Tech Stack

- **Backend:** Flask (Python), Flask-CORS
- **Frontend:** React (Vite), Tailwind CSS
- **Algorithms Used:** KMP String Matching, Trie, Rolling Hash

## Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/code-similarity-checker.git
   cd code-similarity-checker
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   pip install flask flask-cors
   ```
3. Run the backend:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies and start the server:
   ```bash
   npm install
   npm run dev
   ```

## API Endpoint

### Compare Two Code Snippets

**Endpoint:** `POST /compare`

**Request Body:**

```json
{
    "code1": "<first code snippet>",
    "code2": "<second code snippet>"
}
```

**Response:**

```json
{
    "similarity": 85.6,
    "message": "Comparison successful"
}
```

