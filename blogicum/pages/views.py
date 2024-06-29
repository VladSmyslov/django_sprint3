from django.shortcuts import render


def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)
