import grok
from zope.interface import Interface
from uvc.layout.slots.managers import Headers


class FontAwesome(grok.Viewlet):
    grok.viewletmanager(Headers)
    grok.context(Interface)
    grok.name('font-awesome')

    def available(self):
        return getattr(self.view, 'needs_fontawesome', False)

    def render(self):
        return '''<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.2/css/all.css" integrity="sha384-/rXc/GQVaYpyDdyxK+ecHPVYJSN9bmVFBvjA/9eOB+pb3F2w2N6fc5qB9Ew5yIns" crossorigin="anonymous"/>'''
