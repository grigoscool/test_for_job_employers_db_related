import random
from django.db import models
from django.urls import reverse


class AbstractEmploy(models.Model):
    fio = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    employment_date = models.DateTimeField(auto_now_add=True, blank=True)
    salary = models.IntegerField()
    photo = models.ImageField(upload_to='photos', null=True)

    def __str__(self):
        return self.fio

    class Meta:
        abstract = True


class Director(AbstractEmploy):
    asistent = models.ForeignKey('AssociateDir', on_delete=models.SET_DEFAULT, null=True, default='Jos Ner Nfd')

    class Meta:
        verbose_name_plural = 'DIRs'

    def delete(self, *args, **kwargs):
        asistents = AssociateDir.objects.filter(leader_id=self.pk)
        if asistents:
            directors = Director.objects.all().values_list('id')
            print(directors)
            for asistent in asistents:
                asistent.leader_id = random.choice(directors)[0]
                print(asistent.leader_id)
                asistent.save()
        super(Director, self).delete(*args, **kwargs)


class AssociateDir(AbstractEmploy):
    leader = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'AssociateDirs'


class Manager(AbstractEmploy):
    leader = models.ForeignKey(AssociateDir, on_delete=models.PROTECT)


class OperatorsKTZ(AbstractEmploy):
    leader = models.ForeignKey(Manager, on_delete=models.PROTECT)


class OperatorsElec(AbstractEmploy):
    leader = models.ForeignKey(Manager, on_delete=models.PROTECT)


class Crawler(AbstractEmploy):
    leader = models.ForeignKey(OperatorsKTZ, on_delete=models.PROTECT)


class Electric(AbstractEmploy):
    leader = models.ForeignKey(OperatorsElec, on_delete=models.PROTECT)
