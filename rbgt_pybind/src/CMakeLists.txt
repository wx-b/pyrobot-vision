cmake_minimum_required(VERSION 3.10)

# Define libraries
set(LIBRARIES Eigen3::Eigen OpenGL::GL GLEW::GLEW glfw ${OpenCV_LIBRARIES} pthread stdc++fs)

# Define target
# add_executable(evaluate_rbot_dataset evaluate_rbot_dataset.cpp evaluator.cpp 
#     common.cpp body.cpp renderer_geometry.cpp renderer.cpp
#     normal_image_renderer.cpp occlusion_mask_renderer.cpp model.cpp camera.cpp
#     image_loader_camera.cpp dataset_rbot_camera.cpp viewer.cpp image_viewer.cpp
#     normal_image_viewer.cpp region_modality.cpp tracker.cpp)
# target_link_libraries(evaluate_rbot_dataset PUBLIC ${LIBRARIES})

add_executable(evaluate_ablation_study evaluate_ablation_study.cpp evaluator.cpp
    common.cpp body.cpp renderer_geometry.cpp renderer.cpp
    normal_image_renderer.cpp occlusion_mask_renderer.cpp model.cpp camera.cpp
    image_loader_camera.cpp dataset_rbot_camera.cpp viewer.cpp image_viewer.cpp
    normal_image_viewer.cpp region_modality.cpp tracker.cpp)
target_link_libraries(evaluate_ablation_study PUBLIC ${LIBRARIES})

add_executable(run_on_recorded_sequence run_on_recorded_sequence.cpp
    common.cpp body.cpp renderer_geometry.cpp renderer.cpp
    normal_image_renderer.cpp occlusion_mask_renderer.cpp model.cpp camera.cpp
    image_loader_camera.cpp dataset_rbot_camera.cpp viewer.cpp image_viewer.cpp
    normal_image_viewer.cpp region_modality.cpp tracker.cpp)
target_link_libraries(run_on_recorded_sequence PUBLIC ${LIBRARIES})
