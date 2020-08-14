from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreateForm


# Create your views here.
class SignUp(CreateView):
    success_url = reverse_lazy('login')
    form_class = UserCreateForm
    template_name = 'accounts/signup.html'
