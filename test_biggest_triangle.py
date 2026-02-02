from hypothesis import given, strategies as st
from hypothesis.strategies import composite
from hypothesis.extra.numpy import arrays
import numpy as np
import math
from biggest_triangle import solution
MAX_TOTAL = 200000
SQRT_MAX = int(math.sqrt(MAX_TOTAL))

@composite
def diverse_shapes(draw):
    # 이전에 작성한 다양한 형상 생성 전략
    square_strategy = st.tuples(st.integers(1, SQRT_MAX), st.integers(1, SQRT_MAX))
    tall_strategy = st.integers(SQRT_MAX + 1, MAX_TOTAL).flatmap(
        lambda n: st.tuples(st.just(n), st.integers(1, MAX_TOTAL // n))
    )
    wide_strategy = st.integers(SQRT_MAX + 1, MAX_TOTAL).flatmap(
        lambda m: st.tuples(st.integers(1, MAX_TOTAL // m), st.just(m))
    )
    return draw(st.one_of(square_strategy, tall_strategy, wide_strategy))

@given(st.data())
def test_1_minus_1_array(data):
    # 1. 모양(shape) 결정
    n, m = data.draw(diverse_shapes())
    
    # 2. 결정된 shape으로 1과 -1만 포함하는 배열 생성
    matrix = data.draw(arrays(
        dtype=np.int8,  # 메모리 절약을 위해 int8 사용
        shape=(n, m),
        elements=st.sampled_from([1, -1]) # 1 또는 -1만 선택
    ))
    # print(f"Tested shape: {n}x{m}")
    try:
    	solution(matrix)
    except hypothesis.errors.DeadlineExceeded as e:
        # 실패 시에만 npy 파일이나 txt 파일로 저장
        np.savetxt("failed_matrix.txt", matrix, fmt='%d')
        raise e
    