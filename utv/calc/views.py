from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from calc.models import Project_translation

# Create your views here.

menu = ['главня страница', 'расчёт проектов']

context = {'title': 'Главная страница',
           'menu': menu,
           'post': Project_translation.objects.all(),
           }


def home(request):
    return render(request, 'home.html', context)


@require_http_methods(['GET', 'POST'])
def project(request):
    if request.method == 'GET':
        return render(request, 'project.html', context)
    elif request.method == 'POST':
        Project_translation.objects.create(
            title=request.POST["username"],
            customer_price = request.POST["customer_price"],
            сost_price = request.POST["сost_price"],
            money_manager = request.POST["money_manager"],
            preparing_for_broadcast = request.POST["preparing_for_broadcast"],
            installation_Dismantling = request.POST["installation_Dismantling"],
            broadcasting = request.POST["broadcasting"],
            employee_money = request.POST["employee_money"],
            led_screen_rental = request.POST["led_screen_rental"],
            Taxi_transport_costs = request.POST["Taxi_transport_costs"],
            payroll_taxes = request.POST["payroll_taxes"],
            general_running_costs = request.POST["general_running_costs"],
            Profit = request.POST["Profit"],
            Profitability = request.POST["Profitability"],
        )
        return render(request, 'project_all.html', context)


def project_all(request):
    return render(request, 'project_all.html', context)
