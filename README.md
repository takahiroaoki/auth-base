# auth-base

## Requiements
The environment is bellow.

- Windows 11
- Docker Desktop for Windows 4.2.0
- VSCode + Remote Development 0.21.0（VSCode extensions）

## Initial setup
```
# @project root
$ docker compose build
$ docker compose up -d

# Initialize the database. Type "password" when asked.
$ docker exec -it auth-base_db /bin/bash /scripts/setup.sh
```

Then, get access to http://localhost:8000/docs