class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        # 인스턴스 변수 초깃값 설정
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스
        self.prev = None # 전 노드에 대한 레퍼런스

class Single_LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None # 링크드 리스트의 가장 앞 노드
        self.tail = None # 링크드 리스트의 가장 뒤 노드

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"
        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수, 일단 가장 앞 노드로 정의
        iterator = self.head
        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f"{iterator.data} |"
            # 다음 노드로 넘어간다
            iterator = iterator.next
        return res_str

    def find_node_at(self,index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수
        # iterator변수를 이용해서 index번째에 있는 노드로 이동한다
        for _ in range(index):
            # 반복문을 돌때마다 iterator변수가 다음 노드를 가리킨다
            iterator = iterator.next 
        return iterator

    def find_node_with_data(self,data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다.
        단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어있지 않으면
        else: 
            # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail.next = new_node 
            # 마지막 노드를 추가한 노드로 바꿔준다
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메서드"""
        new_node = Node(data)
        
        if previous_node is self.tail:# 가장 마지막 순서 삽입
            self.tail.next = new_node
            self.tail = new_node
        else: # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def delete_after(self, previous_node):
        """링크드 리스트 삭제 연산. 주어진 노드 뒤 노드를 삭제한다"""
        data = previous_node.next.data # 지우려는 노드

        # 지우려는 노드가 tail 노드일 때
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        # 두 노드 사이를 지울 때
        else:
            previous_node.next = previous_node.next.next
        
        return data
    
class Doubly_LinkedList:
    """더블리 링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"
        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수, 일단 가장 앞 노드로 정의
        iterator = self.head
        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            # 다음 노드로 넘어간다
            iterator = iterator.next
        return res_str

    def find_node_at(self,index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수
        # iterator변수를 이용해서 index번째에 있는 노드로 이동한다
        for _ in range(index):
            # 반복문을 돌때마다 iterator변수가 다음 노드를 가리킨다
            iterator = iterator.next 
        return iterator

    def find_node_with_data(self,data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다.
        단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None
    
    def append(self,data):
        """추가 연산 메소드"""
        new_node = Node(data) # 새로운 데이터를 저장하는 노드
        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않다면
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self,previous_node,data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 가장 마지막 노드 뒤에 삽입한다면
        if previous_node is self.tail:
            new_node.prev = previous_node
            previous_node.next = new_node
            self.tail = new_node
        
        # 노드 사이에 삽입한다면
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def prepend(self,data):
        """더블리 링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)

        # 리스트가 비어있다면
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 리스트가 비어있지 않다면
        else: 
            new_node.next = self.head # 새로운 노드의 다음 노드를 head로 지정
            self.head.prev = new_node # head 노드의 전 노드를 새로운 노드로 지정
            self.head = new_node # head 노드 업데이트

    def delete(self,node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 삭제하는 노드가 마지막 남은 노드인 경우
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        # 가장 앞 데이터를 지우는 경우
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
        # 가장 뒤 데이터를 지우는 경우
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        # 두 노드 사이에 있는 데이터를 지우는 경우
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data


