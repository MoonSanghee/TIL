class student:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return '이름: {0}'.format(self.name)

class GraduateStudent(student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return super().__repr__() + ', 전공: {0}'.format(self.major)

student1=student('홍길동')
student2=GraduateStudent('이순신','컴퓨터')
print(student1)
print(student2)