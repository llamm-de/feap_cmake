# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/plot
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB plot_sources ./*.f)

# Create library to link the feap executable against
add_library(plot ${plot_sources})
set_target_properties(plot PROPERTIES LINKER_LANGUAGE Fortran)