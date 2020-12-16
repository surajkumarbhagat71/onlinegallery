from django.shortcuts import render ,redirect
from django.views.generic import TemplateView , ListView ,View , DetailView
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.


class About(TemplateView):
    template_name = 'gallery/about.html'

class Home(ListView):
    model = Image
    context_object_name = 'image'
    template_name = 'gallery/home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        form = ImageForm()
        context['forms'] = form
        return context

class Signup(View):
    def get(self,request):
        form = SignupForm()
        data = {"forms":form}
        return render(request,'gallery/signup.html',data)

    def post(self,request,*args,**kwargs):
        form = SignupForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('login')


class Login(View):
    def get(self,request):

        return render(request,'gallery/login.html')

    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        cond = Q(email = username ) & Q(password = password)

        check = User.objects.filter(cond).count()

        if (check == 1):
            request.session['login'] = username
            return redirect('home')
        else:
            return redirect('login')



class InsertImage(View):
    def post(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        user = User.objects.get(email = request.session['login']).user_id

        form = ImageForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = User(user)
            f.save()
        return redirect('home')


class MyUpload(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return  redirect('home')
        user = User.objects.get(email=request.session['login']).user_id
        data = Image.objects.filter(user = user)

        return render(request,'gallery/my_upload.html',{"image":data})


class DeleteMyImage(View):
    def get(self,request,pk,*args,**kwargs):
        if not request.session.has_key('login'):
            return request('login')
        data = Image.objects.get(img_id = pk)
        data.delete()
        return  render(request,'gallery/my_upload.html')


class ViewImage(DetailView):
    model = Image
    context_object_name = 'image'
    template_name = 'gallery/view_image.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allimage'] = Image.objects.all()
        return context



class Logout(View):
    def get(self,request):
        if request.session.has_key('login'):
            del request.session['login']
            return redirect('home')



