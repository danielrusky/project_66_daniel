from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение от: {name}(телефон:{phone}): {message}')
    return render(request, 'emailserv/home.html')
