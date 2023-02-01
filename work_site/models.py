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


class Directors(AbstractEmploy):

class AssociateDirs(AbstractEmploy):
    leader = models.ForeignKey(Directors, on_delete=models.PROTECT)


class Managers(AbstractEmploy):
    leader = models.ForeignKey(AbstractEmploy, on_delete=models.PROTECT)


class OperatorsKTZ(AbstractEmploy):
    leader = models.ForeignKey(Managers, on_delete=models.PROTECT)


class OperatorsElec(AbstractEmploy):
    leader = models.ForeignKey(Managers, on_delete=models.PROTECT)


class Crawlers(AbstractEmploy):
    leader = models.ForeignKey(OperatorsKTZ, on_delete=models.PROTECT)


class Electric(AbstractEmploy):
    leader = models.ForeignKey(OperatorsElec, on_delete=models.PROTECT)

