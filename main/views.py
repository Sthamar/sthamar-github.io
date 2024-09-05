from django.shortcuts import render
from main.models import Contact, Info, Experience, Skill, Award, Cv

# Create your views here.

def index(request):
    profile = Info.objects.all()[0]
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    contact = Contact.objects.all()[0]
    cv = Cv.objects.all()[0]
    context = {"profile":profile,"experience":experience, "skills":skills, "contact":contact,'cv':cv}
    return render(request, 'main/index.html',context)