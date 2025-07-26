# Python HTTP Redirect Demo

This is a simple demonstration of HTTP behavior using the `python -m http.server` command.

- Simulates a basic file server
- Demonstrates 404 errors (like `favicon.ico` not found)
- Includes a client-side redirect (via HTML meta refresh or JavaScript)
- Also shows how to simulate a 302 redirect using a crafted `index.html`

## How to Use

1. Run: `python -m http.server`
2. Open your browser to: `http://localhost:8000`

This project is used to teach students how HTTP works — including status codes like 200, 302, and 404.
