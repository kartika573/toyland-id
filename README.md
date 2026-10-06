# Toyland.id — Website Bisnis & Company Profile
> **Tagline:** *"Play. Learn. Grow."*  
> **Konsep Bisnis:** Retail + Grosir + Reseller  
> **Tugas Mata Kuliah:** Digital Marketing  
> **Tahun:** 2026

---

## 🎯 1. Identitas & Ringkasan Bisnis

**Toyland.id** adalah bisnis retail mainan anak yang menyediakan aneka pilihan mainan edukatif untuk bermain, belajar, berkreasi, dan mendukung aktivitas tumbuh kembang anak usia **2–12 tahun**.

* **Model Bisnis:** Retail + Grosir + Reseller
* **Target Pasar:**
  * Orang tua dengan anak usia 2–12 tahun
  * Keluarga pencari kado/hadiah edukatif
  * Guru, PAUD, TK, dan institusi pendidikan anak
  * Reseller online & dropshipper
  * Toko retail kecil yang membutuhkan suplai mainan harga grosir
* **Kategori Produk Utama:**
  * Mainan Edukatif & Montessori
  * Puzzle Kayu
  * Building Blocks & Konstruksi Magnetik
  * Mainan Kreatif & Seni (Art & Craft)
  * Boneka & Figure Hewan
  * Diecast & Miniatur Kendaraan
  * Mainan Outdoor & Aktivitas Fisik
  * Flash Card Dwibahasa & Aksesori Anak

---

## 🚀 2. Target Pertumbuhan Bisnis (Strategic Target)

> ⚠️ **CATATAN AKADEMIK PENTING:**  
> Angka omzet **Rp1.000.000.000 (1 Miliar) per bulan** ditampilkan sebagai **TARGET BISNIS STRATEGIS DALAM 12 BULAN**, bukan sebagai omzet yang telah dicapai saat ini.

### Pernyataan Target:
> *"Target Toyland.id adalah mencapai omzet Rp1 miliar per bulan dalam 12 bulan melalui pengembangan penjualan online, toko fisik, grosir, reseller, dan strategi digital marketing terintegrasi."*

### Roadmap 5 Tahap Pertumbuhan:
1. **Bulan 1–3 (Brand & Online Foundation):** Peluncuran website resmi katalog, SEO organik, dan kampanye media sosial awal.
2. **Bulan 4–6 (Social Media & Marketplace):** Ekspansi Shopee Official Store, TikTok Shop, dan aktivasi Live Shopping harian.
3. **Bulan 7–8 (Retail Flagship Experience):** Pembukaan toko fisik/experience showroom ramah keluarga.
4. **Bulan 9–10 (Jaringan Grosir & Reseller):** Rekrutmen mitra reseller dan distribusi partai besar B2B se-Indonesia.
5. **Bulan 11–12 (Ekspansi Omnichannel):** Penetrasi penuh seluruh kanal menuju target omzet **Rp1.000.000.000/bulan**.

---

## 💻 3. Teknologi yang Digunakan

* **Frontend Framework:** React 18 (Component-based Architecture & Hooks)
* **Build & Dev Tool:** Vite
* **Styling:** Vanilla CSS (Custom Design System, Google Fonts *Poppins* & *Nunito*, Flexbox & CSS Grid, Responsive Mobile-First)
* **State Management & Storage:** React State + `localStorage` untuk keranjang belanja (cart)
* **Conversion Layer:** WhatsApp URL Generator (Pesan otomatis terformat rapi untuk retail & reseller)
* **Zero-Config Presentation Support:** Dilengkapi Babel Standalone & Python local server launcher agar dapat langsung dibuka dan dipresentasikan di komputer manapun tanpa instalasi tambahan.

---

## 🛠️ 4. Cara Menjalankan Website

Proyek ini telah dikonfigurasi agar dapat dijalankan dengan sangat mudah melalui 3 metode:

### ✅ CARA 1 (Paling Mudah — Menggunakan Python Local Server):
1. Masuk ke folder `toyland-id`.
2. Klik ganda (double click) file:
   ```
   jalankan-server.bat
   ```
3. Browser akan otomatis terbuka ke alamat: `http://localhost:8080`.
4. Website siap digunakan dan dipresentasikan di kelas!

### ✅ CARA 2 (Buka Langsung index.html):
1. Masuk ke folder `toyland-id`.
2. Klik ganda file:
   ```
   buka-website.bat
   ```
   *(Atau klik kanan `index.html` → Open with Google Chrome / Microsoft Edge).*

### ✅ CARA 3 (Menggunakan Node.js & Vite):
Jika komputer Anda memiliki Node.js terpasang:
```bash
cd toyland-id
npm install
npm run dev
```

---

## 📁 5. Struktur Direktori Proyek

```
toyland-id/
│
├── public/
│   └── images/                     # Aset foto visual & banner
├── images/                         # Mirror aset gambar untuk zero-config server
│
├── src/
│   ├── assets/                     # Aset styling & visual
│   ├── components/                 # Komponen Reusable
│   │   ├── Navbar.jsx              # Navigasi sticky, search, cart count & mobile drawer
│   │   ├── Footer.jsx              # Footer lengkap, branding, social media & disclaimer
│   │   ├── Hero.jsx                # Hero banner ceria & CTA utama
│   │   ├── ProductCard.jsx         # Card produk (foto, badge, rating, harga, tombol)
│   │   ├── CategoryCard.jsx        # Card 8 kategori utama dengan visual ikon
│   │   ├── PromoBanner.jsx         # Banner promo spesial & hemat
│   │   ├── Testimonial.jsx         # Testimoni pelanggan (diberi tanda data contoh)
│   │   ├── WhatsAppButton.jsx      # Floating WhatsApp action & quick popover
│   │   ├── ProductDetailModal.jsx  # Modal detail produk lengkap + WhatsApp inquiry
│   │   ├── CartDrawer.jsx          # Sidebar keranjang belanja + kuantitas
│   │   ├── CheckoutModal.jsx       # Simulasi checkout + format pesan WhatsApp otomatis
│   │   └── GrowthRoadmap.jsx       # Infografis Target Pertumbuhan Rp1 Miliar/Bulan
│   │
│   ├── pages/                      # Halaman Utama
│   │   ├── Home.jsx                # Beranda lengkap dengan 12 bagian terintegrasi
│   │   ├── About.jsx               # Company Profile, Visi, Misi, Transformasi Brand
│   │   ├── Products.jsx            # Katalog produk, live search, filter kategori/usia/harga
│   │   ├── Promo.jsx               # Paket bundling seru anak, flash sale, kode voucher
│   │   ├── Reseller.jsx            # Program Grosir & Reseller + Form pendaftaran ke WhatsApp
│   │   └── Contact.jsx             # Kontak resmi, info toko, dan formulir pesan
│   │
│   ├── data/
│   │   └── products.js             # Dataset 16 produk dummy, kategori, testimoni & roadmap
│   ├── utils/
│   │   └── formatters.js           # Format Rupiah & generator pesan otomatis WhatsApp
│   ├── App.jsx                     # Root application state & router sederhana
│   ├── main.jsx                    # Entry point React
│   ├── app.bundle.js               # Standalone bundle untuk zero-install browser runner
│   └── index.css                   # Design system lengkap, warna brand & animasi
│
├── index.html                      # HTML5 semantic, meta SEO, Open Graph & tracking placeholder
├── package.json                    # Konfigurasi dependensi React & Vite
├── vite.config.js                  # Konfigurasi bundler Vite
├── build-bundle.py                 # Skrip build bundler otomatis
├── buka-website.bat                # Shortcut buka langsung index.html
├── jalankan-server.bat             # Shortcut server lokal Python 8080
└── README.md                       # Dokumentasi lengkap proyek
```

---

## 📈 6. Penerapan Prinsip Digital Marketing

Website ini dirancang khusus untuk memenuhi standar tugas akademik mata kuliah Digital Marketing:

1. **Clear Call-to-Action (CTA):** Tombol aksi terdistribusi secara strategis di Hero, Katalog, Detail Produk, dan Banner Promo.
2. **Conversion Optimization:** Alur belanja disederhanakan dengan integrasi langsung ke WhatsApp untuk konfirmasi pesanan tanpa hambatan teknis.
3. **B2B & B2C Funneling:** Pemisahan segmen yang jelas antara pembeli retail dan mitra grosir/reseller dengan penawaran keuntungan margin yang transparan.
4. **Lead Magnet & Promosi:** Tersedia kode voucher promo (`TOYLANDCERIA`) dan penawaran paket bundling hemat untuk meningkatkan *Average Order Value (AOV)*.
5. **Technical SEO & Social Sharing:**
   * Meta Title & Meta Description teroptimasi
   * Open Graph (OG) tags & Twitter Card untuk preview media sosial yang memikat
   * Semantic HTML5 (`header`, `nav`, `main`, `section`, `footer`)
   * Alt text deskriptif pada semua gambar produk
6. **Analytics Ready (Placeholder Standar):**
   * Google Analytics: `GA_MEASUREMENT_ID`
   * Meta Pixel: `META_PIXEL_ID`
7. **Standarisasi Placeholder:**
   * `[NOMOR_WHATSAPP_TOYLAND]`
   * `[EMAIL TOYLAND]`
   * `[ALAMAT TOKO]`

---

## 🎓 7. Catatan Akademik & Hak Cipta

* Seluruh data produk, ulasan pelanggan, dan simulasi omzet disusun semata-mata untuk keperluan pemenuhan tugas akademik mata kuliah Digital Marketing.
* Hak Cipta & Desain: **© 2026 Toyland.id. All Rights Reserved.**
* Tagline: *"Play. Learn. Grow."*
