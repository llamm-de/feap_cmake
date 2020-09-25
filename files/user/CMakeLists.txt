# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/user
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory and subdirectories
file(GLOB_RECURSE user_sources_fixed ./*.f)
file(GLOB_RECURSE user_sources_free ./*.f90)

# Create library to link the feap executable against
add_library(user ${user_sources_fixed} ${user_sources_free})
set_target_properties(user PROPERTIES LINKER_LANGUAGE Fortran)
target_link_libraries(user tensorTools)
