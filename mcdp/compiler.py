from antlr4 import *
import os

from .dpModules import Functions
from .dpTypes import dpString
from .dpgrammer.dpLexer import dpLexer
from .dpgrammer.dpParser import dpParser
def compileDpScript(fileName,output):
    try:
        os.makedirs(output)
    except FileExistsError:
        pass
    print(f"Compiling {fileName} into {output}")
    ins = FileStream(fileName)

    lexer = dpLexer(ins)
    tokens = CommonTokenStream(lexer)
    parser = dpParser(tokens)
    tree = parser.program()
    stat = tree.stat()
    while stat:
        if stat.dfunc():
            dfunc=stat.dfunc()
            with open(os.path.join(output,dfunc.ID(0).getText()+".mcfunction"),"w") as mcfunction:
                for commandWithRaw in dfunc.command_with_raw():
                    if commandWithRaw.command():
                        command=commandWithRaw.command()
                        print(f"Compiling {command.getText()}")
                        if command.call():
                            call=command.call()
                            func=Functions
                            for i in call.ID():
                                func=getattr(func,i.getText())
                            params=[]
                            for i in call.paramter():
                                if i.string():
                                    params.append(dpString.fromQuoted(i.string().getText()))
                            mcfunction.write(func(*params))
                    else:
                        print("Translating raw")
                        rawScripts=map(str.strip,commandWithRaw.RAW().getText()[10:-8].replace("\r\n","\n").replace("\r","\n").split("\n"))
                        for line in rawScripts:
                            mcfunction.write(line)
        stat=stat.stat()
    
    print(tree.toStringTree(recog=parser))
    return ""