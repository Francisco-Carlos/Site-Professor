from django.shortcuts import render, redirect, get_object_or_404
from .models import Conteudos
from  django.contrib.auth.models import User,auth
from pytube import YouTube
# Create your views here.

def Index(request):
    arquivo = Conteudos.objects.all()
    dados = {'arquivo':arquivo}
    return render(request,'index.html',dados)

def Dados(request):
    arquivos = Conteudos.objects.all()
    dados = {'arquivos':arquivos}
    return render(request,'Conteudos.html',dados)

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username',flat=True).get()
            user = auth.authenticate(request,username=nome,password=senha)
            if user is not None:
                auth.login(request,user)
                return redirect('dashbord')
    else:
        return render(request,'Login.html')

def Sair(request):
    auth.logout(request)
    return redirect('index')

def Cadastrar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha_1 = request.POST['senha']
        senha_2 = request.POST['senha_2']
        if not nome.strip():
            redirect('cadastrar')
        if not email.strip():
            redirect('cadastrar')
        if senha_1 != senha_2:
            redirect('cadastrar')
        if User.objects.filter(email=email).exists():
            return  redirect('cadastrar')
        user = User.objects.create_user(username=nome,email=email,password=senha_1)
        user.save()
        return redirect('login')
    else:
        return render(request,'Cadastrar.html')

def Deletar(request,id):
    arq = Conteudos.objects.get(id=id)
    arq.delete()
    return redirect('dashbord')


def Dashbord(request):
    if request.user.is_authenticated:
        id = request.user.id
        arqui = Conteudos.objects.all().filter(Criador=id)
        dados = {'arqui':arqui}
        return render(request,'Dashbord.html',dados)
    else:
        return redirect('Index')

def Criar(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descri = request.POST['descricao']
        arqui = request.FILES['arquivo']
        user = get_object_or_404(User,pk=request.user.id)
        conte = Conteudos.objects.create(Criador=user,Nome=titulo,Conteudo=descri,Arquivo=arqui)
        conte.save()
        return redirect('dashbord')
    else:
        return render(request,'Dashbord.html')

def Baixar(request):
    if request.method == 'POST':
        link = request.POST['link']
        caminho = request.POST['caminho']
        yt = YouTube(link)
        mensagen =' sucesso'
        ys = yt.streams.filter(res="360p").first()
        ys.download(caminho)
        baixar = {'mensagen':mensagen}
        return render(request,'Baixar.html',baixar)
    else:
        return render(request,'Baixar.html')