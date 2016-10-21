from django.shortcuts import render
from django.shortcuts import redirect, render_to_response, get_object_or_404
from .forms import newPostForm,CommentForm
from .models import Post, Comment
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.base import View

# Create your views here.
def indexing(request):
    posts = Post.objects.all()
    comments=Comment.objects.all()
    return render(request, 'vlg/index.html', {'posts':posts, 'comments':comments})

def new_post(request):
    if request.method=="POST":
        form = newPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(indexing)
    else:
        return render(request, 'vlg/new_post.html', {'form':newPostForm})



def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            obje = comment_form.save(commit=False)
            obje.post = post
            obje.user = request.user
            obje.save()

        else:
            return redirect('vlg/comments.html')
    else:
        obje=CommentForm()
    obje=CommentForm()
    return render(request,'vlg/comments.html', {'post':post,'comments':comments,'comment_form':obje})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'vlg/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "vlg/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user=form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)

        return  HttpResponseRedirect("/")