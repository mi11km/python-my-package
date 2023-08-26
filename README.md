# Python playground
個人的にPythonで色々書いたやつを記録。

## Requirements
- `asdf` or `docker`

## Development in local computer
### setup
```shell
make setup-local
```

### test
```shell
make test-local
```

## Development in container
### test
```shell
docker-compose run --rm app pytest tests -v 
```

### add package
```shell
docker-compose run --rm app poetry add <package_name>
```