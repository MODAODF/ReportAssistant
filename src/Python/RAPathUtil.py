import uno
import unohelper
from com.sun.star.task import XJob
import os,sys
import ReportAssistantConf as TRepoUtility
ProjectName="ReportAssistant"

class getExtensionPath(unohelper.Base, XJob):
    def __init__(self, ctx):
        self.ctx = ctx

    def execute(self, args):
        global ProjectName
        outPath = ""
        for path in sys.path:
            if ProjectName in path and ".oxt" in path:
                outPath = path
                break
        pathToken = outPath.split('\\')
        outPath = ""
        for token in pathToken:
            outPath += token
            outPath += "/"
            if ProjectName in token:
                break
        return outPath


g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(getExtensionPath,
    "ReportAssistant.getExtensionPath",
    ("ReportAssistant.getExtensionPath",),)
