# WebSockets

https://fastapi.tiangolo.com/advanced/websockets/

If you see the following error:

    Unsupported upgrade request.
    WARNING:  No supported WebSocket library detected. Please use 'pip install uvicorn[standard]', or install 'websockets' or 'wsproto' manually.


Solve this by installing the dependency below:

    pip install uvicorn[standard]