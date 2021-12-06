from django.shortcuts import render
from django.views.generic import  DetailView, ListView,TemplateView
from django.http import JsonResponse
from django.core import serializers
from .forms import FriendForm
from .models import Category,Task

from django.views import View

class TaskDetailView(DetailView):
    model = Task

class CategoryListView(ListView):
    model = Category

class TaskListView(ListView):
    model = Task

class HomeView(TemplateView):
    template_name="base.html"

def categorytasks(request,id):
    context={
        'object_list' : Task.objects.filter(category = Category.objects.get(id=id))
    }
    return render(request,'todo/ctask.html',context)

# def IndexView(req):
#     tasks = Task.objects.all()
#     category = Category.objects.all()
    
#     if req.method == 'POST':
#         c = req.POST.get('categories')
#         t = req.POST.get('title')
#         p = req.POST.get('priority')
#         d = req.POST.get('description')
#         time = req.POST.get('time')
       
#         tasks = Task( title = t, priority= p, description= d, time= time )
#         tasks.save()
#         tasks.category.set([Category.objects.get(category_name=c)])
#         # tasks.category.save()
         
#     context = {
#         'category' :category,
#         'task': tasks     
#         }
    

    
def indexView(request):
    form = FriendForm()
    tasks = Task.objects.all()
    return render(request, "index.html", {"form": form, "tasks": tasks})


def PostTask(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

# BONUS CBV
def CheckTask(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        title = request.GET.get("title", None)
        # check for the nick name in the database.
        if Task.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    



class TaskView(View):
    form_class = FriendForm
    template_name = "index.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        tasks = Task.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "tasks": tasks})

    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
        if self.request.is_ajax and self.request.method == "POST":
            # get the form data
            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
        return JsonResponse({"error": ""}, status=400)

        



# Create your views here.
