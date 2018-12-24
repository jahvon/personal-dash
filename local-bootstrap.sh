sudo apt-get update
sudo apt-get install -yq postgresql libpq-dev libffi-dev \
     python3-pip python3.4-venv jq

su vagrant -c 'cd /vagrant &&
    make env/variables &&
    source ~/.profile &&
    make venv/setup &&
    source vagrant-env/bin/activate &&
    make pip/update &&
    make db/create'