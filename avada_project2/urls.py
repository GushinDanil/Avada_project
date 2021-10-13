"""avada_project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include

import kino_app.views
#делать на главной странице проэкта список фильмов только для главного кинотеатра чтобы не усложнять себе жизнь
urlpatterns = [
    path("main.html", kino_app.views.func),
    path("signin.html", kino_app.views.func3),
    path("cinemas.html", kino_app.views.func5),
    path("soon.html", kino_app.views.func6),
    path("schedule.html", kino_app.views.func7),
    path("card_cinema.html", kino_app.views.func8),
    path("film_card.html", kino_app.views.func9),
    path("hall.html", kino_app.views.func10),
    path("bar.html", kino_app.views.func11),
    path("vip_hall.html", kino_app.views.func12),
    path("kids_room.html", kino_app.views.func13),
    path("ads.html", kino_app.views.func14),
    path("mobile_apps.html", kino_app.views.func15),
    path("contacts.html", kino_app.views.func16),
    path("news.html", kino_app.views.func17),
    path("stocks.html", kino_app.views.func18),
    path("page_stock.html", kino_app.views.func19),
    path("page_news.html", kino_app.views.func20),
    path("poster.html", kino_app.views.func2),
    path("register.html", kino_app.views.func4),

]
