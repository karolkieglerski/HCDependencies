#!/usr/bin/python
import os
import platform
import urllib
import zipfile

class Requirement:
    osName = platform.system()
    platform = 'amd64'
    installDir = '/usr/local/bin/'

    def __init__(self, fileName):
        self.fileName = fileName

        print "\n Starting installing dependencies..."

    def openF(self):
        try:
            with open(self.fileName,'r') as f:
                content = f.readlines()
            return [x.strip() for x in content]
        except Exception as e:
            print "File requirements.txt doesn't exist!"
            exit(1)

    def getZip(self, program, version):
        file = program +'_'+ \
               version +'_'+ \
               self.osName.lower() +'_'+ \
               self.platform + '.zip'
        link = 'https://releases.hashicorp.com/' + \
               program +'/'+ \
               version +'/'+ \
               program +'_'+ \
               version +'_'+ \
               self.osName.lower() +'_'+ \
               self.platform + '.zip'

        try:
            urllib.urlretrieve (link, file)
            return file
        except Exception as e:
            print "Cannot get " + program + "_" + version
            exit(1)

    def install(self, file, name):
        try:
            zipF = zipfile.ZipFile(file,'r')
            zipF.extractall(self.installDir)
            os.chmod(self.installDir + name, 755)
            os.remove(file)

            return " Successfuly installed!"
        except Exception as e:
            print "Cannot install " + file
            exit(1)

init = Requirement('requirements.txt')
for c in init.openF():
    name, ver = c.split("=")

    print "\n Downloading " + name
    file = init.getZip(name.lower(), ver)

    print " Installing " + name
    print init.install(file, name)

print '\n All dependencies was installed! \n'
