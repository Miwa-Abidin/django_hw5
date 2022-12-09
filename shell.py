from daamduu.models import *

client1 = Client.objects.create(user=User.objects.create(email='nikname21@gmail.com', password='defender42'), name='Нурсултан Бердиев', card_number='4147565798789009')
worker1 = Worker.objects.create(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'), name='Алтынай Алиева', position='Оператор кассы')

client2 = Client.objects.create(user=User.objects.create(email='nikname44@gmail.com', password='defender4242'), name='Azat Sokolov', card_number='4347555798789009')
client3 = Client.objects.create(user=User.objects.create(email='miko.abidinov@gmail.com', password='forward111'), name='Mirsaid Abidinov', card_number='4337555723489209')

food1 = Food.objects.create(name='Shaurma', start_price=200, type_of_cousine='фастфуд', calories=500)
food2 = Food.objects.create(name='Hamburger', start_price=180, type_of_cousine='фастфуд', calories=350)
food3 = Food.objects.create(name='Паста', start_price=450, type_of_cousine='Италянская', calories=400)
food4 = Food.objects.create(name='Боул', start_price=600, type_of_cousine='Европейская', calories=500)
food5 = Food.objects.create(name='Суши', start_price=400, type_of_cousine='Японская', calories=450)

ingredient1 = Ingredient.objects.create(name='Сыр', extra_price=80, calories=150)
ingredient2 = Ingredient.objects.create(name='курица', extra_price=100, calories=250)
ingredient3 = Ingredient.objects.create(name='говядина', extra_price=120, calories=300)
ingredient4 = Ingredient.objects.create(name='рыба', extra_price=120, calories=270)
ingredient5 = Ingredient.objects.create(name='рис', extra_price=70, calories=100)
ingredient6 = Ingredient.objects.create(name='творог', extra_price=100, calories=170)
ingredient7 = Ingredient.objects.create(name='куриные яйцо', extra_price=50, calories=120)
ingredient8 = Ingredient.objects.create(name='салат', extra_price=50, calories=50)
ingredient9 = Ingredient.objects.create(name='фри', extra_price=50, calories=70)


order1 = food1.start_price + ingredient1.extra_price + ingredient3.extra_price + ingredient4.extra_price + ingredient5.extra_price
print(order1)

order1 = food1.ingredients.set([ingredient1, ingredient3, ingredient4, ingredient5],
                          through_defaults={'client':client1, 'worker': worker1})


order2 = food2.start_price + ingredient2.extra_price + ingredient8.extra_price
print(order2)
order2 = food2.ingredients.set([ingredient2, ingredient8],
                               through_defaults={'client': client2, 'worker': worker1})

order3 = food3.start_price + ingredient8.extra_price + ingredient7.extra_price + ingredient1.extra_price + ingredient6.extra_price
print(order3)
order3 = food3.ingredients.set([ingredient8, ingredient7, ingredient1, ingredient6],
                               through_defaults={'client': client2, 'worker': worker1})

order4 = food5.start_price + ingredient5.extra_price + ingredient4.extra_price + ingredient7.extra_price
print(order4)
order4 = food5.ingredients.set([ingredient5, ingredient4, ingredient7],
                               through_defaults={'client': client2, 'worker': worker1})

order5 = food4.start_price + ingredient5.extra_price + ingredient1.extra_price + ingredient9.extra_price + ingredient8.extra_price + ingredient6.extra_price
print(order5)
order5 = food4.ingredients.set([ingredient5, ingredient1, ingredient9, ingredient8, ingredient6],
                               through_defaults={'client': client2, 'worker': worker1})

# MY ORDERS
order6 = food4.start_price + ingredient6.extra_price + ingredient3.extra_price + ingredient4.extra_price + ingredient2.extra_price + ingredient1.extra_price
print(order6)
order6 = food4.ingredients.set([ingredient6, ingredient3, ingredient4, ingredient2, ingredient1],
                               through_defaults={'client': client3, 'worker': worker1})

order7 = food3.start_price + ingredient6.extra_price + ingredient8.extra_price + ingredient4.extra_price + ingredient2.extra_price + ingredient9.extra_price + ingredient3.extra_price
print(order7)
order7 = food3.ingredients.set([ingredient6, ingredient8, ingredient4, ingredient2, ingredient9, ingredient3],
                               through_defaults={'client': client3, 'worker': worker1})

order8 = food2.start_price + ingredient6.extra_price + ingredient2.extra_price + ingredient4.extra_price + ingredient5.extra_price + ingredient1.extra_price + ingredient9.extra_price
print(order8)
order8 = food2.ingredients.set([ingredient6, ingredient2, ingredient4, ingredient5, ingredient1, ingredient9],
                               through_defaults={'client': client3, 'worker': worker1})

order9 = food4.start_price + ingredient1.extra_price + ingredient2.extra_price + ingredient3.extra_price + ingredient4.extra_price + ingredient6.extra_price + ingredient5.extra_price + ingredient9.extra_price
print(order9)
order9 = food4.ingredients.set([ingredient1, ingredient2, ingredient3, ingredient4, ingredient6, ingredient5, ingredient9],
                               through_defaults={'client': client3, 'worker': worker1})

order10 = food2.start_price + ingredient4.extra_price + ingredient3.extra_price + ingredient2.extra_price + ingredient5.extra_price + ingredient8.extra_price
print(order10)
order10 = food2.ingredients.set([ingredient4, ingredient3, ingredient2, ingredient5, ingredient8],
                               through_defaults={'client': client3, 'worker': worker1})



for fp in Foodcounter.objects.all():
    fp.save()


# food1.ingredients.set([ingredient1, ingredient3, ingredient4, ingredient5],
#                             through_defaults = {'client': client1, 'worker': worker1})
# food2.ingredients.set([ingredient2, ingredient8],
#                                through_defaults={'client': client2, 'worker': worker1})
# food3.ingredients.set([ingredient8, ingredient7, ingredient1, ingredient6],
#                                through_defaults={'client': client2, 'worker': worker1})
# food4.ingredients.set([ingredient5, ingredient1, ingredient9, ingredient8, ingredient6],
#                                through_defaults={'client': client2, 'worker': worker1})
# food5.ingredients.set([ingredient5, ingredient4, ingredient7],
#                                through_defaults={'client': client2, 'worker': worker1})






# order1 = food1.start_price + ingredient1.extra_price + ingredient3.extra_price + ingredient4.extra_price + ingredient5.extra_price
# print(order1)
#
# food2.ingredients.set([ingredient2, ingredient4],
#                       through_defaults={'client': client1, 'worker': worker1})
#
# order2 = food2.start_price + ingredient2.extra_price + ingredient4.extra_price
# print(order2)


