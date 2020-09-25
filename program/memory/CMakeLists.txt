# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/program/memory
# 
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB memory_sources ./*.f)

# Create library to link the feap executable against
add_library(memory ${memory_sources})
set_target_properties(program PROPERTIES LINKER_LANGUAGE Fortran)