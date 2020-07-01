from django.contrib import admin
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


admin.site.site_header = 'TechLab 3D-Printing Admin'
admin.site.site_title = 'TechLab 3D-Printing Admin'
admin.site.index_title = 'TechLab Administration'