import random
from django import template

register = template.Library()

@register.filter(name='praise')
def add_praise(value):
  note_of_praise = [
    "great!",
    "amazing!",
    "super!",
    "fantastic!",
    "unbelievable!",
    "excellent!"
    ]
  return value + " that's " + random.choice(note_of_praise)
