# Laporan Praktikum #2 – FSM String Validator

**Mata Kuliah**: Otomata <br>
**Semester**: Genap 2025/2026 <br>
**Kelompok**: B03

**Anggota:**

* Berwyn Rafif Alvaro (5025241029)
* Mahendra Agung Darmawan (5025241032)
* Agil Lukman Hakim Muchdi (5025241037)

---

## 1. Pendahuluan

### 1.1 Latar Belakang

Finite State Machine (FSM) adalah model komputasi dalam teori bahasa formal dan automata. FSM digunakan untuk mengenali pola tertentu dalam sebuah string. Pada praktikum ini, FSM digunakan untuk memvalidasi apakah sebuah string biner termasuk dalam bahasa tertentu.

### 1.2 Tujuan

* Mengimplementasikan FSM dalam program Python
* Menentukan apakah string termasuk bahasa tertentu
* Menampilkan trace perpindahan state
* Membuat antarmuka sederhana berbasis CLI

### 1.3 Ruang Lingkup

* Alfabet: `{0,1}`
* State: `S, A, B, C`
* Input hanya berupa string biner

---

## 2. Dasar Teori

### 2.1 Finite State Machine

FSM didefinisikan sebagai:

```
M = (Q, Σ, δ, q0, F)
```

* Q = himpunan state
* Σ = alfabet
* δ = fungsi transisi
* q0 = state awal
* F = state penerima

---

### 2.2 Bahasa Formal

Bahasa yang dikenali:

* String berakhir dengan `1`
* Tidak mengandung substring `00`

---

### 2.3 State FSM

| State | Deskripsi      | State Penerima |
| ----- | -------------- | ------ |
| S     | Start          |   Tidak    |
| A     | Setelah baca 0 | Tidak      |
| B     | Setelah baca 1 | Ya      |
| C     | Trap (00)      | Tidak      |

---

## 3. Perancangan Program

### 3.1 Arsitektur

* FSM Simulator (`cek_fsm`)
* Validator Input
* Loop interaktif

---

### 3.2 Tabel Transisi

| State | 0 | 1 |
| ----- | - | - |
| S     | A | B |
| A     | C | B |
| B     | A | B |
| C     | C | C |

---

### 3.3 Alur Program

1. Mulai dari state S
2. Baca tiap karakter
3. Update state
4. Simpan history
5. Tentukan hasil

---

## 4. Implementasi

### 4.1 Lingkungan

* Python 3.x
* Google Colab
* CLI berbasis input

---

### 4.2 Struktur Program

* Fungsi `cek_fsm()`
* Loop utama untuk input user

---

### 4.3 Fitur

* Validasi input
* Trace state
* Penjelasan alasan penolakan
* Loop interaktif

---

## 5. Hasil Pengujian

### String Diterima

| Input | Trace         | Hasil    |
| ----- | ------------- | -------- |
| 1     | S → B         | DITERIMA |
| 01    | S → A → B     | DITERIMA |
| 101   | S → B → A → B | DITERIMA |

---

### String Ditolak

| Input | Alasan                  |
| ----- | ----------------------- |
| 0     | Tidak berakhir dengan 1 |
| 001   | Mengandung 00           |
| 10    | Tidak berakhir dengan 1 |
| 10a   | Input tidak valid       |

---

## 6. Pembahasan

### 6.1 Keunggulan

* Implementasi sederhana
* Mudah dipahami
* Trace informatif
* Penjelasan error jelas

---

### 6.2 Kompleksitas

* Waktu: **O(n)**
* Ruang: **O(n)**

---

## 7. Kesimpulan

* FSM berhasil diimplementasikan
* Program mampu mengenali bahasa dengan benar
* State trap efektif mendeteksi substring `00`
* Kompleksitas efisien

---

## Lampiran

### 📎 Google Colab

👉 https://colab.research.google.com/drive/1ekEuuJI4ZU4-ykZBc-IKXJGD3FsHpZgv?usp=sharing

---

### Source Code

```python
def cek_fsm(s):
    state = 'S'
    history = ['S']
    alasan = ""

    for c in s:
        if c not in ['0', '1']:
            return "Input tidak valid"

        if state == 'S':
            state = 'A' if c == '0' else 'B'
        elif state == 'A':
            if c == '0':
                state = 'C'
                alasan = "mengandung substring '00'"
            else:
                state = 'B'
        elif state == 'B':
            state = 'A' if c == '0' else 'B'
        elif state == 'C':
            state = 'C'

        history.append(state)

    result = " -> ".join(history)

    if state == 'B':
        return f"TRACE FSM:\n{result}\nDITERIMA"
    else:
        return f"TRACE FSM:\n{result}\nDITOLAK\nAlasan: {alasan if alasan else 'tidak berakhir dengan 1'}"
```

---
