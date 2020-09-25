# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/packages/paraview
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB paraview_sources ./*.f)

# Create library to link the feap executable against
add_library(paraview ${paraview_sources})
set_target_properties(paraview PROPERTIES LINKER_LANGUAGE Fortran)