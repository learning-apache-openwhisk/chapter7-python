import pkg_resources
import sys

def main(args):
    print(sys.version)
    res = {}
    for d in pkg_resources.working_set:
        res[d.project_name] = d.version
        print("|%s\t|%s" % (d.project_name, d.version))
    return res
