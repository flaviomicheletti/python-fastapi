![image](https://user-images.githubusercontent.com/1257048/204164980-6e893ff8-f25a-44b9-8baa-1dc6770a3b2d.png)

Some good examples of using the [FASTAPI framework](https://fastapi.tiangolo.com/).


## Instalation

    // your env
    python3 -m venv .venv &&  . .venv/bin/activate

    // in the first time
    pip install fastapi
    pip install uvicorn
    pip install pytest
    pip install httpx

    // or
    pip install -r requirements.txt

    // run
    uvicorn main:app --reload


## Try

+ http://127.0.0.1:8000/
+ http://127.0.0.1:8000/docs
+ http://127.0.0.1:8000/redoc
+ http://127.0.0.1:8000/items/5?q=somequery


## Tests

Run the tests on each folder separately!

    pytest
    pytest -rP
    python -m pytest test_main.py
    pytest --cov . --cov-report html


## Articles

- https://www.linkedin.com/posts/jesumyip_custom-response-html-stream-file-others-activity-7083432591449604097-CSl1
- https://github.com/mjhea0/awesome-fastapi
- https://santoshk.dev/posts/2021/tdd-approach-to-create-an-authentication-system-with-fastapi-part-3/
- https://github.com/mfreeborn/fastapi-sqlalchemy

## Next

- https://fastapi.tiangolo.com/external-links/