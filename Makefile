pypi-register:
	@ echo "[ record       ] package to pypi servers"
	@ (python setup.py register -r pypi 2>&1) >> tracking.log
	@ echo "[ registered   ] the new version was successfully registered"

pypi-upload:
	@ echo "[ uploading    ] package to pypi servers"
	python setup.py sdist bdist_wheel
	twine upload dist/amphipathic-1.0.11*
	@ echo "[ uploaded     ] the new version was successfully uploaded"


POETRY := docker run --rm -v $(PWD):/app ecolell/poetry:3.10-slim


extract-requirements:
	docker build -f Dockerfile.poetry --tag ecolell/poetry:3.10-slim --build-arg PORT=5000 .
	$(POETRY) export --without-hashes -f requirements.txt --output requirements.txt
	$(POETRY) export --without-hashes --only dev -f requirements.txt -o requirements_development.txt


check-safety:
	safety check --full-report -r requirements.txt || true

check-bandit:
	bandit -r amphipathic/*.py -x tests

check-radon:
	radon cc -nb -a amphipathic

check-mypy:
	mypy  --follow-imports=skip

pipeline-test:
	pytest -s --junitxml=pytest$(PYVERSION).xml

check: check-safety check-radon check-bandit