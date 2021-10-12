from django.db import models

class Autor(models.Model):

    name = models.CharField(max_length=250, verbose_name='Имя')
    surename = models.CharField(max_length=250, verbose_name='Фамилия')
    fathername = models.CharField(max_length=250, blank=True, null=True, verbose_name='Отчество')
    city = models.CharField(max_length=250, verbose_name='Город')
    birthday = models.DateField(verbose_name='День рождения')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']

class Books(models.Model):

    name = models.CharField(max_length=250 )
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