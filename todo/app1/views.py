from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from . models import Task
from .forms import ToDoform
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
class Todolist(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "task"
class Tododetail(DetailView):
    model = Task
    template_name = "detail.html"
    context_object_name = "task"
class Todoupdate(UpdateView):
    model = Task
    template_name = "update.html"
    context_object_name = "task"
    fields = ("name","priority","date")

    def get_success_url(self):
        return reverse_lazy('Tododetail',kwargs={"pk":self.object.id})
class Tododelete(DeleteView):
    model = Task
    template_name = "detail.html"
    # template_name = "home.html"
    success_url = reverse_lazy("classlist")
def home(request):
    dic=Task.objects.all()

    if request.method=="POST":
        name=request.POST.get("name","")
        priority = request.POST.get("priority", "")
        date= request.POST.get("date","")

        task=Task(name=name,priority=priority,date=date)
        task.save()
        # redirect("/delete")
    return render(request,"home.html",{"task":dic})
def delete(request,todoid):
    task=Task.objects.get(id=todoid)
    task.delete()
    return redirect("/")
    # dic=Task.objects.all()
    #
    # return render(request, "home.html", {"task": dic})
    # return HttpResponse("tofoid",todoid)
def update(request,todoid):
    task=Task.objects.get(id=todoid)
    f=ToDoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(request,'update.html',{'f':f,"task":task})