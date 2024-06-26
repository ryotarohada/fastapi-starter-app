# fastapi-starter-app

Templates for quickly building commonly configured web applications.

## Docker Compose

```sh
docker-compose up -d --build # Container Build & Launch
docker-compose down # Container termination/deletion
```

## Virtual environment

### Generate

```sh
python3 -m venv .venv
```

### Activate

activate

```sh
source .venv/bin/activate
```

### Deactivate

```sh
deactivate
```

## Install packages

```sh
pip install -r requirements.txt
```

## Linter & Formatter

The code is maintained by `flake8`, `black` and `isort`.
The way to run flake8 and black is to type the command or save the file (vscode extension works).

### Command of flake8.

```sh
flake8 app
```

### Command of black.

```sh
python -m black app
```

### Command of isort.

```sh
isort app --settings-file isort.toml
```

### Command of execute all.

```sh
sh format.sh
```
