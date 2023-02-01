from django.db import models

class AbstractEmploy(models.Model):
    fio = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    employment_date = models.DateTimeField(auto_created=True, blank=True)
    salary = models.IntegerField()

    def __str__(self):
        return self.fio

    class Meta:
        abstract = True


class Director(AbstractEmploy):
    class Meta:
        verbose_name_plural = 'DIRs'


class AssociateDir(AbstractEmploy):
    leader = models.ForeignKey(Director, on_delete=models.PROTECT)
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

