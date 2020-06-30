from django.contrib import admin

# Register your models here.
from .models import Print, Color, Printer, PrintType, Association, Resolution, Infill, Purpose, MailMessage, MailSubjectLine

admin.site.register(Print)
admin.site.register(Color)
admin.site.register(Printer)
admin.site.register(PrintType)
admin.site.register(Association)
admin.site.register(Resolution)
admin.site.register(Infill)
admin.site.register(Purpose)
admin.site.register(MailSubjectLine)
admin.site.register(MailMessage)
