def main(args):
    name = args.get("name", "stranger")
    greeting = "Welcome " + name 
    return {"main": greeting}

def hello(args):
    return {
        "hello": "Hello %s" % 
           args.get("name", "world")
    }
 
def hi(args):
    import hi
    return {"hi": 
        hi.hi(args.get("name"))}