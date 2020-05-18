# This repository represents Docker configuration for Django-applications.
## Features of this configuration are mobility and scalability. Also, thanks to the config.py file, you can easily switch between local and real development.

## Deployment instruction
1. Pre-requirements: Need to install docker and docker-compose.
1. Clone repository to necessary directory(for example to `/opt`)
1. Rename `.env.example` to `.env` and set necessary passwords and secrets instead of default.
1. Optionally. To set custom config use example and docker-entrypoint won't overwrite it `django_api/django_project/config.py.example` to fill `config.py` and fill it. To keep default settings, leave it without changes.
1. Build a docker image using: `docker-compose build` and launch it with: `docker-compose up -d`
1. After completing deploy (only once or after clean deployment) need to run:

`docker exec -it django_project bash`

* and then run:

`python manage.py createsuperuser`

For updating application need to pull changes to repository and then run `docker-compose up -d --build` for changes implementation.

## The repository structure
```
.
├── data
│   └── postgress [error opening dir]
├── docker
│   ├── nginx
│   │   └── metro-admin.conf (nginx config for proxy requests to web service)
│   └── web
│       └── docker-entrypoint.sh (a start script for web service)
├── .env.example (need to rename to `.env` and fill credentials and secrets)
├── docker-compose.yml (deployment config)
├── Dockerfile (docker environment for python application)
├── django_api
│   ├── django_project
│   │   ├── config.py
│   │   ├── config.py.example (default config, that will be used if config.py won't be found)
...
│   ├── manage.py (console management tool)
│   ├── media
│   ├── requirements.txt
│   ├── static
...
└── README.md

```

