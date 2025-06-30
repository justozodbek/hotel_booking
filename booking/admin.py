# booking/admin.py
from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'room_type', 'price', 'is_available', 'created_at']
    list_filter = ['room_type', 'is_available']
    search_fields = ['name', 'description']
    list_editable = ['is_available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'room', 'check_in', 'check_out', 'guests', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'check_in', 'room__room_type']
    search_fields = ['full_name', 'email', 'phone']
    list_editable = ['status']
    readonly_fields = ['total_price', 'created_at']