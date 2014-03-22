.SILENT:
run:
	python news_map/manage.py runserver

syncdb:
	python news_map/manage.py syncdb

test:
	python news_maps/manage.py test 