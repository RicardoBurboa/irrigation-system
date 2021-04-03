from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    #renderea lo que está dentro de la carpeta templates (templates/blog/home.html)
    
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)

#Listar todos los Posts en el home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

#Vista para los posts de cada usuario
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 5

    #consulta a la base de datos para obtener el usuario y sus posts
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#Ver detalle de los Posts
class PostDetailView(DetailView):
    model = Post

#Crear un Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #Agregar el id del autor para que jale el form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Actualizar un Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #Agregar el id del autor para que jale el form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #Validación para que sólo el usuario que creó el post pueda actualizarlo
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#Eliminar Post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #Esta variable redirecciona al home cuando se borra el post
    success_url = '/'

    #Validación para que sólo el usuario que creó el post pueda actualizarlo
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'Acerca De'})