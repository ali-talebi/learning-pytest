import pytest  
import time 

# pytestmark = [pytest.mark.slow("data")]

# @pytest.fixture(scope="function")
# def cli_interface(request):
#     marker = request.node.get_closest_marker("slow")
#     if marker : 
#         args_find = marker.args[0]
#         print("Marker Data "  , args_find ) 
#         return args_find
#     else : 
#         return "DEFAULT"


# def tfu_load_login(request , cli_interface) : 
#     time.sleep(1)
#     print(f"IN TEST : {request.node.name} is " , cli_interface )
# def tfu_DDD(request , cli_interface):
#     print(f"IN TEST : {request.node.name} is " , cli_interface )




# @pytest.fixture
# def my_interface(request):
#     marker   = request.node.get_closest_marker("fast") 
#     if marker : 
#         arg_find = marker.args[0]
#         return arg_find
#     return "Default"

# @pytest.mark.slow("function_one")
# def tfu_one(my_interface) : 
#     print("ARGS OF THIS TEST MARK : " , my_interface )

# @pytest.mark.fast("function_two")
# def tfu_one(my_interface) : 
#     print("ARGS OF THIS TEST MARK : " , my_interface )

# # @pytest.mark.slow("function_three")
# # def tfu_one(my_interface) : 
# #     print("ARGS OF THIS TEST MARK : " , my_interface )



import pytest

# Apply the marker globally to all tests in the module
pytestmark = [pytest.mark.env_name("TML_env")]

@pytest.fixture
def check_marker(request):
    marker = request.node.get_closest_marker("env_name")
    if marker:
        return marker.args[0]
    return "Default"

def tfu_with_marker(check_marker):
    assert check_marker == "TML_env"  # Uses the global marker

@pytest.mark.env_name("Custom_env")
def tfu_with_custom_marker(check_marker):
    assert check_marker == "Custom_env"  # Overrides the global marker

def tfu_without_marker(check_marker):
    assert check_marker == "TML_env"  # Default if no marker is applied
