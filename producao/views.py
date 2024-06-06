from django.shortcuts import render

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            log_Django(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})