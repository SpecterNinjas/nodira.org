from django.shortcuts import render


def main(request):
    return render(request, 'main/index.html')


def python(request):
    return render(request, 'main/tutorial/python/python_default.html')


def python_installing(request):
    return render(request, 'main/tutorial/python/python_installing.html')


def data_types(request):
    return render(request, 'main/tutorial/python/data_types.html')


def indentation(request):
    return render(request, 'main/tutorial/python/indentation_and_comment.html')


def date_time(request):
    return render(request, 'main/tutorial/python/data_and_time.html')


def python_list(request):
    return render(request, 'main/tutorial/python/python_list.html')


def python_set(request):
    return render(request, 'main/tutorial/python/python_set.html')


def python_tuple(request):
    return render(request, 'main/tutorial/python/python_tuple.html')


def python_dict(request):
    return render(request, 'main/tutorial/python/python_dict.html')


def python_operators(request):
    return render(request, 'main/tutorial/python/python_operators.html')


def python_global_local_variables(request):
    return render(request, 'main/tutorial/python/python_global_local_variables.html')


def python_conditions(request):
    return render(request, 'main/tutorial/python/python_conditions.html')


def python_loop(request):
    return render(request, 'main/tutorial/python/python_loop.html')


def python_array(request):
    return render(request, 'main/tutorial/python/python_array.html')


def python_heapq_enum(request):
    return render(request, 'main/tutorial/python/python_heapq&enum.html')


def python_input_output(request):
    return render(request, 'main/tutorial/python/python_input&output.html')


def python_files_folders(request):
    return render(request, 'main/tutorial/python/python_files&folders.html')


def python_os_path(request):
    return render(request, 'main/tutorial/python/python_os&python_path.html')


def python_function(request):
    return render(request, 'main/tutorial/python/python_function.html')


def python_lambda(request):
    return render(request, 'main/tutorial/python/python_lambda.html')


def python_recursion(request):
    return render(request, 'main/tutorial/python/python_recursion.html')


def python_search_filter(request):
    return render(request, 'main/tutorial/python/python_search_filter.html')


def python_map_reduce(request):
    return render(request, 'main/tutorial/python/python_map_reduce.html')


def python_sort_min_max(request):
    return render(request, 'main/tutorial/python/python_sort_min_max.html')


def python_module_package(request):
    return render(request, 'main/tutorial/python/python_module_package.html')


def python_print_function(request):
    return render(request, 'main/tutorial/python/python_print_function.html')


def python_copy_function(request):
    return render(request, 'main/tutorial/python/copying_data.html')


def python_name_variable(request):
    return render(request, 'main/tutorial/python/python_name_variable.html')


def python_pip(request):
    return render(request, 'main/tutorial/python/python_pip.html')


def python_urllib(request):
    return render(request, 'main/tutorial/python/python_urllib.html')


def python_console(request):
    return render(request, 'main/tutorial/python/python_console.html')


def python_tempfile(request):
    return render(request, 'main/tutorial/python/python_tempfile.html')


def python_descriptor(request):
    return render(request, 'main/tutorial/python/python_descriptor.html')


def python_decorator(request):
    return render(request, 'main/tutorial/python/python_decorator.html')


def python_class(request):
    return render(request, 'main/tutorial/python/python_class.html')


def python_regex(request):
    return render(request, 'main/tutorial/python/python_regex.html')


def python_args_kwargs(request):
    return render(request, 'main/tutorial/python/python_args_kwargs.html')


def python_mixins(request):
    return render(request, 'main/tutorial/python/python_mixins.html')


def python_attribute_access(request):
    return render(request, 'main/tutorial/python/python_attribute_access.html')


def python_exceptions(request):
    return render(request, 'main/tutorial/python/python_exceptions.html')


def python_hashlib(request):
    return render(request, 'main/tutorial/python/python_hashlib.html')


def python_design_patterns(request):
    return render(request, 'main/tutorial/python/python_design_patterns.html')


def python_speed(request):
    return render(request, 'main/tutorial/python/python_speed.html')


def python_zip_unzip_files(request):
    return render(request, 'main/tutorial/python/python_zip_unzip_files.html')


def python_http_server(request):
    return render(request, 'main/tutorial/python/python_http_server.html')


def python_generators(request):
    return render(request, 'main/tutorial/python/python_generators.html')


def python_string_manipulation(request):
    return render(request, 'main/tutorial/python/python_string_manipulation.html')


def python_debugging(request):
    return render(request, 'main/tutorial/python/python_debugging.html')


def python_overriding(request):
    return render(request, 'main/tutorial/python/python_overriding.html')


def python_polymorphism(request):
    return render(request, 'main/tutorial/python/python_polymorphism.html')


def python_overloading(request):
    return render(request, 'main/tutorial/python/python_overloading.html')


def python_inheritance(request):
    return render(request, 'main/tutorial/python/python_inheritance.html')


def python_hints(request):
    return render(request, 'main/tutorial/python/python_hints.html')


def python_multiprocessing(request):
    return render(request, 'main/tutorial/python/python_multiprocessing.html')


def python_multithreading(request):
    return render(request, 'main/tutorial/python/python_multithreading.html')


def python_networking(request):
    return render(request, 'main/tutorial/python/python_networking.html')


def python_virtual_environments(request):
    return render(request, 'main/tutorial/python/python_virtual_environments.html')


def python_unit_testing(request):
    return render(request, 'main/tutorial/python/python_unit_testing.html')


def python_final(request):
    return render(request, 'main/tutorial/python/python_final.html')


# --------------------------------------------------------------------------
def article(request):
    return render(request, 'main/article.html')


def algorithm(request):
    return render(request, 'main/algorithm.html')


def quiz(request):
    return render(request, 'main/quiz.html')


def project(request):
    return render(request, 'main/project.html')
