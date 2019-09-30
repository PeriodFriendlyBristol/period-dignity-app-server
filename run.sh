
sleep 3

python server/manage.py makemigrations venue
python server/manage.py makemigrations contact
python server/manage.py migrate

python server/manage.py runserver 0.0.0.0:8000
