from flask import Flask, render_template, request, redirect, session
from datetime import date, timedelta

app = Flask(__name__)

app.secret_key = "sistem-perpustakaan-sekolah"


# =========================================================
# AKUN ADMIN
# =========================================================

akun_admin = {
    "username": "admin",
    "password": "12345"
}


# =========================================================
# DATA BUKU
# =========================================================

daftar_buku = [

    # =====================================================
    # FIKSI - 30 BUKU
    # =====================================================

    {
        "judul": "Laskar Pelangi",
        "penulis": "Andrea Hirata",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Bumi Manusia",
        "penulis": "Pramoedya Ananta Toer",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Negeri 5 Menara",
        "penulis": "Ahmad Fuadi",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Rantau 1 Muara",
        "penulis": "Ahmad Fuadi",
        "kategori": "Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Perahu Kertas",
        "penulis": "Dee Lestari",
        "kategori": "Fiksi",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Dilan 1990",
        "penulis": "Pidi Baiq",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Dilan 1991",
        "penulis": "Pidi Baiq",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Milea",
        "penulis": "Pidi Baiq",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ayat-Ayat Cinta",
        "penulis": "Habiburrahman El Shirazy",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Bulan",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Bintang",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Matahari",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Hujan",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Pulang",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Pergi",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Rembulan Tenggelam di Wajahmu",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Laut Bercerita",
        "penulis": "Leila S. Chudori",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Pulang Pergi",
        "penulis": "Tere Liye",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Aroma Karsa",
        "penulis": "Dee Lestari",
        "kategori": "Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Supernova",
        "penulis": "Dee Lestari",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ronggeng Dukuh Paruk",
        "penulis": "Ahmad Tohari",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Sang Pemimpi",
        "penulis": "Andrea Hirata",
        "kategori": "Fiksi",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Edensor",
        "penulis": "Andrea Hirata",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Cinta di Dalam Gelas",
        "penulis": "Andrea Hirata",
        "kategori": "Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Padang Bulan",
        "penulis": "Andrea Hirata",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Pulang ke Rumah",
        "penulis": "Budi Santoso",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Langit Senja",
        "penulis": "Rina Pratiwi",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Rumah di Ujung Jalan",
        "penulis": "Dina Maharani",
        "kategori": "Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Kisah di Balik Hujan",
        "penulis": "Fajar Nugraha",
        "kategori": "Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Jejak Langkah",
        "penulis": "Pramoedya Ananta Toer",
        "kategori": "Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },


    # =====================================================
    # NON-FIKSI - 30 BUKU
    # =====================================================

    {
        "judul": "Atomic Habits",
        "penulis": "James Clear",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Filosofi Teras",
        "penulis": "Henry Manampiring",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Sapiens",
        "penulis": "Yuval Noah Harari",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Homo Deus",
        "penulis": "Yuval Noah Harari",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "The Psychology of Money",
        "penulis": "Morgan Housel",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Rich Dad Poor Dad",
        "penulis": "Robert Kiyosaki",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Berani Tidak Disukai",
        "penulis": "Ichiro Kishimi",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Mindset",
        "penulis": "Carol S. Dweck",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "The Power of Now",
        "penulis": "Eckhart Tolle",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Think and Grow Rich",
        "penulis": "Napoleon Hill",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "How to Win Friends",
        "penulis": "Dale Carnegie",
        "kategori": "Non-Fiksi",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "The 7 Habits of Highly Effective People",
        "penulis": "Stephen R. Covey",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Start With Why",
        "penulis": "Simon Sinek",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Deep Work",
        "penulis": "Cal Newport",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Digital Minimalism",
        "penulis": "Cal Newport",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ikigai",
        "penulis": "Hector Garcia",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Good Vibes Good Life",
        "penulis": "Vex King",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "The Subtle Art of Not Giving a F*ck",
        "penulis": "Mark Manson",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Essentialism",
        "penulis": "Greg McKeown",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Grit",
        "penulis": "Angela Duckworth",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Outliers",
        "penulis": "Malcolm Gladwell",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Blink",
        "penulis": "Malcolm Gladwell",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "The Tipping Point",
        "penulis": "Malcolm Gladwell",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Quiet",
        "penulis": "Susan Cain",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Educated",
        "penulis": "Tara Westover",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Becoming",
        "penulis": "Michelle Obama",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Steve Jobs",
        "penulis": "Walter Isaacson",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Elon Musk",
        "penulis": "Walter Isaacson",
        "kategori": "Non-Fiksi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Leonardo da Vinci",
        "penulis": "Walter Isaacson",
        "kategori": "Non-Fiksi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "The Art of Thinking Clearly",
        "penulis": "Rolf Dobelli",
        "kategori": "Non-Fiksi",
        "stok": 5,
        "status": "Tersedia"
    },


    # =====================================================
    # BUKU PELAJARAN - 30 BUKU
    # =====================================================

    {
        "judul": "Matematika Dasar",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Bahasa Indonesia",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Bahasa Inggris Dasar",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Fisika untuk SMA",
        "penulis": "Budi Santoso",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Kimia untuk SMA",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Biologi untuk SMA",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Sejarah Indonesia",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Geografi Indonesia",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Ekonomi SMA",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Sosiologi SMA",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Pendidikan Pancasila",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Pendidikan Kewarganegaraan",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Informatika Dasar",
        "penulis": "Andi Publisher",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Pemrograman Python",
        "penulis": "Andi Publisher",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Pemrograman Java",
        "penulis": "Informatika",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Pemrograman Web",
        "penulis": "Informatika",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Basis Data",
        "penulis": "Informatika",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Jaringan Komputer",
        "penulis": "Andi Publisher",
        "kategori": "Buku Pelajaran",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Sistem Operasi",
        "penulis": "Informatika",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Algoritma dan Pemrograman",
        "penulis": "Informatika",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Statistika Dasar",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Kalkulus Dasar",
        "penulis": "Erlangga",
        "kategori": "Buku Pelajaran",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Bahasa Jawa",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Seni Budaya",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Pendidikan Jasmani",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 6,
        "status": "Tersedia"
    },
    {
        "judul": "Prakarya",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Agama Islam",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Pendidikan Agama Kristen",
        "penulis": "Kementerian Pendidikan",
        "kategori": "Buku Pelajaran",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Bahasa Jepang Dasar",
        "penulis": "Andi Publisher",
        "kategori": "Buku Pelajaran",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Bahasa Korea Dasar",
        "penulis": "Andi Publisher",
        "kategori": "Buku Pelajaran",
        "stok": 3,
        "status": "Tersedia"
    },


    # =====================================================
    # REFERENSI - 30 BUKU
    # =====================================================

    {
        "judul": "Ensiklopedia Indonesia",
        "penulis": "Tim Ensiklopedia",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Kamus Besar Bahasa Indonesia",
        "penulis": "Badan Bahasa",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Kamus Bahasa Inggris",
        "penulis": "Oxford",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Kamus Bahasa Jepang",
        "penulis": "Tim Bahasa",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Atlas Dunia",
        "penulis": "Tim Kartografi",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Atlas Indonesia",
        "penulis": "Tim Kartografi",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Sains",
        "penulis": "Tim Sains",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Hewan",
        "penulis": "Tim Ensiklopedia",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Tumbuhan",
        "penulis": "Tim Botani",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Sejarah",
        "penulis": "Tim Sejarah",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Teknologi",
        "penulis": "Tim Teknologi",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Geografi",
        "penulis": "Tim Geografi",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Astronomi",
        "penulis": "Tim Astronomi",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Matematika",
        "penulis": "Tim Matematika",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Fisika",
        "penulis": "Tim Fisika",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Kimia",
        "penulis": "Tim Kimia",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Biologi",
        "penulis": "Tim Biologi",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Panduan Tata Bahasa",
        "penulis": "Tim Bahasa",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Buku Pintar Bahasa Indonesia",
        "penulis": "Tim Bahasa",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Buku Pintar Matematika",
        "penulis": "Tim Matematika",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Buku Pintar Sains",
        "penulis": "Tim Sains",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Panduan Dunia Digital",
        "penulis": "Tim Teknologi",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Panduan Komputer",
        "penulis": "Tim Komputer",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Panduan Internet",
        "penulis": "Tim Teknologi",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Daftar Istilah Sains",
        "penulis": "Tim Sains",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Daftar Istilah Teknologi",
        "penulis": "Tim Teknologi",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Panduan Penulisan",
        "penulis": "Tim Bahasa",
        "kategori": "Referensi",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Panduan Penelitian",
        "penulis": "Tim Pendidikan",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Budaya Indonesia",
        "penulis": "Tim Budaya",
        "kategori": "Referensi",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Ensiklopedia Tokoh Dunia",
        "penulis": "Tim Sejarah",
        "kategori": "Referensi",
        "stok": 4,
        "status": "Tersedia"
    },


    # =====================================================
    # KOMIK - 30 BUKU
    # =====================================================

    {
        "judul": "Doraemon Vol. 1",
        "penulis": "Fujiko F. Fujio",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Doraemon Vol. 2",
        "penulis": "Fujiko F. Fujio",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Doraemon Vol. 3",
        "penulis": "Fujiko F. Fujio",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Doraemon Vol. 4",
        "penulis": "Fujiko F. Fujio",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Doraemon Vol. 5",
        "penulis": "Fujiko F. Fujio",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Naruto Vol. 1",
        "penulis": "Masashi Kishimoto",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Naruto Vol. 2",
        "penulis": "Masashi Kishimoto",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Naruto Vol. 3",
        "penulis": "Masashi Kishimoto",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Naruto Vol. 4",
        "penulis": "Masashi Kishimoto",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Naruto Vol. 5",
        "penulis": "Masashi Kishimoto",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "One Piece Vol. 1",
        "penulis": "Eiichiro Oda",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "One Piece Vol. 2",
        "penulis": "Eiichiro Oda",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "One Piece Vol. 3",
        "penulis": "Eiichiro Oda",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "One Piece Vol. 4",
        "penulis": "Eiichiro Oda",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "One Piece Vol. 5",
        "penulis": "Eiichiro Oda",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Detective Conan Vol. 1",
        "penulis": "Gosho Aoyama",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Detective Conan Vol. 2",
        "penulis": "Gosho Aoyama",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Detective Conan Vol. 3",
        "penulis": "Gosho Aoyama",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Crayon Shinchan Vol. 1",
        "penulis": "Yoshito Usui",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Crayon Shinchan Vol. 2",
        "penulis": "Yoshito Usui",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Crayon Shinchan Vol. 3",
        "penulis": "Yoshito Usui",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Dragon Ball Vol. 1",
        "penulis": "Akira Toriyama",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Dragon Ball Vol. 2",
        "penulis": "Akira Toriyama",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Dragon Ball Vol. 3",
        "penulis": "Akira Toriyama",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "Haikyuu Vol. 1",
        "penulis": "Haruichi Furudate",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "Haikyuu Vol. 2",
        "penulis": "Haruichi Furudate",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "Haikyuu Vol. 3",
        "penulis": "Haruichi Furudate",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    },
    {
        "judul": "My Hero Academia Vol. 1",
        "penulis": "Kohei Horikoshi",
        "kategori": "Komik",
        "stok": 5,
        "status": "Tersedia"
    },
    {
        "judul": "My Hero Academia Vol. 2",
        "penulis": "Kohei Horikoshi",
        "kategori": "Komik",
        "stok": 4,
        "status": "Tersedia"
    },
    {
        "judul": "My Hero Academia Vol. 3",
        "penulis": "Kohei Horikoshi",
        "kategori": "Komik",
        "stok": 3,
        "status": "Tersedia"
    }
]

# =========================================================
# DATA PEMINJAMAN
# =========================================================

peminjaman = []


# =========================================================
# FUNGSI BANTUAN
# =========================================================

def sudah_login():
    return "login" in session


def adalah_admin():
    return session.get("role") == "admin"


def adalah_siswa():
    return session.get("role") == "siswa"


def siswa_punya_pinjaman_terlambat(username):
    hari_ini = date.today()

    for data in peminjaman:

        if (
            data["username"] == username
            and data["status"] == "Dipinjam"
        ):

            batas = date.fromisoformat(
                data["batas_pengembalian"]
            )

            if hari_ini > batas:
                return True

    return False


def update_status_buku(id_buku):
    if 0 <= id_buku < len(daftar_buku):

        if daftar_buku[id_buku]["stok"] > 0:
            daftar_buku[id_buku]["status"] = "Tersedia"
        else:
            daftar_buku[id_buku]["status"] = "Tidak Tersedia"


# =========================================================
# LOGIN
# =========================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        role = request.form.get("role")

        # -------------------------------------------------
        # LOGIN ADMIN
        # -------------------------------------------------

        if role == "admin":

            username = request.form.get("username")
            password = request.form.get("password")

            if (
                username == akun_admin["username"]
                and password == akun_admin["password"]
            ):

                session.clear()

                session["login"] = True
                session["role"] = "admin"
                session["username"] = username
                session["nama"] = "Administrator"
                session["kelas"] = "-"

                return redirect("/admin")

            return render_template(
                "login.html",
                error="Username atau password admin salah!"
            )

        # -------------------------------------------------
        # LOGIN SISWA
        # -------------------------------------------------

        elif role == "siswa":

            nama = request.form.get(
                "nama",
                ""
            ).strip()

            kelas = request.form.get(
                "kelas",
                ""
            ).strip()

            if nama == "" or kelas == "":

                return render_template(
                    "login.html",
                    error="Nama lengkap dan kelas wajib diisi!"
                )

            session.clear()

            session["login"] = True
            session["role"] = "siswa"
            session["nama"] = nama
            session["kelas"] = kelas
            session["username"] = nama

            return redirect("/siswa")

    return render_template("login.html")


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    if not sudah_login():
        return redirect("/")

    if adalah_admin():
        return redirect("/admin")

    if adalah_siswa():
        return redirect("/siswa")

    return redirect("/")


# =========================================================
# DASHBOARD ADMIN
# =========================================================

@app.route("/admin")
def admin():

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    total = len(daftar_buku)

    tersedia = sum(
        buku["stok"]
        for buku in daftar_buku
        if buku["stok"] > 0
    )

    dipinjam = sum(
        1
        for buku in daftar_buku
        if buku["status"] == "Dipinjam"
        or buku["stok"] == 0
    )

    total_peminjaman = len(peminjaman)

    return render_template(
        "admin.html",
        total=total,
        tersedia=tersedia,
        dipinjam=dipinjam,
        total_peminjaman=total_peminjaman
    )


# =========================================================
# KELOLA DATA BUKU
# =========================================================

@app.route("/admin/buku")
def admin_buku():

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    error = request.args.get("error")
    sukses = request.args.get("sukses")

    return render_template(
        "buku.html",
        buku=daftar_buku,
        error=error,
        sukses=sukses
    )


# =========================================================
# KOLEKSI BUKU
# =========================================================

@app.route("/admin/koleksi")
def admin_koleksi():

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    return render_template(
        "koleksi.html",
        buku=daftar_buku
    )


# =========================================================
# TAMBAH BUKU
# =========================================================

@app.route("/tambah", methods=["POST"])
def tambah():

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    judul = request.form.get(
        "judul",
        ""
    ).strip()

    penulis = request.form.get(
        "penulis",
        ""
    ).strip()

    kategori = request.form.get(
        "kategori",
        ""
    ).strip()

    status = request.form.get(
        "status",
        "Tersedia"
    )

    stok_text = request.form.get(
        "stok",
        "0"
    ).strip()

    # -----------------------------------------------------
    # CEK DATA KOSONG
    # -----------------------------------------------------

    if (
        judul == ""
        or penulis == ""
        or kategori == ""
    ):

        return redirect(
            "/admin/buku?error="
            "Judul%2C%20penulis%2C%20dan%20kategori%20wajib%20diisi!"
        )

    # -----------------------------------------------------
    # CEK STOK
    # -----------------------------------------------------

    try:
        stok = int(stok_text)
    except ValueError:
        stok = 0

    if stok <= 0:

        return redirect(
            "/admin/buku?error="
            "Jumlah%20stok%20harus%20lebih%20dari%200!"
        )

    # -----------------------------------------------------
    # CEK JUDUL DUPLIKAT
    # -----------------------------------------------------

    for buku in daftar_buku:

        if buku["judul"].strip().lower() == judul.lower():

            return redirect(
                "/admin/buku?error="
                "Buku%20dengan%20judul%20tersebut%20sudah%20ada!"
            )

    # -----------------------------------------------------
    # STATUS OTOMATIS
    # -----------------------------------------------------

    if stok > 0:
        status = "Tersedia"
    else:
        status = "Tidak Tersedia"

    # -----------------------------------------------------
    # TAMBAHKAN BUKU
    # -----------------------------------------------------

    daftar_buku.append({
        "judul": judul,
        "penulis": penulis,
        "kategori": kategori,
        "stok": stok,
        "status": status
    })

    return redirect(
        "/admin/buku?sukses="
        "Buku%20berhasil%20ditambahkan!"
    )


# =========================================================
# EDIT BUKU
# =========================================================

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    if id < 0 or id >= len(daftar_buku):
        return redirect("/admin/buku")

    if request.method == "POST":

        judul = request.form.get(
            "judul",
            ""
        ).strip()

        penulis = request.form.get(
            "penulis",
            ""
        ).strip()

        kategori = request.form.get(
            "kategori",
            ""
        ).strip()

        stok_text = request.form.get(
            "stok",
            "0"
        ).strip()

        if (
            judul == ""
            or penulis == ""
            or kategori == ""
        ):

            return redirect(
                "/admin/buku?error="
                "Data%20buku%20wajib%20diisi!"
            )

        try:
            stok = int(stok_text)
        except ValueError:
            stok = -1

        if stok < 0:

            return redirect(
                "/admin/buku?error="
                "Stok%20tidak%20boleh%20kurang%20dari%200!"
            )

        # -------------------------------------------------
        # CEK DUPLIKAT JUDUL
        # -------------------------------------------------

        for index, buku in enumerate(daftar_buku):

            if index != id:

                if (
                    buku["judul"].strip().lower()
                    == judul.lower()
                ):

                    return redirect(
                        "/admin/buku?error="
                        "Judul%20buku%20sudah%20digunakan!"
                    )

        # -------------------------------------------------
        # UPDATE DATA
        # -------------------------------------------------

        daftar_buku[id]["judul"] = judul
        daftar_buku[id]["penulis"] = penulis
        daftar_buku[id]["kategori"] = kategori
        daftar_buku[id]["stok"] = stok

        update_status_buku(id)

        return redirect(
            "/admin/buku?sukses="
            "Data%20buku%20berhasil%20diubah!"
        )

    return render_template(
        "edit.html",
        buku=daftar_buku[id],
        id=id
    )


# =========================================================
# HAPUS BUKU
# =========================================================

@app.route("/hapus/<int:id>")
def hapus(id):

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    if 0 <= id < len(daftar_buku):

        # Jangan hapus kalau masih ada yang meminjam
        sedang_dipinjam = False

        for data in peminjaman:

            if (
                data["id_buku"] == id
                and data["status"] == "Dipinjam"
            ):

                sedang_dipinjam = True
                break

        if sedang_dipinjam:

            return redirect(
                "/admin/buku?error="
                "Buku%20sedang%20dipinjam%20dan%20tidak%20bisa%20dihapus!"
            )

        daftar_buku.pop(id)

    return redirect(
        "/admin/buku?sukses="
        "Buku%20berhasil%20dihapus!"
    )


# =========================================================
# DATA PEMINJAMAN ADMIN
# =========================================================

@app.route("/admin/peminjaman")
def admin_peminjaman():

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    hari_ini = date.today()

    data_peminjaman = []

    for data in peminjaman:

        item = data.copy()

        batas = date.fromisoformat(
            data["batas_pengembalian"]
        )

        if (
            data["status"] == "Dipinjam"
            and hari_ini > batas
        ):

            item["terlambat"] = True

        else:

            item["terlambat"] = False

        data_peminjaman.append(item)

    return render_template(
        "peminjaman.html",
        peminjaman=data_peminjaman
    )


# =========================================================
# KEMBALIKAN BUKU
# =========================================================

@app.route("/admin/kembalikan/<int:id>")
def kembalikan(id):

    if not sudah_login():
        return redirect("/")

    if not adalah_admin():
        return redirect("/siswa")

    if 0 <= id < len(peminjaman):

        data = peminjaman[id]

        if data["status"] == "Dipinjam":

            data["status"] = "Dikembalikan"

            id_buku = data["id_buku"]

            if (
                0 <= id_buku
                < len(daftar_buku)
            ):

                # STOK BERTAMBAH SAAT BUKU KEMBALI
                daftar_buku[id_buku]["stok"] += 1

                update_status_buku(id_buku)

    return redirect("/admin/peminjaman")


# =========================================================
# HALAMAN SISWA
# =========================================================

@app.route("/siswa")
def siswa():

    if not sudah_login():
        return redirect("/")

    if not adalah_siswa():
        return redirect("/admin")

    username = session["username"]

    terlambat = siswa_punya_pinjaman_terlambat(
        username
    )

    # -----------------------------------------------------
    # FILTER KATEGORI
    # -----------------------------------------------------

    kategori = request.args.get(
        "kategori",
        "Semua"
    )

    buku_siswa = []

    for index, buku in enumerate(daftar_buku):

        # Kalau bukan Semua, tampilkan sesuai kategori
        if (
            kategori != "Semua"
            and buku["kategori"] != kategori
        ):
            continue

        data = buku.copy()

        data["id"] = index

        buku_siswa.append(data)

    return render_template(
        "siswa.html",
        buku=buku_siswa,
        terlambat=terlambat,
        nama=session.get("nama"),
        kelas=session.get("kelas"),
        kategori_dipilih=kategori
    )


# =========================================================
# SISWA MEMINJAM BUKU
# =========================================================

@app.route(
    "/siswa/pesan/<int:id>",
    methods=["GET", "POST"]
)
def pesan_buku(id):

    if not sudah_login():
        return redirect("/")

    if not adalah_siswa():
        return redirect("/admin")

    if id < 0 or id >= len(daftar_buku):
        return redirect("/siswa")

    username = session["username"]

    # -----------------------------------------------------
    # CEK KETERLAMBATAN
    # -----------------------------------------------------

    if siswa_punya_pinjaman_terlambat(username):

        return render_template(
            "pesan.html",
            buku=daftar_buku[id],
            error=(
                "Kamu masih memiliki buku yang "
                "melewati batas 3 hari. "
                "Silakan kembalikan buku terlebih dahulu."
            )
        )

    # -----------------------------------------------------
    # CEK STOK
    # -----------------------------------------------------

    if daftar_buku[id]["stok"] <= 0:

        return render_template(
            "pesan.html",
            buku=daftar_buku[id],
            error="Stok buku sedang habis."
        )

    if request.method == "POST":

        tanggal_peminjaman = request.form.get(
            "tanggal_peminjaman"
        )

        if not tanggal_peminjaman:

            return render_template(
                "pesan.html",
                buku=daftar_buku[id],
                error="Tanggal peminjaman wajib diisi."
            )

        try:

            tanggal_pinjam = date.fromisoformat(
                tanggal_peminjaman
            )

        except ValueError:

            return render_template(
                "pesan.html",
                buku=daftar_buku[id],
                error="Format tanggal tidak valid."
            )

        if tanggal_pinjam < date.today():

            return render_template(
                "pesan.html",
                buku=daftar_buku[id],
                error=(
                    "Tanggal peminjaman tidak boleh "
                    "sebelum hari ini."
                )
            )

        # Batas 3 hari
        batas_pengembalian = (
            tanggal_pinjam
            + timedelta(days=3)
        )

        # -------------------------------------------------
        # CATAT PEMINJAMAN
        # -------------------------------------------------

        peminjaman.append({

            "username": username,

            "nama_siswa": session.get(
                "nama"
            ),

            "kelas": session.get(
                "kelas"
            ),

            "id_buku": id,

            "judul_buku": daftar_buku[id][
                "judul"
            ],

            "tanggal_peminjaman":
                tanggal_pinjam.strftime(
                    "%Y-%m-%d"
                ),

            "batas_pengembalian":
                batas_pengembalian.strftime(
                    "%Y-%m-%d"
                ),

            "status": "Dipinjam"
        })

        # -------------------------------------------------
        # STOK BERKURANG
        # -------------------------------------------------

        daftar_buku[id]["stok"] -= 1

        update_status_buku(id)

        return redirect(
            "/siswa/peminjaman"
        )

    return render_template(
        "pesan.html",
        buku=daftar_buku[id],
        error=None
    )


# =========================================================
# PEMINJAMAN SAYA
# =========================================================

@app.route("/siswa/peminjaman")
def siswa_peminjaman():

    if not sudah_login():
        return redirect("/")

    if not adalah_siswa():
        return redirect("/admin")

    username = session["username"]

    data_saya = []

    hari_ini = date.today()

    for data in peminjaman:

        if data["username"] == username:

            item = data.copy()

            batas = date.fromisoformat(
                data["batas_pengembalian"]
            )

            item["terlambat"] = (
                data["status"] == "Dipinjam"
                and hari_ini > batas
            )

            data_saya.append(item)

    return render_template(
        "siswa_peminjaman.html",
        peminjaman=data_saya,
        nama=session.get("nama"),
        kelas=session.get("kelas")
    )


# =========================================================
# JALANKAN PROGRAM
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)