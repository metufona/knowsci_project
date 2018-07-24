import sitesettings.models as models
import application.models as app_models
import datetime

def first_path(request):
    return {
        'first_path': request.path.split('/')[1],
        'actuals': models.ActualArticles.objects.first(),
        'homepage': models.MainPage.objects.first(),
        'regpage': models.ReqPage.objects.first(),
        'payment': models.PaymentPage.objects.first(),
        'special': models.SpecialPage.objects.first(),
        'today_year': datetime.date.today().year,
        'last_number_pk': app_models.Magazine.objects.last().number,
    }