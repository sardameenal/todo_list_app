from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    """query all the objects in the database that represents the Todo

    Args:
        todo_list: will search for all the objects within the Todo Query set

    Returns:
        will return the todo_list & the form input
    """
    todo_list = Todo.objects.order_by('id')
# todo form instantitated and added in the context to pass it to the template
    form = TodoForm()

    context ={'todo_list' : todo_list, 'form':form}
    
    return render(request, 'todo/index.html', context)

@require_POST #decorator is added to ensure that the addtodo view accepts only POST request
def addtodo(request):
    """this view is created in order to add a new todo item in the list

    Returns:
        Since it is a single page application so it will redirect to the index page only and add the recently added item in the list displayed
    """
    form = TodoForm(request.POST) # form is instatitaed with TodoForm along with the data passed

    #print(request.POST['text'])
    #if the form is valid then the entered value will be immediately added to the database and redirect to the index page and send the items to the template which will be displayed on the screen
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect(index)

#to mark the todo items complete
def completetodo(request, todo_id):
    """this view is created to mark the items complete. So when a user click on the todo item displayed on the list the item will be marked complete.

    Args:
        request
        todo_id

    Returns:
        The item will be crossed once the link is clicked. So it will redirect to the index page and make the changes in the list
    """
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

#to delete the completed tasks from the screen
def deletecompleted(request):
    """This view will delete the completed todo items from the list when the Delete Completed button is clicked. This will filter out the todo items from the databse whose value is True and delete them. 

    Returns:
        The template will display only those todo items which are marked complete=false when redirected to the index page.
    """
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

#to delete all the items
def deleteall(request):
    """This view will delete/clear the todo list when the Delete All button is clicked fromm the template

    Returns:
         All the todo items will be deleted. 
    """
    Todo.objects.all().delete()

    return redirect('index')