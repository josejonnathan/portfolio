from django.shortcuts import render
from pass_generator.pass_generator import PassGenerator

# Create your views here.


def home_pass(request):
    'this function render the first view of the generator, whitout the password block'
    return render(request, "pass_generator.html")


def pass_generator(request):
    'here the variables are obtained from the response, call the generator and render the result'
    lenght = int(request.GET.get('length', 10))
    upper = request.GET.get('uppercase', False)
    special = request.GET.get('special', False)
    numbers = request.GET.get('numbers', False)

    password = PassGenerator()
    generated_password = password.pass_generator(
        lenght, upper, special, numbers)

    context = {
        'length': int(lenght),
        'uppercase': upper,
        'special': special,
        'numbers': numbers,
        'password': generated_password}
    return render(request, 'pass_generator.html', context)
