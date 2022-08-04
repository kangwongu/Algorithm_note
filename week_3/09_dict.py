class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 데이터 삽입
    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    # key값에 해당하는 value값 가져오기
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))