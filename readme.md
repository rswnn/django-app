how to run in local?
clone : 
* git clone https://github.com/rswnn/django-app.git
create virtal environment:
* mkvirtualenv mywebsite
* pip install -r requirements.txt
Duplicate mywebsite/mywebsite/local_settings_example.py and save as local_settings.py.

Enter your database settings in local_settings.py.

* Initialize your database.

* python ./manage.py syncdb
* python ./manage.py migrate

* python ./manage.py createsuperuser

run server with 

* pyhton manage.py runserver



* <============================== run in your terminal