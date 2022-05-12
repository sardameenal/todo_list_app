# todo_list_app
To set up the djago enviroment
1. Open command prompt and veify if python is installed. (if not then download the latest stable version of python)
>> python --version

2. create virtual environment (test)
>> py -m create venv test 

3. activate the virtual environment
>> test\Scripts\activate.bat
(now here the test environment will be activated)

4. Install django
>> py -m pip install django
Verify the django version
>> djnago-admin --verison

5. Move to respective directory using the cd command and then create myproject app
>> django-admin startproject myproject
this will create a myproject project in your current directory.

6. Now open any editor (here we have used VSCode editor)
Open the folder where your project is.
7. Open the terminal and select cmd. Then activate the test virtual enviroment (also set the virtual enviornment as the python interpreter by goinf to views>command pallete>Python:select interpreter)
create an app todo
>>py manage.py startapp todo

8. Navigate to settings.py/myproject and in the installed apps field add todo app
9. In the terminal run py manage.py runserver
