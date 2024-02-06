import json
from pkgutil import get_data
packFormat = json.loads(get_data(__package__, 'pack_format.json'))
def parseMetadata(ymlContent):
    out={"pack":{"pack_format":0,"description":""}}
    out["pack"]["pack_format"]=packFormat[ymlContent["targetVersion"]]
    out["pack"]["description"]=ymlContent["datapack"]["description"]
    of=open("output/pack.mcmeta","w")
    json.dump(out,of,separators=(',',':'))
    of.close()
