from django.db import models


class MainPage(models.Model):
    priem = models.TextField(blank=True, null=True, verbose_name='Прием статей', help_text="Блок Открыт прием статей")
    main_image = models.ImageField(upload_to="settings", blank=True, null=True, verbose_name="Главная картинка")
    email = models.EmailField(verbose_name="Почта для вопросов", default="synergy-journal-question@mail.ru")
    bottom = models.TextField(verbose_name="Футер")
    about = models.TextField(verbose_name="о журнале")

    def __str__(self):
        return "Изменить"

    class Meta:
        verbose_name = "Настройки главной страницы"
        verbose_name_plural = "Настройки главной страницы"



class ActualArticles(models.Model):
    header_1 = models.CharField(max_length=150, verbose_name='Заголовок актуальной статьи 1')
    image_1 = models.ImageField(upload_to="actual", verbose_name="Изображение актуальной статьи 1")
    text_1 = models.TextField( verbose_name="Текст актуальной статьи 1")
    link_1 = models.CharField(max_length=150,verbose_name="Ссылка статиьи 1")

    header_2 = models.CharField(max_length=150, verbose_name='Заголовок актуальной статьи 2')
    image_2 = models.ImageField(upload_to="actual",
                                verbose_name="Изображение актуальной статьи 2")
    text_2 = models.TextField(verbose_name="Текст актуальной статьи 2")
    link_2 = models.CharField(max_length=150,verbose_name="Ссылка статиьи 2")

    header_3 = models.CharField(max_length=150, verbose_name='Заголовок актуальной статьи 3')
    image_3 = models.ImageField(upload_to="actual",
                                verbose_name="Изображение актуальной статьи 3")
    text_3 = models.TextField(verbose_name="Текст актуальной статьи 3")
    link_3 = models.CharField(max_length=150,verbose_name="Ссылка статиьи 3")

    def __str__(self):
        return "Изменить"

    class Meta:
        verbose_name = "Настройки актуальных статей"
        verbose_name_plural = "Настройки актуальных статей"


class ReqPage(models.Model):
    text = models.TextField(verbose_name="Текст")
    examle_link = models.URLField(verbose_name="Ссылка на пример оформления")
    information_link = models.URLField(verbose_name="Ссылка на сопроводительную информацию")

    def __str__(self):
        return "Изменить"

    class Meta:
        verbose_name = "Настройки страницы требований"
        verbose_name_plural = "Настройки страницы требований"


class PaymentPage(models.Model):
    public = models.TextField(verbose_name="Текст - Оплата публикаций")
    editor = models.TextField(verbose_name="Текст - Оплата оформления статьи")

    yandex_widget_1 = models.TextField(verbose_name="Виджет - Оплата публикаций")
    yandex_widget_2 = models.TextField(verbose_name="Виджет - Оплата оформления статьи")

    def __str__(self):
        return "Изменить"

    class Meta:
        verbose_name = "Настройки страницы оплаты"
        verbose_name_plural = "Настройки страницы оплаты"


class SpecialPage(models.Model):
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return "Изменить"

    class Meta:
        verbose_name = "Настройки страницы информации о спецвыпуске"
        verbose_name_plural = "Настройки страницы информации о спецвыпуске"
