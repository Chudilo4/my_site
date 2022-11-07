start:
	poetry run python coolsite/manage.py runserver
makemigration:
	poetry run python coolsite/manage.py makemigrations
migrate:
	poetry run python coolsite/manage.py migrate

