import grok
from grokcore.traverser import Traverser
from zope.component.hooks import setSite, getSite
from zope.publisher.skinnable import setDefaultSkin
import zope.security.management


@grok.subscribe(grok.IApplication, grok.IBeforeTraverseEvent)
def setSkin(app, event=None):
    if getSite() != app:
        setSite(app)
    request = zope.security.management.getInteraction().participations[0]
    setDefaultSkin(request)


class appTraverser(Traverser):
    grok.context(grok.IApplication)

    def traverse(self, name):
        setSkin(self.context)
        return self.context.get(name)

