# pyNTakeApp
pyNTakeApp is a submission/intake system for 3D prints, specifcally designed for Makerspaces and startup like spaces. It allows for users to easily submit prints, and for the makerspaces to easily adapt the system to their needs and capability. Currently running on a Heroku dyno and Postgres database with file storage on Google Cloud Storage, can be adapted to a variety of storage options and databases through Django Storage and built-in Django functionality respectively.

## Technology Stack:
- Django
- Django Storages
- Google Cloud Storage*
- Gunicorn*
- Postgres*
- Sqreen**
- Timber.io**
- Dj-Database-Url*
- Crispy Forms
- Django Smart Selects
- WhiteNoise
- Boostrap 4/Argon Design System

* -- Other providers/solutions can be used - Outlines in install.txt
** -- Not necessary for operation - Used with Heroku
