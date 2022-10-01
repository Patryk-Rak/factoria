from django.db import models
from datetime import datetime , timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class BasicManager(BaseUserManager):
    def create_user(self, email, name, phone, picture, password):
        email = self.normalize_email(email)
        user = self.model(
            name=name,
            phone=phone,
            picture=picture
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


def picture_path_file_name(instance, filename):
    print(instance.id)
    print(instance.name)
    return 'clients/'+'/'.join(filter(None, (str(instance.id), filename)))


class Client(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to=picture_path_file_name)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now())
    last_login = models.DateTimeField(null=True)

    object = BasicManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    # zapisuje instancje wyciaga id i zapisuje obraz
    def save_intance(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.picture
            self.picture = None
            super(Client, self).save(*args, **kwargs)
            self.picture = saved_image
            super(Client, self).save(*args, **kwargs)
        else:
            super(Client, self).save(*args, **kwargs)

