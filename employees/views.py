from django.shortcuts import render

'''def home(request):
    return render(request, 'dashboard.html')'''

def employee_list(request):
    return render(request, 'employees.html')
