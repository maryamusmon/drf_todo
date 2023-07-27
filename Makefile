mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver

admin:
	python3 manage.py createsuperuser

req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
