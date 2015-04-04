from setuptools import setup, find_packages

if __name__ == '__main__':
    package_name = 'python_pin'
    setup(
        name=package_name,
        author='Samuel Marks',
        version='0.2.1',
        test_suite=package_name + '.tests',
        packages=find_packages(),
        package_dir={package_name: package_name}
    )

