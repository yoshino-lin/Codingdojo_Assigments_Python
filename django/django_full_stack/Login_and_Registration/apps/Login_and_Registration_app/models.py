from __future__ import unicode_literals
from django.db import models
import re
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
from datetime import datetime

class InputChecker(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #检查字符长度
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        #检查邮箱地址是否非法
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Are you kidding me? This is not even an invalid email address!"
        #检查邮箱是否唯一
        email_list_exist = User.objects.filter(email = postData['email'])
        if len(email_list_exist)>0:
            errors["not_unique_email"] = "Some one already used this email to regist an account!"
        if len(postData["password"]) < 8:
            errors["password"] = "Hey! Did you know that your password should be at least 8 characters?!"
        if postData["password"] != postData["password_confirm"]:
            errors["password_not_match"] = "The passwords do not match! Do you know how to copy and paste?"
        if (datetime.now() - datetime.strptime(postData["birthday"], '%Y-%m-%d')).days < 365*13:
            if datetime.strptime(postData["birthday"], '%Y-%m-%d') > datetime.now():
                errors["birthday_in_the_future"] = "Sorry you cannot born in the future."
            else:
                errors["not_old_enough"] = "Sorry kiddo you are not old enough."

        return errors
    def basic_validator_2(self, postData):
        errors = {}
        try:
            user = User.objects.get(email = postData["email_login"])
            if bcrypt.checkpw(postData['password_login'].encode(), user.password.encode()):
                pass
            else:
                if len(postData["password_login"]) < 8:
                    errors["password_login"] = "Hey! Did you know that your password must be at least 8 characters?!"
                else:
                    errors['password_not_correct'] = "The password is not correct!"
        except ObjectDoesNotExist:
            errors['email_not_exist'] = "I cannot fin your email! Please double check everything."
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = InputChecker()
