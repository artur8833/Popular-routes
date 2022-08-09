ENV := export FLASK_APP=webapp && export FLASK_ENV=development && export FLASK_DEBUG=1

run:
	${ENV} && flask run

db_init:
	${ENV} && flask db init

db_head:
	${ENV} && flask db stamp head

db_upgrade:
	${ENV} && flask db upgrade