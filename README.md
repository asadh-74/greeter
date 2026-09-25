# greeter

A tiny Python web app that shows a greeting with my name. Built as part of the
"Ship a Containerized App with Git & Docker" exercise.

## Run it directly

```bash
python3 app.py
```

Then open http://localhost:8080

## Run it with Docker

```bash
docker build -t greeter:1.0 .
docker run -d -p 8080:8080 --name greeter greeter:1.0
```

Then open http://localhost:8080
