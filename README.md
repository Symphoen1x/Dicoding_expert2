# Sistem Rekomendasi Program Studi Saintek Menggunakan Teknik Conten Based Filtering dan Collaborative Filtering.

## Project Overview
  Dalam menempuh pendidikan ke jenjang perguruan tinggi, bukanlah suatu perjalanan yang mudah untuk dihadapi, melainkan suatu perjalanan yang di dalamnya para mahasiswa akan menemui berbagai tantangan dan rintangan. Salah satu hal yang sering menjadi masalah di bagian awal adalah tidak mudahnya dalam memilih jurusan yang sesuai dengan diri sehingga banyak mahasiswa yang mengalami salah jurusan. Berdasarkan penelitian dari Youthmanual tentang profil mahasiswa di seluruh Indonesia bahwa hasil penelitian menunjukan fakta yang cukup menarik, yakni 92% mahasiswa tidak tahu akan menjadi apa kedepannya dan 45% mahasiswa merasa salah mengambil jurusan [[1]](http://www.skystarventures.com/youthmanual-angka-siswa-yang-salah-pilih-jurusan-masih-tinggi/). Penilitian lain dari Data Indonesia Career Center Network (ICCN) tahun 2017 mengungkapkan demikian bawha lebih dari 71,7% orang bekerja tidak linier dengan pendidikannya dan lebih dari 87% pelajar dan mahasiswa tidak sesuai dengan minatnya ketika mengambil jurusan di dunia pendidikan [[2]](https://indonesiacareercenter.id/). Kedua penelitian tersebut menunjukan bahwa para mahasiswa memiliki masalah dalam memilih jurusan yang disebabkan oleh beberapa faktor. Salah satu faktor yang bisa menjadi penyebab dari masalah tersebut adalah kurangnya eskplorasi data atau infromasi dari setiap jurusan bagi beberapa mahasiswa. Disamping itu, era saat ini yang penuh dengan infromasi dari berbagai sumber membuat beberapa mahasiswa bingung untuk memilih sumber mana yang akan dijadikan patokan dalam mengeskplorasi data atau informasi terkait program studi.
  
  Maka dari itu, sebuah sistem rekomendasi (recommendation system) diperlukan agar dapat memberikan rekomendasi jurusan masuk perguruan tinggi berdasarkan ketertarikan dan kebutukan dalam pencarian referensi. Dalam sistem rekomendasi, algoritma yang biasanya digunakan adalah **content based filtering(CB)** dan collaborative filtering (CF). Ide dari sistem rekomendasi **content based filtering(CB)** adalah merokomendasikan suatu item yang menggunakan deskripsi dari item tersebut. Cara kerjanya sendiri dengan mempelajari minat pengguna baru berdasarkan item yang mirip dengan yang disukai pengguna di masa lalu atau sedang dilihat di masa kini. Semakin banyak informasi yang diberikan pengguna maka akan semakin baik akurasi sistem rekomendasi [[3]](https://www.dicoding.com/academies/319/corridor). Berbeda dengan Collaborative filtering(CF), model ini  dibagi menjadi dua jenis, yaitu  Model-based (metode berbasis model *machine learning*) dan Memory-based (metode berbasis memori). Jenis Model-based tidak jauh algoritma Memory-based, yaitu tetap menggunakan nilai rating sebagai sumber data. Namun, algoritma ini memanfaatkan teknik-teknik di data mining atau machine learning seperti Bayesian, clustering, dan *Deep learning atau Neural Network* [[4]](https://journal.widyatama.ac.id/index.php/jitter/article/view/44). Sedangkan, pada jenis Memori-based terbagi lagi menjadi User-based Collaborative Filtering  dan Item-based Collaborative Filtering. User-based Collaborative Filtering atau user-based CF dan bekerja dengan menemukan kesamaan antar pengguna lalu model akan merekomendasikan selera yang sama dengan pengguna lain kepada pengguna tersebut [[5]](https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=Handrico%2C+A.+%22Sistem+rekomendasi+buku+perpustakaan+fakultas+sains+dan+teknologi+dengan+metode+collaborative+filtering%22.++Jurusan+teknik+informatika%2C+Fakultas+sains+dan+Teknologi+universitas+Islam+negeri+Sultan+Syarif+Kasim+Riau.+Pekanbaru&btnG=).  bekerja dengan cara menghitung kesamaan beberapa item [[6]](https://doi.org/10.30864/eksplora.v9i1.244).

  Rumpun program studi atau jurusan terbagi menjadi dua bagian, yaitu saintek dan soshum. Saintek atau sains dan teknologi berasal dari kelompok IPA, sedangkan soshum atau sosial dan humaniora berasal dari kelompok IPS.
Berdasarkan hasil riset dari jurnal RevoU pada tahun 2023 tentang pertumbuhan peminat jurusan saintek dan non-saintek atau Soshum di 10 kampus terbaik Indonesia, ada sebanyak 29 jurusan Saintek dan 21 jurusan non-saintek dengan persentase masing-masing 58% dan 42% dengan selisih 16% [[7]](https://journal.revou.co/pertumbuhan-program-studi-2023/). Penelitian lain juga memperkuat hasil tersebut bahwa data jumlah peminat mahasiswa jurusan saintek dan soshum dari tahun 2016-2020 di salah satu universitas yang ada di Indonesia menunjukan perbedaan pada jurusan saintek yang lebih unggul daripada jurusan soshum [[8]](https://www.researchgate.net/publication/352553378_ANALISIS_PROBABILITAS_PEMINAT_JURUSAN_SAINTEK_DI_UNIVERSITAS_JEMBER_TAHUN_2021_MENGGUNAKAN_METODOLOGI_DISTRIBUSI_POISSON). Kondisi ini menunjukan bahwa daya saing dan minat mahasiswa terhadap kedua pilihan jurusan tersebut hampir setara, tetapi peminat saintek sedikit unggul jumlahnya dari peminat non-saintek.  

Dapat diambil kesimpulan dari beberapa infromasi diatas bahwa sistem rekomendasi sangat diperlukan dalam rangka meminimalisasi terjadinya kasus mahasiswa salah jurusan karena banyaknya sumber informasi yang beredar terkait infromasi jurusan sehingga membuat para mahasiswa bingung untuk mengeksplorasinya. Kemudian dalam hal teknis, sistem rekomendasi yang akan dikembangkan menggunakan dua teknik, yaitu **content based filtering(CB)** dan collaborative filtering (CF). Terakhir, pengembangan sistem rekomendasi ini akan disesuaikan berdasarkan dua riset yang menunjukan saintek memiliki peminat yang lebih banyak dari pada jurusan soshum. Oleh karena itu, model sistem rekomendasi yang akan dibuat akan lebih spesifik menggunakan sampel data dari peminat jurusan saintek karena dilihat dari segi jumlahnya yang lebih banyak.
## Business Understanding
### 1. Problem Statements
Berdasarkan latar belakang yang telah diuraikan sebelumnya, sistem rekomendasi akan dikembangkan dalam bentuk model untuk menjawab dua permasalahan berikut:
* Bagaimana menciptakan sistem rekomendasi jurusan yang sesuai dengan preferensi mahasiswa?
* Dengan data rata-rata skor ujian yang dimiliki para mahasiswa, bagaimana cara merekomendasikan jurusan yang mungkin cocok dan belum pernah diketahui oleh mereka?
### 2. Goals
Untuk menjawab pertanyaan tersebut, sebuah model sistem rekomendasi akan dibuat dengan tujuan atau goals sebagai berikut:
* Menghasilkan sejumlah rekomendasi jurusan yang sesuai dengan preferensi mahasiswa dengan teknik content-based filtering(CB).
* Menghasilkan sejumlah rekomendasi jurusan yang sesuai dengan rata-rata skor ujian para mahasiswa dan belum pernah diketahui sebelumnya dengan teknik collaborative filtering(CF).
### 3. Solution Statements
Dalam rangka mencapai tujuan sebelumnya, yaitu menggunakan **Content Based Filtering** dan **Collaborative Filtering**, kedua teknik dipilih karena efektif dan solutif untuk model sistem rekomendasi. Model dengan **Content Based Filtering** akan merekomendasikan nama jurusan atau program studi yang sesuai dengan preferensi mahasiswa. Pada tahap ini, proses yang dilakukan diantaranya, representasi fitur penting dengan **TF-IDF (Term Frequency - Inverse Document Frequency) Vertorizer**, kalkulasi tingkat kesamaan (similarity measure) dengan **cosine similarity**, dan  rekomendasi top-N jurusan berdasarkan kesamaan yang telah dihitung sebelumnya. Sedangkan, Model **Collaborative Filtering** akan merekomendasikan sejumlah top jurusan atau program studi kepada pengguna(mahasiswa) berdasarkan nilai rata-rata yang telah diberikan sebelumnya. Dari data nilai pengguna tersebut akan muncul nama jurusan dan nama universitas yang mirip dan belum pernah diketahui oleh pengguna sebelumnya.


## Data Understanding
Data yang digunakan pada proyek ini diunduh dari platform Kaggle dengan nama [*Indonesia College Entrance Examination - UTBK 2019*](https://www.kaggle.com/datasets/ekojsalim/indonesia-college-entrance-examination-utbk-2019). Berdasarkan infromasi yang berasal dari sumber data, data yang dikumpulkan oleh Eko J. Salim diperoleh dari situs pemeringkatan tempat peserta ujian. Ada sekitar 147 ribu sampel (dari 1,1 juta jumlah skor total) dan data ini tidak menunjukkan keseluruhan 1,1 juta kumpulan data karena dikumpulkan dari sumber pihak ketiga (mungkin ada beberapa data yang tidak valid). Terdapat 4 buah dataset yang ada, tetapi yang digunakan dalam pengembangan model sistem rekomendasi kali ini hanya 3 buah. Ketiga dataset, yaitu major atau jurusan, score_science atau skor saintek, dan universities.
### 1. Variabel - variabel yang ada pada ketiga dataset *Indonesia College Entrance Examination - UTBK 2019* adalah sebagai berikut:
**Variabel pada dataset major**
Dataset major menyimpan data-data yang berkaitan dengan jurusan yang diidentifikasi memiliki primary key id_major. Pada dataset ini terdapat 3167 baris data dan 5 buah variabel, yakni:

* id_major: Merupakan kode unik yang digunakan untuk mengidentifikasi secara unik sebuah jurusan atau program studi dalam dataset.
* id_university: Merupakan kode unik yang digunakan untuk mengidentifikasi secara unik sebuah universitas dalam dataset.
* type: Variabel ini mungkin menggambarkan jenis atau kategori tertentu yang terkait dengan jurusan atau program studi, meskipun deskripsi spesifiknya tidak disediakan dalam penjelasan yang diberikan.
* major_name: Merupakan nama dari jurusan atau program studi.
* capacity: Merupakan kapasitas atau jumlah maksimum mahasiswa yang dapat diterima dalam jurusan atau program studi tersebut.

**Variabel pada dataset score_science**
Dataset score_science menyimpan data-data yang berkaitan dengan user beserta universitas dan jurusan yang dipilih. Dataset ini memiliki primary key id_user. Pada dataset ini terdapat 86570 baris data dan 11 buah variabel, yakni:
* id_major: Merupakan kode unik yang digunakan untuk mengidentifikasi secara unik sebuah jurusan atau program studi dalam dataset.
* id_university: Merupakan kode unik yang digunakan untuk mengidentifikasi secara unik sebuah universitas dalam dataset.
* id_user: Merupakan kode unik yang digunakan untuk mengidentifikasi secara unik seorang calon mahasiswa atau pengguna dalam dataset.
* score_bio: Merupakan skor yang diperoleh oleh pengguna dalam tes biologi.
* score_fis: Merupakan skor yang diperoleh oleh pengguna dalam tes fisika.
* score_kim: Merupakan skor yang diperoleh oleh pengguna dalam tes kimia.
* score_kmb: Merupakan skor yang diperoleh oleh pengguna dalam tes kemampuan memahami bacaan dan menulis.
* score_kpu: Merupakan skor yang diperoleh oleh pengguna dalam tes kemampuan penalaran umum.
* score_kua: Merupakan skor yang diperoleh oleh pengguna dalam tes kemampuan kuantitatif.
* score_mat: Merupakan skor yang diperoleh oleh pengguna dalam tes matematika.
* score_ppu: Merupakan skor yang diperoleh oleh pengguna dalam tes pengetahuan dan pemahaman umum.

**Variabel pada dataset universities**
Dataset universities menyimpan data-data yang berkaitan dengan infromasi universitas. Dataset ini memiliki primary key id_university. Pada dataset ini terdapat 85 baris data dan 2 buah variabel, yakni:
* id_university: Merupakan kode unik yang digunakan untuk mengidentifikasi secara unik sebuah universitas dalam dataset.
* university_name: Merupakan nama dari sebuah universitas.

## 2. Exploratory Data Analysis (EDA)
### Dataset Universitas
* Droping column

Tahap ini melibatkan penghapusan kolom atau variabel tertentu dari dataset. Kolom yang akan adalah sebuah kolom duplikasi dari id_univ sehingga tidak perlu digunakan secara ganda untuk tahapan analisis data. Selain itu, penghapusan kolom dilakukan untuk menyederhanakan dataset dan meningkatkan efisiensi komputasi.
* Check Characteristic Dataset
  
Tahap ini melibatkan pemeriksaan karakteristik atau sifat-sifat dari dataset. Ini mencakup informasi umum tentang dataset, seperti jumlah baris, tipe data dari setiap kolom, dan statistik deskriptif (misalnya, rata-rata, median, quartil, maks, min, dan standar deviasi). Memahami karakteristik dataset sangat penting untuk mempersiapkan analisis yang tepat dan mengidentifikasi masalah potensial dalam data. Pada datset univ, semua variabel yang telah dicek tidak menampilkan permasalahan. Jadi bisa dikatakan dataset ini cukup aman dari sumber data.
* Count Uniq Value
  
Tahap ini melibatkan menghitung jumlah nilai unik dalam suatu kolom atau variabel dalam dataset. Ini membantu dalam memahami variasi data dan distribusi nilai di dalamnya. Dengan menghitung nilai unik, kita dapat mengetahui seberapa bervariasi atau seberapa seragam data dalam suatu kolom. Pada kolom atau variabel universities, dataset menampilkan jumlah uniq dari beberapa variabel dengan keterangan jumlah uniq variabel id universitas dan nama universitas adalah 85.
### Dataset Program Studi
* Droping column
  
Tahap ini melibatkan penghapusan kolom atau variabel tertentu dari dataset. Kolom yang akan adalah sebuah kolom duplikasi dari id_major sehingga tidak perlu digunakan secara ganda untuk tahapan analisis data. Selain itu, penghapusan kolom dilakukan untuk menyederhanakan dataset dan meningkatkan efisiensi komputasi.
* Check Characteristic Dataset
  
Tahap ini melibatkan pemeriksaan karakteristik atau sifat-sifat dari dataset. Ini mencakup  informasi umum tentang dataset, seperti jumlah baris, tipe data dari setiap kolom, dan statistik deskriptif (misalnya, rata-rata, median, quartil, maks, min, dan standar deviasi). Memahami karakteristik dataset sangat penting untuk mempersiapkan analisis yang tepat dan mengidentifikasi masalah potensial dalam data. Pada dataset jurusan, semua variabel yang telah dicek juga tidak menampilkan permasalahan. Kembali lagi diambil kesimpulan bahwa dataset ini cukup aman dari sumber data.
* Count Uniq Value
  
Tahap ini melibatkan menghitung jumlah nilai unik dalam suatu kolom atau variabel dalam dataset. Ini membantu dalam memahami variasi data dan distribusi nilai di dalamnya. Dengan menghitung nilai unik, kita dapat mengetahui seberapa bervariasi atau seberapa seragam data dalam suatu kolom. Pada variabel major ini, dataset menampilkan jumlah uniq dari beberapa variabel dengan keterangan jumlah uniq id universitas adalah 85, uniq id major sebanyak  3167, dan uniq kapasitas sejumlah 143 baris.
### Dataset Score Science
* Droping column
  
Tahap ini melibatkan penghapusan kolom atau variabel tertentu dari dataset. Kolom yang akan adalah beberapa kolom duplikasi variabel lain sehingga tidak perlu digunakan untuk tahapan analisis data. Selain itu, penghapusan kolom dilakukan untuk menyederhanakan dataset dan meningkatkan efisiensi komputasi.
* Check Characteristic Dataset
  
Tahap ini melibatkan pemeriksaan karakteristik atau sifat-sifat dari dataset. Ini mencakup melihat informasi umum tentang dataset, seperti jumlah baris, tipe data dari setiap kolom, dan statistik deskriptif (misalnya, rata-rata, median, quartil, maks, min, dan standar deviasi). Memahami karakteristik dataset sangat penting untuk mempersiapkan analisis yang tepat dan mengidentifikasi masalah potensial dalam data. Pada dataset Score Science, semua variabel yang telah dicek juga tidak menampilkan permasalahan. Kembali lagi diambil kesimpulan bahwa dataset ini cukup aman dari sumber data.
* Count Uniq Value
  
Tahap ini melibatkan menghitung jumlah nilai unik dalam suatu kolom atau variabel dalam dataset. Ini membantu dalam memahami variasi data dan distribusi nilai di dalamnya. Dengan menghitung nilai unik, kita dapat mengetahui seberapa bervariasi atau seberapa seragam data dalam suatu kolom. Pada variabel major ini, dataset menampilkan jumlah uniq dari beberapa variabel dengan keterangan jumlah uniq id_university adalah 80, uniq id major sebanyak  1546, dan uniq id_user, dan sejumlah 86570. Dari dua dataset sebelumnya, jika dicocokan dengan datset ini maka ada sedikit perbedaan terkait jumlah variabel id_university dan id_major. Untuk itu, datset akan dilakukan teknik data cleaning pada tahap selanjutnya guna mengatasi masalah missing value.
* Count Mean of Specific Column
  
Karena syarat terkait kualifikasi nilai ujian yang diminta adalah rata-rata dari beberapa tes atau ujian maka  kolom baru yang berisi hasil rata-rata nilai ujian dari beberapa subtes akan dibuat. Beberapa subtes tersebut, yaitu Biologi(Bio),	Fisika(Fis),	Kimia(Kim),	Kemampuan Membaca dan Menulis(KMB),	Kemampuan Penalaran Umum(KPU),	Kemampuan Kuantitatif(Kua),	Matematika(Mat), dan	Pengetahuan dan Pemahaman Umum(PPU).
### Merge Third Column -Dataset Final
Tahap kali ini akan dilakukan percobaan menggabungkan ketiga dataset, yaitu major, score science dan universities. Percobaan pertama adalah penggabungan antara dataset major dengan science score berdasarkan kolom id_major. Kemudian dilanjut menggabungkan dataset hasil percobaan pertama dengan universities berdasarkan kolom id_university. Alasan dari penggabungan ketiga dataset tersebut agar informasi penting dari ketiga datset yang akan digunakan dapat disatukan secara lengkap.
### Filtering Irrelevant Values
Pada tahap ini, beberapa value dari kolom type mengandung jenis yang berbeda dengan tujuan bisnis, yaitu value *humanities*. Karena fokus di projek ini adalah data sampel jurusan saintek maka value tersebut akan dilakukan peng-fileteran untuk penanganan value tersebut.
### Removing Irrelevant Values
Pada tahap ini, penghapusan beberapa variabel yang kurang relevan dan telah diketahui dari tahap sebelumnya akan di hapus.
### Overcoming Missing Value
Setelah proses penggabungan Dataset, banyak baris yang menjadi missing value. Hal ini disebabkan adanya perbedaan baris data dari masing-masing dataset sehingga menimbulkan hilangnya beberapa baris data sehingga teridentifikasi missing value. Beberapa variabel yang mengandung missing value, yaitu type, major_name, capacity, id_university, dan university_name. Hanya variabel id_major, id_user, dan rata-rata nilai saja yang teridentifikasi memiliki 0 missing value. Alasan dilakukan tahap ini agar ketika pelatihan model nanti tidak terdapat informasi yang hilang sehingga model yang dihasilkan lebih optimal.
### Dropping Duplicated Columns
Proses "Dropping Duplicated Columns" dilakukan untuk menghapus kolom-kolom yang memiliki nilai yang sama di setiap barisnya. Tujuan utamanya adalah untuk membersihkan data dan menghilangkan redundansi, sehingga memungkinkan analisis data yang lebih akurat dan efisien. Kali ini variabel major_name terdeteksi mengandung duplikat data.
## Data Preparation - **Content Based Filtering**
### Convert Series-List Data
Tujuan dari proses ini untuk mengubah bentuk data yang awalnya berbentuk dataframe menjadi berbentuk list sehingga persyaratan pada input tahap TF-IDF Vectorizer terpenuhi. Proses ini akan menggunakan fungsi `tolist().
### Creating a Dictionary
Tujuan dari proses ini untuk membuat dictionary dari beberapa variabel dataset final. Proses ini akan menggunakan fungsi *DataFrame()* sebagai alat pembuatanya.

## Model Development -**Content Based Filtering**
Ide dari sistem rekomendasi content based filtering(CB) adalah merokomendasikan suatu item yang menggunakan deskripsi dari item tersebut. Cara kerja dari model ini dengan mempelajari minat pengguna baru berdasarkan item yang mirip dengan yang disukai pengguna di masa lalu atau sedang dilihat di masa kini. Semakin banyak informasi yang diberikan pengguna maka akan semakin baik akurasi sistem rekomendasi

Kelebihan teknik **Content Based Filtering**:
* Transparansi: Rekomendasi yang diberikan dapat dijelaskan dengan menganalisis fitur atau konten dari item yang disukai pengguna.
  
* Tidak Memerlukan Data dari Pengguna Lain: Rekomendasi dihasilkan hanya berdasarkan preferensi dan riwayat pengguna itu sendiri, sehingga tidak memerlukan data dari pengguna lain.
  
* Dapat Menangani Data Baru: Teknik ini dapat memberikan rekomendasi untuk item baru yang belum dirating oleh pengguna lain, selama item tersebut memiliki fitur atau konten yang serupa dengan item yang disukai pengguna.

Kekurangan teknik **Content Based Filtering**:
* Masalah Keterbatasan Analisis Konten: Analisis konten yang terbatas dapat menyebabkan rekomendasi yang kurang akurat, terutama untuk item-item yang memiliki fitur atau konten yang kompleks dan sulit dianalisis secara otomatis.
  
* Tidak Dapat Menangkap Preferensi yang Berubah: Teknik ini hanya merekomendasikan item-item yang serupa dengan item yang telah disukai pengguna di masa lalu, sehingga tidak dapat menangkap perubahan preferensi pengguna.
  
* Masalah Keberagaman Rekomendasi: Rekomendasi cenderung homogen dan kurang beragam karena hanya merekomendasikan item-item yang serupa dengan yang telah disukai pengguna.
### TF-IDF Vectorizer
Metode evaluasi ini, yang dikenal sebagai TF-IDF (Term Frequency-Inverse Document Frequency), bertujuan untuk menilai signifikansi suatu kata dalam konteks kata-kata lain dalam sebuah dokumen. Matematisnya, TF-IDF terdiri dari dua faktor: TF (Term Frequency) dan IDF (Inverse Document Frequency). TF mengukur seberapa sering sebuah kata muncul dalam sebuah teks, sementara IDF mengukur seberapa umum kata tersebut di seluruh dokumen. Panjang teks dapat bervariasi antar dokumen sehingga mempengaruhi cara perhitungan TF dan IDF. Maka dari itu, perhitungan TF-IDF penting dilakukan karena memberikan cara yang lebih cermat untuk mengevaluasi signifikansi suatu kata dalam sebuah dokumen daripada hanya menggunakan frekuensi kemunculan kata tersebut (seperti yang dilakukan dalam metode TF biasa).  Proses ini menggunakan fungsi ` TfidfVectorizer()`. Kemudian variabel *major_name* akan digunakan dalam perhitungan idf, mapping array dari fitur index integer ke fitur nama, dan  transfromasi fit ke bentuk matrix. Hasilnya adalah sebuah matrix dengan ukuran sebesar 1541 ukuran data x 220 jenis nama jurusan. Selanjutnya matrix dibentuk dengan menggunakan fungsi `todense()`. Proses ini bertujuan sebagai bahan untuk dapat diproses ke tahap berikutnya, yaitu menghitung tingkat kemiripan(Cosine Similarity)
### Cosine Similarity

Tujuan dari tahap Kesamaan cosinus adalah mengukur kesamaan antara dua vektor dan menentukan apakah mereka mengarah ke arah yang sama. Tahap kesamaan kosinus penting dalam model content-based filtering karena memberikan cara yang efektif untuk mengukur kesamaan antara dua vektor yang mewakili item-item dengan menghitung sudut kosinusnya. Semakin kecil sudut cosinusnya, semakin besar nilai kesamaan cosinus. Metrik ini sering digunakan untuk mengukur kesamaan dokumen dalam analisis teks. Sebelumnya, dataframe dibuat dengan nama `tfidf_matrix' untuk menghitung kesamaan cosinus antar id jurusan. Proses tersebut menggunakan fungsi `cosine_similarity()`. Hasil akhir dari proses ini adalah dataframe baru dengan nama 'df' yang berisi hasil hitung kesamaan cosinus antara variabel id major dengan id major.

### Presenting Top-N Recommendation
Pada tahap ini, fungsi yang dapat menghasilkan rekomendasi jursan akan dibuat dengan beberapa parameter yang terdiri dari parameter wajib 'id_major'(jurusan yang ingin dicari rekomendasinya) dan sisanya opsional, yaitu 'similarity_data'(Matriks kesamaan kosinus antar-jurusan yang telah dihitung sebelumnya), 'items'(DataFrame yang berisi informasi mengenai setiap jurusan, termasuk ID jurusan, nama universitas, dan nama jurusan), dan 'k'(Jumlah rekomendasi yang ingin diberikan. Ini adalah parameter opsional dengan nilai default 5). Fungsi ini berkerja dengan mengambil data melalui menggunakan fungsi `argpartition()` untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan, selanjutnya melakukan pengubahan data menjadi numpy dan membuat range yang terdiri dari `range(start, stop, step)`. Setelah itu, data akan diambil pada similarity terbesar dari index yang ada. Terdapat pula langkah menghapus id jurusan sehingga model tidak merekomendasikan nama jurusan yang sama dengan yang dimasukan pengguna/user melalui fungsi `drop()`. Hasil akhir dari fungsi ini adalah mengembalikan sebuah dataframe yang berisi 5 rekomendasi jurusan. Berikut tampilan input user dan hasil rekomendasi berdasarkan input tersebut:
- **Tabel 1. Data Jurusan dengan Id `3611476`** :

|index|id\_major|university\_name|major\_name|
|------:|------:|-----------------:|:------------|
|118|3611476|UNIVERSITAS GADJAH MADA|HIGIENE GIGI|

- **Tabel 2. 5 Rekomendasi Jurusan, Berdasarkan Target Jurusan dengan Id `3611476`**

|index|id\_major|university\_name|major\_name|
|------:|------:|-----------------:|:------------|
|0|3721305|UNIVERSITAS BRAWIJAYA|PENDIDIKAN DOKTER GIGI|
|1|1111181|UNIVERSITAS SYIAH KUALA|PENDIDIKAN DOKTER GIGI|
|2|6111262|UNIVERSITAS UDAYANA|PENDIDIKAN DOKTER GIGI|
|3|3511212|UNIVERSITAS JENDERAL SOEDIRMAN|PENDIDIKAN DOKTER GIGI|
|4|1711075|UNIVERSITAS SRIWIJAYA|PENDIDIKAN DOKTER GIGI|

Berdasarkan hasil rekomendasi dari tabel 2, rekomendasi jurusan dari id jurusan 3611476 dengan nama HIGIENE GIGI yang ada pada tabel 1 menghasilkan 5 jurusan yang serupa dengan keyword *gigi*.

## Data Preparation -**Collaborative Filtering**
### Encode Dataset
Mengubah variabel `id_user` dan 'id_major' menjadi list tanpa nilai dengan fungsi `unique()` dan `tolist()`. Setelah itu,  melakukan encoding ke masing-masing  variable yang telah diubah tersebut ke dalam indeks integer dan melakukan proses encoding angka ke masing-masing  variable yang telah diubah tersebut.
### Mapping Features
Selanjutnya, kedua variabel tadi akan disimpan ke variabel `user` dan `prodi` dan dilakukan pemetaan ke dataframe yang berkaitan. Langkah selanjutnya adalah mencari jumlah user, prodi, nilai minimum dan maksimum hasil rata-rata nilai tes mahasiswa. Hasilnya terdapat 1541 jumlah user dan jumlah prodi, 395.125 nilai min hasil rata-rata nilai tes, dan 758.0 nilai max hasil rata-rata nilai tes.
Tahap tersebut penting dilakukan dalam pemodelan data karena memberikan pemahaman yang lebih mendalam tentang karakteristik data yang akan digunakan dalam analisis atau pemodelan selanjutnya
### Split Data Training and Validation
Pada tahap ini, beberapa tindakan akan dilakukan. Pertama, urutan data dalam dataframe `df` akan diacak menggunakan metode `.sample()`. Ini akan dilakukan dengan mengambil seluruh baris (`frac=1`) dan memastikan hasil yang dapat direproduksi dengan menetapkan `random_state=42`. Setelah pengacakan, kolom 'user' dan 'prodi' akan dipisahkan sebagai fitur `x`, sementara kolom 'rata_rata_nilai' akan dinormalisasi sehingga nilainya berada dalam rentang antara 0 dan 1 menggunakan metode min-max scaling. Selanjutnya, data akan dibagi menjadi dua bagian: 80% untuk data latih dan 20% untuk data validasi. Akhirnya, hasil akhir dari proses ini akan menjadi data fitur `x` dan target `y`, yang siap untuk digunakan dalam proses pelatihan. Data latih dan data validasi akan dipisahkan sesuai dengan proporsi yang telah ditentukan.

## Model Development -**Collaborative Filtering**
Model **Collaborative Filtering(CF)** adalah pendekatan dalam sistem rekomendasi yang berfokus pada penggunaan perilaku pengguna terhadap item (produk atau layanan) serta perilaku pengguna lainnya untuk membuat rekomendasi. Model ini didasarkan pada ide bahwa pengguna yang memiliki preferensi atau perilaku serupa terhadap item-item tertentu cenderung memiliki preferensi yang serupa juga terhadap item lainnya. Pada projek ini model bekerja dengan menemukan jurusan-jurusan yang mirip dan tidak pernah diketahui oleh mahasiswa dengan mempertimbangkan preferensi user berdasarkan suatu nilai yang di input diawal.

**Kelebihan teknik Collaborative Filtering:**
* Tidak memerlukan informasi item: Collaborative filtering tidak memerlukan analisis konten atau metadata item, melainkan hanya menggunakan data interaksi pengguna (seperti rating atau perilaku) untuk memberikan rekomendasi.
* Dapat menemukan insight tersembunyi: Metode ini dapat menemukan pola atau hubungan tersembunyi antara pengguna dan item yang mungkin tidak terlihat secara eksplisit.
* Menggunakan sumber informasi yang kaya: Collaborative filtering memanfaatkan data interaksi dari seluruh komunitas pengguna, yang merupakan sumber informasi yang kaya dan sulit untuk diperoleh dengan cara lain.
  
**Kekurangan teknik Collaborative Filtering:**
* Masalah data jarang (sparsity): Pada dataset dengan banyak item dan sedikit interaksi, collaborative filtering dapat mengalami masalah dalam memberikan rekomendasi yang akurat.
* Masalah cold start: Metode ini sulit memberikan rekomendasi yang baik untuk pengguna atau item baru yang belum memiliki data interaksi sebelumnya.
* Escalasi preferensi populer: Collaborative filtering cenderung merekomendasikan item populer yang disukai oleh banyak pengguna, sehingga mengabaikan item niche atau kurang populer.

### Generate Class RecommenderNet
Pada tahap ini, kelas `RecommenderNet`akan didefinisikan sebagai model neural network untuk sistem rekomendasi. Model ini menggunakan embedding layers untuk merepresentasikan pengguna (mahasiswa) dan produk (prodi) dalam ruang fitur (embedding space). Setiap pengguna dan produk direpresentasikan sebagai vektor embedding dengan ukuran yang ditentukan oleh `embedding_size`. Embedding layers digunakan untuk mengekstraksi representasi vektor dari pengguna dan produk, sementara embedding bias layers digunakan untuk menangani bias yang terkait dengan setiap pengguna dan produk. Selanjutnya, dalam metode `call`, vektor embedding pengguna dan produk diambil dari embedding layers sesuai dengan input, kemudian dilakukan operasi dot product antara vektor pengguna dan produk. Hasilnya ditambahkan dengan bias pengguna dan bias produk, dan diaktifkan menggunakan fungsi sigmoid. Hasil akhirnya adalah probabilitas bahwa pengguna (mahasiswa) akan menyukai produk(prodi) tersebut.
### Complie Model
Pada tahap ini, model RecommenderNet yang telah didefinisikan sebelumnya akan dicompile melalui beberapa proses. Pertama, model diinisialisasi dengan menyediakan jumlah pengguna (num_user), jumlah produk (num_prodi), dan ukuran embedding (embedding_size) dibuat sebanyak 50 dan dijadikan argumen saat membuat objek model. Kemudian, model dikompilasi dengan menentukan fungsi kerugian (loss function), optimizer, dan metrik evaluasi yang akan digunakan selama pelatihan. Dalam hal ini, digunakan *BinaryCrossentropy* sebagai fungsi kerugian karena tugas ini adalah prediksi biner (pengguna menyukai atau tidak suka pada produk), Adam (*Adaptive Moment Estimation*) sebagai optimizer untuk mengoptimalkan fungsi kerugian, dan RootMeanSquaredError sebagai metrik untuk mengukur performa model selama pelatihan. Setelah kompilasi, model siap untuk dilatih dengan data
### Implement the Callbacks function
Kita menggunakan fungsi `ReduceLROnPlateau()` dan `EarlyStopping()` untuk meningkatkan efektivitas dan efisiensi proses pelatihan model. Melalui *callbacks* dinamis ini relatif model dapat mengecilkan nilai *learning rate* (kecepatan belajar) seiring pertambahan *epochs* sehingga memudahkan model menemukan titik optimal (konvergen) dalam mengeneralisasi data.
Pada tahap ini, dua callback didefinisikan untuk digunakan selama pelatihan model neural network. Pertama, ReduceLROnPlateau digunakan untuk mengurangi laju pembelajaran (learning rate) jika tidak terjadi peningkatan dalam nilai loss pada data validasi (val_loss) setelah beberapa epoch (patience). Faktor pengurangannya ditentukan oleh factor, sementara min_lr menentukan batas terendah untuk laju pembelajaran. Callback kedua, EarlyStopping, akan menghentikan pelatihan model jika tidak terjadi penurunan dalam nilai loss pada data validasi (val_loss) setelah beberapa epoch (patience). Hal ini membantu mencegah overfitting dan menghemat waktu pelatihan. restore_best_weights=True memastikan bahwa bobot model akan dikembalikan ke nilai terbaik saat pelatihan ketika pelatihan dihentikan.
### Training Model
Tahap ini adalah  pelatihan model neural network menggunakan metode `fit()` pada objek model yang telah dikompilasi sebelumnya. Data latih (`x_train` dan `y_train`) digunakan untuk melatih model dengan batch size sebesar 64 selama 100 epoch. Data validasi (`x_val` dan `y_val`) digunakan untuk memantau kinerja model selama pelatihan. Selama pelatihan, callback `reduce_lr` dan `early_stop` digunakan untuk mengurangi laju pembelajaran (learning rate) jika tidak terjadi peningkatan dalam nilai loss pada data validasi (val_loss) setelah beberapa epoch, serta untuk menghentikan pelatihan jika tidak terjadi penurunan dalam nilai loss pada data validasi (val_loss) setelah beberapa epoch. Hasil pelatihan disimpan dalam variabel `history` untuk analisis selanjutnya atau visualisasi.
### Presenting Top-N Recommendation
Pada tahap ini terdiri dari beberapa proses. Pertama, proses pengambilan sampel data secara acak dari dataframe 'df' dan mengekstraksi semua program studi (prodi) yang dipilih oleh pengguna tersebut. Kemudian, prodi-prodi yang tidak dipilih oleh pengguna tersebut diidentifikasi dan disaring untuk memastikan bahwa hanya prodi-prodi yang ada dalam kamus encode prodi yang dipertimbangkan. Selanjutnya, dilakukan pembuatan array yang berisi ID pengguna yang diulang sebanyak jumlah prodi yang tidak dipilih, serta ID prodi-prodi yang tidak dipilih. Array tersebut kemudian digunakan untuk memprediksi skor (rating/nilai pengguna) untuk setiap pasangan pengguna-prodi, dan 10 prodi dengan skor tertinggi dipilih sebagai rekomendasi. Rekomendasi tersebut kemudian ditampilkan bersama dengan prodi-prodi yang telah dipilih oleh pengguna untuk memberikan konteks lebih lanjut tentang preferensi pengguna tersebut.

Selanjutnya, terdapat beberapa langkah untuk memberikan rekomendasi program studi (prodi) kepada pengguna berdasarkan model collaborative filtering yang telah dilatih sebelumnya. Pertama, model digunakan untuk memprediksi skor (rating) untuk setiap pasangan pengguna-prodi yang tidak dipilih sebelumnya oleh pengguna. Kemudian, 10 prodi dengan skor tertinggi dipilih sebagai rekomendasi, dan ID prodi tersebut diubah kembali menjadi nama prodi. Selanjutnya, kode menampilkan prodi-prodi yang telah dipilih oleh pengguna, bersama dengan nama universitasnya, sebagai pembanding untuk rekomendasi yang diberikan. Terakhir, daftar 10 prodi yang direkomendasikan oleh model ditampilkan bersama dengan nama universitasnya untuk membantu pengguna dalam pengambilan keputusan. Proses ini memberikan pengguna gambaran yang lebih lengkap tentang pilihan prodi yang mungkin sesuai dengan preferensi mereka, serta memberikan alternatif yang relevan berdasarkan model collaborative filtering yang telah dilatih sebelumnya.

**Tabel 3. Input untuk user dengan id `8705` dan jurusan 'Fisika'** :

|index|id\_major|id\_user|rata\_rata\_nilai|type|major\_name|capacity|id\_university|university\_name|user|prodi|
|-----:|------------:|-------------:|:-----------|-------------:|:--------------|:---------------|:--------------|:---------------------------------|:------------|:------------|
|1549|3341046|8772|593\.125|science|PENDIDIKAN KIMIA|41\.0|334\.0|UNIVERSITAS PENDIDIKAN INDONESIA|661|661|

**Tabel 4. Hasil rekomendasi untuk user dengan id `8705` dan jurusan 'Fisika'** :

|index|id\_major|id\_user|rata\_rata\_nilai|type|major\_name|capacity|id\_university|university\_name|user|prodi|
|-----:|------------:|-------------:|:-----------|-------------:|:--------------|:-----------|:--------------|:---------------------------------|:------------|:------------|
|152|3531015|891|677\.5|science|KEDOKTERAN|110\.0|353\.0|UNIVERSITAS SEBELAS MARET|135|135|
|11990|1311016|58569|476\.5|science|FISIKA|48\.0|131\.0|UNIVERSITAS RIAU|1090|1090|
|2391|1311024|12885|553\.125|science|KIMIA|48\.0|131\.0|UNIVERSITAS RIAU|772|772|
|8773|3711261|44972|549\.0|science|PROTEKSI TANAMAN|25\.0|371\.0|UNIVERSITAS JEMBER|1043|1043|
|954|3721336|5939|614\.25|science|FARMASI|48\.0|372\.0|UNIVERSITAS BRAWIJAYA|527|527|
|6021|3621084|31881|562\.5|science|PENDIDIKAN TEKNIK ELEKTRO|32\.0|362\.0|UNIVERSITAS NEGERI YOGYAKARTA|973|973|
|3644|3621126|18463|582\.75|science|KIMIA|32\.0|362\.0|UNIVERSITAS NEGERI YOGYAKARTA|880|880|
|2549|3621173|13574|471\.875|science|ILMU KEOLAHRAGAAN|16\.0|362\.0|UNIVERSITAS NEGERI YOGYAKARTA|794|794|
|1484|3621134|8494|592\.625|science|BIOLOGI|32\.0|362\.0|UNIVERSITAS NEGERI YOGYAKARTA|647|647|
|1822|3531062|10376|622\.5|science|ILMU DAN TEKNOLOGI PANGAN|50\.0|353\.0|UNIVERSITAS SEBELAS MARET|702|702|

Dari gambar di atas terlihat, sistem menampilkan jurusan dengan skor yang sesuai dari input user. Sistem rekomendasi menampilkan 10 rekomendasi jurusan yang belum pernah diketahui user dan memiliki skor yang berada dibawah hingga diatas input user. Dengan demikian, user dapat melihat prodi apa yang sesuai dengan skor mereka berdasarkan rekomendasi skor dari minimum hingga maksimum. Harapanya
## Evaluation

### 1. Model **Content Based Filtering**
Berdasarkan hasil dari penggunaan teknik permodelan **Content Based Filtering** bahwa sistem rekomendasi dapat menghasilkan output rekomendasi yang cukup baik karena dari 5 hasil yang ada, semuanya hampir mirip dengan input user. Terlebih beberapa jurusan yang direkomendasikan memiliki kesamaan keyword, yaitu *gigi. Metrix yang akan digunakan adalah Recomender System Precision (RSP). Metrix ini mengukur seberapa relevan rekomendasi yang diberikan oleh sistem dengan preferensi pengguna yang sebenarnya. Maka dari itu, metrik ini sesuai dengan masalah dan solusi karena ingin memberikan rekomendasi yang sesuai/relevan.

Untuk Formula metrik Recomender System Precision (RSP) ini adalah sebagai berikut :

$$RSP = R_R/R_A$$

Ket :

$R_R$ = Jumlah rekomendasi yang relevan/terkait

$R_A$ = Jumlah keseluruhan rekomendasi model yang diprediksi


Cara kerja metrik ini adalah dengan membandingkan seberapa banyak prediksi model yang relevan atau sesuai dengan keseluruhan rekomendasi yang telah diberikan.

Berikut tampilan input user dan hasil rekomendasi berdasarkan input tersebut:
- **Tabel 1. Data Jurusan dengan Id `3611476`** :

|index|id\_major|university\_name|major\_name|
|------:|------:|-----------------:|:------------|
|118|3611476|UNIVERSITAS GADJAH MADA|HIGIENE GIGI|

- **Tabel 2. 5 Rekomendasi Jurusan, Berdasarkan Target Jurusan dengan Id `3611476`**

|index|id\_major|university\_name|major\_name|
|------:|------:|-----------------:|:------------|
|0|3721305|UNIVERSITAS BRAWIJAYA|PENDIDIKAN DOKTER GIGI|
|1|1111181|UNIVERSITAS SYIAH KUALA|PENDIDIKAN DOKTER GIGI|
|2|6111262|UNIVERSITAS UDAYANA|PENDIDIKAN DOKTER GIGI|
|3|3511212|UNIVERSITAS JENDERAL SOEDIRMAN|PENDIDIKAN DOKTER GIGI|
|4|1711075|UNIVERSITAS SRIWIJAYA|PENDIDIKAN DOKTER GIGI|


Hasil diatas menunjukan bahwa presisi dari sistem rekomendasi dengan teknik **Content Based Filtering** pada uji coba ini, yakni 5/5 = 100%.

### 2. Model Collaborative Filtering
Metrik Root Mean Squared Error (RMSE) dipilih untuk mengevaluasi seberapa baik model Collaborative Filtering dalam memberikan rekomendasi. Pemilihan metrik RMSE didasarkan pada konteks data yang menggunakan angka, yakni berdasarkan ratings, sehingga diperlukan penilaian seberapa baik model memprediksi nilai rating dengan kesalahan yang minimal. Terkait dengan konteks masalah dan solusi, yaitu pengembangan sistem rekomendasi berbasis rating pengguna secara efektif dan efisien, metrik ini dianggap sesuai karena bertujuan untuk mengurangi tingkat error sehingga sistem lebih efektif. Lebih lanjut, metrik RMSE memungkinkan interpretasi langsung karena mencerminkan rata-rata tingkat kesalahan yang sudah diakarkan.
.
Untuk Formula metrik Root Mean Squared Error (RMSE):

$$RMSE = \sqrt{\sum{(Y_t - Y_p)^2} \over n}$$

Ket :

$Y_t$ = Y true (Aktual/target)

$Y_p$ = Y predict (Prediksi)

n = jumlah data

Metrik Root Mean Squared Error (RMSE) bekerja dengan menghitung akar kuadrat dari rata-rata kuadrat selisih antara nilai prediksi dan nilai sebenarnya. Semakin kecil nilai RMSE, semakin baik model dalam memprediksi nilai, karena menunjukkan bahwa kesalahan prediksi model cenderung kecil. Ini membuat RMSE menjadi metrik yang berguna dalam mengevaluasi kualitas prediksi model regresi dan rekomendasi. Berikut hasil visualisasi metrix RMSE pada model sistem rekomendasi jurusan dengan teknik collaborative filltering.

![Pict RMSE](https://raw.githubusercontent.com/Symphoen1x/Dicoding_expert2/main/image.png)

Gambar 1.0 Hasil RMSE pada model Collaborative Filltering.

Hasil dari gambar tersebut menunjukan model *Collaborative Filtering* telah bekerja cukup lumayan karena cenderung memiliki eror yang kurang stabil. Tidak terlihat ada kendala seperti *overfitting* karena range selisih eror training dan validation sekitar 0.5-0.6 saja. Namun, Nilai RMSE 0,18 dan 0,19 menunjukkan bahwa model masih memiliki kesalahan prediksi yang cukup besar. Hal ini berarti model masih dapat dioptimasi lebih lanjut untuk meningkatkan akurasinya.


## Conclusion
Projek ini telah berhasil dibuat dengan beberapa tahapan yang cukup kompleks. Diawali dari project overview, buisness understanding, pembuatan model yang tahap-tahap, dan evaluasi model. Prblem statement yang diminta juga sudah selesai dibuat dan sesuai dengan tujuan yang melalui 2 teknik, yaitu **Collaborative Filtering** dan **Content Based Filtering**. Hasil dari keduanya cukup lumayan untuk menjadi sebuah sistem rekomendasi, tetapi perlu adanya optimasi lebih lanjut pada model agar menghasilkan rekomendasi jurusan yang lebih sesuai dan tepat.

## Reference

[1]. Putri, N. "Angka siswa yang salah pilih jurusan masih tinggi". Skystar Ventures. 2018.Tersedia: [tautan](http://www.skystarventures.com/youthmanual-angka-siswa-yang-salah-pilih-jurusan-masih-tinggi/).  Diakses pada 14 Maret 2024.

[2]. Indonesia Career Center Network. "Hasil penelitian ICCN(indonesia career center network)". ICCN. 2017. Tersedia: [tautan](https://indonesiacareercenter.id/).

[3]. Setiani, Tia Dwi. "Machine Learning Terapan". Dicoding. 2021. Tersedia: [tautan](https://www.dicoding.com/academies/319/corridor). Diakses pada 14 Maret 2024.

[4]. Eka, Angga Laksana. "COLLABORATIVE FILTERING DAN APLIKASINYA". Universitas Widyatama. 2014. Tersedia: [tautan](https://journal.widyatama.ac.id/index.php/jitter/article/view/44). Diakses pada 14 Maret 2024.

[5]. Handrico, A. "Sistem rekomendasi buku perpustakaan fakultas sains dan teknologi dengan metode collaborative filtering". Google Scholar. 2012. Tersedia: [tautan](https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=Handrico%2C+A.+%22Sistem+rekomendasi+buku+perpustakaan+fakultas+sains+dan+teknologi+dengan+metode+collaborative+filtering%22.++Jurusan+teknik+informatika%2C+Fakultas+sains+dan+Teknologi+universitas+Islam+negeri+Sultan+Syarif+Kasim+Riau.+Pekanbaru&btnG=). Diakses pada 14 Maret 2024.

[6]. Prasetyo Bondan, et al. "Implementasi Metode Item-Based Collaborative Filtering dalam Pemberian Rekomendasi Calon Pembeli Aksesoris Smartphone". Jurnal Eksplora Informatika. 2019. Tersedia: [tautan](https://eksplora.stikom-bali.ac.id/index.php/eksplora/issue/view/17). Diakses pada 14 Maret 2024.

[7]. Vazrina Putri. "Jurusan Kuliah dengan Pertumbuhan Mahasiswa Terbesar di Indonesia". RevoU. 2023. Tersedia: [tautan](https://journal.revou.co/pertumbuhan-program-studi-2023/). Diakses pada 14 Maret 2024.

[8]. Pragnata Galang, et al. "ANALISIS PROBABILITAS PEMINAT JURUSAN SAINTEK DI UNIVERSITAS JEMBER TAHUN 2021 MENGGUNAKAN METODOLOGI DISTRIBUSI POISSON". ResearchGate. 2021. Tersedia: [tautan](https://www.researchgate.net/publication/352553378_ANALISIS_PROBABILITAS_PEMINAT_JURUSAN_SAINTEK_DI_UNIVERSITAS_JEMBER_TAHUN_2021_MENGGUNAKAN_METODOLOGI_DISTRIBUSI_POISSON). Diakses pada 14 Maret 2024.
