from django import forms
from .models import Article
'''
# models랑 비슷
# 사용자로부터 입력받는 값만
class ArticleForm(forms.Form):
    # 인풋태그가 될 title에 조건을 줘
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
'''

class ArticleForm(forms.ModelForm):
    class Meta:
        # 어떤 모델과 연동할 건지, Article()로 호출 노노
        model = Article
        # 그 모델에서 어떤 필드 쓸 건지 (전체)
        fields = '__all__'
        # exclude = ('title') # 제거