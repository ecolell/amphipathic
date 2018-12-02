pypi-register:
	@ echo "[ record       ] package to pypi servers"
	@ (python setup.py register -r pypi 2>&1) >> tracking.log
	@ echo "[ registered   ] the new version was successfully registered"

pypi-upload:
	@ echo "[ uploading    ] package to pypi servers"
	@ (python setup.py sdist upload -r https://pypi.python.org/pypi 2>&1) >> tracking.log
	@ echo "[ uploaded     ] the new version was successfully uploaded"

pypitest-register:
	@ echo "[ record       ] package to pypi servers"
	@ python setup.py register -r testpypi
	@ echo "[ registered   ] the new version was successfully registered"

pypitest-upload:
	@ echo "[ uploading    ] package to pypi servers"
	python setup.py sdist upload -r https://testpypi.python.org/pypi
	@ echo "[ uploaded     ] the new version was successfully uploaded"