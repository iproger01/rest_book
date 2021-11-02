from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save


class AutorManager(models.Manager):
    def create_autor(self, name, surename, fathername, city, birthday):

        autor = self.create(name=name.capitalize(), surename=surename.capitalize(), fathername=fathername.capitalize(), city=city.capitalize(), birthday=birthday)
        return autor

# class StatistManager(models.Manager):


class Autor(models.Model):

    name = models.CharField(max_length=250, verbose_name='Имя')
    surename = models.CharField(max_length=250, verbose_name='Фамилия')
    fathername = models.CharField(max_length=250, blank=True, null=True, verbose_name='Отчество')
    city = models.CharField(max_length=250, verbose_name='Город')
    birthday = models.DateField(verbose_name='День рождения')

    objects = AutorManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']

class Books(models.Model):

    name = models.CharField(max_length=250)
    write_date = models.DateField()
    description = models.CharField(max_length=4000, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/%y/%m/%d')
    autor_relative = models.ForeignKey('Autor', on_delete=models.PROTECT, verbose_name='Автор произведения', null=True)

    def book_autor(self, obj):
        autor = Autor.objects.get(id=obj.id)
        return f'{autor.name} {autor.surename} {autor.fathername}'

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']

class Review(models.Model):

    nic = models.CharField(max_length=250)
    review = models.CharField(max_length=3000)
    book_id = models.ForeignKey('Books', on_delete=models.PROTECT, verbose_name='Книга')

    def __str__(self):
        return str(self.nic)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['nic']

class Shop(models.Model):

    name = models.CharField(verbose_name='Название магазина', max_length=150)
    adress = models.CharField(verbose_name='Адрес', max_length=1000)
    phone = models.CharField(verbose_name='Телефон', max_length=16)
    assort = models.ManyToManyField(Books, related_name='assort_to_books', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        ordering = ['name']


class StatistData(models.Model):

    save_books = models.IntegerField(verbose_name='Кол-во книг')
    save_date = models.DateField(auto_now_add=True, verbose_name='День сохранения')
    save_books_name = models.CharField(verbose_name='Книги, которые добавили в этот день', max_length=1500, blank=True, null=True)

    def __str__(self):
        return str(self.save_date)

    class Meta:
        verbose_name = "статистику за день"
        verbose_name_plural = "статистика за день"


@receiver(pre_save, sender=Books)
def save_book(sender, **kwargs):
    date_now = datetime.now().date()
    queryset = StatistData.objects.filter(save_date=date_now)
    if queryset.exists():
        print('повторное сохранение статистики')

        for item in queryset:
            colvo = item.save_books + 1
            print(colvo)

            item.save_books = colvo
            item.save()

    else:
        print('сохранение статистики впервые')
        StatistData.objects.create(save_books=1, save_date=date_now)


# pre_save.conect(save_book, sender=Books)


