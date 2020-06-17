SET(CMAKE_HOST_SYSTEM_NAME Darwin)

set(DARWINX_COMPILER_PREFIX "darwinx" CACHE STRING
    "What compiler prefix to use for darwinx")

set(DARWINX_SYSROOT "/Library/Frameworks/GSharpKit" CACHE STRING
    "What sysroot to use for darwinx")

# Which compilers to use for C and C++
find_program(CMAKE_RC_COMPILER NAMES ${DARWINX_COMPILER_PREFIX}-windres)
find_program(CMAKE_C_COMPILER NAMES ${DARWINX_COMPILER_PREFIX}-gcc)
find_program(CMAKE_CXX_COMPILER NAMES ${DARWINX_COMPILER_PREFIX}-g++)

if(NOT CMAKE_LIBTOOL)
    find_program(CMAKE_LIBTOOL NAMES libtool)
  endif()
  if(CMAKE_LIBTOOL)
    set(CMAKE_LIBTOOL ${CMAKE_LIBTOOL} CACHE PATH "libtool executable")
    message(STATUS "Found libtool - ${CMAKE_LIBTOOL}")
    get_property(languages GLOBAL PROPERTY ENABLED_LANGUAGES)
    foreach(lang ${languages})
      set(CMAKE_${lang}_CREATE_STATIC_LIBRARY
        "${CMAKE_LIBTOOL} -static -o <TARGET> <LINK_FLAGS> <OBJECTS> ")
    endforeach()
endif()

SET(CMAKE_FIND_ROOT_PATH ${DARWINX_SYSROOT})

# Adjust the default behaviour of the FIND_XXX() commands:
# Search headers and libraries in the target environment; search
# programs in the host environment.
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

