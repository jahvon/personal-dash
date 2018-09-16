SHELL = /bin/bash
WORKDIR = /vagrant

PSQL = sudo -u postgres psql
DBNAME = personaldash
DBUSER = jahvon
DBPASS = secret

db/console:
	$(PSQL) $(DBNAME)

db/create: db/create/user db/create/database

db/create/database:
	@echo "--> create DB"
	$(PSQL) -c "CREATE DATABASE $(DBNAME) OWNER $(DBUSER);"

db/create/user:
	@echo "--> create DB user"
	$(PSQL) -c "DROP ROLE IF EXISTS $(DBUSER);"
	$(PSQL) -c "CREATE USER $(DBUSER) WITH PASSWORD '$(DBPASS)';"

db/seed:
	python seed.py

flask/server:
	python run.py

pip/freeze:
	@echo "--> saving python dependencies to requirements.txt"
	pip freeze > requirements.txt

pip/update:
	@echo "--> updating python dependencies from requirements.txt"
	pip install -r requirements.txt

venv/setup: venv/setup_virtualenv venv/setup_shell

venv/setup_shell:
	@echo "--> configuring python environment"
	(test -f ~/.bash_profile  && grep venv/bin/activate ~/.bash_profile) || \
		echo "cd $(WORKDIR) && source venv/bin/activate" >> ~/.bash_profile

venv/setup_virtualenv:
	@echo "--> creating python virtual environment"
	test -d venv || virtualenv venv
