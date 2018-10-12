import os 
def main(args):
    m =  os.environ
    return { x:m[x] 
             for x in m.keys() 
             if x.startswith("__OW_") }
