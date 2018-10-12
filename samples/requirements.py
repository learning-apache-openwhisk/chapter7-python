import pkg_resources

def main(args):
    requirements = ""    
    for d in pkg_resources.working_set:
        requirements += d.project_name
        requirements += "=="
        requirements += d.version
        requirements += "\n"
    return {
        "body": requirements
    }
