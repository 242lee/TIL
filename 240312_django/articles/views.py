from django.shortcuts import render

# Create your views here.
# main page를 만드는 index라는 이름의 함수를 작성할게

def index(request): # 인자로 꼭 뭘 받아야 함
    return render(request, 'index.html') # templates 이후 경로를 작성