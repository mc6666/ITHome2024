from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    # 定義 Rich Text Field, not mandatory
    body = RichTextField(blank=True)
    
    # 加入 body
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    
    