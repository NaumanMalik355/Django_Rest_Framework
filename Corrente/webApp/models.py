from django.db import models

class Consumo(models.Model):
    x = models.DateTimeField(auto_now_add=False,null=True)
    consumo_r = models.DecimalField(max_digits=15,decimal_places=2)
    consumo_s = models.DecimalField(max_digits=15, decimal_places=2)
    consumo_t = models.DecimalField(max_digits=15, decimal_places=2)
    consumo_total = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return str(self.consumo_r) +' | '+str(self.consumo_s)