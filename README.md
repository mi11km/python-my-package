# python playground
個人的にPythonで色々書いたやつを記録。

## requirements
- poetry
- docker

### test
```shell
docker-compose run --rm app pytest tests -v 
```

### add package
```shell
docker-compose run --rm app poetry add <package_name>
```