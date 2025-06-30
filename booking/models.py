# booking/models.py
from django.db import models


class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Yakka xonali'),
        ('double', 'Ikki xonali'),
        ('suite', 'Lyuks'),
        ('family', 'Oilaviy'),
    ]

    name = models.CharField(max_length=100, verbose_name="Xona nomi")
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, verbose_name="Xona turi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi (kunlik)")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='rooms/', verbose_name="Rasm")
    is_available = models.BooleanField(default=True, verbose_name="Mavjudmi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"

    def __str__(self):
        return f"{self.name} - {self.get_room_type_display()}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('confirmed', 'Tasdiqlangan'),
        ('cancelled', 'Bekor qilingan'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Xona")
    full_name = models.CharField(max_length=100, verbose_name="To'liq ismi")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    check_in = models.DateField(verbose_name="Kelish sanasi")
    check_out = models.DateField(verbose_name="Ketish sanasi")
    guests = models.IntegerField(verbose_name="Mehmonlar soni")
    special_requests = models.TextField(blank=True, verbose_name="Maxsus talablar")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Holati")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Umumiy narx")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.room.name} ({self.check_in})"