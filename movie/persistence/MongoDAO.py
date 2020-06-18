from pymongo import MongoClient


# class 작성
class MongoDAO: # python에서 class와 method는 공백(enter)을 두 칸 만드는 것이 규칙
    reply_list=[] # MongoDB Document를 담을 list 선언
    
    # 생성자 : 객체를 생성하면서 추가적으로 어떤 작업을 수행하는 코드, 객체 생성 시 한 번만 실행됨

    # MongoDB Connection
    def __init__(self):
        # 객체를 생성할 때 하는 일을 작성한 코드
        self.client=MongoClient('127.0.0.1', 27017) # 클래스 객체 할당(ip, Port)
        self.db=self.client['local'] # MongoDB의 'local' DB 할당
        self.collection=self.db.get_collection('movie') # 동적으로 Collection 선택

    # MongoDB에 Insert
    def mongo_write(self, data):
        print('>> MongoDB WRITE DATA')
        self.collection.insert(data) # JSON Type=Dict Type(Python)

    # MongoDB에서 SelectAll
    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0, 'content':1, 'score':1}):
            self.reply_list.append([one['title'], one['content'], one['score']]) # dict에서 value와 score만 추출
        return self.reply_list