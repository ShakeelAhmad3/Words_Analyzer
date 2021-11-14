import operator
from _operator import itemgetter

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def result(request):
    article = request.GET['article']
    words = article.split()
    words_count = len(words)
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    var_dic =sorted(dict_words.items(), key=operator.itemgetter(1),reverse= True)
    return render(request, 'result.html', {'article': article, 'words_count': words_count, 'dict_words': var_dic})