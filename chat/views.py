from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect
from .models import Full_chat , Message
from .forms import ChatForm
from django.contrib.auth.models import  User, auth
from django.urls import reverse
from django.views import generic



from django import forms

# print(request.user.username)

def chat_view(request) :

    a=(request.user.username)
    form = ChatForm()
    chat = Full_chat.objects.all()

    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user or None
            obj.save()

            

    context = { 'form' : form ,
                 'all_chat' : chat[::-1] ,
                'a':a ,
                }

    return render(request, 'chat/chat.html', context)

def user_post(request) :
    chat = Full_chat.objects.all()
    username = request.GET.get('username')
    # if username != None :
    user_chat = chat.filter(user__username__iexact = username)
    context = {'user_chat':user_chat}

    return render(request, 'chat/user_post.html' ,context)


# @permission_classes([IsAuthenticated])

def total_likes(request , pk ) :
    chat = Full_chat.objects.get(id=pk)
    total = chat.total_likes()
    context = {'total_likes': total}

    return render(request, 'chat/chat.html', context)
def like_chat(request, pk) :
    # chat = get_object_or_404(Full_chat, id=request.POST.get('post_id'))
    chat = Full_chat.objects.get(id= pk)
    chat.likes.add(request.user)

    return HttpResponseRedirect('/chat/')
    # return HttpResponseRedirect(reverse('update_chat' , args=[str(pk)] ))
    # chat_to_like = Full_chat.objects.get(id= pk)
    # if request.user in chat_to_like.likes.all() :
    #     chat_to_like.likes.remove(request.user)
    # else :
    #     chat_to_like.likes.add(request.user)
    # return HttpResponseRedirect('/chat/')

def delete_chat(request, chat_id) :
    chat_to_delete = Full_chat.objects.get(id= chat_id)
    chat_to_delete.delete()
    return HttpResponseRedirect('/chat/')



def update_chat(request , pk) :
    all_chat = Full_chat.objects.get(id=pk)
    form = ChatForm(instance= all_chat)

    context = {'form' : form}

    if request.method == 'POST' :
        form = ChatForm(request.POST, instance=all_chat)
        if form.is_valid():
            form.save()
            return redirect('/chat/')

    return render(request, 'chat/update.html', context)



