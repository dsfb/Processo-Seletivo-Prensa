from django.db import models


"""
Consulta 

{'bin': {'issuer': {'name': 'BANCO DO BRASIL SA'}, 'product': {'name': 'Grafite'}, 'allowedCaptures': [{'name': 'POS', 'code': 1}, {'name': 'TEF', 'code': 2}, {'name': 'INTERNET', 'code': 3}, {'name': 'TELEMARKETING', 'code': 4}, {'name': 'ATM', 'code': 5}], 'usages': [{'name': 'Crédito Elo à vista ', 'code': 0}, {'name': 'Elo Parcelado Loja', 'code': 0}, {'name': 'Débito Elo à Vista', 'code': 0}], 'services': []}}
"""

class TabelaBin(models.Model):
    number_bin = models.IntegerField(primary_key=True)
    name_issuer = models.CharField(max_length=100)
    name_product = models.CharField(max_length=100)
    allowedCaptures_name = models.CharField(max_length=100)
    allowedCaptures_code = models.IntegerField()
    usages_name = models.CharField(max_length=100)
    usages_code = models.IntegerField()
    services_name = models.CharField(max_length=100)
    services_isExchangeableOffer = models.BooleanField(default=False)
