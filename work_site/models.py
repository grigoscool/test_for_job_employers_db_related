import random
from django.db import models
from django.db.models import Q
from stdimage import StdImageField


class DirectorManager(models.Manager):
    def search(self, searching_data=None):
        if searching_data is None or searching_data == '':
            return self.get_queryset().none()
        lookups = (
                Q(fio__icontains=searching_data) |
                Q(job__icontains=searching_data) |
                Q(salary__icontains=searching_data)
        )
        return self.get_queryset().filter(lookups)


class AbstractEmploy(models.Model):
    fio = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    employment_date = models.DateTimeField(
        auto_now_add=True, blank=True
    )
    salary = models.IntegerField()
    photo = StdImageField(
        upload_to='photos', null=True, blank=True,
        variations={'thumbnail': {'width': 100, 'height': 75}}
    )


    def __str__(self):
        return self.fio

    class Meta:
        abstract = True


class Director(AbstractEmploy):
    asistent = models.ForeignKey(
        'AssociateDir', on_delete=models.SET_DEFAULT,
        null=True, default='Jos Ner Nfd'
    )

    objects = DirectorManager()

    class Meta:
        verbose_name_plural = 'DIRs'

    def delete(self, *args, **kwargs):
        asistents = AssociateDir.objects.filter(leader_id=self.pk)
        if asistents:
            directors = Director.objects.all().values_list('id')
            for asistent in asistents:
                asistent.leader_id = random.choice(directors)[0]
                asistent.save()
        super(Director, self).delete(*args, **kwargs)


class AssociateDir(AbstractEmploy):
    leader = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = 'AssociateDirs'


class Manager(AbstractEmploy):
    leader = models.ForeignKey(
        AssociateDir, on_delete=models.PROTECT
    )


class OperatorsKTZ(AbstractEmploy):
    leader = models.ForeignKey(
        Manager, on_delete=models.PROTECT
    )


class OperatorsElec(AbstractEmploy):
    leader = models.ForeignKey(
        Manager, on_delete=models.PROTECT
    )


class Crawler(AbstractEmploy):
    leader = models.ForeignKey(
        OperatorsKTZ, on_delete=models.PROTECT
    )


class Electric(AbstractEmploy):
    leader = models.ForeignKey(
        OperatorsElec, on_delete=models.PROTECT
    )
