from solutions.lesson4_frog_river_one import solution

def test_for_x_5_time_found():
    solution([1,3,1,4,2,3,5,4],5)
def test_for_x_5_time_not_found():
    solution([1,3,1,4,2,3,6,4],5)