from django.utils.translation import ugettext_lazy as _
from django import forms
from django.shortcuts import render

class GreetForm(forms.Form):
    user_name = forms.CharField(
        label = ('Enter your name:'),
        max_length=100,
    )

def basic_form_view(request):
    result = ''
    if request.method == 'POST':
        form = GreetForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            result = 'Merhaba {user_name}'.format(user_name=user_name)
    else:
        form = GreetForm()
    params = {
        'form': form,
        'result': result,
    }
    return render(
        request,
        'basic_form_view.html',
        params,
    )