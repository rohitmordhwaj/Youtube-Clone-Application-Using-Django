from django.shortcuts import render
from .forms import  NewVedioForm,RegesterForm,LoginForm,CommentsForm
from django.views.generic.base import View,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .models import Vedio, Comments
from django.contrib.auth import authenticate, login ,logout


# Create your views here.


class VedioView(View):
	template_name = 'Video.html'
	
	def get(self,request,id):
		vedio_by_id = Vedio.objects.get(id=id)
		vedio = Vedio.objects.get(id=id)
		comments = Comments.objects.filter(video=vedio).order_by('-id')[:5]
		if request.user.is_authenticated:
			form = CommentsForm()
			return render (request,self.template_name,{'form':form,'vedio_by_id':vedio_by_id,'comments':comments})
		else:
			return render (request,self.template_name,{'vedio_by_id':vedio_by_id,'comments':comments})


class CommentView(View):

    def post(self, request):
        # pass filled out HTML-Form from View to CommentForm()
        form = CommentsForm(request.POST)
        if form.is_valid():
            # create a Comment DB Entry
            text = form.cleaned_data['text']
            vedio_id = request.POST.get('vedio')
            vedio = Vedio.objects.get(id=vedio_id)
            
            new_comment = Comments(text=text, user=request.user, video=vedio)
            new_comment.save()
            return HttpResponseRedirect('/youtube/video/{}'.format(str(vedio_id)))





class Regester(View):
	template_name = 'Regester.html'
	
	def get(self,request):
		if request.user.is_authenticated:
			return HttpResponseRedirect('/')
		form =  RegesterForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = RegesterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password  = form.cleaned_data['password']
			email = form.cleaned_data['email']
			new_user = User(username=username,email=email)
			new_user.set_password(password)
			new_user.save()
			return HttpResponseRedirect('/youtube/login')
		#return HttpResponse('This is Register view. POST Request.')

class Login(View):
	template_name = 'Login.html'
	
	def get(self,request):
		if request.user.is_authenticated:
			return HttpResponseRedirect('/')
		form =  LoginForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password  = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/youtube/login')
		#return HttpResponse('This is Login view. POST Request.')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

		


class NewVideo(View):
	template_name = 'new_vedio.html'
	
	def get(self,request):
		if request.user.is_authenticated == False:
			return HttpResponseRedirect('/youtube/login')
		form = NewVedioForm()
		return render (request, self.template_name, {'form': form})



	def post(self,request):
		form = NewVedioForm(request.POST,request.FILES)
		if form.is_valid():
			Title = form.cleaned_data['Title']
			Discription  = form.cleaned_data['Discription']
			path = form.cleaned_data['path']
			new_vedio = Vedio(Title=Title,Discription=Discription,path=path)
			new_vedio.user=request.user
			new_vedio.save()
		return HttpResponseRedirect('/')



