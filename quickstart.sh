#! /bin/bash

echo "Create virtual env"
virtualenv venv
echo "Start virtual env"
. venv/bin/activate
echo "Install dependencies"
pip install pyyaml
pip install click
pip install psycopg2
echo "Install Datahub-clt"
pip install --editable .
echo "Done. Run Datahub-clt --help for INFO. To quit virtualenv, type deactivate"
