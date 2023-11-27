from typing import *
from Array_Sorting import SelectionSort, InsertionSort, BubbleSort

# Array_Sorting 실행 함수
if __name__ == "__main__":
    """프로그램의 실행을 위한 시작 지점 역할을 수행하는(제일 먼저 실행되는) 메인 함수"""
    array_to_sort: List = [96, 88, 34, 8, 13, 65, 25, 72, 47, 51]

    # 원하는 정렬 주석 풀어서 실행
    type_to_sort =  SelectionSort(data=array_to_sort) # 선택 정렬
    # type_to_sort = InsertionSort() # 삽입 정렬
    # type_to_sort= BubbleSort() # 버블 정렬

    array_to_type_sort = array_to_sort.copy()
    # 원본 데이터를 복사하여 새로운 배열 생성
    type_to_sort.sorting(data = array_to_type_sort)
    # 선택 정렬된 배열을 반환
    print(array_to_type_sort)
