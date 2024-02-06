import sys
from antlr4 import *

from .compiler import compileDpScript
import yaml
from . import packMeta
import os
def fullRemoveDir(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def parseArgs(argv):
    args={"source":""}
    for i in range(1,len(argv)):
        args["source"]=argv[i]
    if args["source"]=="":
        print("Error: No source was given.",file=sys.stderr)
        sys.exit(1)
    return args
def main(argv):
    args=parseArgs(argv)
    projectPath=args["source"]
    fullRemoveDir("output")
    try:
        os.makedirs("output")
    except FileExistsError:
        pass
    packMeta.parseMetadata(yaml.load(open(os.path.join(projectPath,"metadata.yml")),yaml.FullLoader))
    compileScripts(projectPath)

def compileScripts(projectPath):
    scriptPath=os.path.join(projectPath,"script/")
    if os.path.exists(scriptPath):
        treeCompile(scriptPath,"")
def treeCompile(scriptPath,dirPath):
    for name in os.listdir(os.path.join(scriptPath,dirPath)):
        childPath=dirPath+name
        if os.path.isdir(os.path.join(scriptPath,childPath)):
            treeCompile(scriptPath,childPath+"/")
        else:
            outputPath=os.path.join("output",".".join(childPath.split(".")[:-1]),"")
            compileDpScript(os.path.join(scriptPath,childPath),outputPath)

if __name__ == '__main__':
    main(sys.argv)