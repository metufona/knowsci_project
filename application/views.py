from django.shortcuts import render, redirect, Http404, HttpResponse
from application.models import Article, Magazine, Science, Feedback, SpecialMagazine
from django.views.generic.base import TemplateView, View


class ArticleView(View):

    def get(self, request, *args, **kwargs):

        pagename = kwargs['pagename']

        if not pagename:
            raise Http404

        number = int(pagename)

        article = Article.objects.get(number = number)
        return render(request, 'article.html', locals())


class MagazineView(View):

    def get(self, request, *args, **kwargs):

        magazine = kwargs['magazine']
        if not magazine:
            raise Http404
        magazine = int(magazine)
        magazine = Magazine.objects.get(number=magazine)

        scis = [ x.science.pk for x in magazine.article_set.all() ]
        scis = Science.objects.filter(pk__in = scis).order_by("ordering")

        for s in scis:
            s.arts = s.article_set.filter(magazine=magazine)

        return render(request, 'magazine.html', locals())



class MagazineListView(View):
    def get(self, request, *args, **kwargs):

        years = range(2015, 2025)[::-1]
        years_magazine = [Magazine.objects.filter(year=y).order_by('mouth') for y in years]

        magazines = zip(years, years_magazine)

        return render(request, 'archive.html', locals())



class FeedbackView(View):

    def post(self, request, *args, **kwargs):

        name = request.POST.get("name", "")
        question = request.POST.get("comment", "")
        email = request.POST.get("e-mail", "")

        Feedback.objects.create(name=name, question=question, email=email)

        try:
            from django.core.mail import send_mail
            from sitesettings.models import MainPage

            to = MainPage.objects.first().email

            send_mail(
                'Вопрос на сайте nauka-journal.ru',
                'Имя: {}\nПочта: {}\nВопрос: {}\n'.format(name, email, question),
                's.pi7@mail.ru',
                [to],
                fail_silently=False,
            )
        except:
            pass


        return redirect("/")
