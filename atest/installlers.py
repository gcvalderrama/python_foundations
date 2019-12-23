import unittest


class PackageEntity:

    def __init__(self):
        self.name = None
        self.version = "1.0.0.0"
        self.dependencies = list()
        self.installed = False


def install(package):
    if not package:
        return

    if package.installed:
        return

    for item in package.dependencies:
        install(item)

    package.installed = True
    print(package.name)


class Test(unittest.TestCase):

    def test_case(self):

        #  a->B,C
        #  B->D
        #  C->D

        d_package = PackageEntity()
        d_package.name = "D"
        d_package.version = "1.0.0.0"

        c_package = PackageEntity()
        c_package.name = "C"
        c_package.version = "1.0.0.0"
        c_package.dependencies = [d_package]

        b_package = PackageEntity()
        b_package.name = "B"
        b_package.version = "1.0.0.0"
        b_package.dependencies = [d_package]

        package = PackageEntity()
        package.name = "A"
        package.version = "1.0.0.0"
        package.dependencies = [b_package, c_package]

        install(package)
