from django.contrib import admin

from .models.studentinfo import Student

from .models.universityinfo import University

from .models.stdquery import Stdquery
from .models.stddetail import Stddetail

from.models.univdetail import Univdetail

from.models.newcourse import Newcourse
from.models.saved import Saved
admin.site.register(Student)
admin.site.register(University)
admin.site.register(Stdquery)
admin.site.register(Stddetail)
admin.site.register(Univdetail)
admin.site.register(Newcourse)
admin.site.register(Saved)