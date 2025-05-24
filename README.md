# 🌡️ Akıllı Oda İklim Kontrolü (Fuzzy Logic Tabanlı)

Bu proje, **Python** programlama dili ve **bulanık mantık (fuzzy logic)** yaklaşımı ile geliştirilmiş, kullanıcı dostu bir **oda içi iklim kontrol sistemi** uygulamasıdır. Proje, ortam sıcaklığı, nem, dış sıcaklık, CO₂ seviyesi ve içerideki kişi sayısını göz önünde bulundurarak **ısıtma** ve **fan hızını** otomatik olarak ayarlamaktadır.

## 🚀 Proje Özellikleri

- 🔁 **Bulanık Mantık Sistemi:** 5 girdi – 2 çıktı yapısı ile çoklu çevresel faktöre göre kontrol.
- 🧠 **Gerçek Hayat Senaryosu:** Ortam konforunu optimize etmek üzere kurgulandı.
- 🖥️ **Kullanıcı Arayüzü (GUI):** Tkinter ile kolay ve sade bir arayüz.
- 🧪 **Kurallar Sistemi:** IF–THEN bulanık kurallarla mantıklı karar verme.
- 🔧 **Modüler Kodlama:** Genişletilebilir Python modülleri ile tasarım.

---

## 📥 Girdiler

Kullanıcıdan alınan giriş verileri şunlardır:

| Girdi | Açıklama |
|-------|----------|
| Oda Sıcaklığı (°C) | İç ortam sıcaklığı |
| Nem (%) | İç ortamdaki bağıl nem seviyesi |
| CO₂ Seviyesi (ppm) | Karbondioksit yoğunluğu |
| İnsan Sayısı | Odada bulunan kişi sayısı |
| Dış Sıcaklık (°C) | Dış ortam sıcaklığı |

---

## 📤 Çıktılar

Sistem aşağıdaki iki çıktıyı üretir:

- **Isıtma Düzeyi (%):** Oda sıcaklığını dengelemek için gereken ısıtma oranı.
- **Fan Hızı (%):** Havanın temizliği ve serinliği için gerekli fan hızı.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|-----------|----------|
| Python | Projenin temel programlama dili |
| Tkinter | Grafiksel kullanıcı arayüzü (GUI) için |
| Scikit-Fuzzy | Bulanık mantık işlemleri için |
| NumPy / SciPy | Sayısal işlemler ve modelleme |

---

## 🖥️ Arayüz Özellikleri

- Kullanıcıdan giriş değerlerini alır.
- “Hesapla” butonu ile anında çıktı verir.
- Çıktılar arayüzde sade şekilde gösterilir.
- Girişler değiştirilerek sistem kolayca yeniden hesaplama yapabilir.

---

## 🔍 Örnek Kullanım

1. Arayüzü açın.
2. Giriş kutucuklarına değerleri girin (örn. sıcaklık: 18°C, nem: 70%).
3. “Hesapla” tuşuna tıklayın.
4. Sonuçlar (ısıtma düzeyi, fan hızı) anında gösterilecektir.

---

## 🧠 Örnek Kurallar

- Eğer **oda sıcaklığı düşük** ve **dış sıcaklık çok düşükse**, ısıtma **yüksek** olmalıdır.
- Eğer **CO₂ seviyesi yüksek** ve **nem de yüksekse**, fan hızı **yüksek** olmalıdır.
- Eğer **oda sıcaklığı yüksek** ve **dış sıcaklık yüksekse**, ısıtma **düşük** olmalıdır.

---



