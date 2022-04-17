from django.shortcuts import render, redirect

from .forms import ChatForm, PostForm, PostSearchForm
from .models import Avatar, Chat, Post

from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

# Create your views here.
def inicio(request):
    print(str(request.user.is_authenticated))
    if (request.user.is_authenticated):
        avatar = Avatar.objects.filter(user=request.user)
        print(avatar)
        if len(avatar)>0:
            return render(request, 'appblog/index.html', {"avatar": avatar[0]})
        else:
            return render(request, 'appblog/index.html')
    return render(request, 'appblog/index.html')

def posts_view(request):
    avatar = None
    if (request.user.is_authenticated):
        avatar = Avatar.objects.filter(user=request.user)
        if len(avatar)>0:
            avatar = avatar[0]
        print(avatar)
    posts = Post.objects.all()
    no_posts = True
    if len(posts) > 0:
        no_posts = False
    return render(request, 'appblog/posts.html', {"posts": posts, "avatar": avatar, "no_posts": no_posts})

class PostDetail(DetailView):
    model = Post
    template_name = "appblog/post_detail.html"

@login_required
def create_post(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    formulario = PostForm()
    #Cuando se envían los datos entra a POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            curso = Post(content=data['content'],author=data['author'], image=data["image"], title=data["title"], subtitle=data["subtitle"], user=request.user)
            curso.save()
            return redirect('Pages')
        else:
            return render(request, 'appblog/createPost.html', {'formulario': form, "avatar": avatar})
    #Cuando hay un get
    else :
        return render(request, 'appblog/createPost.html', {'formulario': formulario, "avatar": avatar})

@login_required
def update_post(request, id):
    print(id)
    post = Post.objects.filter(id = id).first()
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            existent_post = Post.objects.filter(id = id)
            if len(existent_post)>0:
                print("Hay post existente!")
                existent_post = existent_post[0]
                existent_post.title = data["title"]
                existent_post.subtitle = data["subtitle"]
                existent_post.image = data["image"]
                existent_post.content = data["content"]
                existent_post.author = data["author"]
                existent_post.save()
            return redirect('Pages')
        else:
            return render(request, 'appblog/createPost.html', {'formulario': form, "avatar": avatar})
    else:
        if post:
            form = PostForm({"title":post.title,"subtitle":post.subtitle, "image": post.image, "content": post.content, "author": post.author})
            return render(request, 'appblog/createPost.html', {'formulario': form, "avatar": avatar})
        else:
            return redirect('Pages')

@login_required
def remove_post(request, id):
    try:
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('Pages')
    except Exception as e:
        print(e)
        return redirect('Pages')

@login_required
def search_post(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    form_search_post = PostSearchForm()
    title = request.GET.get('title', "")
    if title:
        print(title)
        form_with_data = PostSearchForm(request.GET)
        if form_with_data.is_valid():
            post = Post.objects.filter(title__contains=title)
            print (post)
            if len(post) > 0:
                return render(request, 'appblog/search_post.html', {"search_form": form_search_post,"post": post, "avatar": avatar})
            return render(request, 'appblog/search_post.html', {"search_form": form_search_post, "nopost": True, "avatar": avatar})

        return render(request, 'appblog/search_post.html', {"search_form": form_search_post, "error": form_with_data.errors, "avatar": avatar})
    
    return render(request, 'appblog/search_post.html', {"search_form": form_search_post, "avatar": avatar})

def about(request):
    return render(request, 'appblog/about.html')

@login_required
def chat (request):
    avatar = Avatar.objects.filter(user=request.user).first()
    chat_form = ChatForm()
    chat = Chat.objects.all()
    print (chat.__str__())
    if request.method == 'POST':
        chat_form_content = ChatForm(request.POST)
        if chat_form_content.is_valid():
            data = chat_form_content.cleaned_data
            chat = Chat(chat=data["chat"], user=request.user)
            chat.save()
            return redirect('Chat')
        else:
            return render(request, 'appblog/ochat.html', {"chat_form": chat_form_content, "avatar": avatar, "chat": chat})
    else:
        return render(request, 'appblog/chat.html', {"chat_form": chat_form, "avatar": avatar, "chat": chat})