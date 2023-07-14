from django.urls import path
from .views import *

urlpatterns = [
    path("chome",CustomHomeView.as_view(),name="home"),
    path("dresscat",DressCategoryView.as_view(),name="drscat"),
    path("outf",OutfitView.as_view(),name="out"),
    path("dressder/<int:did>",DressDetailsView.as_view(),name="drsdet"),
    path("addcar/<int:id>",AddCart.as_view(),name="addcar"),
    path("delcart/<int:id>",deletecartitem,name="delcart"),
    path("cartview",CartListView.as_view(),name="vcart"),
    path("check/<int:cid>",CheckoutView.as_view(),name="check"),
    path("orderv",OrderListView.as_view(),name="vorder"),
    path("delorder/<int:id>",deleteorderitem,name="delorder"),
    path("search",SearchView.as_view(),name="search"),
    path("catview/<int:id>",OutfitinCatView.as_view(),name="catpro")
]

