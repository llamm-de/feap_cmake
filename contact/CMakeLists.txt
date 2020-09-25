# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/contact
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB_RECURSE contact_sources ./*.f)

# Create library to link the feap executable against
add_library(contact ${contact_sources})
set_target_properties(contact PROPERTIES LINKER_LANGUAGE Fortran)