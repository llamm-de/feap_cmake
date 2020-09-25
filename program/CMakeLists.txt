# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/program
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB program_sources ./*.f)

# Create library to link the feap executable against
add_library(program ${program_sources})
set_target_properties(program PROPERTIES LINKER_LANGUAGE Fortran)
target_link_libraries(program unix user)
