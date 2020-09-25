# CMake Configuratin file for FEAP84 for subdirectory
# 
# Directory: (feap84)/unix
#
# Please only modify this file, if you know what you are doing!

# Find all source files in directory
file(GLOB unix_sources ./*.f ./*.c)

# Set memory option according to variable
if(FEAP_MEMORY STREQUAL standard)
    message("-- FEAP: Using STANDARD MEMORY routines")
    file(GLOB mem_sources ./memory/*.c)
elseif(FEAP_MEMORY STREQUAL large)
    message("-- FEAP: Using LARGE MEMORY routines")
    file(GLOB mem_sources ./largemem/*.c)
endif()

# Set JPEG options according to variable
if(FEAP_JPEG STREQUAL none)
    message("-- FEAP: Using NOJPEG routines")
    file(GLOB jpg_sources ./nojpeg/*.c)
elseif(FEAP_JPEG STREQUAL jpeg)
    message("-- FEAP: Using JPEG routines")
    find_package(JPEG REQUIRED)
    file(GLOB jpg_sources ./jpeg/*.c)
endif()

# Create library to link the feap executable against
add_library(unix ${unix_sources} ${mem_sources} ${jpg_sources})
set_target_properties(unix PROPERTIES LINKER_LANGUAGE Fortran)
target_link_libraries(unix program plot memory ${JPEG_LIBRARY})
