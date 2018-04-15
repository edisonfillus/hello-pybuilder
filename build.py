from pybuilder.core import use_plugin, init

#Core Plugins
use_plugin("python.core") 
use_plugin("python.install_dependencies") #pyb install_dependencies

#Test Plugins
use_plugin("python.unittest")
use_plugin("python.coverage")

#Package Plugins
use_plugin("python.distutils") #Create a setup.py

name = "tutorial-env"
default_task = "publish"


@init
def set_properties(project):
    pass

@init
def initialize(project):
    project.build_depends_on('mockito')  #Dependencies just for Build (ex: Tests)
    #project.depends_on("awesome-library") #Dependencies for Build and Runtime
    project.build_depends_on_requirements("requirements-dev.txt") #Dependencies on File Just for Build
    project.depends_on_requirements("requirements.txt") #Dependencies on File For Build and Runtime