from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.borrows, name='borrows'),
    path("borrow/<int:borrow_id>", views.borrow, name="borrow"),
    path("completes", views.completes, name="completes"),
    path("borrow/<int:borrow_id>/returned", views.returned, name="returned"),
    path('accounts/', include('django.contrib.auth.urls')),
]
