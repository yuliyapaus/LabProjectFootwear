from django.urls import path
from .views import (BbCreateView,
                    BbIndexView,
                    BbDetailView,
                    BbByRubricView)


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('', BbIndexView.as_view(), name = 'index'),
    ]