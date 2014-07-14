# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import uvclight

from uvc.layout.interfaces import IAboveContent
from skin import ITBSkinLayer
#from dolmen.app.breadcrumbs import crumbs
from uvc.layout.viewlets import flashmessages


## class Breadcrumbs(crumbs.Breadcrumbs):
##     uvclight.layer(ITBSkinLayer)
##     uvclight.viewletmanager(uvc.layout.interfaces.IAboveContent)
##     uvclight.order(20)
##     uvclight.templatedir('templates')
    

class FlashMessages(flashmessages.FlashMessages):
    uvclight.layer(ITBSkinLayer)
    uvclight.viewletmanager(IAboveContent)
    uvclight.order(30)
    template = uvclight.get_template('flashmessages.cpt', __file__)
