# 🔥 Akıllı Oda İklim Kontrolcüsü

Bu proje, bir odanın ortam koşullarına göre **ısıtma gücünü** ve **havalandırma fan hızını** otomatik olarak ayarlayan, Python tabanlı bir **bulanık mantık kontrol sistemi** sunar. Sistem, sıcaklık, nem, CO₂ seviyesi, dış sıcaklık ve oda içindeki kişi sayısı gibi etmenleri analiz ederek karar verir.

---

## 🎯 Proje Amacı

Günlük yaşamda sıkça karşılaşılan iç ortam konforunu artırma ihtiyacına yönelik olarak geliştirilen bu uygulama, enerji tasarrufu ve hava kalitesini iyileştirmeyi hedefler. Manuel müdahale olmadan ortam koşullarına göre otomatik kontrol sağlar.

✅ 1. Problem Ne?
İç ortam konforunu artırmak:

Oda sıcaklığı, nem, dış sıcaklık, insan sayısı ve CO₂ seviyesi gibi faktörlere göre,

Otomatik olarak ısıtma düzeyini ve fan hızını ayarlamak.

Bu, hem enerji verimliliği hem de yaşam konforu açısından günlük hayatta çok yaygın bir problemdir.

✅ 2. Algoritma: Bulanık Mantık Denetleyici
Proje şu şekilde çalışır:

Girdiler (5 tane):

Oda sıcaklığı

Nem seviyesi

CO₂ seviyesi

Oda içindeki insan sayısı

Dış ortam sıcaklığı

Kurallar (fuzzy logic ile):

Girdilere göre ısıtma ve fan hızını ayarlamak için IF–THEN tarzı bulanık kurallar uygulanır.

Örnek kural:Eğer oda sıcaklığı düşük VE insan sayısı fazla ise ISITMA yüksek olsun
Eğer CO₂ yüksek VE nem yüksekse FAN hızı yüksek olsun

✅ 3. Arayüz: Kullanıcı Dostu (Tkinter ile)
Arayüz gui.py içinde oluşturulmuştur ve Python’un Tkinter kütüphanesiyle yazılmıştır.

Girdiler kullanıcı tarafından kolayca elle girilir (input kutuları).

Sonuçlar, “Hesapla” butonuna basıldığında net bir şekilde alt tarafta gösterilir.

Her şey tek bir pencere üzerinde ve sade bir yapıyla tasarlanmıştır.


