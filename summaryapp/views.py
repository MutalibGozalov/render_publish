
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .forms import AssignmentForm, ServiceFrom, BarberFrom
from summaryapp.models import AssingmentModel, ServiceModel, BarberModel
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

@login_required(login_url="/login")
def dashboard(request):

    

    assignments = AssingmentModel.objects.all().order_by('-id')[:5]

    now = datetime.now()
    year = now.year
    month = now.month
    today = now.day

    assignments_day = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month) & Q(created_at__day = today))

    assignments_month = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month))
   
    sum_month = []
    sum_day = []
   
    for assignment in assignments_day:
        prize_day = 0
        prize_day += assignment.service.prize
        prize_day += assignment.tip
        sum_day.append(prize_day)

    for assignment in assignments_month:
        prize_month = 0
        prize_month += assignment.service.prize
        prize_month += assignment.tip
        sum_month.append(prize_month)

# ---------------------------------------------------------------
    assignments_day_before = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month) & Q(created_at__day = (int(today)-1)))
    assignments_month_before = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = (int(month)-1)))

    sum_month_before = []
    sum_day_before = []
    
    for assignment in assignments_day_before:
        prize_day_before = 0
        prize_day_before += assignment.service.prize
        prize_day_before += assignment.tip
        sum_day_before.append(prize_day_before)

    for assignment in assignments_month_before:
        prize_month_before = 0
        prize_month_before += assignment.service.prize
        prize_month_before += assignment.tip
        sum_month_before.append(prize_month_before)

# ------------------------------- chart -------------------------------

    month_before2 = month-2
    month_before3 = month-3
    month_before4 = month-4
    month_before5 = month-5
    month_before6 = month-6

    assignments_month_before2 = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month_before2))
    assignments_month_before3 = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month_before3))
    assignments_month_before4 = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month_before4))
    assignments_month_before5 = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month_before5))
    assignments_month_before6 = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month_before6))
    

    assignments9= AssingmentModel.objects.filter(created_at__month = datetime.now().month-3)
    print("assignments9")
    for ass in assignments9:
        print(ass.created_at)

    print("--------------------------------------------")

    # ssignments_month_before = AssingmentModel.objects.filter(Q(created_at__year = 2022) & Q(created_at__month = 9))
    ssignments_month_before = assignments9.filter(created_at__year = int(2023))

    print("assignments_month_before/month-2")
    for ass in ssignments_month_before:
        print(ass.created_at)
    

    sum_month_before2 = []
    sum_month_before3 = []
    sum_month_before4 = []
    sum_month_before5 = []
    sum_month_before6 = []

    for assignment in assignments_month_before2:
        prize_month_before2 = 0
        prize_month_before2 += assignment.service.prize
        prize_month_before2 += assignment.tip
        sum_month_before2.append(prize_month_before2)
    
    for assignment in assignments_month_before3:
        prize_month_before3 = 0
        prize_month_before3 += assignment.service.prize
        prize_month_before3 += assignment.tip
        sum_month_before3.append(prize_month_before3)

    for assignment in assignments_month_before4:
        prize_month_before4 = 0
        prize_month_before4 += assignment.service.prize
        prize_month_before4 += assignment.tip
        sum_month_before4.append(prize_month_before4)

    for assignment in assignments_month_before5:
        prize_month_before5 = 0
        prize_month_before5 += assignment.service.prize
        prize_month_before5 += assignment.tip
        sum_month_before5.append(prize_month_before5)

    for assignment in assignments_month_before6:
        prize_month_before6 = 0
        prize_month_before6 += assignment.service.prize
        prize_month_before6 += assignment.tip
        sum_month_before6.append(prize_month_before6)

    chart_data = [sum(sum_month), sum(sum_month_before), sum(sum_month_before2), sum(sum_month_before3), sum(sum_month_before4), sum(sum_month_before5), sum(sum_month_before6)]
    chart_data.reverse()
# ----------------------------- END chart -----------------------------
   
    return render(request, 'dashboard/home.html', {"assignments": assignments, "sum_day": sum(sum_day), "sum_month": sum(sum_month), 'month_sum_before':sum(sum_month_before), 'day_sum_before':sum(sum_day_before), "sum": chart_data})


@login_required(login_url="/login")
def services(request):
    if request.method == "POST":
        form = ServiceFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/services")
    else:
        form = ServiceFrom()
    
    
    services = ServiceModel.objects.all()
    return render(request, 'dashboard/services.html', {"services": services, "form": form})

@login_required(login_url="/login")
def edit_service(request, pk):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            obj = ServiceModel.objects.get(id=pk)
            obj.name = request.POST['Name']
            Hour = request.POST['Hour']
            Minute = request.POST['Minute']
            obj.time = timedelta(hours=int(Hour), minutes=int(Minute))
            obj.prize = request.POST['Prize']
            obj.save()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

@login_required(login_url="/login")
def delete_service(request, pk):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            obj = ServiceModel.objects.get(id=pk)
            obj.delete()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

@login_required(login_url="/login")
def summary(request):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            month = request.POST['Month']
            day= request.POST['Day']
            assignments_day = AssingmentModel.objects.filter(Q(created_at__month = month) & Q(created_at__day = day))
            assignments_month = AssingmentModel.objects.filter(Q(created_at__month = month) & Q(created_at__month = month))

            sum_month = []
            sum_day = []
            
            for assignment in assignments_day:
                prize_day = 0
                prize_day += assignment.service.prize
                prize_day += assignment.tip
                sum_day.append(prize_day)

            for assignment in assignments_month:
                prize_month = 0
                prize_month += assignment.service.prize
                prize_month += assignment.tip
                sum_month.append(prize_month)

            return JsonResponse({'month_sum':sum(sum_month), 'day_sum':sum(sum_day)})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

@login_required(login_url="/login")
def transactions(request):
    assignments = AssingmentModel.objects.all()

    page = Paginator(assignments, 15)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    now = datetime.now()
    year = now.year
    month= now.month
    today = now.day
   
    assignments_day = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month) & Q(created_at__day = today))

    month = now.month
    assignments_month = AssingmentModel.objects.filter(Q(created_at__year = year) & Q(created_at__month = month))
   
    sum_month = []
    sum_day = [] 

    for assignment in assignments_day:
        prize_day = 0
        prize_day += assignment.service.prize
        prize_day += assignment.tip
        sum_day.append(prize_day)

    for assignment in assignments_month:
        prize_month = 0
        prize_month += assignment.service.prize
        prize_month += assignment.tip
        sum_month.append(prize_month)

    return render(request, 'dashboard/transactions.html', {"page": page, "sum_day": sum(sum_day), "sum_month": sum(sum_month)})

@login_required(login_url="/login")
def transactions_filter(request):
    from django.http import JsonResponse
    try:
        assignments_service = AssingmentModel.objects.values_list('service__name')
        assignments_tip = AssingmentModel.objects.values_list('tip')
        assignments_duration = AssingmentModel.objects.values_list('service__time')
        assignments_ca = AssingmentModel.objects.values_list('created_at')

        service_prize = AssingmentModel.objects.values_list('service__prize')
        outcome_pairs = list(zip(service_prize, assignments_tip))
        outcome = []
        for pair in outcome_pairs:
            oc = pair[0][0]+pair[1][0]
            outcome.append(oc)

        assignments_list = list(zip(assignments_service, assignments_duration, assignments_ca, assignments_tip, outcome))
        return JsonResponse({'transactions_service': assignments_list})
    except ServiceModel.DoesNotExist:
        return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})

@login_required(login_url="/login")
def barbers(request):
    if request.method == "POST":
        form = BarberFrom(request.POST)
        form.save()
        return redirect("/barbers")
    else:
        form = BarberFrom()

    barbers = BarberModel.objects.all()
    profits = []
    barber_profits = ()

    for barber in barbers:
        barber_transactions = AssingmentModel.objects.filter(employee_id = barber.id)
        Sum = 0 #gain from all assignments

        for assignment in barber_transactions:
            Sum += assignment.service.prize
            Sum += assignment.tip

        profits.append(Sum)
        
    barber_profits = list(zip(barbers,profits))
    return render(request, 'dashboard/barbers.html', {"form":form, "barber_profits": barber_profits})

def delete_barber(request, pk):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            obj = BarberModel.objects.get(id=pk)
            obj.delete()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})


@login_required(login_url="/login")
def reception(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        form.save()
        return redirect("/reception")
    else:
        form = AssignmentForm()

    assignments = AssingmentModel.objects.all().order_by('-id')[:5]
    return render(request, 'dashboard/reception.html', {"assignments": assignments, "form": form})


@login_required(login_url="/login")
def sidebar(request):
    from django.http import JsonResponse
    try:
        assignment_count = AssingmentModel.objects.all().count()
        service_count = ServiceModel.objects.all().count()
        barber_count = BarberModel.objects.all().count()
        return JsonResponse({'ac': assignment_count, 'sc': service_count, 'bc': barber_count})
    except ServiceModel.DoesNotExist:
        return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
