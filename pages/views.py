from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def count(request):
    textinput = request.GET['textinput']
    wordlist = textinput.split()
    count = len(wordlist)

    context = {
        'count': count,
        'textinput': textinput,
    }

    return render(request, 'pages/count.html', context)