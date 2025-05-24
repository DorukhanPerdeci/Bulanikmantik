# 🔥 Smart Room Climate Controller

Bu proje, bir odanın ortam koşullarına göre **ısıtma gücünü** ve **havalandırma fan hızını** otomatik olarak ayarlayan, Python tabanlı bir **bulanık mantık kontrol sistemi** sunar. Sistem, sıcaklık, nem, CO₂ seviyesi, dış sıcaklık ve oda içindeki kişi sayısı gibi etmenleri analiz ederek karar verir.

---

## 🎯 Proje Amacı

Günlük yaşamda sıkça karşılaşılan iç ortam konforunu artırma ihtiyacına yönelik olarak geliştirilen bu uygulama, enerji tasarrufu ve hava kalitesini iyileştirmeyi hedefler. Manuel müdahale olmadan ortam koşullarına göre otomatik kontrol sağlar.

---

## 🔍 Özellikler

- **5 Girdi:**
  - Oda Sıcaklığı (°C)
  - Nem Seviyesi (%)
  - Karbon Dioksit (CO₂) Seviyesi (ppm)
  - Oda İçindeki İnsan Sayısı
  - Dış Sıcaklık (°C)

- **2 Çıktı:**
  - Isıtma Düzeyi (%)
  - Fan Hızı (%)

- Kullanıcı dostu arayüz (Tkinter ile)
- Python ile geliştirilmiş, modüler yapı
- Fuzzy Logic sistemiyle karar verme yeteneği

📌 Kullanım Açıklaması
Program açıldığında kullanıcıdan aşağıdaki değerler istenir:

Oda sıcaklığı (°C)

Nem oranı (%)

CO₂ seviyesi (ppm)

Oda içindeki kişi sayısı

Dış ortam sıcaklığı (°C)

Bu bilgiler girildikten sonra “Hesapla” butonuna basıldığında sistem, bulanık mantık kurallarına göre ısıtma düzeyi ve fan hızı sonuçlarını ekrana yazdırır.


