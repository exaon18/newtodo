from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
    if request.method == 'POST':
        item=request.POST['item_name']
        todo=Todo(title=item)
        todo.save()
        return redirect('index')
    else:
        todo=Todo.objects.all()
        return render(request, 'index.html', {'todo':todo})
def completed(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    if todo.completed==True:
        todo.completed=False
        todo.save()
        messages.success(request, 'item '+todo.title+'not completed')
    else:
        todo.completed=True
        todo.save()
        messages.success(request, 'item '+todo.title+' completed')
    
    
    return redirect('index')


