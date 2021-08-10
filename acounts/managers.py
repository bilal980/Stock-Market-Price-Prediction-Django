from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManger(BaseUserManager):
    def create_user(self, email, password,**extrafields):
        if not email:
            raise ValueError(_('Email must be set!'))
        email=self.normalize_email(email)
        user=self.model(email=email,**extrafields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extrafields):

        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)
        if extrafields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extrafields.get("is_superuser") is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **extrafields)