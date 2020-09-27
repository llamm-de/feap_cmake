# CMake Configuratin file for FEAP84 main subdirectory
# 
# Please only modify this file, if you know what you are doing!
#
# Version: 0.1.0 (04/2020)
# Author:  Lukas Lamm (lamm@ifam.rwth-aachen.de)
cmake_minimum_required(VERSION 3.10)
project(FEAP_main)

#--------------------------------------------------------------------#

# Set directory for Fortran modules
set(CMAKE_Fortran_MODULE_DIRECTORY ${CMAKE_BINARY_DIR}/modules)

# Include required packages (e.g. X11, LAPACK)
message("-- Searching for external libraries")

# X11
find_package(X11 REQUIRED)
include_directories(${X11_INCLUDE_DIR})
link_directories(${X11_LIBRARIES})

# LAPACK & BLAS
if(NOT FEAP_LIBS STREQUAL intern)
    message("-- FEAP: Using external LAPACK / BLAS libraries")
    find_package(LAPACK REQUIRED)
    link_directories(${LAPACK_LIBRARIES})
else()
    message("-- FEAP: Using internal LAPACK / BLAS libraries")
    add_subdirectory(../packages/blas ../packages/blas)
    add_subdirectory(../packages/lapack ../packages/lapack)
    set(LAPACK_LIBRARIES lapack blas)
endif()

#--------------------------------------------------------------------#

# Add the include directory of .h files
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    # 64bit includes
    message("-- FEAP: Selecting 64-bit include files (integer8)")
    include_directories(BEFORE ../include ../include/integer8)
else()
    # 32bit includes
    message("-- FEAP: Selecting 32-bit include files (integer4)")
    include_directories(BEFORE ../include ../include/integer4)
endif()

#--------------------------------------------------------------------#

# Add subdirectories to project
add_subdirectory(../contact ../contact)
add_subdirectory(../elements ../elements)
#add_subdirectory(../fe2)
#add_subdirectory(../parfeap)
add_subdirectory(../plot ../plot)
add_subdirectory(../program ../program)
add_subdirectory(../program/memory/ ../program/memory/)
add_subdirectory(../unix ../unix)
add_subdirectory(../user ../user)
add_subdirectory(../packages/arpack ../packages/arpack)
add_subdirectory(../packages/meshmod ../packages/meshmod)
add_subdirectory(../packages/paraview ../packages/paraview)

#--------------------------------------------------------------------#

# Add main executable for FEAP
set(feap_sources feap84.f)
add_executable(feap ${feap_sources})

# Link subdirectories as libraries
target_link_libraries(feap 
                      program 
                      memory 
                      plot 
                      unix 
                      elements 
                      user 
                      contact
                      arpack
                      meshmod
                      paraview
                      ${X11_LIBRARIES}
                      ${LAPACK_LIBRARIES}
                      )


