# CMake configuration for FEAP
This is a basics CMake configuration for the propriatery finite element sofware FEAP (&copy; University of California Berkley). Supported versions of FEAP are:
- Version 84

This configuration is still under development and does only support unix like oparting systems as well as the gfortran compiler. Furthermore, the *fe2* and *parfeap* modules are not supported yet. If you have any suggestions or improvements for this configuration, please take a look in the *Participate* section of this file.

## Getting started
### Prerequisites
Before installing the CMake support for FEAP, please make shure that you have the FEAP sourcecode available an your system. Information on how to purchase this software can be found at the [FEAP website](http://projects.ce.berkeley.edu/feap/) of the University of California Berkeley.

Next, make sure you have a recent installation of [Python](https://www.python.org) installed on your system. This is required for the installation process, if you do not want to copy the CMake configuration files by hand. To install the dependencies of the Python script, you can either use *pipenv* or install the dependencies globally by using ```pip3 install -r requirements.txt```.

Now, you can clone the repository by using 
```
git clone https://github.com/llamm-de/feap_cmake.git
```
from your command line.

### Installation
The installation process is straight forward, if you use the provided Python script. For this, go to the directory cloned this project into and execute
```
python3 install.py
```
The installation wizzard will guide you through the installation process.

If you do not want to use the Python installation wizzard, you can also copy the *CMakeLists.txt* from the ```files``` directory directly into your FEAP project folder. The folder names should match those names of your FEAP sources.

## Building FEAP
After sucessfully installation of the CMake configuration files, you should be able to build a working executable of feap by going to your FEAP source folder and executing
```
mkdir build
cd build
cmake ..
make
```
This should automatically set up all needed Makefiles and compile the source 
code. You will find the executable in the ```/build``` directory.

### Building options
CMake has been configured with some default options for the building process. If you want to change any of these options, you can use
```
cmake -D<OptName>=<OptValue> ..
```
to pass any option to cmake while creating your makefiles. You can also pass in multiple option commands. Please keep in mind, that you should only use one of these options, if you really need them. Otherwise, you should stick to the default settings.

#### Build type
The **default** build type is ```CMAKE_BUILD_TYPE=Debug```, which means that Feap will be build without any kind of compiler optimization and additional information for the debugger to work. If you want to switch off ```Debug```-mode, use
```
cmake -DCMAKE_BUILD_TYPE=release ..
```
when calling CMake. This will automatically switch on the ```-O2``` optimization of the compiler.

#### FEAP Include files
By default, CMake detects automatically which kin dof system you are running and selects either 32-bit or 64-bit include files. As of now, there is no option to change this behaviour.

#### FEAP Memory
FEAP lets you choose between standard memory routines and large memory routines. The **default** value for this is set to ```FEAP_MEMORY=standard```, which uses the **standard** memory routines. If you want to switch to large memory, use
```
cmake -DFEAP_MEMORY=large ..
```
when calling CMake.

#### FEAP Jpeg packages
By **default**, the Jpeg routines are disabled in the FEAP build by the value ```FEAP_JPEG=none```. To include the routines, use
```
cmake -DFEAP_JPEG=jpeg ..
```
when calling CMake.

#### LAPACK & BLAS support
LAPACK and BLAS can be either supported by external libraries that you ihave installed on your system, or from the FEAP internal packages. By **default**, CMake automatically detects and uses the external libraries installed on your system. If you instead would like to compile the internal FEAP packages for LAPACK and BLAS, use
```
cmake -DFEAP_LIBS=intern ..
```
when calling CMake.

## Creating user defined routines
When creating user defined routines (e.g. UELMT or UMAT) the workflow is as 
follows. Choose a free dummy routine (e.g. elmt02.f) within the ```/user``` 
directory. Create a new subdirectory within ```/user``` and move the dummy file 
into this subdirectory, e.g.
```
mkdir my_Element
mv elmt02.f ./my_Element/
```
Now you can start changing the dummy file to fit your needs. You 
can place all other newly written source files, which are asscociated with your
routine, also in the newly created subdirectory. Every time you move a file or
add a new file, you have to run cmake before compiling. This will track all new 
and/or moved files in your source tree. For this, go to the ```/build``` directory and
run
```
cmake ..
```
If you did only change existing files you can skip cmake and directly build the
new application using
```
make
```
in the ```/build``` directory.

## Executing FEAP
You can start feap directly from the ```/build``` directory in your source folder. To make feap available from everywhere on your system, I would recommend the following workflow.\
First set a symbolic link to FEAP in your ```~/bin``` directory. This can be done by executing
```
ln -s ~/bin/feap /path/to/feap/build/dir
```
where ```/path/to/feap/build/dir``` must be replaced by the absolute path of the FEAP building directory.\
If you haven't already done it, add the ```~/bin``` directory to your path. For this open the ```~/.bashrc``` and append the following lines
```
export PATH=$PATH:~/bin
```
Now you should be able to call FEAP from anywhere on your system.

## Contribution & Bug reports
If you want to contribute to this project or just report bugs, please feel free to leave a github issue or open a pull request. You can also contact me directly via mail.

## License
This project is licensed under the MIT licens. Please see the [License.md](License.md) file for further information.