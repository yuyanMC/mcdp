class dpString:
    value:str
    def __init__(self,value:str=""):
        self.value=value
    def fromQuoted(value:str):
        ds=dpString()
        ds.value=value[1:-1]
        return ds