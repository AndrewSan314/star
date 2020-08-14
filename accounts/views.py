from django.views.generic import CreateView

from .forms import UserCreateForm
from .models import User


# Create your views here.
class SignUp(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'accounts/signup.html'
