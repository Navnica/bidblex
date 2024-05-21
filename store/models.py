from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserRole(models.Model):
    name = models.CharField(max_length=100)
    power_level = models.IntegerField(default=2)


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        superuser_role = UserRole.objects.filter(power_level=100).first()
        if not superuser_role:
            superuser_role = UserRole.objects.create(name='Superuser', power_level=100)
        extra_fields.setdefault('role', superuser_role)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name="users", default=1)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class ContactData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contact_datas")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    manufacturer = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductDoc(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='docs')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='store/static/store/docs')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='store/static/store/img/')


class Storage(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ProductStorage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='storages')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='products')
    count = models.IntegerField(default=0)
