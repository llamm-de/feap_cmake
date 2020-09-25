# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/packages/arpack
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB_RECURSE arpack_sources ./*.f)

# Create library to link the feap executable against
add_library(arpack ${arpack_sources})
set_target_properties(arpack PROPERTIES LINKER_LANGUAGE Fortran)