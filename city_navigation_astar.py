import heapq  # Digunakan untuk implementasi priority queue
import math   # Digunakan untuk menghitung jarak Euclidean

# Koordinat tiap kota
cities = {
    "A": (0, 0),
    "B": (2, 1),
    "C": (4, 2),
    "D": (5, 5),
    "E": (1, 4)
}

# Representasi graph: daftar kota dan tetangganya (tetangga langsung)
roads = {
    "A": ["B", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C"],
    "E": ["A", "D"]
}

# Fungsi untuk menghitung jarak Euclidean antara dua kota
def euclidean(a, b):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

# Implementasi algoritma A* untuk pencarian jalur terpendek
def a_star(start, goal):
    open_set = [(0, start)]  # Priority queue berisi tuple (f_score, nama_kota)
    came_from = {}  # Untuk melacak rute/jalur balik dari goal ke start
    g_score = {city: float('inf') for city in cities}  # Biaya dari start ke tiap node
    g_score[start] = 0  # Biaya dari start ke dirinya sendiri adalah 0
    visited_nodes = 0  # Untuk menghitung berapa node yang dikunjungi

    while open_set:
        _, current = heapq.heappop(open_set)  # Ambil node dengan f_score terkecil
        visited_nodes += 1

        # Jika sudah sampai ke goal, bangun kembali jalur dari goal ke start
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], visited_nodes  # Balikkan path supaya dari start ke goal

        # Periksa semua tetangga dari node saat ini
        for neighbor in roads[current]:
            tentative_g = g_score[current] + euclidean(current, neighbor)  # Hitung biaya baru ke tetangga
            if tentative_g < g_score[neighbor]:
                # Jika biaya lebih kecil, update jalur terbaik
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + euclidean(neighbor, goal)  # f(n) = g(n) + h(n)
                heapq.heappush(open_set, (f_score, neighbor))  # Masukkan ke open_set

    return None, visited_nodes  # Jika tidak ditemukan jalur

# Pemanggilan fungsi a_star untuk menguji jalur dari A ke D
start = "A"
goal = "D"
path, visited_nodes = a_star(start, goal)

# Menampilkan hasil
if path:
    print(f"Path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}")

print(f"Visited nodes: {visited_nodes}")
