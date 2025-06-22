from models.person import Person

class Character(Person):
    def __init__(self, name, description, anime_origin, personality, rating):
        super().__init__(name, description)
        self.anime_origin = anime_origin
        self.personality = personality
        self.rating = rating

    def get_description(self):
        return f"{self.name} dari anime {self.anime_origin} adalah {self.description} ({self.personality}), rating: {self.rating}"