![image](https://user-images.githubusercontent.com/1257048/204164980-6e893ff8-f25a-44b9-8baa-1dc6770a3b2d.png)


Some good examples of using the [Flask framework](https://flask.palletsprojects.com/).


## Instalation

    // your env
    python3 -m venv venv
    . venv/bin/activate

    // in the first time
    pip install fastapi
    pip install uvicorn
    pip install pytest
    pip install httpx

    // run
    uvicorn main:app --reload


## Try

+ http://127.0.0.1:8000/
+ http://127.0.0.1:8000/docs
+ http://127.0.0.1:8000/redoc
+ http://127.0.0.1:8000/items/5?q=somequery


## Tests

See the example [extende_test/](04extented_test/).

![image](https://user-images.githubusercontent.com/1257048/206860950-4cac2e58-a5c9-41b9-add2-06c83bddf7c0.png)


## Awesome

- https://github.com/mjhea0/awesome-fastapi