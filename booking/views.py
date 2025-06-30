# booking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Room, Booking
from .forms import BookingForm


def home(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/home.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'booking/room_detail.html', {'room': room})


def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room

            # Umumiy narxni hisoblash
            days = (booking.check_out - booking.check_in).days
            booking.total_price = room.price * days

            booking.save()
            messages.success(request, 'Sizning buyurtmangiz muvaffaqiyatli yuborildi!')
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'booking/book_room.html', {'room': room, 'form': form})


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking/booking_success.html', {'booking': booking})