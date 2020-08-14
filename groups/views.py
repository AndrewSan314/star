from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import Group, GroupMember


# Create your views here.
class ListGroups(generic.ListView):
    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    model = Group
    fields = ('name', 'description')


class DeleteGroup(LoginRequiredMixin, generic.DeleteView):
    model = Group
    success_url = reverse_lazy('groups:all')


class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, 'You already in this group')
        else:
            messages.success(self.request, 'You are joined this group')
        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug'))
        except:
            messages.warning(self.request, 'You are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You are leaved this group')
        return super().get(request, *args, **kwargs)
