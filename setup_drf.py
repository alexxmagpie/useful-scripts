# -*- coding: utf-8 -*-

import os
import pip
import sys
import subprocess


proj_name = raw_input("Enter new project name: ")
app_name = raw_input("Enter first app name (or leave it empty to ignore creation): ")


os.makedirs(proj_name)
os.chdir(proj_name)
p = subprocess.Popen(['virtualenv', 'venv'])
p.communicate()

execfile('venv/bin/activate_this.py', dict(__file__='venv/bin/activate_this.py'))

pip.main(['install', 'django-extensions'])
pip.main(['install', 'djangorestframework'])
pip.main(['install', 'Django'])
pip.main(['install', 'markdown-editor'])
pip.main(['install', 'django-nose'])

django_admin = os.getcwd() + '/venv/bin/django-admin.py'
venv_python = os.getcwd() + '/venv/bin/python'

p = subprocess.Popen([venv_python, django_admin, 'startproject', proj_name])
p.communicate()

os.chdir(proj_name)
os.makedirs('static')
os.makedirs('static/js')
os.makedirs('static/css')
os.makedirs('templates')

if app_name:
    subprocess.Popen([venv_python, django_admin, 'startapp', app_name])

if app_name:
    sys.stdout.write("Django %s project successfully created with %s application name.\n" % (proj_name, app_name))
else:
    sys.stdout.write("Django %s project successfully created.\n" % proj_name + \
                    "Don't forget to configure settings py for django-extensions and django-nose.")

