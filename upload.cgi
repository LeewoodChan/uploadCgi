#!/usr/bin/python3.4
import cgitb; cgitb.enable()
import sys, os, string, cgi
import binascii
import argparse
import json


form = cgi.FieldStorage()

path = ""

sys.stderr = sys.stdout

print("Content-Type: text/html")
print()

class rFile(object):
    def __init__(self, name):
        self.fileName = name
        self.contentFile = ""

def mkDir():
    if not os.path.exists("files"):
        os.makedirs("files")
        os.chmod("files", 0o755)

    global path
    newDir = binascii.hexlify(os.urandom(16)).decode()
    path = "files/" + newDir
    if not os.path.exists(path):
        os.makedirs(path)
        os.chmod(path, 0o755)

def mkJson(dictJson):
    newJson = path +  "/jsonFile.json"
    open(newJson, 'w').write(json.dumps(dictJson))
    os.chmod(newJson, 0o755)

def mkPage():
    printPage = ("""<!DOCTYPE html>
<html>
<head>
    <title>Result Upload File</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
    <script type="text/javascript" src="../openJson.js"></script>
</head>
<body>
    <ol id="myJson" rel="%s">Thank you for using this upload. Unforunately, the back end is not finish yet...</ol>
</body>
</html>"""%("jsonFile.json"))
    newPage = path + "/result.html" 
    open(newPage, 'w').write(printPage)
    os.chmod(newPage, 0o755)

def getFile(checkFile):
    listing = os.listdir(path)
    file_dic = {}
    
    for infile in listing:
        with open(os.path.join(path, infile),'r') as readFile:
            name = os.path.splitext(infile)[0]
            file_dic[name] = str(readFile.read())

    print(file_dic)

    data = {"name":"Jack","age":31}
    #os.system("touch new.json")
#    os.chmod(new.json, 0o777)
#    with open("new.json","w") as fJson:
    #with open("jsonFile.json","w") as fJson:
    #    json.dump(file_dic, fJson)

    # call mkJson to make json file
    mkJson(file_dic)
    mkPage()

def main():
    message = ""

    mkDir()

    useArgv = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--check", metavar="", help="check the file")
    parser.add_argument("files", nargs="*", help="list of files")
    args = parser.parse_args()

    if 'GATEWAY_INTERFACE' in os.environ:
        fileItems = form['filename[]']
        for fileItem in fileItems:
            if fileItem.file:
                fn = os.path.basename(fileItem.filename.replace("\\","/"))
                try:
                    open(path + '/' + fn, 'wb').write(fileItem.file.read())
                except:
                    print("""Content-Type: text/html\n\n
                          <html>
                          <body>
                              <p>%s</p>
                          </body>
                          </html>
                          """ %(path+'/'+fn))
                    sys.exit()
    else:
        if not args.files:
            print("usage: upload.cgi [-h][--help]")
            print("usage: upload.cgi [list of the files]")
            print("usage: upload.cgi [-c]/[--check] [checked file] [list of the file]")
            sys.exit(0)
        useArgv = True
        fileItems = args.files
        for fileItem in fileItems:
            op = open(fileItem,'r').read()
            fn = os.path.basename(fileItem)
            try:
                open(path + '/' + fn, 'w').write(op)
            except:
                sys.exit()

    
    checkFile = args.check
    getFile(checkFile)


    printResult = path + "/result.html"
#    printResult = "result.html"
    redirectStr = ("""Content-Type: text/html\n\n
<html>
    <head>
        <meta http-equiv="refresh" content="0; url=%s"/>
    </head>
    <body>
        <p>Redirecting to <a href="%s">result.html</a></p>
    </body>
</html>
"""%(printResult, printResult))
    if(not useArgv):
        print(redirectStr)
    else:
        print("completed")

if __name__ == "__main__":
    main()
    sys.exit(0)
