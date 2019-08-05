
from buildkite import Organization
from buildkite import Organizations

def list_orgs():
    orgs = Organizations()
    for o in orgs.list():
        print(o)

def get_org():
    o = Organization()
    o.get('abc')
    print(o)

def main():
    list_orgs()
    get_org()


if __name__ == "__main__":
    main()
