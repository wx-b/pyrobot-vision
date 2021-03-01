cmake_minimum_required(VERSION 3.10)

# Region Based Gaussian Tracker
# =============================================================================
project(RBGT_PY)

# Libraries
# =============================================================================
find_package(Eigen3 3.3.2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)
find_package(glfw3 3.1.2 REQUIRED)
find_package(OpenCV 3.0.0 REQUIRED)

find_package(OpenMP)
if(OPENMP_FOUND)
	set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
	set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()


# Compiler Settings
# =============================================================================

# Default settings
set(CMAKE_CXX_STANDARD 17)

# Directories
# =============================================================================

# Include Directories
include_directories("${CMAKE_SOURCE_DIR}/third_party")

# Sub Directories
# add_subdirectory(src)

file (GLOB SOURCE_FILES 
					src/common.cpp src/body.cpp src/renderer_geometry.cpp src/renderer.cpp
					src/normal_image_renderer.cpp src/occlusion_mask_renderer.cpp src/model.cpp src/camera.cpp
					src/viewer.cpp src/image_viewer.cpp
					src/normal_image_viewer.cpp src/region_modality.cpp ndarray_converter.cpp)
file (GLOB HEADER_FILES "src/*.h" ndarray_converter.h)
file (GLOB PYTHON_FILES "rbgt_pybind.cpp")

set(LIBRARIES Eigen3::Eigen OpenGL::GL GLEW::GLEW glfw ${OpenCV_LIBRARIES} pthread stdc++fs)

add_subdirectory(pybind11)
pybind11_add_module(rbgt_pybind ${SOURCE_FILES}
								${HEADER_FILES}
								${PYTHON_FILES})
target_link_libraries(rbgt_pybind PUBLIC ${LIBRARIES})
