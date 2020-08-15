coding_practice
=====
##### 
This project is for storing practice problem's solution implementations


setup
=====
##### 

* Required
    * python3.7+
    * pip3
* setup virtual environment (optional)
	* `python3 -m pip install --user virtualenv`
	* `python3 -m venv venv`
	* `source venv/bin/activate`
* download dependencies
	* `pip3 install -r requirements.txt` 
	* `brew install bats`
* confirm repo in `PYTHONPATH`
	* example:
		* add to `~/.bash_profile`:
			* `export PYTHONPATH="${PYTHONPATH}:/Users/william/Documents/code/coding_practice"`
			* `export PYTHONPATH`
		* commit update
			* `source ~/.bash_profile`



testing
=====
##### 
* **test/**
   * `make test`