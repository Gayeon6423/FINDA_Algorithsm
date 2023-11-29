from linked_list import Node, Single_LinkedList, Doubly_LinkedList

# 노드 생성
## 데이터 2,3,5,7,11을 담는 노드를 생성
head_node = Node(2) # 노드 인스턴스 생성, 2는 data 속성에 저장
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)
## 노드들을 연결(레퍼런스로 연결)
head_node.next = node_1 # head_node의 다음 노드를 node_1으로 설정
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node
## 노드 순서대로 출력
iterator = head_node # iterator : 반복문을 돌 때 도움을 주는 역할 값
while iterator is not None:
    print(iterator.data) # node의 data속성 출력(처음에는 head의 data 출력)
    # 기존 속성의 next속성이 가지고 있는 값을 넣어줌
    # tail_node 다음에는 iterator가 0으로 변하고 반복문 종료
    iterator = iterator.next 


# 새로운 링크드 리스트 생성
my_list = Single_LinkedList()
## 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)
## 링크드 리스트 출력
iterator = my_list.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

# 접근 연산 예시
## 링크드 리스트 노드에 접근(데이터 가지고 오기)
print(my_list.find_node_at(3).data)
## 링크드 리스트 노드에 접근(데이터 바꾸기), 2번째 인덱스의 값을 13으로 변경
my_list.find_node_at(2).data = 13
print(my_list)

# 삽입 연산 예시
## 인덱스 2에 있는 노드 접근
node_2 = my_list.find_node_at(2)
## 인덱스 2 뒤에 6 삽입
my_list.insert_after(node_2,6)
print(my_list)
## 헤드 노드 접근
head_node = my_list.head
## 헤드 노드 뒤에 9 삽입
my_list.insert_after(head_node, 9)
print(my_list)

# 삭제 연산 예시
## 인덱스 2노드 접근
node_2 = my_list.find_node_at(2)
## 인덱스 2 뒤 노드 삭제
my_list.delete_after(node_2)
print(my_list)

## 맨 끝에서 두 번째 노드 접근
second_to_last_node = my_list.find_node_at(2)
my_list.delete_after(second_to_last_node)
print(my_list)


# 더블리 링크드 리스트
# 추가 연산 예시
## 빈 링크드 리스트 정의
my_list = Doubly_LinkedList()
## 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
print(my_list)

# 삽입 연산 예시
## tail 노드 뒤에 노드 삽입
tail_node = my_list.tail  # 4 번째(마지막)노드를 찾는다
my_list.insert_after(tail_node, 5)  # 4 번째(마지막)노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)

# 삭제 연산 예시
## 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

## 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

## 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

## 마지막 노드 삭제
last_node  = my_list.head
my_list.delete(last_node)
print(my_list)