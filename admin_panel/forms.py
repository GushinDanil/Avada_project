import django.forms as forms
from admin_panel.models import *


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['name',
                  'description',
                  'card_img',
                  'released',
                  'trailer_link',
                  'banner',
                  'year',
                  'budget',
                  'legal_age',
                  'duration',
                  'genres',
                  'producers',
                  'editors',
                  'scriptwriters',
                  'operators',
                  'technology_types',
                  'countries'

                  ]

        genres = forms.ModelMultipleChoiceField(
            queryset=Genre.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
        producers = forms.ModelMultipleChoiceField(
            queryset=Producer.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
        scriptwriters = forms.ModelMultipleChoiceField(
            queryset=ScriptWriter.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
        countries = forms.ModelMultipleChoiceField(
            queryset=Country.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
        operators = forms.ModelMultipleChoiceField(
            queryset=Operator.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
        technology_types = forms.ModelMultipleChoiceField(
            queryset=TechnologyType.objects.all(),
            widget=forms.CheckboxSelectMultiple,

        )
        widgets = {

            'genres': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
            'editors': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
            'producers': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
            'scriptwriters': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
            'operators': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
            'technology_types': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
            'countries': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', }),
        }


class SeoBlockForm(forms.ModelForm):
    class Meta:
        model = SeoBlock
        fields = '__all__'


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'short_description', 'description', 'turn_on', 'video_link', 'banner', 'card_img')


class StockImgForm(forms.ModelForm):
    class Meta:
        model = StockImg
        fields = ('img',)


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('name', 'banner', 'description', 'first_pic', 'second_pic', 'third_pic', 'description2', 'turn_on',)


class PageUpdateForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('banner', 'description', 'first_pic', 'second_pic', 'third_pic', 'description2', 'turn_on',)


class PageImgForm(forms.ModelForm):
    class Meta:
        model = PageImg
        fields = ('img',)


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = ('number', 'number2', 'seo_text',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('name', 'short_description', 'description', 'turn_on', 'video_link', 'banner', 'card_img')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'address', 'coordinate', 'logo',)


class NewsImgForm(forms.ModelForm):
    class Meta:
        model = NewsImg
        fields = ('img',)


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ('number', 'description', 'banner', 'num_tickets', 'scheme')


class HallImgForm(forms.ModelForm):
    class Meta:
        model = CinemaImg
        fields = ('img',)
        widgets = {
            'img': forms.FileInput(attrs={
                'class': 'file-input',

            }),
        }


class FilmImgForm(forms.ModelForm):
    class Meta:
        model = FilmImg
        fields = ('img',)


class CinemaImgForm(forms.ModelForm):
    class Meta:
        model = CinemaImg
        fields = ('img',)


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['name',
                  'description',
                  'banner',
                  'logo',
                  ]


class CafeBarMenuForm(forms.ModelForm):
    class Meta:
        model = CafeBarMenu
        fields = ['name',
                  'weight',
                  'price',
                  ]
