import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0'}
DOMAIN = "http://synergy-journal.ru/"

url = "http://synergy-journal.ru/archive/article0127"


r = requests.get(url, headers=HEADERS)  # Выполняем запрос
bs = BeautifulSoup(r.text, 'html.parser')  # Распарс ответа

desc_headers = ['Авторы:', 'Степень', 'Место учебы/работы:']
annotation_headers = ['Аннотация на русском языке:', 'The summary in English:', 'Ключевые слова:', "Key words:"]


def parse_titles(bs):
    ret = []
    for i in bs.find('div', 't-title').find_all("strong"):
        if 0 > str(i).count("</strong>") > 1:
            continue
        else:
            ret.append(i.text)

    if len(ret) < 2:
        ret = str(bs.find('div', 't-title').find("strong")[0]).split('<br>')

    return {"title_rus":ret[0], "title_eng": ret[1]}


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

def main():

    errors = []
    for i in [16, 126]:
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

            print(obj)

        except Exception as e:
            print(e)
            errors.append(link)
            print("Errors: {}".format(errors))

    print("Errors: {}".format(errors))

def test_1():
    pass

if __name__ == "__main__":
    main()

# import requests
# from bs4 import BeautifulSoup
#
# HEADERS = {'User-Agent': 'Mozilla/5.0'}
# DOMAIN = "http://synergy-journal.ru/"
#
# url = "http://synergy-journal.ru/archive/10"
#
#
# def parse_articles():
#     articles = [x for x in bs.find_all("div", "r") if x["data-record-type"] == "374"]
#     #[x.find("a")["href"] for x in bs.find_all("div", "r") if x["data-record-type"] == "374"]
#
#
# if __name__ == "__main__":
#     main()


