# create virtual environment
python3 -m venv venv

# create/update requirements.txt
pip freeze > requirements.txt

# change permission
chmod +x ./entrypoint.sh

# up container
docker compose up -d

# down container
docker compose down

# open container shell
docker exec -it container_name /bin/sh