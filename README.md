# Python playground
個人的にPythonで色々書いたやつを記録。

## Requirements
- `asdf` or `docker`

## Development in local computer
### setup
```shell
make setup-local
```

### run
```shell
make run-local
```

### test
```shell
make test-local
```

### add dependency
```shell
poetry add ${PACKAGE_NAME}
```
開発環境のみの依存パッケージインストールは`--group dev`をつける

## Development in container
### run
```shell
make run-container
```

### test
```shell
make test-container
```