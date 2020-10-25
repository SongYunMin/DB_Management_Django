from django.shortcuts import render


# Create your views here.
def home(request):
    # render : 첫번째 인자부터 요청, 템플릿 이름, 딕셔너리형 자료형
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    # text 변수에 텍스트 받음
    text = request.GET['fulltext']
    words = text.split() # split : 공백 기준으로 나눔
    word_dictionary = {}

    for word in words :
        if word in word_dictionary:
            word_dictionary[word] += 1
        else :
            #add to dictionary
            word_dictionary[word] = 1
    # 세번째 인자 키:값
    return render(request, 'result.html',
                  {'full': text, 'total': len(words),
                   'dictionary': word_dictionary.items()})

