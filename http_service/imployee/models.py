from django.db import models


class Imployee(models.Model):
    id_redmine = models.IntegerField(verbose_name='ID для Redmine')
    name = models.CharField(verbose_name='ФИО', max_length=150)
    is_enabled = models.BooleanField(default=True, verbose_name='Включено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']


class VacationDate(models.Model):
    date_start = models.DateField(verbose_name='Дата начала')
    date_finish = models.DateField(verbose_name='Дата конца')
    reason = models.CharField(max_length=150, verbose_name='Причина')
    imployee = models.ForeignKey('Imployee', on_delete=models.PROTECT, verbose_name='сотрудник')

    def __str__(self):
        return "%s - %s/%s" % (self.reason, self.date_start, self.date_finish)
