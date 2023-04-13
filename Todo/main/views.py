from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm, userCreation
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django 
# Create your views here.
def home(request):
    # context={
    #     # "massage":massage
    #     "todos":"",
    # }
    # try:
    todos=Todo.objects.all()
    # except:
    #    return render(request,'home.html',context)
    massage="""
         hola from django ^_^
    """
    context={
        # "massage":massage
        "todos":todos,
    }
    # return HttpResponse(massage)
    return render(request,'home.html',context)

def detailed(request,id):
    todo=Todo.objects.get(id=id)
    items=todo.todoitems_set.all()
    context={
         "todo":todo,
         "items":items,
    }
    return render(request,'detailed.html',context)

def create(request):
    form=TodoForm()
    if request.method =="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/')
    context={
        "form":form,
    }
    return render(request,'create.html',context)

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm(instance=todo)
    if request.method =="POST":
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return  redirect('/')
    context={
        "form":form,
    }
    return render(request,'update.html',context)

def delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()

    return  redirect('/')

def createUser(request):
    form = userCreation()
    if request.method == 'POST':
        form = userCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('/login')