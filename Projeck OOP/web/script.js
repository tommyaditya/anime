// Ambil dan tampilkan semua anime
function loadAnime() {
    fetch('http://127.0.0.1:5000/anime')
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById('animeList');
        list.innerHTML = '';
        data.forEach((anime, i) => {
            const div = document.createElement('div');
            div.innerHTML = `
            <h3>${anime.judul}</h3>
            <p><strong>Genre:</strong> ${anime.genre}</p>
            <p><strong>Episode:</strong> ${anime.episode_terakhir}/${anime.total_episode}</p>
            <p><strong>Status:</strong> ${anime.status}</p>
            <p><strong>Rating:</strong> ${anime.rating}</p>
            <p><strong>Karakter:</strong></p>
            <ul>
            ${anime.characters?.map(c => `<li>${c.name} - ${c.description} (${c.personality}, rating ${c.rating})</li>`).join('') || '<li>Tidak ada karakter.</li>'}
            </ul>
        `;
        list.appendChild(div);
        });
    });
}

// Tambah anime
document.getElementById('animeForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const data = {
    judul: document.getElementById('judul').value,
    genre: document.getElementById('genre').value,
    total_episode: parseInt(document.getElementById('total').value),
    episode_terakhir: 0,
    status: 'Belum Ditonton',
    rating: parseFloat(document.getElementById('rating').value),
    characters: []
    };
    fetch('http://127.0.0.1:5000/anime', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
    }).then(() => {
    loadAnime();
    this.reset();
    });
});

// Tambah karakter
document.getElementById('charForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const index = parseInt(document.getElementById('animeIndex').value);
    const data = {
    name: document.getElementById('charName').value,
    description: document.getElementById('charDesc').value,
    anime_origin: 'unknown',
    personality: document.getElementById('charPersonality').value,
    rating: parseFloat(document.getElementById('charRating').value)
    };
    fetch(`http://127.0.0.1:5000/anime/${index}/character`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
}).then(() => {
    loadAnime();
    this.reset();
});
});

// Muat data awal saat halaman dibuka
loadAnime();