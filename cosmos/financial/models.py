from django.db import models
from django.utils import timezone

class CorpBaseModel( models.Model ):
        
    name    = models.CharField( verbose_name= 'corp name', max_length=100 )
    ticker  = models.CharField( verbose_name= 'corp ticker', max_length= 30 )
    
    class Meta:
        abstract = True

class CorpHistoricalModel( CorpBaseModel):
    
    open    = models.IntegerField()
    high    = models.IntegerField()
    low     = models.IntegerField()
    close   = models.IntegerField()
    volumn  = models.IntegerField()
    date    = models.DateField( default= timezone.now() )
    
    class Meta:
        db_table = 'corp_historical_table'
        
