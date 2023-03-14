from rest_framework import generics, response, status, serializers
from .models import CorpHistoricalModel
from datetime import datetime

# serializer

class CorpModelSerializer( serializers.Serializer ):
    
    class Meta:
        model = CorpHistoricalModel
        fields = [ 'name', 'ticker', 'open', 'high', 'low', 'close', 'volumn', 'date' ]
    
    name = serializers.CharField( max_length = 100 )
    ticker = serializers.CharField( max_length = 30 )
    open    = serializers.IntegerField()
    high    = serializers.IntegerField()
    low     = serializers.IntegerField()
    close   = serializers.IntegerField()
    volumn  = serializers.IntegerField()
    date    = serializers.DateField( default= datetime.now() )

class CorpHistoricalView( generics.ListCreateAPIView ):
    serializer_class = CorpModelSerializer
    
    def get( self, request ):
        for obj in CorpHistoricalModel.objects.all():
            print( obj )
        
        return response.Response( dict( msg = 'temporary' ), status=status.HTTP_200_OK )
        
    # def post( self, request ):
    #     return response.Response( dict(), status=status.HTTP_200_OK )


class CorpListView( generics.ListAPIView ):
        
    def get( self, request ):        
        resp = list(set([ obj.name for obj in CorpHistoricalModel.objects.all() ]))
        
        return response.Response( dict( data = resp, msg = 'corporate list' ), status=status.HTTP_200_OK )
            
        
        