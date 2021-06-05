from django.urls import path,include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchList,StreamPlatformList,StreamPlatformDetailAV,ReviewList

router = DefaultRouter()
router.register('list', WatchList,basename='watchlist')

urlpatterns = [
    path('',include(router.urls)),
    # path('list/', WatchListAV.as_view(),name='watch-list'),
    # path('<int:pk>' ,WatchDetailAV.as_view(),name='watch-detail'),


    path('stream/',StreamPlatformList.as_view(), name='stream-platform' ),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-platform-detail'),

    path('review/', ReviewList.as_view(), name='review-list')

]
