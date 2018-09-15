# Challenger System
This is a system that users propose challenges for themselves.

<center>

![Azazel](https://img.shields.io/badge/challenger--system-Top-brightgreen.svg)
![PyPI](https://img.shields.io/pypi/v/nine.svg)
![GitHub top language](https://img.shields.io/github/languages/top/agata-project/azazel.svg)

[![Build Status](https://travis-ci.org/cuzik/challenges-system.svg?branch=master)](https://travis-ci.org/cuzik/challenges-system)
[![Coverage Status](https://coveralls.io/repos/github/cuzik/challenges-system/badge.svg)](https://coveralls.io/github/cuzik/challenges-system)

</center>

## Table of Contents

* [Environment](#environment)
  * [Dependences](#environment-dependences)
  * [Init](#environment-init)
  * [Variables](#environment-variables)
* [Development](#development)
* [Run](#run)

## Environment

### Environment Dependences

* Postgresql 10.4
* Python 3.6.5
* pyenv
* pipenv

### Environment Init

* open shell end load `.env`

```sh
pipenv shell
```

* install `python` dependences

```sh
pipenv install
pipenv install --dev
```

### Environment Variables

cp .env.example .env

## Development

### Create DB

```sh
pipenv run setupdbdev
pipenv run setupdbtest
```

```sh
pipenv run migrate
```

## Run

```sh
pipenv run server
```


## Todo

- Add validators on `ChallangeForm()`.
- Add messages to sessions.
- Change messages from alarts to flashs.
- Add tests.
- Add I18n.
- Add thumb of image on challenge/edit.
- Better buttons to number of `point` and `achievements`.
