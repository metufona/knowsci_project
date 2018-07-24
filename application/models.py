from django.db import models
import datetime

class Article(models.Model):

    number = models.IntegerField(unique=True, verbose_name='Порядковый номер статьи', help_text="Используется для ссылки: 1 -> article0001")

    magazine = models.ForeignKey("Magazine", verbose_name='Выпуск журнала')
    science = models.ForeignKey("Science", verbose_name='Вид наук')

    magazine_title = models.CharField(max_length=300, verbose_name='Название статьи (Rus)', help_text="Используются для вывода выходных данных и отображения в списке статей при просмотре номера журнала")
    title_eng = models.CharField(max_length=300, verbose_name='Название статьи (Eng)', help_text="Заголовок (на английском языке) при отображении статьи")

    authors = models.CharField(blank=True, null=True, max_length=300, verbose_name='Авторы', help_text="Авторы при отображении статьи (Фамилия Имя Отчество полностью)")
    magazine_authors = models.CharField(max_length=300, verbose_name='Авторы в журнале', help_text="(Фамилия И.О.) Используются для вывода выходных данных и отображения в списке статей при просмотре номера журнала")

    grade = models.CharField(max_length=300, blank=True, null=True, verbose_name='Степень')
    workplace = models.CharField(max_length=300, blank=True, null=True, verbose_name='Место работы/учебы')

    annotation_rus = models.TextField(verbose_name='Аннотация (Rus)', default="")
    annotation_end = models.TextField(verbose_name='Аннотация (Eng)', default="")

    keywords_rus = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ключевые слова (Rus)')
    keywords_end = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ключевые слова (Eng)')

    pages = models.CharField(max_length=300, blank=True, null=True, verbose_name='Страницы в журнале', help_text="Используются для вывода выходных данных")

    url = models.CharField(max_length=300, verbose_name='Cсылка', help_text="Ссылка на Google Drive")

    badge = models.ImageField(upload_to="articles", blank=True, null=True, verbose_name='Бейджик для соцсетей')

    def __str__(self):
        return self.magazine_title

    def title(self):
        return self.magazine_title

    def make_url_to_remote(self):
        return "http://nauka-journal.ru/archive/article" + "0" * (4 - len(str(self.number))) + str(self.number)

    def make_short_url(self):
        return "/archive/article" + "0" * (4 - len(str(self.number))) + str(self.number)

    def get_prev(self):
        try:
            return Article.objects.get(number=self.number-1)
        except Exception:
            return None

    def get_next(self):
        try:
            return Article.objects.get(number=self.number+1)
        except Exception:
            return None

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Science(models.Model):
    name = models.CharField(max_length=150, verbose_name='Вид науки', unique=True)
    image = models.ImageField(upload_to="science", blank=True, null=True, verbose_name='Изображение')
    ordering = models.IntegerField(default=0, verbose_name='Сортировка')

    def __str__(self):
        return self.name

    def get_image(self):
        return self.image.url

    class Meta:
        ordering = ["ordering"]
        verbose_name = "Вид наук"
        verbose_name_plural = "Виды наук"

MOUTHS = (
    (1, 'Январь'),
    (2, 'Февраль'),
    (3, 'Март'),
    (4, 'Апрель'),
    (5, 'Май'),
    (6, 'Июнь'),
    (7, 'Июль'),
    (8, 'Август'),
    (9, 'Сентябрь'),
    (10, 'Октябрь'),
    (11, 'Ноябрь'),
    (12, 'Декабрь'),
)

DMOUTHS = dict(MOUTHS)


class Magazine(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер журнала', unique=True)
    mouth = models.IntegerField(verbose_name="Месяц", choices=MOUTHS)
    year = models.IntegerField(verbose_name="Год")
    image = models.ImageField(upload_to="magazine", verbose_name='Обложка')

    priem = models.DateField(verbose_name="Прием статей")
    publish = models.DateField(verbose_name="Размещение журнала в электронном виде")
    elibrary = models.DateField(verbose_name="Отправка журнала в Elibrary")

    url = models.CharField(max_length=300, blank=True, null=True, verbose_name='Полный выпуск', help_text="Ссылка на Google Drive")

    def __str__(self):
        return "Выпуск №{} ({}/{})".format(self.number, self.mouth, self.year)

    def get_nice_mouth(self):
        return DMOUTHS.get(self.mouth, "")

    def is_it_last(self):
        return max(Magazine.objects.all().values_list('number', flat=True)) == self.number

    def active_stage(self):
        stage = 0
        today = datetime.date.today()

        if today > self.elibrary:
            return 0

        if self.publish < today <= self.elibrary:
            return 3

        if self.priem < today <= self.publish:
            return 2

        if self.priem <= today:
            return 1

        return stage

    class Meta:
        ordering = ("year", "mouth")
        verbose_name = "Выпуск журнала"
        verbose_name_plural = "Выпуски журнала"


class SpecialMagazine(models.Model):
    number = models.CharField(max_length=300, verbose_name='Номер журнала', unique=True, help_text="Используется для ссылки: 9 -> S9")
    day = models.IntegerField(verbose_name="День")
    mouth = models.IntegerField(verbose_name="Месяц", choices=MOUTHS)
    year = models.IntegerField(verbose_name="Год")
    image = models.ImageField(upload_to="magazine", blank=True, null=True, verbose_name='Обложка')

    title = models.CharField(max_length=300, verbose_name='Заголовок журнала', unique=True)
    organizator = models.TextField(blank=True, null=True, verbose_name='Организатор', help_text="Отображается на странице журнала")

    example = models.TextField(blank=True, null=True, verbose_name='Пример выходных данных', help_text="Отображается на странице журнала")

    url = models.CharField(max_length=300, blank=True, null=True, verbose_name='Полный выпуск',
                           help_text="Ссылка на Google Drive")

    def __str__(self):
        return "Специальный Выпуск №{} ({}/{})".format(self.pk, self.mouth, self.year)

    def get_nice_mouth(self):
        return DMOUTHS.get(self.mouth, "")

    class Meta:
        ordering = ("year", "mouth")
        verbose_name = "Специльный выпуск журнала"
        verbose_name_plural = "Специльные выпуски журнала"


class Feedback(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name='Имя')
    question = models.TextField(blank=True, null=True, verbose_name='Вопрос')
    email = models.CharField(max_length=300, blank=True, null=True, verbose_name='Электронная почта')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

