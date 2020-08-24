# mp3bot

Diskteki müzik dosyalarını bulur, saklar ve tanınamaz hale getirir. Oluşturduğu rapor dosyasını kullanarak işlemi geri alabilirsiniz.

**Not:** Artık bu projeyi geliştirmiyorum, arşiv amacıyla koydum. İşinize yararsa alın kullanın 😊

## Neden böyle bir programa ihtiyaç duydum?

Okuduğum lisede akıllı tahtalar şifresizdi. Bazı öğrenciler müzik arşivlerini tahtaya yüklüyor ve teneffüslerde son ses müzik açıyorlardı. Müzik zevki konusunda çok seçici olan ben teneffüslerde [Mezdeke](https://www.youtube.com/watch?v=jDJK3E4b6Go) dinlemekten rahatsız oluyordum. Çıkışta müzikleri gizlice sildiğim olmuştu, ama her seferinde daha gizli klasörlere geri yüklemişlerdi. Ben de arka planda düzenli olarak (mesela 15 dakikada bir) çalışacak ve tüm müzikleri bulup ortadan kaldıracak bir *robot bekçi* hayal etmiştim.

## Neden doğrudan silmek yerine saklıyor?

Hatırladığım kadarıyla okul idaresi benimle aynı fikirde değildi. Teneffüste olduğu sürece bunda bir sorun görmüyorlardı. Bu durumda izinsiz yaptığım bir işlemi geri çevirememem başıma bela açabilirdi.

Ayrıca yükleyen öğrenci "bende o müziklerin yedeği yoktu", "orada manevi değeri olan müziklerim vardı", "sunumumda kullanacağım fon müziğini de silmişsin" gibi çıkışlarda bulunabilirdi.

## Sondaki "reborn"un anlamı ne?

O zamanlar bilgisayarda programlama yapmıyordum, MEB'in Fatih Projesi kapsamında dağıttığı tablette Pydroid3 üzerinde yapıyordum. Böylece okulda teneffüslerde ve boş derslerde (ve bazen beden eğitimi derslerinde 😅) programlama çalışabiliyordum ve evde özel bir vakit ayırmama gerek kalmıyordu.

mp3bot'u bitirdikten birkaç hafta sonra tablette durmasına gerek olmayan dosyaları bilgisayara aktarmaya karar verdim. Böylece mp3bot ve diğer kodlarım da daha güvende olacaktı. Tableti kabloyla bilgisayara bağladım, ama dosyaları aktarmaya başlamadan önce hatırlamadığım bir sebepten dolayı bilgisayarın başından kalktım. 5 dk kadar sonra geri döndüğümde ise bir şeyler yanlış gidiyordu, çünkü bilgisayardan bakınca tabletin içi bomboş görünüyordu. Başta kablonun bozuk olduğunu düşündüm, ama acı gerçek şuydu ki **tabletin dosya sistemi bozulmuştu**. Kendi kendine, ortada hiçbir sebep yokken.

O gün mp3bot'un yanı sıra birçok başka önemli dosyalarımı da kaybetmiştim. Moralim sıfıra düşmüştü. Kendi kendime "keşke daha önce yedekleseydim" diyordum.

Birkaç hafta sonra mp3bot'u sıfırdan, daha kısa sürede ve daha iyi şekilde yazmak bana teselli oldu. (Ve bu sefer biter bitmez Google Drive'a yedekledim.)

## Mutlu Son *(ya da öyle mi?)*

mp3bot-reborn'u bitirdikten (ve hatta unuttuktan) birkaç ay sonra ise önceki mp3bot'un geliştirilme aşamasındaki bir kopyasını buldum. O an gözlerim doldu.

## Dosyalar

- `mp3bot.py`: mp3bot-reborn'un son hali
- `sshs_mp3bot_v1.py`: Eski mp3bot'un tamamlanmadan önceki bir hali
- `pydene-mp3bot-edited.zip`: mp3bot'u test ederken kullandığım dosyalar (içinde gerçek müzikler vardı, telif haklarını ihlal etmemek için dosyaların içeriğini değiştirdim)

## İlginç bilgiler 😂

- mp3bot'u hiçbir zaman akıllı tahtada kullanmadım. 
- mp3bot hala düzenli olarak otomatik çalışma özelliğine sahip değil, elle çalıştırmak gerekiyor.
- O zamanlar `sys.argv`'den haberim yoktu. Normal ve geri alma modları arasında geçiş yapmak için kodu açıp `job` değişkeninin değerini değiştirmek gerekiyor.
- Tabletteki dosyalarımı kaybettiğim o günden sonra dosya aktarımı için kablo dışında bir yol araştırırken FTP ile tanıştım.

