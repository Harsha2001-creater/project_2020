from django.contrib import admin

from .models.studentinfo import Student

from .models.universityinfo import University

from .models.stdquery import Stdquery
from .models.stddetail import Stddetail
admin.site.register(Student)
admin.site.register(University)
admin.site.register(Stdquery)
admin.site.register(Stddetail)
