from django.urls import path,include
from LMSapp_admin.views import issuebook,view_issuebook,edit_issuebook,delete_book,user_logout,search

urlpatterns = [
    path('issuebook/',issuebook,name='issue'),
    path('view_book/',view_issuebook,name='book_details'),
    path('<int:id>/',edit_issuebook,name='update_data'),
    path('delete_book/<int:id>',delete_book,name='delete'),
    path('logout',user_logout,name='logout'),
    path('search',search,name='search')

]