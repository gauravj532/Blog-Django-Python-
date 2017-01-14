from django.shortcuts import get_object_or_404, render ,render_to_response
from django.views import generic
from . import models
from models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .form import loginForm , RegistrationForm
import datetime
from django.utils import timezone
from django.views.generic.edit import CreateView,FormView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView ,View , TemplateView
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# class StartView(FormView):
# 	form_class="loginForm"
# 	template_name=start.html
# 	success_url='/asiblog/'

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('asiblog/login.html',c)

def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username,password=password)
	if user is not None:
		return HttpResponseRedirect('/asiblog')
	else:
		return render(request, 'asiblog/login.html', {
            'error_message': "Wrong user name or password. Please try again",
        })
    
def logoutme(request):
	logout(request)
	return HttpResponseRedirect('/accounts/login')

class Register_user(FormView):
	# import pdb
	# pdb.set_trace()
	form_class = RegistrationForm
	model = User
	template_name = 'asiblog/register_user.html'
	#fields = ['username','email','password1','password2']
	success_url = "/account/register_success/"

	def form_valid(self,form):
		form.save()
		return super(Register_user, self).form_valid(form)

#def Register_user(request):


class Register_success(TemplateView):
	template_name = 'asiblog/register_success.html'

# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return view

class MainView(generic.ListView):
	context_object_name='postset'
	template_name = 'asiblog/mainview.html'	
	paginate_by = 2

	def get_queryset(self):
		allPost=Post.objects.order_by('-created')[:]
		presentPost=[]
		for post in allPost:
			if post.publish:
				presentPost.append(post)
		return presentPost
	# @method_decorator(login_required)
 #    def dispatch(self, *args, **kwargs):
 #        return super(ProtectedView, self).dispatch(*args, **kwargs)
	
# def addPost(request):
# 	if request.method == 'POST':
# 		form = newPostForm(request.POST)
# 		if form.is_valid():
# 			p=Post(title=form.cleaned_data['title'],body=form.cleaned_data['body'])
# 			p.save()
# 			return HttpResponseRedirect(reverse('asiblog:index'))
# 	else:
# 		form = newPostForm()
			
# 	return render(request, 'asiblog/addPost.html',{'form': form})

class PostCreat(CreateView):
	
	model=Post
	template_name= 'asiblog/addPost.html'
	
	fields = ['title','body']
	success_url = '/asiblog/'
	

# def edit(request,post_id):
	
# 	if request.method == 'POST':
		
# 		form = newPostForm(request.POST)
# 		if form.is_valid():
			
# 			p = Post.objects.get(pk=post_id)
# 			p.title = form.cleaned_data['title']
# 			p.body =  form.cleaned_data['body']
# 			#p.modified = models.DateField(auto_now=True)
# 			p.save()
# 			return HttpResponseRedirect(reverse('asiblog:index'))
# 	else : 
# 		# form = newPostForm()
# 		p = Post.objects.get(pk=post_id)

# 		# form.fields['title'].initial = p.title 
# 		# form.fields['body'].initial = p.body
# 		form = newPostForm(initial={'title':p.title,'body':p.body})

# 	return render(request, 'asiblog/addPost.html',{'form': form})

class PostUpdate(UpdateView):
	# import pdb
	# pdb.set_trace()

	model = Post
	fields = ['title','body']
	#fields="__all__"
	template_name= 'asiblog/addPost.html'
	success_url = '/asiblog/'

# def delete(request,post_id):
# 	p= get_object_or_404(Post,pk=post_id);
	
# 	p.publish=False
# 	p.save()
# 	return HttpResponseRedirect(reverse('asiblog:index'))
# 	#return HttpResponseRedirect("/asiblog/")

class SoftDelete(View):
	def get(self,request,*args, **kwargs):
		p= get_object_or_404(Post,pk=kwargs['pk']);
	 	p.publish=False
	 	p.save()
	 	return HttpResponseRedirect(reverse('asiblog:index'))




