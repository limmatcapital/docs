# coding: utf-8

"""
    QES Quant Service API

    QES Quant Service API provides easy access to Risk/Optimization API   # noqa: E501

    OpenAPI spec version: 0.0.4
    Contact: luo.qes@wolferesearch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="QES Quant Service API",
    author_email="luo.qes@wolferesearch.com",
    url="",
    keywords=["Swagger", "QES Quant Service API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    QES Quant Service API provides easy access to Risk/Optimization API   # noqa: E501
    """
)
