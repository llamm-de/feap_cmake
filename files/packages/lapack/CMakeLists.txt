# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/packages/lapack
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB lapack_sources ./*.f)

# Create library to link the feap executable against
add_library(lapack ${lapack_sources})
set_target_properties(lapack PROPERTIES LINKER_LANGUAGE Fortran)