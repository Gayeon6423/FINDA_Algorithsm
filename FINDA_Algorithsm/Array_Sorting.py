from abc import ABC, abstractmethod
from typing import *

class SortingAlgorithm(ABC):
    """정렬 알고리즘의 일관성을 유지하는 SortingAlgorithm 부모 추상 클래스"""
    @abstractmethod
    def sorting(self, data):
        """상속(자식) 구체 클래스에서 반드시 오버라이딩해야 하는 sorting 추상 메서드"""
        pass

class SelectionSort(SortingAlgorithm):
    """선택된 정렬 구체 클래스"""
    def __init__(self, data:any):
        self.data = data

    def sorting(self, data):
        """배열 등 추상 자료형의 왼쪽에서 오른쪽으로 진행하면서 
        가장 작은 값을 반복적으로 선택하여 적합한 위치로 교환하는 메서드"""
        length = len(data)

        for index in range(0,length,1):
            # data 변수에 입력되는 배열에서 가장 작은 값의 인덱스 번호(첫번째 값이 min으로 초기화)
            min_index = index
            for next_index in range(index+1, length, 1):
                # 다음 인덱스 위치 값 < 가장 작은 인덱스 위치 값 (5, 3) 
                if data[next_index] < data[min_index]:
                    # 가장 작은 값의 인덱스 위치를 다음 인덱스 위치로 변경
                    min_index = next_index
                    print(min_index, data)
            data[index], data[min_index] = data[min_index], data[index]

            # 가장 작은 인덱스 위치 값 < 그 다음 인덱스 위치 값
            # 정렬 보장 위해 가장 작은 인덱스 위치 값과 인덱스 위치 값 교환
            # data[min_index]가 data[index]보다 앞에 있는 인덱스 위치로 재배치

class InsertionSort(SortingAlgorithm):
    """삽입 정렬 구체 클래스"""
    def sorting(self, data):
        length = len(data)
        
        for index in range(1, length, 1): 
            # 두 번째 인덱스부터
            min_index = index

            for prior_index in range(index,0,-1):
                # 가장 작은 값의 인덱스 위치보다 1만큼 감소된 위치에서 루프 반복
                if data[prior_index-1] <= data[prior_index]:
                    # 바로 옆에 있는 데이터와 비교한다는 점에서 안정정렬
                    break # 전 인덱스 값보다 크거나 같게 정렬되었으므로 멈춤
                    print(min_index, data)
                # 전 인덱스 값보다 작을 경우(오름차순X)
                # 비 순차적인 두 값에 따라 인덱스의 위치를 교환
                data[index], data[prior_index] = data[prior_index], data[index]

class BubbleSort(SortingAlgorithm):
    """버블 정렬 구체 클래스"""
    def sorting(self, data):
        length = len(data)

        for index in range(0,length-1,1):
            # 이전 인덱스
            for prior_index in range(0,length-2,1):
                # 2개 전 인덱스
                if data[prior_index] > data[prior_index+1]:
                    # 인덱스와 이전 인덱스의 요소가 오름차순 정렬이 아니라면
                    data[prior_index], data[prior_index+1] = data[prior_index+1],data[prior_index]     
                    # 두 위치 값을 교환
                    print(prior_index,data)
