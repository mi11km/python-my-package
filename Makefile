PORT=8080

TEST_COMMAND=pytest tests -v
FORMAT_COMMAND=black .
LINT_COMMAND=flake8 --ignore=E501 src/ tests/
SORT_COMMAND=isort .

run:
	poetry run python -m src

test:
	poetry run ${TEST_COMMAND} && \
	poetry run ${FORMAT_COMMAND} && \
	poetry run ${LINT_COMMAND} && \
	poetry run ${SORT_COMMAND}

build-container:
	docker build -t app . && docker image prune --force

run-container: build-container
	docker run \
		-v $(shell pwd):/src \
		-p ${PORT}:${PORT} \
		--rm api

test-in-container: build-container
	docker run \
		-v $(shell pwd):/api \
		--rm api \
		bash -c '${TEST_COMMAND} && ${FORMAT_COMMAND} && ${LINT_COMMAND} && ${SORT_COMMAND}'
