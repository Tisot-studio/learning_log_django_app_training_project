from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Регистрация нового пользователя."""
	if request.method != 'POST':
		#Отобразить пустую регистрационную форму
		form = UserCreationForm()
	else:
		#Процесс завершения формы.
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#залогинить пользователя и вернуть на домашнюю страницу.
			login(request, new_user)
			return redirect('learning_logs:index')
	#Отобразить пустую или проверенную форму.
	context = {'form':form}
	return render(request, 'registration/register.html', context)
				
 
