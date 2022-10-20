# from django.shortcuts import redirect, render
# from .models import Employee
# from employee.forms import EmployeeForm

# # Create your views here.
# def emp(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass

#         else: 
#             form = EmployeeForm()
#             return render(request, 'index.html', {'form': form})

# def show(request):
#     employees = Employee.objects.all()
#     return(render, 'index.html', {'employees': employees})

