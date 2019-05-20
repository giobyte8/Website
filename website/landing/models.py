from django.db import models

# Create your models here.


class Project(object):
    def __init__(self):
        self.title = None
        self.stack = None
        self.desc = None
        self.link = None
