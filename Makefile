CONTAINER_TAG=python-app

FORMAT_COMMAND=black .
SORT_COMMAND=isort .
TEST_COMMAND=pytest tests -v
LINT_COMMAND=flake8 --max-line-length 119 src/ tests/
TYPE_CHECK_COMMAND=mypy .

add-plugin:
	- asdf plugin-add python https://github.com/danhper/asdf-python.git
	- asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git

setup-local: add-plugin
	asdf install
	poetry config virtualenvs.in-project true
	poetry install

run-local:
	poetry run python __main__.py

test-local:
	poetry run ${FORMAT_COMMAND} && echo "\n" && \
	poetry run ${SORT_COMMAND}  && echo "===== Finish Format =====\n" && \
	poetry run ${TEST_COMMAND} && echo "===== Finish Test =====\n" && \
	poetry run ${LINT_COMMAND} && echo "===== Finish Lint =====\n" && \
	poetry run ${TYPE_CHECK_COMMAND} && echo "===== Finish Type Check =====\n"


build-container:
	docker build -t ${CONTAINER_TAG} . && docker image prune --force

run-container: build-container
	docker run --rm ${CONTAINER_TAG}

test-container: build-container
	docker run --rm ${CONTAINER_TAG} \
		bash -c 'poetry install && ${TEST_COMMAND} && ${FORMAT_COMMAND} && ${LINT_COMMAND} && ${SORT_COMMAND} && ${TYPE_CHECK_COMMAND}'
