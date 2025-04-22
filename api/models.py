from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #unique=True sets it so that no two users can share the email address
    email = models.EmailField(unique=True)

    #adds the created_at automatically.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    #if a user is deleted, all the items that the user has posted gets deleted
    #related_name = 'items' allows access the items that the user owns by user.items.all()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item')
    
    pickup_location = models.CharField(max_length=255)
    return_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    #we have a 2-tuple, first element of the tuple is what is stored in the database
    #the second element is what our application sees (not too sure about it because we are using Vue.js tho)

    STATUS_CHOICES = [
        ('In progress', 'In progress'),
        ('Overdue', 'Overdue'),
        ('Completed', 'Completed')
    ]
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bookings')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_bookings')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    booking_start = models.DateTimeField()
    booking_end = models.DateTimeField()

    #null=True, this allows date_returned to be null in the database.
    #blank=True, this allows the field to be left empty, so that we can add it later.
    date_returned = models.DateTimeField(null=True, blank=True)
