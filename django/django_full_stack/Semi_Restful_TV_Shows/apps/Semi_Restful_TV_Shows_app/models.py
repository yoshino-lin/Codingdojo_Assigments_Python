from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #检查字符长度
        if len(postData["title_add"]) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData["network_add"]) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData["description_add"]) != 0:
            if len(postData["description_add"]) < 10:
                errors["description"] = "Description should be at least 10 characters"
        try:
            get_item = Show.objects.get(title = postData["title_add"])
            if get_item != None:
                errors["Same title"] = "The title must be unqiue"
        except ObjectDoesNotExist:
            pass
        if datetime.strptime(postData["release_date_add"], '%Y-%m-%d') > datetime.now():
            errors["release_date"] = "Release Date cannot be in the future."
        """
        #检查邮箱地址是否非法
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        """
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
