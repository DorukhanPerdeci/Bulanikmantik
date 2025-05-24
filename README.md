# 🔥 Akıllı Oda İklim Kontrolörü

Bu proje, bir odanın ortam koşullarına göre **ısıtma gücünü** ve **havalandırma fan hızını** otomatik olarak ayarlayan, Python tabanlı bir **bulanık mantık kontrol sistemi** sunar. Sistem, sıcaklık, nem, CO₂ seviyesi, dış sıcaklık ve oda içindeki kişi sayısı gibi etmenleri analiz ederek karar verir.

---

## 🎯 Proje Amacı

Günlük yaşamda sıkça karşılaşılan iç ortam konforunu artırma ihtiyacına yönelik olarak geliştirilen bu uygulama, enerji tasarrufu ve hava kalitesini iyileştirmeyi hedefler. Manuel müdahale olmadan ortam koşullarına göre otomatik kontrol sağlar.


PROJE SONUÇ RAPORU
Proje Adı
Akıllı Oda İklim Kontrolü: Bulanık Mantık Tabanlı Isıtma ve Havalandırma Sistemi


Proje Sahibi
Ad Soyad: DORUKHAN PERDECİ           
Numara:21430070029
Bölüm: BİLİŞİM SİSTEMLERİ VE TEKNONOJİLERİ


Proje Amacı
Bu projenin amacı, oda içerisindeki çevresel faktörleri dikkate alarak iç ortam konforunu artıracak bir bulanık mantık kontrol sistemi tasarlamaktır. Sistem, sıcaklık, nem, insan sayısı, dış sıcaklık ve CO₂ seviyesine göre ısıtma düzeyi ve fan hızını otomatik olarak ayarlayacak şekilde geliştirilmiştir.
Kullanılan Yöntem ve Teknolojiler


- Python: Temel programlama dili olarak kullanıldı.
- Tkinter: Kullanıcı arayüzü oluşturmak için kullanıldı.
- Scikit-Fuzzy (skfuzzy): Bulanık mantık modelini kurmak için kullanıldı.
- NumPy / SciPy: Sayısal işlemler ve destekleyici hesaplamalar için.
Sistem Girdileri ve Çıktıları


Girdiler (Toplam 5):
1. Oda sıcaklığı (°C)
2. Nem seviyesi (%)
3. CO₂ seviyesi (ppm)
4. İnsan sayısı
5. Dış sıcaklık (°C)

Çıktılar (Toplam 2):
1. Isıtma düzeyi (%)
2. Fan hızı (%)

Uygulanan Algoritma
Sistem, bulanık mantık kontrolü (fuzzy logic) ile çalışmaktadır. Bulanık küme tanımları (düşük, orta, yüksek vb.) ve kurallar (IF–THEN) yardımıyla, insan benzeri kararlar verir.

Örnek Kurallar:
- Eğer oda sıcaklığı düşük VE dış sıcaklık çok düşükse, ISITMA yüksek olsun.
- Eğer CO₂ seviyesi yüksek VE nem yüksekse, FAN hızı yüksek olsun.
- Eğer oda sıcaklığı yüksek VE dış sıcaklık yüksekse, ISITMA düşük olsun.

  
Arayüz Tasarımı
Kullanıcı dostu bir Tkinter GUI arayüzü tasarlanmıştır:
- Girdiler kullanıcıdan alınır.
- Hesapla butonu ile anında çıktı alınır.
- Sonuçlar açık şekilde gösterilir.

  
Sonuçlar
Geliştirilen sistem test edilmiş ve aşağıdaki kazanımlar gözlenmiştir:
- Kullanılabilirlik: Arayüz sezgisel ve kolay.
- Gerçekçilik: Kurallar günlük yaşamla uyumlu.
- Esneklik: Yeni kurallar kolayca eklenebilir.
- Verimlilik: Konforu optimize eder.

  
Sonuç
Bu proje, bulanık mantık ile iç ortam konforunu optimize etmede başarılı olmuş, hem teknik hem kullanıcı dostu bir çözüm sunmuştur.
