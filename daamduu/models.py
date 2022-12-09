from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    card_number = models.CharField(max_length=20, verbose_name='Номер карты')

    def __str__(self):
        return self.name

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    position = models.CharField(max_length=20, verbose_name='Должность')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование ингредиента')
    extra_price = models.IntegerField(verbose_name='Стоимость надбавки')
    calories = models.IntegerField(verbose_name='Количество калорий')

    def __str__(self):
        return self.name

class Food(models.Model):
    ingredients = models.ManyToManyField(Ingredient, related_name='food', through='Order')
    name = models.CharField(max_length=25, verbose_name='Блюдо')
    start_price = models.IntegerField(verbose_name='Начальная стоимость')
    type_of_cousine = models.CharField(max_length=50, verbose_name='Тип кухни')
    calories = models.IntegerField(verbose_name='Количество калорий')

    def __str__(self):
        return self.name

class Order(models.Model):
    food = models.ForeignKey(Food, related_name='orders', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='orders', on_delete=models.CASCADE)
    vegeterian = models.BooleanField(default=False)
    food_status = models.CharField(max_length=50, verbose_name='Тип блюда')
    final_price = models.IntegerField(verbose_name='Финальная стоимость', null=True, blank=True)
    order_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')

    def __str__(self):
        return f'{self.food.name} - {self.ingredient.name} - {self.client.name} - {self.worker.name}'


class Foodcounter(Order):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        ingredient2 = 'Курица'
        ingredient3 = 'Говядина'
        ingredient4 = 'Рыба'
        if self.ingredient.name == ingredient2:
            self.vegeterian = False
        elif self.ingredient.name == ingredient3:
            self.vegeterian = False
        elif self.ingredient.name == ingredient4:
            self.vegeterian = False
        else:
            self.vegeterian = True
        calories_count = self.food.calories + self.ingredient.calories
        if calories_count <= 400:
            self.food_status = 'Перекус'
        elif calories_count >= 400 and calories_count <= 600:
            self.food_status = 'Обед'
        elif calories_count > 1000:
            self.food_status = 'Обжиралово'
        self.final_price = self.food.start_price + self.ingredient.extra_price
        super().save(*args, **kwargs)



