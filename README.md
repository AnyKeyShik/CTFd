# ![](https://github.com/CTFd/CTFd/blob/master/CTFd/themes/core/static/img/logo.png?raw=true)

## What is CTFd?

CTFd is a Capture The Flag framework focusing on ease of use and customizability. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes.

![CTFd is a CTF in a can.](https://github.com/CTFd/CTFd/blob/master/CTFd/themes/core/static/img/scoreboard.png?raw=true)

## Install

1. Install [Docker](https://docs.docker.com/install/)
2. Install [Docker compose](https://docs.docker.com/compose/install/)
3. Clone this repo
4. Run `head -c 64 /dev/urandom > .ctfd_secret_key` at the root of this repo
5. Run `docker-compose up -d`
6. Wait
7. Profit. You get CTFd at [http://localhost:8000/](http://localhost:8000/)

## For production deploy

* Change `debug` mode in [wsgi.py](./wsgi.py)
* Change `FLASK_ENV` to `production` in [.flaskenv](./.flaskenv)
* Remove expose port for `ctfd` container in docker compose
* Setup nginx for SSL (TODO: Upload example config)
