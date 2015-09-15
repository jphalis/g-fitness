from django.dispatch import Signal


membership_lesson_update = Signal(providing_args=['new_lesson_count'])
membership_lesson_completed = Signal(providing_args=['new_lesson_count'])
membership_lesson_canceled = Signal(providing_args=['new_lesson_count'])
