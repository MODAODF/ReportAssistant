import zipfile, os
import xml.etree.cElementTree as ET

ProjectName = "ReportAssistant"

if __name__=="__main__":
    tree = ET.ElementTree(file=f"src\\description.xml")
    root = tree.getroot()
    versionAttr = root.findall(".//{http://openoffice.org/extensions/description/2006}version")[0].attrib
    version = versionAttr['value']
    extName = f"{ProjectName}-{version}.oxt"
    zf = zipfile.ZipFile(extName, mode='w', compression = zipfile.ZIP_DEFLATED)
    os.chdir("src")
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            zf.write(aFile)
    zf.close()