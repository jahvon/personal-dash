SHELL = /bin/bash
WORKDIR = /vagrant

PSQL = sudo -u postgres psql
DBNAME = personaldash
DBUSER = jahvon
DBPASS = secret

define GetFromConfig
	$(shell jq .$(1) env-config.json)
endef

CLIENT_ID = $(call GetFromConfig,client_id)
CLIENT_SECRET = $(call GetFromConfig,client_secret)

db/console:
	$(PSQL) $(DBNAME)

db/create: db/create/user db/create/database

db/create/database:
	@echo "--> create DB"
	$(PSQL) -c "CREATE DATABASE $(DBNAME) OWNER $(DBUSER);"

db/create/user:
	@echo "--> create DB user"
	$(PSQL) -c "CREATE USER $(DBUSER) WITH PASSWORD '$(DBPASS)';"

db/seed:
	python seed.py

flask/run:
	flask run --host=0.0.0.0 --cert cert.pem --key key.pem

flask/db:
	flask db migrate
	flask db upgrade

pip/freeze:
	@echo "--> saving python dependencies to requirements.txt"
	pip3 freeze > requirements.txt

pip/update:
	@echo "--> updating python dependencies from requirements.txt"
	pip3 install -r requirements.txt

venv/setup: venv/setup_virtualenv venv/setup_shell

venv/setup_shell:
	@echo "--> configuring python environment"
	(test -f ~/.bash_profile  && grep vagrant-env/bin/activate ~/.bash_profile) || \
		echo "cd $(WORKDIR) && source vagrant-env/bin/activate" >> ~/.bash_profile

venv/setup_virtualenv:
	@echo "--> creating python virtual environment"
	test -d vagrant-env || python3 -m venv vagrant-env

env/variables:
	@echo "--> setting environment variables"
	(test -f ~/.bash_profile && grep /.profile ~/.bash_profile) || \
		(echo "source ~/.profile" >> ~/.bash_profile && \
		echo "export FLASK_APP=manage.py" >> ~/.profile && \
		echo "export FLASK_ENV=development" >> ~/.profile && \
		echo "export APP_SETTINGS=config.DevelopmentConfig" >> ~/.profile && \
		echo "export SECRET_KEY=secretssecretsarenofun1" >> ~/.profile && \
		echo "export DATABASE_URL=postgresql://jahvon:secret@localhost/personaldash" >> ~/.profile && \
		echo "export CLIENT_ID=$(strip $(CLIENT_ID))" >> ~/.profile && \
		echo "export CLIENT_SECRET=$(strip $(CLIENT_SECRET))" >> ~/.profile)

gen/ssl:
	openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
