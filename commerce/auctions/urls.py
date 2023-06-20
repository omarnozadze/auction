from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category", views.category, name="category"),
    path("create_auction", views.create_auction, name="create-auction"),
    path("show_listing/<list_id>", views.show_listing, name="show-listing"),
    path("update_auction/<list_id>", views.update_auction, name="update-auction"),
    path("delete_auction/<list_id>", views.delete_auction, name="delete-auction"),
    path("addBid/<list_id>", views.addBid, name="addBid"),
]
