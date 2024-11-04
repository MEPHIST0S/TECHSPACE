from modeltranslation.translator import translator, TranslationOptions
from .models import Department, Position, Employee

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)  # Translate the 'name' field

class PositionTranslationOptions(TranslationOptions):
    fields = ('name',)  # Corrected to translate the 'name' field

# Register the translation options
translator.register(Department, DepartmentTranslationOptions)
translator.register(Position, PositionTranslationOptions)