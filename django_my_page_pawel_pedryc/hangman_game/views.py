from django.shortcuts import render

# Create your views here.
def easter_egg_hangman_game(request, *args, **kwargs):
	print("args, kwargs: ", args, kwargs) # checking args and kwargs in console
	print("User's name that is log in now is: ", request.user) # checking username that is log in (in console)
	# return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request, "hangman.html")

