# CMake Configuratin file for FEAP84
#
# CMake will automatically generate Maekfiles for building FEAP.
# For details on how to use CMake with FEAP, see the README.md 
# file in this directory.
#
# Please only modify this file, if you know what you are doing!
#
# Version: 0.1.0 (04/2020)
# Author:  Lukas Lamm (lamm@ifam.rwth-aachen.de)
cmake_minimum_required(VERSION 3.10)
project(FEAP)
enable_language(Fortran)

#--------------------------------------------------------------------#
# Set default CMAKE variables for this project

# Set debug mode as standard
# Use option -DCMAKE_BUILD_TYPE=Release for performance optimization
if(NOT CMAKE_BUILD_TYPE OR CMAKE_BUILD_TYPE STREQUAL Debug)
    set(CMAKE_BUILD_TYPE Debug)
    set(CMAKE_Fortran_FLAGS_DEBUG "-Wall -Wextra -O0 -g")
    message("-- Build type: ${CMAKE_BUILD_TYPE}")
    message("-- Compiler flags: ${CMAKE_Fortran_FLAGS_DEBUG}")
elseif(CMAKE_BUILD_TYPE STREQUAL Release)
    set(CMAKE_Fortran_FLAGS_RELEASE "-O2")
    message("-- Build type: ${CMAKE_BUILD_TYPE}")
    message("-- Compiler flags: ${CMAKE_Fortran_FLAGS_RELEASE}")
endif()

# Set option for memory routines
if((NOT FEAP_MEMORY) OR (NOT FEAP_MEMORY STREQUAL large))
    set(FEAP_MEMORY standard)
endif()

# Set option for jpeg routines
if((NOT FEAP_JPEG) OR (NOT FEAP_JPEG STREQUAL jpeg))
    set(FEAP_JPEG none)
endif()

#--------------------------------------------------------------------#
# Set output directory for feap executable
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

#--------------------------------------------------------------------#
# Add main directory
add_subdirectory(main)