clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

test: clean
	# --capture=sys allows us capture print() output
	py.test --verbose --cov=test --capture=sys --color=yes test/
# 	bats test/test_unix