# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/packages/meshmod
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB meshmod_sources ./*.f)

# Create library to link the feap executable against
add_library(meshmod ${meshmod_sources})
set_target_properties(meshmod PROPERTIES LINKER_LANGUAGE Fortran)