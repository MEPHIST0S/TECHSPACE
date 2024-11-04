from django.db import models
from django.utils.translation import gettext_lazy as _
from googletrans import Translator  # GOOGLE TRANSLATOR

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Department Name"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        
        if self.name and not self.name_az:
            try:
                translation_az = translator.translate(self.name, dest='az')
                self.name_az = translation_az.text if translation_az and translation_az.text else self.name
            except Exception as e:
                print(f"ERROR DURING AZ-LANG TRANSLATION: {e}")
                self.name_az = self.name

        if self.name and not self.name_en:
            self.name_en = self.name

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Position Name"))
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        translator = Translator()

        # Translate name to Azerbaijani if not set
        if self.name and not self.name_az:
            try:
                translation_az = translator.translate(self.name, dest='az')
                self.name_az = translation_az.text if translation_az and translation_az.text else self.name
            except Exception as e:
                print(f"ERROR DURING AZ-LANG TRANSLATION: {e}")
                self.name_az = self.name

        # Set English name
        if self.name and not self.name_en:
            self.name_en = self.name

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employees")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name="employees")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"