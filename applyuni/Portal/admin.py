from django.contrib import admin

from .models.studentinfo import Student

from .models.universityinfo import University
# Register your models here.


admin.site.register(Student)
admin.site.register(University)
