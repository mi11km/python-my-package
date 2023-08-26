PORT=8080

FORMAT_COMMAND=yapf -i -r src/ tests/
SORT_COMMAND=isort .
TEST_COMMAND=pytest tests -v
LINT_COMMAND=flake8 --max-line-length 119 src/ tests/


setup-local:
	asdf install
	poetry config virtualenvs.in-project true
	poetry install

run-local:
	poetry run python -m src

test-local:
	poetry run ${FORMAT_COMMAND} && echo "\n" && \
	poetry run ${SORT_COMMAND}  && echo "===== Finish Format =====\n" && \
	poetry run ${TEST_COMMAND} && echo "===== Finish Test =====\n" && \
	poetry run ${LINT_COMMAND} && echo "===== Finish Lint =====\n"



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
