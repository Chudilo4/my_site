from django.db import models

# Create your models here.


class Project_translation(models.Model):
    title = models.CharField(max_length=255)  # Название проекта
    time_create = models.DateTimeField(auto_now_add=True)  # Дата создания проекта
    customer_price = models.IntegerField()  # Цена для клиента
    сost_price = models.IntegerField()  # Себестоимость
    money_manager = models.IntegerField() # Деньги менеджера 10%
    preparing_for_broadcast = models.IntegerField()  # Подготовка к трансляции
    installation_Dismantling = models.IntegerField()  # Монтаж демонтаж оборудования
    broadcasting = models.IntegerField()  # Проведение трансляции
    employee_money = models.IntegerField()  # Деньги наемного работника
    led_screen_rental = models.IntegerField()  # Аренда экрана
    Taxi_transport_costs = models.IntegerField()  # Такси и грузоперевозки
    payroll_taxes = models.IntegerField()  # Налоги с зп
    general_running_costs = models.IntegerField()  # Общехозяйственные расходы
    Profit = models.IntegerField()  # Прибыль
    Profitability = models.IntegerField()  # Рентабельность

    def __str__(self):
        return self.title
