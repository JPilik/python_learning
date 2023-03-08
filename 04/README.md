# First thing to work on with just Python basics
Write the code to print out "Hello, World" with a carriage return
on the end that will pass the linting rules and a test that verifies it works.

# To prepare the repo for work run the following commands
```
cd 03
py -m venv ./venv
./venv/Scripts/Activate.ps1
pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
cd content

start this up with the following command

uvicorn main:app --reload
then access it via http://127.0.0.1:8000 and http://127.0.0.1:8000/docs
```
Then attemp to make it all work the file should pass tests when pytest is ran and it should pass when pylint is ran against hellow world

This is a work in progress as we move forward im hopeful these will be less messy.