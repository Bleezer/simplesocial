from django.conf.urls import url
from django.contrib.auth import views as auth_views # aliasolni
from . import views

app_names = 'accounts'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'), # kell neki template_name, hogy tudja mit olvasson
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'), # itt viszont nem kell feltétlen, mert az alapbeállítás, hogy logout után visszamegy a homepage-re és az pont jó nekünk
    url(r'signup/$',views.SignUp.as_view(),name='signup'),
]
