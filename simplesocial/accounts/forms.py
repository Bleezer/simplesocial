from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model() # ezzel hívja be a django előre definiált User modeljét (amit ugye így nem kell megykreálni a modelbe)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name' # ezzel lehet customizálni a megjelenő labeleket, átírni hogy ne a default érték jelenjen meg
        self.fields['email'].label = "Email Address"
