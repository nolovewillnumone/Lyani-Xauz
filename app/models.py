from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class MenuCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Menu(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_access = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    partners = models.CharField(max_length=255, blank=True, null=True)  # Поле для партнеров
    partners_image = models.ImageField(upload_to='partners_images/', blank=True, null=True)  # Фото партнеров
    calories = models.IntegerField(blank=True, null=True)  # Новое поле для калорий

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    
    



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


class Subscriber(models.Model):
      email = models.EmailField(unique=True,null=True,blank=True)
      subscribed_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

      def __str__(self):
         return self.email

