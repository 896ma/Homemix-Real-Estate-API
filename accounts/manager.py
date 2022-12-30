from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    '''
    custom user model where email is the unique identifier for authentication instead of username

    '''
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email or not password:
            raise ValueError("Users must have an email and password")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


