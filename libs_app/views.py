from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process_lib(request):
    
    request.session['first_noun'] = request.POST['first_noun']
    request.session['first_color'] = request.POST['first_color']
    request.session['farm_animal'] = request.POST['farm_animal']
    request.session['celebrity'] = request.POST['celebrity']
    request.session['kitchen_appliance'] = request.POST['kitchen_appliance']
    request.session['country'] = request.POST['country']
    request.session['article_of_clothing'] = request.POST['article_of_clothing']
    request.session['emotion'] = request.POST['emotion']
    return redirect('/display_lib')

# Create your views here.
def display_lib(request):
    context = {
        'first_noun': request.session['first_noun'],
        'first_color': request.session['first_color'],
        'farm_animal': request.session['farm_animal'],
        'celebrity': request.session['celebrity'],
        'kitchen_appliance': request.session['kitchen_appliance'],
        'country': request.session['country'],
        'article_of_clothing': request.session['article_of_clothing'],
        'emotion': request.session['emotion'],
    }    

    return render(request, 'display_lib.html', context)