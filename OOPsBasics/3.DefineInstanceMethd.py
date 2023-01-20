class Course:
    def __init__(self, name, ratings):
        self.name =name
        self.ratings = ratings
    def average(self):
        numOfRatings = len(self.ratings)
        avg = sum(self.ratings)/numOfRatings
        print(avg)

obj = Course("java", [1,2,2,5,2])
print(obj.ratings)
print(obj.name)
print(obj.average())