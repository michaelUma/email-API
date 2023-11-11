from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,BaseUserManager)

from uuid import uuid4

class Usermanager(BaseUserManager):

    def create_user(self,email, password, **exrtra_fields):
        if not email:
            raise ValueError
        user = self.model(email=self.normalize_email(email),**exrtra_fields)
        user.set_password(password)
        user.save()
        return user 


    def create_superuser(self,username ,email,password=None, **extra_fields):
        user = self.create_user(email=email,username=username, password=password)
        user.is_superuser = True 
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    objects = Usermanager()