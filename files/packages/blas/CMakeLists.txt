# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/packages/blas
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB blas_sources ./*.f)

# Create library to link the feap executable against
add_library(blas ${blas_sources})
set_target_properties(blas PROPERTIES LINKER_LANGUAGE Fortran)