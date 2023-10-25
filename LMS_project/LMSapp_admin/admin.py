from django.contrib import admin
from LMSapp_admin.models import Book,issued_book,User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.register(User)
class UserAdmin(UserAdmin):
     list_display=['id','first_name','last_name','email','is_active',]
     readonly_fields = ["id",
                       "created_on", "updated_on"]
     fieldsets = (
        # User Informations
        (
            "Register Info:",
            {
                "fields": ("id", "email", "phone","password")
            }
        ),

        # Personal Informations
        (
            "Personal Info",
            {
                "fields": ("first_name", "last_name", "profile_image"),
            },
        ),


        # Other Informations
        (
            "Other Info",
            {
                "fields": ("user_type",),
            },
        ),

        # Login Informations
        (
            "Login Info",
            {
                "fields": ("updated_on", "created_on", "last_login",),
            },
        ),

        # Permissions
        (
            "Permissions",
            {
                "fields": ("user_permissions", "groups"),
            },
        ),


        # Authentications
        (
            "Authentication",
            {
                "fields": (
                    "is_active",
                ),
            },
        ),

        # Admin Login
        (
            "Admin Login",
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                ),
            },
        ),
    )
@admin.register(Book)
class admin_book(admin.ModelAdmin):
    list_display=["title","Author","published_date"]

@admin.register(issued_book)
class admin_book(admin.ModelAdmin):
    list_display=["name","book","borrow_date","return_date"]
