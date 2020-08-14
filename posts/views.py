from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()
from .models import Post


# Create your views here.
class ListPosts(SelectRelatedMixin, generic.ListView):
    model = Post
    select_related = ['user', 'group']


class UserPosts(generic.ListView):
    model = Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post_user'] = self.post_user
        return context


class SinglePost(SelectRelatedMixin, generic.DetailView):
    model = Post
    select_related = ['user', 'group']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = Post
    fields = ('message', 'group')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Post
    select_related = ['user', 'group']
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__id=self.request.user.id)
