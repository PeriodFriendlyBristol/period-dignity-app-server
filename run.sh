set -e

I=0
while ! nc -z postgres-server 5432; do
  sleep 1 # wait for ostara-db port to be open
  I=$((I+1))
  if [ $I == 300 ]
  then
      echo "ostara db port 5432 still not open after 5min EXITING"
      exit 1
  fi
done

python3 manage.py makemigrations

python3 manage.py migrate

# TODO admin user must be made manually in production
python3 manage.py shell < tools/create_admin.py

python3 manage.py runserver 0.0.0.0:8000
