class Course:
    def __init__(self, name, ratings):
        self.name =name
        self.ratings = ratings

obj = Course("java", [1,2,2,5,2])

print(obj.ratings)
print(obj.name)