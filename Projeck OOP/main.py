import json
import os
from models.anime import Anime
from models.character import Character

DATA_FILE = 'data/anime_data.json'
anime_list = []

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            for anime_data in data:
                anime = Anime(
                    anime_data['judul'],
                    anime_data['genre'],
                    anime_data['total_episode'],
                    anime_data.get('rating', 0.0)
                )
                anime.update_progress(anime_data['episode_terakhir'])
                anime.status = anime_data['status']
                for char_data in anime_data.get('characters', []):
                    character = Character(
                        char_data['name'],
                        char_data['description'],
                        char_data['anime_origin'],
                        char_data['personality'],
                        char_data['rating']
                    )
                    anime.add_character(character)
                anime_list.append(anime)

def save_data():
    data = []
    for anime in anime_list:
        data.append({
            "judul": anime.title,
            "genre": anime.genre,
            "total_episode": anime.total_episodes,
            "episode_terakhir": anime.last_episode,
            "status": anime.status,
            "rating": anime.rating,
            "characters": [{
                "name": c.name,
                "description": c.description,
                "anime_origin": c.anime_origin,
                "personality": c.personality,
                "rating": c.rating
            } for c in anime.characters]
        })
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def menu():
    while True:
        print("\n=== AnimeTrack CLI ===")
        print("1. Tambah Anime")
        print("2. Tambah Karakter ke Anime")
        print("3. Lihat Semua Anime")
        print("4. Update Progress Anime")
        print("5. Edit Anime atau Karakter")
        print("6. Simpan dan Keluar")
        choice = input("Pilih menu (1-6): ")

        if choice == '1':
            title = input("Judul Anime: ")
            genre = input("Genre: ")
            total = int(input("Total Episode: "))
            rating = float(input("Rating Anime (1-10): "))
            anime = Anime(title, genre, total, rating)
            anime_list.append(anime)
            print("Anime berhasil ditambahkan!")

        elif choice == '2':
            if not anime_list:
                print("Belum ada anime!")
                continue
            for idx, anime in enumerate(anime_list):
                print(f"{idx+1}. {anime.title}")
            idx = int(input("Pilih anime ke berapa: ")) - 1
            if 0 <= idx < len(anime_list):
                name = input("Nama Karakter: ")
                desc = input("Deskripsi singkat: ")
                origin = anime_list[idx].title
                personality = input("Sifat karakter: ")
                rating = float(input("Rating (1-10): "))
                char = Character(name, desc, origin, personality, rating)
                anime_list[idx].add_character(char)
                print("Karakter berhasil ditambahkan!")
            else:
                print("Pilihan tidak valid.")

        elif choice == '3':
            if not anime_list:
                print("Belum ada data anime.")
                continue
            for anime in anime_list:
                info = anime.get_info()
                print(f"\nJudul: {info['judul']}")
                print(f"Genre: {info['genre']}")
                print(f"Progress: {info['episode_terakhir']}/{info['total_episode']}")
                print(f"Status: {info['status']}")
                print(f"Rating: {info['rating']}")
                print(f"Jumlah Karakter: {info['jumlah_karakter']}")
                for char in anime.characters:
                    print("  -", char.get_description())

        elif choice == '4':
            if not anime_list:
                print("Belum ada anime!")
                continue
            for idx, anime in enumerate(anime_list):
                print(f"{idx+1}. {anime.title} (Progress: {anime.last_episode}/{anime.total_episodes})")
            idx = int(input("Pilih anime ke berapa: ")) - 1
            if 0 <= idx < len(anime_list):
                new_progress = int(input(f"Episode terakhir yang kamu tonton ({anime_list[idx].last_episode}): "))
                anime_list[idx].update_progress(new_progress)
                print("Progress berhasil diperbarui!")
                print(f"Status sekarang: {anime_list[idx].status}")
            else:
                print("Pilihan tidak valid.")

        elif choice == '5':
            if not anime_list:
                print("Belum ada anime!")
                continue
            for idx, anime in enumerate(anime_list):
                print(f"{idx+1}. {anime.title}")
            idx = int(input("Pilih anime yang ingin diedit: ")) - 1
            if 0 <= idx < len(anime_list):
                anime = anime_list[idx]
                print(f"\nEdit Anime: {anime.title}")
                print("1. Ubah Judul")
                print("2. Ubah Genre")
                print("3. Ubah Total Episode")
                print("4. Ubah Rating")
                print("5. Edit Karakter")
                sub_choice = input("Pilih menu edit (1-5): ")

                if sub_choice == '1':
                    anime.title = input("Masukkan judul baru: ")
                    print("Judul berhasil diubah!")
                elif sub_choice == '2':
                    anime.genre = input("Masukkan genre baru: ")
                    print("Genre berhasil diubah!")
                elif sub_choice == '3':
                    anime.total_episodes = int(input("Masukkan total episode baru: "))
                    print("Total episode berhasil diubah!")
                elif sub_choice == '4':
                    anime.rating = float(input("Masukkan rating baru (1-10): "))
                    print("Rating berhasil diubah!")
                elif sub_choice == '5':
                    if not anime.characters:
                        print("Anime ini belum punya karakter.")
                        continue
                    for i, char in enumerate(anime.characters):
                        print(f"{i+1}. {char.name}")
                    cidx = int(input("Pilih karakter yang ingin diedit: ")) - 1
                    if 0 <= cidx < len(anime.characters):
                        char = anime.characters[cidx]
                        print("1. Nama")
                        print("2. Deskripsi")
                        print("3. Sifat")
                        print("4. Rating")
                        field = input("Pilih bagian karakter yang ingin diedit (1-4): ")
                        if field == '1':
                            char.name = input("Nama baru: ")
                        elif field == '2':
                            char.description = input("Deskripsi baru: ")
                        elif field == '3':
                            char.personality = input("Sifat baru: ")
                        elif field == '4':
                            char.rating = float(input("Rating baru (1-10): "))
                        else:
                            print("Pilihan tidak valid.")
                        print("Data karakter berhasil diubah!")
                    else:
                        print("Pilihan karakter tidak valid.")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Pilihan anime tidak valid.")

        elif choice == '6':
            save_data()
            print("Data disimpan. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    print(">> Memulai AnimeTrack...")
    load_data()
    menu()