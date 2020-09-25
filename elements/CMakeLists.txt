# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/elements
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB_RECURSE element_sources ./*.f)

# Create library to link the feap executable against
add_library(elements ${element_sources})
set_target_properties(elements PROPERTIES LINKER_LANGUAGE Fortran)