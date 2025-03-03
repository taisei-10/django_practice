from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm
from .models import Employee
from .forms import EmployeeAdd
from django.shortcuts import redirect
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!!!")

def index(request):
    my_dict={
        'insert_something':"views.pyのinsert_something部分です。",
        'name':'yasunari',
        'test_titles':["title 1","title 2","title 3"],
        'form': TestForm(),
        'insert_forms': '初期値',
    }

    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    
    return render(request, 'httpserverapp/index.html',my_dict)

def info(request):
    employees = Employee.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title':'テスト',
        'employees': employees,
        'header': header,
    }

    return render(request, 'httpserverapp/info.html', my_dict2)


def create(request):

    message = ''
    if (request.method == 'POST'):
        form = EmployeeAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/info')
        else:
            message = '再入力してください'
    modelform_dict = {
        'title': 'modelformテスト',
        'form': EmployeeAdd(),
        'message':message,
    }
    return render(request, 'httpserverapp/create.html', modelform_dict)

def update(request, num):
    message = ''
    employee_obj = Employee.objects.get(id=num)
    if (request.method == 'POST'):
        employee = EmployeeAdd(request.POST, instance=employee_obj)
        if employee.is_valid():
            employee.save()
            return redirect(to='/info')
        else:
            message = '再入力してください'
    update_dict = {
        'title': '登録情報更新画面',
        'id': num,
        'form': EmployeeAdd(instance=employee_obj),
        'message':message,
    }
    return render(request, 'httpserverapp/update.html', update_dict)

def delete(request, num):
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    message = ''
    employee_obj = Employee.objects.get(id=num)
    if (request.method == 'POST'):
        employee_obj.delete()
        return redirect(to='/info')
    delete_dict = {
        'title': '削除画面',
        'header': header,
        'id': num,
        'employee': employee_obj,
        'message': message,
    }
    return render(request, 'httpserverapp/delete.html', delete_dict)