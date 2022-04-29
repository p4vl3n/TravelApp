from django.contrib import admin

# Register your models here.
from TravelApp.travel.models import Trip, TripDay


class TripDaysInline(admin.TabularInline):
    model = TripDay


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('destination',
                    'duration',
                    'departure_date',
                    'departure_time',
                    )
    inlines = [TripDaysInline,]


@admin.register(TripDay)
class TripDayAdmin(admin.ModelAdmin):
    list_display = ('description',
                    )



