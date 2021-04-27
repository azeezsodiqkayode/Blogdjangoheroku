from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
# Create your views here.
#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class UpdatePostView(UpdateView):
	 model = Post
	 form_class = EditForm
	 template_name = 'update_post.html'
	 # = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	 model = Post
	 template_name = 'delete_post.html'
	 success_url = reverse_lazy('home')

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwards['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')
	