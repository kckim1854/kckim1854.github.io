from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'intro.html')

def product(request):
    return render(request, 'product.html')
def floor(request):
    return render(request, 'floor.html')
def wall(request):
    return render(request, 'wall.html')
def stone(request):
    return render(request, 'stone.html')
def tile(request):
    return render(request, 'tile.html')
def bath(request):
    return render(request, 'bath.html')
def furniture(request):
    return render(request, 'furniture.html')

def project(request):
    return render(request, 'project.html')

def faq(request):
    return render(request, 'faq.html')
def contact(request):
    return render(request, 'contact.html')
def action_name(request):
    if request.method == 'GET':
        return render(request, 'new_page.html')
    if request.method == 'POST':
        my_variable = request.POST['input_name']
        output_data1 = 'kyuchull'
        output_data2 = 'hangjung'
        return render(request, 'new_page.html',
                      {'outputdata1': my_variable, 'outputdata2': output_data2})

