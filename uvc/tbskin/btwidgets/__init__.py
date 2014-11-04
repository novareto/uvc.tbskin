# this is a package.

import os.path
from grokcore.chameleon.components import ChameleonPageTemplateFile


TEMPLATES = os.path.join(os.path.dirname(__file__), 'templates')


def getTemplate(path):
    return ChameleonPageTemplateFile(os.path.join(TEMPLATES, path))
