set -e

sleep 3

python3 server/manage.py migrate

# TODO admin user must be made manually in production
python3 server/manage.py shell < server/tools/create_admin.py

python3 server/manage.py runserver 0.0.0.0:8000
