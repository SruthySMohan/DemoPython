from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import Todoform
from .models import Task


class TaskListView(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'


class TaskDetail(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




def index(request):
    task1 = Task.objects.all()
    if request.POST:
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()


    return render(request,'home.html',{'task1':task1})
# def details(request):
#
#     return render(request,'details.html')
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or  None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
    return render(request,'edit.html',{'f':f,'task':task})