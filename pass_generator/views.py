from django.shortcuts import render
from pass_generator.pass_generator import PassGenerator

# Create your views here.


def home_pass(request):
    return render(request, "pass_generator.html")


# def pass_generator(request):
#     char_list = list('abcdefghijklmnopqrstuvxyz')
#     generated_password = ''
#     lenght = int(request.GET.get('length'))
#     upper = request.GET.get('uppercase')
#     special = request.GET.get('special')
#     numbers = request.GET.get('numbers')

#     if upper:
#         char_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

#     if special:
#         char_list.extend(list('_-?[]?$%&#@'))

#     if numbers:
#         char_list.extend(list('123456789'))

#     for x in range(lenght):
#         generated_password += random.choice(char_list)

#     return render(request, 'pass_generator.html', {'password': generated_password})
    # return render(request, 'pass_generator.html')

def pass_generator(request):
    lenght = int(request.GET.get('length'))
    upper = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')
    password = PassGenerator()
    generated_password = password.pass_generator(
        lenght, upper, special, numbers)
    return render(request, 'pass_generator.html', {'password': generated_password})
