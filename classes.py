class Candidate:
    def __init__(self, id_, name, picture, position, gender, age, skills):
        self.id = id_
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def __repr__(self):
        return self.name
