def main(args):
    name = args.get("name", "world")
    greeting = "Hello " + name + "!"
    print(greeting)
    return {"hello": greeting}