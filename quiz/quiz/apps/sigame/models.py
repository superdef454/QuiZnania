from django.db import models

class Section(models.Model):
    title = models.CharField('Название раздела', max_length=100)
    view = models.BooleanField('Отображать на сайте', default=True) # для скрытия

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class Subject(models.Model):
    section = models.ForeignKey(Section, null=False, on_delete=models.CASCADE, verbose_name="Раздел")
    title = models.CharField('Заголовок темы', max_length=100)
    round = models.PositiveIntegerField("Раунд")
    type = models.CharField('Тип игры', max_length=70) # поле, к какой игре относится тема (игра 1/игра 2/игра 3/итоговая работа/ а там выбирать уже), всё равно в каждом разделе игра 1, итоговая и тп
    view = models.BooleanField('Отображать на сайте', default=True) # для скрытия

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title

class Question(models.Model):
    # section = models.ForeignKey(Section, null=False, on_delete=models.CASCADE, verbose_name="Раздел")
    # Удалить секцию, и брать название игры из субьекта, а оттуда брать общую тему
    # а также поменять порядок фильтра в теме и тп
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Тема")
    cost = models.PositiveIntegerField('Стоимость вопроса')
    description = models.TextField('Вопроc', null=False)
    answer = models.TextField('Ответ', null=False)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        out = self.subject.title + " . " + str(self.cost)
        return out