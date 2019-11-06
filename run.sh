set -e

sleep 3

python3 manage.py migrate

# TODO admin user must be made manually in production
python3 manage.py shell < server/tools/create_admin.py

python3 manage.py runserver 0.0.0.0:8000
