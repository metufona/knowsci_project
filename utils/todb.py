import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0'}
DOMAIN = "http://synergy-journal.ru/"

desc_headers = ['Авторы:', 'Степень (должность):', 'Место учебы/работы:']
annotation_headers = ['Аннотация на русском языке:', 'The summary in English:', 'Ключевые слова:', "Key words:"]


def parse_titles(bs):

    bs.find('div', 't-title').find_all("strong")

    # ret = [x for x in bs.find('div', 't-title').find_all("strong") if str(x).count("</strong>") == 1 and x.text]

    text = bs.find('div', 't-title').text

    # if len(ret) !== 2:
    #
    #     if len(ret) == 1:
    #
    #
    #     raise Exception("sdasdasd")

    return {"title_rus": text, "title_eng": ""}


def parse_desc(bs):

    ret = []
    desc = str(bs.find('div', 't-descr')).replace("<br/>", " ")
    desc = desc.split("<strong>")

    for line in desc:
        line = line.replace("</div>", "")

        for h in desc_headers:
            if h in line:
                ret.append([x.strip() for x in line.split("</strong>")])
                continue

    return dict(ret)


def parse_annotation(bs):
    text = bs.find('div', 't004').find('div', 't-text').text
    borders = [ (text.find(x), text.find(x)+len(x) ) for x in annotation_headers]

    contents = []
    for i in range(len(borders)):
        try:
            contents.append(text[borders[i][1] : borders[i+1][0] ])
        except IndexError:
            contents.append(text[borders[i][1]:])

    return dict([(h,x.strip()) for h, x in zip(annotation_headers,contents) ])


def parse_article_link(bs):
    return {"link": bs.find('iframe')["src"]}

def parse_input_data(bs):
    return bs.find_all('div','t004')[-1].text


from application.models import Article
def main():

    errors = []
    for i in range(1, 358):
        link = "http://synergy-journal.ru/archive/article" + "0" * (4 - len(str(i))) + str(i)

        try:
            r = requests.get(link, headers=HEADERS)  # Выполняем запрос
            bs = BeautifulSoup(r.text, 'html.parser')  # Распарс ответа

            obj = {}
            obj.update(parse_titles(bs))
            obj.update(parse_desc(bs))
            obj.update(parse_annotation(bs))
            obj.update(parse_article_link(bs))
            obj.update({'link': link, 'pk': i})

            #print(obj)

            # ['Место учебы/работы:', 'Аннотация на русском языке:', 'title_eng', 'Key words:', 'Ключевые слова:',
            #  'title_rus', 'link', 'The summary in English:', 'Степень:', 'Авторы:', 'pk']

            article, cr = Article.objects.get_or_create(
                # magazine = obj.get()
                # science = obj.get()
                title = obj.get('title_rus'),
                title_eng = obj.get('title_eng'),
                authors = obj.get('Авторы:'),
                grade = obj.get('Степень:'),
                workplace = obj.get('Место учебы/работы:'),
                annotation_rus = obj.get('Аннотация на русском языке:'),
                annotation_end = obj.get('The summary in English:'),
                keywords_rus = obj.get('Ключевые слова:'),
                keywords_end = obj.get('Key words:'),
                url = obj.get('link'),
            )

            if cr:
                print(article)

        except Exception as e:
            print(e)
            errors.append(link)
            print("Errors: {}".format(errors))

    print("Errors: {}".format(errors))


def doparse_grade():

    for a in Article.objects.filter(grade=None):
        link = a.url
        r = requests.get(link, headers=HEADERS)  # Выполняем запрос
        bs = BeautifulSoup(r.text, 'html.parser')  # Распарс ответа
        obj = {}
        obj.update(parse_desc(bs))
        a.grade = obj.get('Степень (должность):', None)
        print(a.grade)
        a.save()


def doparse():

    for a in Article.objects.filter():
        link = a.url
        r = requests.get(link, headers=HEADERS)  # Выполняем запрос
        bs = BeautifulSoup(r.text, 'html.parser')  # Распарс ответа
        a.input_data = parse_input_data(bs)
        print(a.input_data)
        a.save()


from application import models
def make_number_to_db():
    for a in models.Article.objects.filter(input_data__isnull=False):
        number = int(str(a.input_data)[str(a.input_data).index("№")+2])
        m = models.Magazine.objects.get(pk = number)
        a.magazine = m
        a.save()




def test():
    errors = []
    for i in range(1, 358):
        link = "http://synergy-journal.ru/archive/article" + "0" * (4 - len(str(i))) + str(i)

        try:
            r = requests.get(link, headers=HEADERS)  # Выполняем запрос
            bs = BeautifulSoup(r.text, 'html.parser')  # Распарс ответа

            print(link)
            print(parse_titles(bs))

        except Exception as e:
            print(e)
            errors.append(link)
            print("Errors: {}".format(errors))


#test()

a = ['http://synergy-journal.ru/archive/article0016', 'http://synergy-journal.ru/archive/article0065',
     'http://synergy-journal.ru/archive/article0126', 'http://synergy-journal.ru/archive/article0127',
     'http://synergy-journal.ru/archive/article0317', 'http://synergy-journal.ru/archive/article0320',
     'http://synergy-journal.ru/archive/article0334', 'http://synergy-journal.ru/archive/article0344',
     'http://synergy-journal.ru/archive/article0345']
