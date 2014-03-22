.SILENT:
run:
	python news_map/manage.py runserver

syncdb:
	python news_map/manage.py syncdb

test:
	python news_map/manage.py test

create-migration:
	python news_map/manage.py schemamigration $(appName) --initial

run-migrate:
	python news_map/manage.py migrate $(appName)