import logging
from hypothesis import given, strategies as st
from perfect_crime import solution3, solution

info_strategy = st.lists(
    st.lists(st.integers(min_value=1, max_value=3), min_size=2, max_size=2),
    min_size=1,
    max_size=20
)
catch_strategy = st.integers(min_value=1, max_value=120)


@given(info=info_strategy, catch_a=catch_strategy, catch_b=catch_strategy)
def test_zero(info, catch_a, catch_b):
	# print(info, catch_a, catch_b)
	# answer = solution3(info, catch_a, catch_b)
	assert solution(info,catch_a,catch_b) == solution3(info, catch_a, catch_b)
	# print(catch_a, catch_b)
	# print("answer is ",answer[0])
	# print(answer[1])
	# caplog.set_level(logging.INFO)
	# print(caplog.text) 

# print(st.lists(
#     st.lists(st.integers(min_value=1, max_value=3), min_size=2, max_size=2),
#     min_size=1,
#     max_size=40
# ).example())
# print(st.lists(st.integers() | st.floats(allow_nan=False)).example())