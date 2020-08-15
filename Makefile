clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

test: clean
	py.test --verbose --color=yes test/
# 	bats test/test_unix