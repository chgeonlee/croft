from django.urls import path
from .views import CorpHistoricalView, CorpListView
urlpatterns = [
    path( 'corps/', CorpListView.as_view() ),
    path( 'hist/', CorpHistoricalView.as_view() )
]
