# python_learning
Python repo creating a new item

once those are done update pip to the latest version
* python.exe -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip

execute the following in the base folder
* cd {base_folder}
* create a README.md file similar to this and add a description
* py -m venv ./.venv
* ./venv/Scripts/Activate.ps1
* pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org pytest
* pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org pylint
* any additional libraries you need to install
* python -m pip --trusted-host pypi.org --trusted-host files.pythonhosted.org freeze > requirements.txt
then commit the requirements file.



Usefull commands
py <script>.py -> run the said script in windows
pytest <script>_test.py -> run the unit tests associated with your scipt
pylint <script>.py or <script>_test.py -> run linter against script or test script to ensure proper formatting/annotations

within the content folder run the following
py -m pydoc -b -> Should pop open a web browser with a huge amount of documentation to include what was added in by your code.

