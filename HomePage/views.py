from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request,template_name='../templates/app/nav.html')





def base(request):
    return render(request,template_name='../templates/app/Base.html')




def Login(request):
    return render(request,template_name='../templates/app/Login.html')


def Registation(request):
    return render(request,template_name='../templates/app/Registration.html')


