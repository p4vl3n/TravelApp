from django.contrib import admin

# Register your models here.
from TravelApp.accounts.models import ApplicationUser, Profile, Relationship


@admin.register(ApplicationUser)
class ApplicationUserAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'country_of_residence',
                    'gender',
                    'date_of_birth',
                    )


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('sender',
                    'receiver',
                    'status',
                    'updated',
                    'created',
                    )

