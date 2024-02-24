from django.shortcuts import render, redirect
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .utils import is_ajax, classify_face
import base64
from django.core.files.base import ContentFile
from core_Profile .models import *
from core_Logs .models import Log

def Login_view(request):
    if not request.user.is_authenticated:
        context = {

        }
        return render(request, 'login.html', context)
    else:
        return redirect('home')

@login_required(login_url='login')
def Logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Home_view(request):
    return render(request, 'home.html')


def Find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = User.objects.filter(username=res).exists()
            if user_exists:
                user = User.objects.get(username=res)
                profile = User_profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})