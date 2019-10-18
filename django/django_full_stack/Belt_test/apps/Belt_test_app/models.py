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
            errors['email_not_exist'] = "I cannot find your email! Please double check everything."
        return errors

class InputChecker_trip(models.Manager):
    def basic_validator3(self, postData):
        errors = {}
        if len(postData["Desination_add"]) < 3:
            errors['Desination_add_to_short'] = "Sorry, but a trip destination must consist of at least 3 characters"
        if len(postData["Plan_add"]) < 3:
            errors['Plan_add_to_short'] = "Sorry, but a trip plan must consist of at least 3 characters"
        if postData["Start_date_add"] != "":
            if datetime.strptime(postData["Start_date_add"], '%Y-%m-%d') < datetime.now():
                errors["Start_date_NOT_in_the_future"] = "Sorry the start date need to be in the future."
        else:
            errors["not_Start_date_input"] = "You need to enter your Start date!"
        if postData["End_date_add"] != "":
            if datetime.strptime(postData["End_date_add"], '%Y-%m-%d') < datetime.strptime(postData["Start_date_add"], '%Y-%m-%d'):
                errors["Start_date_NOT_in_the_future"] = "Sorry the end date should be after the start date."
        else:
            errors["not_End_date_input"] = "You need to enter the End date!"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = InputChecker()

class Trip(models.Model):
    Destination = models.CharField(max_length=45)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    plan = models.TextField()
    users_who_go = models.ManyToManyField(User, related_name="travlers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_by_who")
    objects = InputChecker_trip()
