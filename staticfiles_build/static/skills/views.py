from django.shortcuts import render

# Create your views here.
def skills(request):
    context = {'skill':'active'}
    return render(request, 'skills/skills.html', context)