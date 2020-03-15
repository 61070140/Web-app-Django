from django.db import models

# Create your models here.
"""------------------------------------- Faculty Table ----------------------------------"""
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

"""------------------------------------- Restaurant Table -------------------------------"""

class Restaurant(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.IntegerField()
    approve_by = models.CharField(max_length=50)
    approve_date = models.DateField()
    def __str__(self):
        return self.name

"""------------------------------------- Food Table ----------------------------------"""

class Food(models.Model):
    name = models.CharField(max_length=50)
    is_vegan = models.BooleanField()
    def __str__(self):
        return self.name

"""------------------------------- Restaurant Food Table -----------------------------"""
class RestaurantFood(models.Model):  
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.FloatField()

"""------------------------------------- Rating Table ---------------------------------"""
class RestaurantRating(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return '(%s)' %(self.restaurant_id)
        