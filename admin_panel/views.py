from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from admin_panel import forms as my_forms
from user import forms as user_forms
from django.forms import inlineformset_factory, modelformset_factory
# Create your views here.
from admin_panel.models import *


def statistic(request):
    data={'users_count':User.objects.count()}
    return render(request, 'admin_panel/statistic.html',context=data)


def clients(request):
    data = {'users': User.objects.all()
            }
    return render(request, 'admin_panel/clients.html', context=data)


def update_client(request, id):
    client = User.objects.get(id=id)
    if request.method == 'POST':
        client_form = user_forms.UserForm(request.POST, instance=client)
        if client_form.is_valid():
            client_form.save()
            return redirect('clients')
    client_form = user_forms.UserForm(instance=client)
    data = {'client_form': client_form, 'client_id': id}
    return render(request, 'admin_panel/update_client.html', context=data)


def delete_client(request, id):
    client = User.objects.get(id=id)
    client.delete()
    data = {'users': User.objects.all()
            }
    return render(request, 'admin_panel/clients.html', context=data)


# Create your views here.
def films(request):
    if request.method == 'POST':
        filmImgFormSet = modelformset_factory(FilmImg, form=my_forms.FilmImgForm, extra=1, )
        gallery_formset = filmImgFormSet(request.POST, request.FILES)
        film_form = my_forms.FilmForm(request.POST, request.FILES)
        seo_block = my_forms.SeoBlockForm(request.POST)
        if seo_block.is_valid():
            seo_obj = seo_block.save()
            if film_form.is_valid() and gallery_formset.is_valid():
                film_obj = film_form.save()
                film_obj.seo_block_id = seo_obj.id
                film_obj.save()
                for form in gallery_formset.cleaned_data:
                    if form:
                        FilmImg.objects.create(img=form['img'], film_id=film_obj.id)

    films = Film.objects.all()

    data = {'films': films, 'title': 'Фильмы'}
    return render(request, 'admin_panel/films.html', context=data)


def cinemas(request):
    if request.method == "POST":
        hall_form = my_forms.HallForm(request.POST, request.FILES)
        seo_form = my_forms.SeoBlockForm(request.POST)
        hallImgFormSet = modelformset_factory(FilmImg, form=my_forms.FilmImgForm, extra=1, )
        gallery_formset = hallImgFormSet(request.POST, request.FILES)
        if seo_form.is_valid():
            seo_obj = seo_form.save()
            if hall_form.is_valid() and gallery_formset.is_valid():
                hall_obj = hall_form.save()
                hall_obj.seo_block_id = seo_obj.id
                hall_obj.cinema_id = 1
                hall_obj.save()
                for form in gallery_formset.cleaned_data:
                    if form:
                        HallImg.objects.create(img=form['img'], hall_id=hall_obj.id)

    cinemas = Cinema.objects.all()
    data = {'cinemas': cinemas}
    return render(request, 'admin_panel/cinemas_all.html', context=data)


def choose_client(request):
    return render(request, 'admin_panel/choose_client.html')


def mailing(request):
    return render(request, 'admin_panel/mailing.html')


def stocks(request):
    if request.method == "POST":
        stock_form = my_forms.StockForm(request.POST, request.FILES)
        seo_form = my_forms.SeoBlockForm(request.POST)
        stockImgFormSet = modelformset_factory(StockImg, form=my_forms.StockImgForm, extra=1, )
        gallery_formset = stockImgFormSet(request.POST, request.FILES)
        if seo_form.is_valid():
            seo_obj = seo_form.save()
            if stock_form.is_valid() and gallery_formset.is_valid():
                stock_obj = stock_form.save()
                stock_obj.seo_block_id = seo_obj.id
                stock_obj.save()
                for form in gallery_formset.cleaned_data:
                    if form:
                        StockImg.objects.create(img=form['img'], stock_id=stock_obj.id)

    stocks = Stock.objects.all()
    data = {'stocks': stocks}
    return render(request, 'admin_panel/stocks.html', context=data)


def get_stock_form(request):
    stockImgFormSet = modelformset_factory(StockImg, form=my_forms.StockImgForm, extra=1)
    stockImgs_form = stockImgFormSet(queryset=StockImg.objects.none())
    stock_form = my_forms.StockForm()
    seo_form = my_forms.SeoBlockForm()

    data = {'stock_form': stock_form, 'stockImgs_form': stockImgs_form, 'seo_form': seo_form}
    return render(request, 'admin_panel/stock_card.html', context=data)


def update_stock(request, id):
    stock = Stock.objects.get(id=id)
    if request.method == 'POST':
        stock_form = my_forms.StockForm(request.POST, request.FILES, instance=stock)
        seo_obj = SeoBlock.objects.get(id=stock.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if stock_form.is_valid() and seo_form.is_valid():
            stock_form.save()
            seo_form.save()
            return redirect('stocks_table')

    stock_form = my_forms.StockForm(instance=stock)
    seo_obj = SeoBlock.objects.get(id=stock.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)
    data = {'stock_form': stock_form, 'stock_id': stock.id, 'seo_form': seo_form}
    return render(request, 'admin_panel/stock_update.html', context=data)


def delete_stock(request, id):
    stock = Stock.objects.get(id=id)
    seo_block = SeoBlock.objects.get(id=stock.seo_block.id)
    seo_block.delete()
    stock.delete()

    return redirect('stocks_table')


def news(request):
    if request.method == "POST":
        news_form = my_forms.NewsForm(request.POST, request.FILES)
        seo_form = my_forms.SeoBlockForm(request.POST)
        newsImgFormSet = modelformset_factory(NewsImg, form=my_forms.NewsImgForm, extra=1, )
        gallery_formset = newsImgFormSet(request.POST, request.FILES)

        if seo_form.is_valid():

            seo_obj = seo_form.save()
            if news_form.is_valid() and gallery_formset.is_valid():

                news_obj = news_form.save()
                news_obj.seo_block_id = seo_obj.id
                news_obj.save()
                for form in gallery_formset.cleaned_data:
                    if form:
                        NewsImg.objects.create(img=form['img'], news_id=news_obj.id)

    news_list = News.objects.all()
    data = {'news_list': news_list}
    return render(request, 'admin_panel/news.html', context=data)


def get_news_form(request):
    newsImgFormSet = modelformset_factory(NewsImg, form=my_forms.NewsImgForm, extra=1)
    newsImgs_form = newsImgFormSet(queryset=NewsImg.objects.none())
    news_form = my_forms.NewsForm()
    seo_form = my_forms.SeoBlockForm()

    data = {'news_form': news_form, 'newsImgs_form': newsImgs_form, 'seo_form': seo_form}
    return render(request, 'admin_panel/news_card.html', context=data)


def update_news(request, id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        news_form = my_forms.NewsForm(request.POST, request.FILES, instance=news)
        seo_obj = SeoBlock.objects.get(id=news.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if news_form.is_valid() and seo_form.is_valid():
            news_form.save()
            seo_form.save()
            return redirect('news_table')

    news_form = my_forms.NewsForm(instance=news)
    seo_obj = SeoBlock.objects.get(id=news.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)
    data = {'news_form': news_form, 'news_id': news.id, 'seo_form': seo_form}
    return render(request, 'admin_panel/news_update.html', context=data)


def delete_news(request, id):
    news = News.objects.get(id=id)
    seo_block = SeoBlock.objects.get(id=news.seo_block.id)
    seo_block.delete()
    news.delete()

    return redirect('news_table')


def get_film_form(request):
    filmImgFormSet = modelformset_factory(FilmImg, form=my_forms.FilmImgForm, extra=1)
    filmImg_form = filmImgFormSet(queryset=FilmImg.objects.none())

    film_form = my_forms.FilmForm()
    seo = my_forms.SeoBlockForm()

    data = {'form': film_form, 'filmImg_form': filmImg_form, 'seo_form': seo}
    return render(request, 'admin_panel/film_card.html', context=data)


def cinema_card(request, name):
    cinema = Cinema.objects.get(name=name)
    if request.method == 'POST':
        cinema_form = my_forms.CinemaForm(request.POST, request.FILES, instance=cinema)
        seo_obj = SeoBlock.objects.get(id=cinema.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if cinema_form.is_valid() and seo_form.is_valid():
            cinema_form.save()
            seo_form.save()
            return redirect('cinemas')
        else:
            cinema_form = my_forms.CinemaForm(instance=cinema)
            seo_obj = SeoBlock(id=cinema.seo_block.id)
            seo_form = my_forms.SeoBlockForm(instance=seo_obj)
            data = {'form': cinema_form, 'cinema_name': cinema.name, 'seo_form': seo_form}
            return render(request, 'admin_panel/cinema_card.html', context=data)
    seo_obj = SeoBlock.objects.get(id=cinema.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)
    halls = Hall.objects.filter(cinema_id=cinema.id)
    cinema_form = my_forms.CinemaForm(instance=cinema)
    data = {'form': cinema_form, 'cinema_name': cinema.name, 'seo_form': seo_form, 'halls': halls}
    return render(request, 'admin_panel/cinema_card.html', context=data)


def get_hall_form(request):
    hallImgFormSet = modelformset_factory(HallImg, form=my_forms.HallImgForm, extra=1)
    hallImgs_form = hallImgFormSet(queryset=HallImg.objects.none())

    hall_form = my_forms.HallForm()
    seo_form = my_forms.SeoBlockForm()

    data = {'hall_form': hall_form, 'hallImgs_form': hallImgs_form, 'seo_form': seo_form}
    return render(request, 'admin_panel/hall_card.html', context=data)


def banners_sliders(request):
    return render(request, 'admin_panel/banners_sliders.html')


def pages(request):
    if request.method == "POST":
        page_form = my_forms.PageForm(request.POST, request.FILES)
        seo_form = my_forms.SeoBlockForm(request.POST)
        pageImgFormSet = modelformset_factory(PageImg, form=my_forms.PageImgForm, extra=1, )
        gallery_formset = pageImgFormSet(request.POST, request.FILES)

        if seo_form.is_valid():

            seo_obj = seo_form.save()
            if page_form.is_valid() and gallery_formset.is_valid():

                page_obj = page_form.save()
                page_obj.seo_block_id = seo_obj.id
                page_obj.save()
                for form in gallery_formset.cleaned_data:
                    if form:
                        PageImg.objects.create(img=form['img'], page_id=page_obj.id)

    page_list = Page.objects.all()
    data = {'page_list': page_list}
    return render(request, 'admin_panel/pages.html', context=data)


def get_page_form(request):
    pageImgFormSet = modelformset_factory(PageImg, form=my_forms.PageImgForm, extra=1)
    pageImgs_form = pageImgFormSet(queryset=PageImg.objects.none())
    page_form = my_forms.PageForm()
    seo_form = my_forms.SeoBlockForm()

    data = {'page_form': page_form, 'pageImgs_form': pageImgs_form, 'seo_form': seo_form}
    return render(request, 'admin_panel/page_card.html', context=data)


def update_page(request, id):
    page = Page.objects.get(id=id)

    if request.method == 'POST':

        page_form = my_forms.PageUpdateForm(request.POST, request.FILES, instance=page)
        seo_obj = SeoBlock.objects.get(id=page.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if page_form.is_valid() and seo_form.is_valid():
            page_form.save()
            seo_form.save()
            return redirect('pages')

    page_form = my_forms.PageUpdateForm(instance=page)
    seo_obj = SeoBlock.objects.get(id=page.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)

    data = {'page_form': page_form, 'page_id': page.id, 'seo_form': seo_form}
    if page.name == 'Кафе-Бар':
        menuFormset = modelformset_factory(can_delete=True, model=CafeBarMenu, form=my_forms.CafeBarMenuForm, extra=1)
        menu_formset = menuFormset(queryset=CafeBarMenu.objects.all())
        data['menu_formset'] = menu_formset
        data['labels'] = my_forms.CafeBarMenuForm
        return render(request, 'admin_panel/cafe_bar_update.html', context=data)
    return render(request, 'admin_panel/page_update.html', context=data)


def delete_page(request, id):
    page = Page.objects.get(id=id)
    seo_block = SeoBlock.objects.get(id=page.seo_block.id)
    seo_block.delete()
    page.delete()

    return redirect('pages')


def update_film(request, name):
    film = Film.objects.get(name=name)
    if request.method == 'POST':

        film_form = my_forms.FilmForm(request.POST, request.FILES, instance=film)
        seo_obj = SeoBlock.objects.get(id=film.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if film_form.is_valid() and seo_form.is_valid():
            film_form.save()
            seo_form.save()
            return redirect('films')

    film_form = my_forms.FilmForm(instance=film)
    seo_obj = SeoBlock.objects.get(id=film.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)
    data = {'form': film_form, 'film_name': film.name, 'seo_form': seo_form}
    return render(request, 'admin_panel/film_card2.html', context=data)


def update_hall(request, number):
    hall = Hall.objects.get(number=number)
    if request.method == 'POST':

        hall_form = my_forms.HallForm(request.POST, request.FILES, instance=hall)
        seo_obj = SeoBlock.objects.get(id=hall.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if hall_form.is_valid() and seo_form.is_valid():
            hall_form.save()
            seo_form.save()
            return redirect('cinemas')

    hall_form = my_forms.HallForm(instance=hall)
    seo_obj = SeoBlock.objects.get(id=hall.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)
    data = {'hall_form': hall_form, 'hall_number': hall.number, 'seo_form': seo_form}
    return render(request, 'admin_panel/hall_update.html', context=data)


def delete_hall(request, number):
    hall = Hall.objects.get(number=number)
    seo_block = SeoBlock.objects.get(id=hall.seo_block.id)
    seo_block.delete()
    hall.delete()

    return redirect('cinemas')


def update_main_page(request):
    main_page_obj = MainPage.objects.first()

    if request.method == 'POST':
        main_page_form = my_forms.MainPageForm(request.POST, instance=main_page_obj)
        seo_obj = SeoBlock.objects.get(id=main_page_obj.seo_block.id)
        seo_form = my_forms.SeoBlockForm(request.POST, instance=seo_obj)
        if main_page_form.is_valid() and seo_form.is_valid():
            main_page_form.save()
            seo_form.save()
            return redirect('pages')
    main_page_form = my_forms.MainPageForm(instance=main_page_obj)
    seo_obj = SeoBlock.objects.get(id=main_page_obj.seo_block.id)
    seo_form = my_forms.SeoBlockForm(instance=seo_obj)
    data = {'main_page_form': main_page_form, 'seo_form': seo_form}
    return render(request, 'admin_panel/main_page.html', context=data)


def update_contacts(request):
    contactFormset = modelformset_factory(can_delete=True, model=Contact, form=my_forms.ContactForm, extra=1)
    if request.method == 'POST':
        contacts_formset = contactFormset(request.POST, request.FILES)
        if contacts_formset.is_valid():
            contacts_formset.save()
            redirect("pages")
    contacts_formset = contactFormset(queryset=Contact.objects.all())
    data = {'contacts_formset': contacts_formset}
    return render(request, 'admin_panel/update_contacts.html', context=data)
