class Anime:
    def __init__(self, title, genre, total_episodes, rating):
        self.title = title
        self.genre = genre
        self.total_episodes = total_episodes
        self.last_episode = 0
        self.status = "Belum Ditonton"
        self.rating = rating  # Tambahkan atribut rating
        self.characters = []

    def update_progress(self, episode):
        self.last_episode = episode
        if episode >= self.total_episodes:
            self.status = "Selesai"
        elif episode > 0:
            self.status = "Sedang Ditonton"
        else:
            self.status = "Belum Ditonton"

    def add_character(self, character):
        self.characters.append(character)

    def get_info(self):
        return {
            "judul": self.title,
            "genre": self.genre,
            "total_episode": self.total_episodes,
            "episode_terakhir": self.last_episode,
            "status": self.status,
            "rating": self.rating,
            "jumlah_karakter": len(self.characters)
        }