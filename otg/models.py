from django.db import models
from django.utils import timezone


class otgadki(models.Model):
    method_ot = models.CharField(max_length=100)
    text_ot = models.TextField()
    created_date_ot = models.DateTimeField(
            default=timezone.now)
    colprogon = models.IntegerField(default = 0, verbose_name = "Количество ПРОгонов")
    pop1 = models.IntegerField(default = 0, verbose_name = "Попытка 1-я")
    pop2 = models.IntegerField(default = 0, verbose_name = "Попытка 2-я")
    pop3 = models.IntegerField(default = 0, verbose_name = "Попытка 3-я")
    pop4 = models.IntegerField(default = 0, verbose_name = "Попытка 4-я")
    pop5 = models.IntegerField(default = 0, verbose_name = "Попытка 5-я")
    pop6 = models.IntegerField(default = 0, verbose_name = "Попытка 6-я")
    pop7 = models.IntegerField(default = 0, verbose_name = "Попытка 7-я")
    pop8 = models.IntegerField(default = 0, verbose_name = "Попытка 8-я")
    pop9 = models.IntegerField(default = 0, verbose_name = "Попытка 9-я")
    pop10 = models.IntegerField(default = 0, verbose_name = "Попытка 10-я")
    pop11 = models.IntegerField(default = 0, verbose_name = "Попытка 11-я")
	
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.method_ot
