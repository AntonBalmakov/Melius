from django.db import models


class Manufacturer(models.Model):
    name = models.TextField(max_length=200, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class CreditBit(models.Model):
    name = models.TextField(max_length=200, null=True)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, related_name="creditbits")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Кредитная заявка"
        verbose_name_plural = "Кредитные заявки"


class Product(models.Model):
    name = models.TextField(max_length=200, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="products", null=True)
    creditbit = models.ForeignKey('CreditBit', on_delete=models.CASCADE, related_name="products", null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Contract(models.Model):
    name = models.TextField(max_length=200, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
