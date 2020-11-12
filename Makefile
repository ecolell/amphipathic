pypi-register:
	@ echo "[ record       ] package to pypi servers"
	@ (python setup.py register -r pypi 2>&1) >> tracking.log
	@ echo "[ registered   ] the new version was successfully registered"

pypi-upload:
	@ echo "[ uploading    ] package to pypi servers"
	python setup.py sdist bdist_wheel
	twine upload dist/amphipathic-1.0.0*
	@ echo "[ uploaded     ] the new version was successfully uploaded"
