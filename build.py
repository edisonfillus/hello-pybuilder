from pybuilder.core import use_plugin, init, task, depends
from pybuilder.errors import BuildFailedException

#Core Plugins
use_plugin("python.core")
use_plugin("python.install_dependencies") #pyb install_dependencies

#QA Plugins
use_plugin("python.unittest")
use_plugin("python.coverage")

#Package Plugins
use_plugin("python.distutils") #Create a setup.py

name = "hello-pybuilder"
default_task = ["clean","install_dependencies","publish",'run_sonar_analysis']


# Coverage configuration:
#coverage_allow_non_imported_modules = "True"
#coverage_exceptions = [ 'file.py' ]


@init(environments='venv')
def set_properties(project):
    pass

@init
def initialize(project):
    project.build_depends_on('mockito')  #Dependencies just for Build (ex: Tests)
    #project.depends_on("awesome-library") #Dependencies for Build and Runtime
    project.build_depends_on_requirements("requirements-dev.txt") #Dependencies on File Just for Build
    project.depends_on_requirements("requirements.txt") #Dependencies on File For Build and Runtime

'''Overring run_sonar_analysis in order to lunch sonar-scanner instead of sonar-runner'''
@task("run_sonar_analysis", description="Launches sonar-scanner for analysis.")
@depends("analyze")
def run_sonar_analysis():
    import subprocess
    result = subprocess.run(['sonar-scanner', '-X'], shell=True) #sonar-scanner must have a link on /bin directory
    if result.returncode != 0:
        raise BuildFailedException("Sonar analysis failed.")