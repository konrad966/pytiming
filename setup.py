from setuptools import setup, find_packages

package_name = "pytiming"
package_dir = "src/pytiming"
packages = ['pytiming']
required = ['numpy']

setup(
    name=package_name,
    author='Konrad Lis',
    author_email='konrad.lis11@gmail.com',
    url='https://github.com/konrad966/pytiming',
    version="0.0.3",
    install_requires=required,
    package_dir={package_name: package_dir},
    packages=packages
)
