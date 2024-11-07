# Civic Education Backend

About project

## How to run

1. Clone the repository
2. Navigate into project root - `cd backend`
3. Create a virtual environment

```shell
python3 -m virtualenv venv
```

4. Activate virtual environment

```shell
source ./venv/bin/activate
```

5. Run the server

```shell
python3 manage.py runserver
```

To make migrations run

```shell
python manage.py makemigrations && python manage.py migrate
```