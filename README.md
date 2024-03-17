# Sistem Rekomendasi Program Studi Saintek Menggunakan Teknik Conten Based Filtering dan Collaborative Filtering.

## Project Overview
  Dalam menempuh pendidikan ke jenjang perguruan tinggi, bukanlah suatu perjalanan yang mudah untuk dihadapi, melainkan suatu perjalanan yang di dalamnya para mahasiswa akan menemui berbagai tantangan dan rintangan. Salah satu hal yang sering menjadi masalah di bagian awal adalah tidak mudahnya dalam memilih jurusan yang sesuai dengan diri sehingga banyak mahasiswa yang mengalami salah jurusan. Berdasarkan penelitian dari Youthmanual tentang profil mahasiswa di seluruh Indonesia bahwa hasil penelitian menunjukan fakta yang cukup menarik, yakni 92% mahasiswa tidak tahu akan menjadi apa kedepannya dan 45% mahasiswa merasa salah mengambil jurusan [[1]](http://www.skystarventures.com/youthmanual-angka-siswa-yang-salah-pilih-jurusan-masih-tinggi/). Penilitian lain dari Data Indonesia Career Center Network (ICCN) tahun 2017 mengungkapkan demikian bawha lebih dari 71,7% orang bekerja tidak linier dengan pendidikannya dan lebih dari 87% pelajar dan mahasiswa tidak sesuai dengan minatnya ketika mengambil jurusan di dunia pendidikan [[2]](https://indonesiacareercenter.id/). Kedua penelitian tersebut menunjukan bahwa para mahasiswa memiliki masalah dalam memilih jurusan yang disebabkan oleh beberapa faktor. Salah satu faktor yang bisa menjadi penyebab dari masalah tersebut adalah kurangnya eskplorasi data atau infromasi dari setiap jurusan bagi beberapa mahasiswa. Disamping itu, era saat ini yang penuh dengan infromasi dari berbagai sumber membuat beberapa mahasiswa bingung untuk memilih sumber mana yang akan dijadikan patokan dalam mengeskplorasi data atau informasi terkait program studi.
  
  Maka dari itu, sebuah sistem rekomendasi (recommendation system) diperlukan agar dapat memberikan rekomendasi jurusan masuk perguruan tinggi berdasarkan ketertarikan dan kebutukan dalam pencarian referensi. Dalam sistem rekomendasi, algoritma yang biasanya digunakan adalah content based filtering(CB) dan collaborative filtering (CF). Ide dari sistem rekomendasi content based filtering(CB) adalah merokomendasikan suatu item yang menggunakan deskripsi dari item tersebut. Cara kerjanya sendiri dengan mempelajari minat pengguna baru berdasarkan item yang mirip dengan yang disukai pengguna di masa lalu atau sedang dilihat di masa kini. Semakin banyak informasi yang diberikan pengguna maka akan semakin baik akurasi sistem rekomendasi [[3]](https://www.dicoding.com/academies/319/corridor). Berbeda dengan Collaborative filtering(CF), model ini  dibagi menjadi dua jenis, yaitu  Model-based (metode berbasis model *machine learning*) dan Memory-based (metode berbasis memori). Jenis Model-based tidak jauh algoritma Memory-based, yaitu tetap menggunakan nilai rating sebagai sumber data. Namun, algoritma ini memanfaatkan teknik-teknik di data mining atau machine learning seperti Bayesian, clustering, dan *Deep learning atau Neural Network* [[4]](https://journal.widyatama.ac.id/index.php/jitter/article/view/44). Sedangkan, pada jenis Memori-based terbagi lagi menjadi User-based Collaborative Filtering  dan Item-based Collaborative Filtering. User-based Collaborative Filtering atau user-based CF dan bekerja dengan menemukan kesamaan antar pengguna lalu model akan merekomendasikan selera yang sama dengan pengguna lain kepada pengguna tersebut [[5]](https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=Handrico%2C+A.+%22Sistem+rekomendasi+buku+perpustakaan+fakultas+sains+dan+teknologi+dengan+metode+collaborative+filtering%22.++Jurusan+teknik+informatika%2C+Fakultas+sains+dan+Teknologi+universitas+Islam+negeri+Sultan+Syarif+Kasim+Riau.+Pekanbaru&btnG=).  bekerja dengan cara menghitung kesamaan beberapa item [[6]](https://doi.org/10.30864/eksplora.v9i1.244).

  Rumpun program studi atau jurusan terbagi menjadi dua bagian, yaitu saintek dan soshum. Saintek atau sains dan teknologi berasal dari kelompok IPA, sedangkan soshum atau sosial dan humaniora berasal dari kelompok IPS.
Berdasarkan hasil riset dari jurnal RevoU pada tahun 2023 tentang pertumbuhan peminat jurusan saintek dan non-saintek atau Soshum di 10 kampus terbaik Indonesia, ada sebanyak 29 jurusan Saintek dan 21 jurusan non-saintek dengan persentase masing-masing 58% dan 42% dengan selisih 16% [[7]](https://journal.revou.co/pertumbuhan-program-studi-2023/). Penelitian lain juga memperkuat hasil tersebut bahwa data jumlah peminat mahasiswa jurusan saintek dan soshum dari tahun 2016-2020 di salah satu universitas yang ada di Indonesia menunjukan perbedaan pada jurusan saintek yang lebih unggul daripada jurusan soshum [[8]](https://www.researchgate.net/publication/352553378_ANALISIS_PROBABILITAS_PEMINAT_JURUSAN_SAINTEK_DI_UNIVERSITAS_JEMBER_TAHUN_2021_MENGGUNAKAN_METODOLOGI_DISTRIBUSI_POISSON). Kondisi ini menunjukan bahwa daya saing dan minat mahasiswa terhadap kedua pilihan jurusan tersebut hampir setara, tetapi peminat saintek sedikit unggul jumlahnya dari peminat non-saintek.  

Dapat diambil kesimpulan dari beberapa infromasi diatas bahwa sistem rekomendasi sangat diperlukan dalam rangka meminimalisasi terjadinya kasus mahasiswa salah jurusan karena banyaknya sumber informasi yang beredar terkait infromasi jurusan sehingga membuat para mahasiswa bingung untuk mengeksplorasinya. Kemudian dalam hal teknis, sistem rekomendasi yang akan dikembangkan menggunakan dua teknik, yaitu content based filtering(CB) dan collaborative filtering (CF). Terakhir, pengembangan sistem rekomendasi ini akan disesuaikan berdasarkan dua riset yang menunjukan saintek memiliki peminat yang lebih banyak dari pada jurusan soshum. Oleh karena itu, model sistem rekomendasi yang akan dibuat akan lebih spesifik menggunakan sampel data dari peminat jurusan saintek karena dilihat dari segi jumlahnya yang lebih banyak.
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
## Merge Third Column -Dataset Final
Tahap kali ini akan dilakukan percobaan menggabungkan ketiga dataset, yaitu major, score science dan universities dengan fungsi merge(). Percobaan pertama adalah penggabungan antara dataset major dengan science score berdasarkan kolom id_major. Kemudian dilanjut menggabungkan dataset hasil percobaan pertama dengan universities berdasarkan kolom id_university dengan fungsi merge(). Alasan dari penggabungan ketiga dataset tersebut agar informasi penting dari ketiga datset yang akan digunakan dapat disatukan secara lengkap.
### Filtering Irrelevant Values
Pada tahap ini, beberapa value dari kolom type mengandung jenis yang berbeda dengan tujuan bisnis, yaitu value *humanities*. Karena fokus di projek ini adalah data sampel jurusan saintek maka value tersebut akan dilakukan peng-fileteran dengan fungsi isin().
### Removing Irrelevant Values
Pada tahap ini, penghapusan beberapa variabel yang kurang relevan dan telah diketahui dari tahap sebelumnya akan di hapus. 
### Overcoming Missing Value
Setelah proses penggabungan Dataset, banyak baris yang menjadi missing value. Hal ini disebabkan adanya perbedaan baris data dari masing-masing dataset sehingga menimbulkan hilangnya beberapa baris data sehingga teridentifikasi missing value. Beberapa variabel yang mengandung missing value, yaitu type, major_name, capacity, id_university, dan university_name. Hanya variabel id_major, id_user, dan rata-rata nilai saja yang teridentifikasi memiliki 0 missing value. Fungsi dropna akan digunakan dalam mengatasi missing value. Alasan dilakukan tahap ini agar ketika pelatihan model nanti tidak terdapat informasi yang hilang sehingga model yang dihasilkan lebih optimal.
### Dropping Duplicated Columns
Proses "Dropping Duplicated Columns" dilakukan untuk menghapus kolom-kolom yang memiliki nilai yang sama di setiap barisnya. Tujuan utamanya adalah untuk membersihkan data dan menghilangkan redundansi, sehingga memungkinkan analisis data yang lebih akurat dan efisien. Kali ini variabel major_name terdeteksi mengandung duplikat data.
## Data Preparation - Content Based Filtering
### Convert Series-List Data
Tujuan dari proses ini untuk mengubah bentuk data yang awalnya berbentuk dataframe menjadi berbentuk list sehingga persyaratan pada input tahap TF-IDF Vectorizer terpenuhi. Proses ini akan menggunakan fungsi `tolist().
### Creating a Dictionary
Tujuan dari proses ini untuk membuat dictionary dari beberapa variabel dataset final. Proses ini akan menggunakan fungsi *DataFrame()* sebagai alat pembuatanya.

## Model Development -Content Based Filtering
Ide dari sistem rekomendasi content based filtering(CB) adalah merokomendasikan suatu item yang menggunakan deskripsi dari item tersebut. Cara kerja dari model ini dengan mempelajari minat pengguna baru berdasarkan item yang mirip dengan yang disukai pengguna di masa lalu atau sedang dilihat di masa kini. Semakin banyak informasi yang diberikan pengguna maka akan semakin baik akurasi sistem rekomendasi

Kelebihan teknik Content Based Filtering:
* Transparansi: Rekomendasi yang diberikan dapat dijelaskan dengan menganalisis fitur atau konten dari item yang disukai pengguna.
  
* Tidak Memerlukan Data dari Pengguna Lain: Rekomendasi dihasilkan hanya berdasarkan preferensi dan riwayat pengguna itu sendiri, sehingga tidak memerlukan data dari pengguna lain.
  
* Dapat Menangani Data Baru: Teknik ini dapat memberikan rekomendasi untuk item baru yang belum dirating oleh pengguna lain, selama item tersebut memiliki fitur atau konten yang serupa dengan item yang disukai pengguna.

Kekurangan teknik Content Based Filtering:
* Masalah Keterbatasan Analisis Konten: Analisis konten yang terbatas dapat menyebabkan rekomendasi yang kurang akurat, terutama untuk item-item yang memiliki fitur atau konten yang kompleks dan sulit dianalisis secara otomatis.
  
* Tidak Dapat Menangkap Preferensi yang Berubah: Teknik ini hanya merekomendasikan item-item yang serupa dengan item yang telah disukai pengguna di masa lalu, sehingga tidak dapat menangkap perubahan preferensi pengguna.
  
* Masalah Keberagaman Rekomendasi: Rekomendasi cenderung homogen dan kurang beragam karena hanya merekomendasikan item-item yang serupa dengan yang telah disukai pengguna.
### TF-IDF Vectorizer
Metode evaluasi ini, yang dikenal sebagai TF-IDF (Term Frequency-Inverse Document Frequency), bertujuan untuk menilai signifikansi suatu kata dalam konteks kata-kata lain dalam sebuah dokumen. Matematisnya, TF-IDF terdiri dari dua faktor: TF (Term Frequency) dan IDF (Inverse Document Frequency). TF mengukur seberapa sering sebuah kata muncul dalam sebuah teks, sementara IDF mengukur seberapa umum kata tersebut di seluruh dokumen. Panjang teks dapat bervariasi antar dokumen sehingga mempengaruhi cara perhitungan TF dan IDF. Maka dari itu, perhitungan TF-IDF penting dilakukan karena memberikan cara yang lebih cermat untuk mengevaluasi signifikansi suatu kata dalam sebuah dokumen daripada hanya menggunakan frekuensi kemunculan kata tersebut (seperti yang dilakukan dalam metode TF biasa).  Proses ini menggunakan fungsi ` TfidfVectorizer()`. Kemudian variabel *major_name* akan digunakan dalam perhitungan idf, mapping array dari fitur index integer ke fitur nama, dan  transfromasi fit ke bentuk matrix. Hasilnya adalah sebuah matrix dengan ukuran sebesar 1541 ukuran data x 220 jenis nama jurusan. Selanjutnya matrix dibentuk dengan menggunakan fungsi `todense()`. Proses ini bertujuan sebagai bahan untuk dapat diproses ke tahap berikutnya, yaitu menghitung tingkat kemiripan(Cosine Similarity)
### Cosine Similarity

Tujuan dari tahap Kesamaan cosinus adalah mengukur kesamaan antara dua vektor dan menentukan apakah mereka mengarah ke arah yang sama. Tahap kesamaan kosinus penting dalam model content-based filtering karena memberikan cara yang efektif untuk mengukur kesamaan antara dua vektor yang mewakili item-item dengan menghitung sudut kosinusnya. Semakin kecil sudut cosinusnya, semakin besar nilai kesamaan cosinus. Metrik ini sering digunakan untuk mengukur kesamaan dokumen dalam analisis teks. Sebelumnya, dataframe dibuat dengan nama `tfidf_matrix' untuk menghitung kesamaan cosinus antar id jurusan. Proses tersebut menggunakan fungsi `cosine_similarity()`. Hasil akhir dari proses ini adalah dataframe baru dengan nama 'df' yang berisi hasil hitung kesamaan cosinus antara variabel id major dengan id major.

### Presenting Top-N Recommendation
Pada tahap ini, fungsi yang dapat menghasilkan rekomendasi jursan akan dibuat dengan beberapa parameter yang terdiri dari parameter wajib 'id_major'(jurusan yang ingin dicari rekomendasinya) dan sisanya opsional, yaitu 'similarity_data'(Matriks kesamaan kosinus antar-jurusan yang telah dihitung sebelumnya), 'items'(DataFrame yang berisi informasi mengenai setiap jurusan, termasuk ID jurusan, nama universitas, dan nama jurusan), dan 'k'(Jumlah rekomendasi yang ingin diberikan. Ini adalah parameter opsional dengan nilai default 5). Fungsi ini berkerja dengan mengambil data melalui menggunakan fungsi `argpartition()` untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan, selanjutnya melakukan pengubahan data menjadi numpy dan membuat range yang terdiri dari `range(start, stop, step)`. Setelah itu, data akan diambil pada similarity terbesar dari index yang ada. Terdapat pula langkah menghapus id jurusan sehingga model tidak merekomendasikan nama jurusan yang sama dengan yang dimasukan pengguna/user melalui fungsi `drop()`. Hasil akhir dari fungsi ini adalah mengembalikan sebuah dataframe yang berisi 5 rekomendasi jurusan.

Berikut hasil rekomendasi dari jurusan dengan target id jurusan `0155061224` :
|-----:|-----:|-------------:|:-----------|----------:|:---------|:-----------|:--------------|:------------|:------------|:------------|:---------------|:-------------|:-------------|:-----------|:-------------|--------------:|

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

Berdasarkan hasil rekomendasi dari tabel 2, rekomendasi jurusan dari id jurusan 3611476 dengan nama HIGIENE GIGI menghasilkan 5 jurusan yang serupa dengan keyword *gigi* dan *pendidikan*.

## Data Preparation - Collaborative Filtering

### Encode Dataset
Mengubah variabel `id_user` dan 'id_major' menjadi list tanpa nilai dengan fungsi `unique()` dan `tolist()`. Setelah itu,  melakukan encoding ke masing-masing  variable yang telah diubah tersebut ke dalam indeks integer dan melakukan proses encoding angka ke masing-masing  variable yang telah diubah tersebut.
### Mapping Features
Selanjutnya, kedua variabel tadi akan disimpan ke variabel `user` dan `prodi` dan dilakukan pemetaan ke dataframe yang berkaitan. Langkah selanjutnya adalah mencari jumlah user, prodi, nilai minimum dan maksimum hasil rata-rata nilai tes mahasiswa. Hasilnya terdapat 1541 jumlah user dan jumlah prodi, 395.125 nilai min hasil rata-rata nilai tes, dan 758.0 nilai max hasil rata-rata nilai tes.
Tahap tersebut penting dilakukan dalam pemodelan data karena memberikan pemahaman yang lebih mendalam tentang karakteristik data yang akan digunakan dalam analisis atau pemodelan selanjutnya
### Split Data Training and Validation
Tahap kali ini akan dilakukan beberapa tindakan. Pertama, dataframe `df` diacak menggunakan metode `.sample()` dengan menyertakan parameter `frac=1` untuk mengambil seluruh baris dan `random_state=42` untuk memastikan reproducibility. Kemudian, kolom 'user' dan 'prodi' dipisahkan sebagai fitur `x`, sementara kolom 'rata_rata_nilai' dinormalisasi ke rentang antara 0 dan 1 menggunakan formula min-max scaling. Data kemudian dibagi menjadi 80% data latih dan 20% data validasi. Hasil akhir dari pemrosesan ini adalah data fitur `x` dan target `y` yang siap untuk digunakan dalam proses training dengan data latih dan validasi yang terpisah sesuai dengan proporsi yang ditentukan.


## Model Development -Collaborative Filtering
Model Collaborative Filtering (CF) adalah pendekatan dalam sistem rekomendasi yang berfokus pada penggunaan perilaku pengguna terhadap item (produk atau layanan) serta perilaku pengguna lainnya untuk membuat rekomendasi. Model ini didasarkan pada ide bahwa pengguna yang memiliki preferensi atau perilaku serupa terhadap item-item tertentu cenderung memiliki preferensi yang serupa juga terhadap item lainnya. Pada projek ini model bekerja dengan menemukan jurusan-jurusan yang mirip dan tidak pernah diketahui oleh mahasiswa dengan mempertimbangkan preferensi user berdasarkan suatu nilai yang di input diawal. 

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
Pada tahap ini terdiri dari beberapa proses. Pertama, proses pengambilan sampel data sebagai target yang dicari.
Setelah sampel didapatkan maka akan dibuat sebuah variabel terkait jurusan yang sudah pernah dipilih user sebelumnya dan variabel terkait jurusan yang belum pernah diketahui user. Selanjutnya data akan dipersiapkan menjadi bentuk array sehingga dapat digunakan model. Model dilakukan pelatihan untuk memprediksi kemudian 

Kemudian kita menggunakan model yang telah dilatih untuk memberikan prediksi lalu mengumpulkan hasil prediksi model. Kemudian kita menampilkan hasil kepada user dalam bentuk 2 hal. Pertama terkait 5 buku yang memiliki rating tertinggi yang diberikan user. Kedua terkait 10 buku yang belum pernah dibeli user dan diperkirakan akan digemari user berdasarkan pertimbangan preferensi user (rating), preferensi ini menggunakan nilai median agar dapat melihat nilai rating tengah atau nilai rating yang dapat mewakilkan buku tersebut.

Berikut hasil rekomendasi untuk user id `185233` :

- **Books with High Ratings from User**

| No | ISBN | Book Author | Book Title | Rating |
|--|---|:---:|---|---|
| 1. | 043935806X | J. K. Rowling | Harry Potter and the Order of the Phoenix (Book 5) | 10.0 |
| 2. | 0307010368 | Little Golden Staff | Snow White and the Seven Dwarfs | 9.0 |
| 3. | 0812550544 | Michael Norman | Haunted America (Haunted America) | 10.0 |
| 4. | 0451169530 | Michael Norman | The Stand: Complete and Uncut | 10.0 |
| 5. | 078686382X | Deanna F. Cook | Disneys Family Cookbk-OS | 10.0 |


- **Top 10 Books Recommendation**

| No | ISBN | Book Author | Book Title | Rating |
|--|---|:---:|---|---|
| 1. | 0091842050 | Bradley Trevor Greive | The Blue Day Book: A Lesson in Cheering Yourself Up | 10.0 |
| 2. | 0394800389 | Dr. Seuss | Fox in Socks (I Can Read It All by Myself Beginner Books) | 10.0 |
| 3. | 0823401898 | Florence Parry Heide | The Shrinking of Treehorn | 10.0 |
| 4. | 1563891336 | Neil Gaiman | Death: The High Cost of Living | 10.0 |
| 5. | 3522128001 | Michael Ende | Die unendliche Geschichte: Von A bis Z | 10.0 |
| 6. | 0920668364 | Robert Munsch | Love You Forever | 9.5 |
| 7. | 0316779059 | Martha Sears | The Baby Book: Everything You Need to Know About Your Baby from Birth to Age Two | 9.0 |
| 8. | 1844262553 | Paul Vincent | Free | 9.0 |
| 9. | 2205054252 | Larcenet | Le Combat ordinaire, tome 1 | 9.0 |
| 10. | 0064440508 | Else Holmelund Minarik | A Kiss for Little Bear | 8.5 |



## Kelebihan dan Kekurangan Setiap Pendekatan


### Content Based Filtering

- **Kelebihan** : Model dapat memberikan rekomendasi yang serupa dengan buku yang telah kita beli sehingga relatif dapat membeli buku yang tepat dan telah terbukti diminati kita karena berdasarkan kemiripan judul buku di masa lalu.

- **Kekurangan** : Cenderung model hanya memberikan rekomendasi buku yang mirip atau relatif bukan buku yang unik.


### Collaborative Filtering

- **Kelebihan** : Model dapat memberikan rekomendasi yang lebih unik karena mempertimbangkan segi preferensi (rating) bukan konten yang pernah dibeli pengguna dan relatif masih disukai oleh konsumen karena memiilki rating serupa dengan buku yang pernah dibeli.

- **Kekurangan** : Cenderung model hanya memberikan rekomendasi buku unik dan kemungkinan tidak disukai konsumen karena belum terbukti diminati sebab tidak berdasarkan kemiripan judul buku di masa lalu.



## Evaluation

### 1. Model Content Based Filtering

Pertama pada model *Content Based Filtering* dapat dikatakan sudah sangat baik karena relatif 5 dari 5 rekomendasi yang diberikan sistem pada data sampel cenderung mirip karena memberikan rekomenedasi dengan keyword *Rites* dan *of Passage*. Kita menggunakan metrik *recomender system precision*. Metrik ini sesuai dengan konteks data kita yaitu teks karena berdasarkan judul buku sehingga perlu melihat apakah kata-kata antar judul mirip. Kemudian terkait konteks masalah dan solusi yaitu ingin menghasilkan sistem rekomendasi secara efektif karena judul yang diberikan relatif relevan dan efisien karena berbasis sistem sehingga cepat, jadi metrik ini sesuai dengan masalah dan solusi karena ingin meningkatkan ketepatan memberikan rekomendasi yang sesuai/relevan.

Formula metrik Recomender System Precision (RSP) ini adalah sebagai berikut :

$$RSP = R_R/R_A$$

Ket :

$R_R$ = Jumlah rekomendasi yang relevan

$R_A$ = Jumlah keseluruhan rekomendasi yang prediksi model


Cara kerja metrik ini adalah dengan membandingkan seberapa banyak prediksi model yang relevan atau sesuai dengan keseluruhan rekomendasi yang telah diberikan.

Berikut hasil rekomendasi dari buku dengan ISBN `0155061224` :

- **Data Buku `0155061224`** :

| No | ISBN | Book Author | Book Title |
|--|---|:---:|---|
| 1. | 0155061224 | Judith Rae	| Rites of Passage |


- **5 Rekomendasi Buku, Berdasarkan Konten Buku `0155061224`**

| No | ISBN | Book Author | Book Title |
|--|---|:---:|---|
| 1. | 0553580515 | Connie Willis | Passage |
| 2. | 0679435506 | Marianne Williamson | Illuminata: Thoughts, Prayers, Rites of Passage |
| 3. | 0380715325 | Alison McLeay | Passage Home |
| 4. | 0812510488 | Christopher Pike	 | The Season of Passage |
| 5. | 0373031203 | Rebecca Winters | Rites Of Love (Harlequin Romance, No 3120) |


Sehingga presisi sistem rekomendasi *Content Based Filtering* pada sampel ini adalah 5/5 = 100%.

### 2. Model Collaborative Filtering

Kedua pada model *Collaborative Filtering*, menggunakan metrik *Root Mean Squared Error (RMSE)* untuk mengevaluasi seberapa baik model dalam memberikan rekomendasi. Kita memilih metrik RMSE karena sesuai dengan konteks data kita yaitu angka karena berdasarkan ratings sehingga perlu melihat apakah model dapat memprediksi nilai rating dengan selisih kesalahan terkecil. Kemudian terkait konteks masalah dan solusi yaitu ingin menghasilkan sistem rekomendasi secara efektif karena berbasis rating pengguna dan efisien karena berbasis sistem sehingga cepat, jadi metrik ini sesuai dengan masalah dan solusi karena ingin mengecilkan tingkat error sehingga sistem lebih efektif. Selain itu, dengan metrik RMSE relatif dapat diinterpretasikan langsung karena merupakan nilai rata-rata tingkat kesalahan dan sudah diakarkan.

Formula metrik Root Mean Squared Error (RMSE) adalah sebagai berikut :

$$RMSE = \sqrt{\sum{(Y_t - Y_p)^2} \over n}$$

Ket :

$Y_t$ = Y true (Aktual)

$Y_p$ = Y predict (Prediksi)

n = jumlah data

Cara kerja metrik ini adalah dengan menyelisihkan nilai aktual dengan nilai prediksi lalu dikuadratkan kemudian ditotalkan dengan seluruh data dan selanjutnya dibagi dengan jumlah data, terakhir diakarkan.

![Hasil RMSE](https://user-images.githubusercontent.com/83503249/200128246-1ee97eb6-3d89-49e6-a551-9febbc4375d8.png)

Kalau kita lihat performa model *Collaborative Filtering* sudah bagus karena cenderung memiliki error yang menurun dan relatif sudah stabil seiring pertambahan epochs. Cenderung tidak *overfitting* karena selisih error antara training dan validasi masih wajar sekitar 0.06 atau 6% an. Selain itu, model dapat dikatakan lumayan *good fit* karena relatif sudah mencapai titik error optimal di angka 0.3-an, kemudian relatif hasil RMSE *training* dan validasi sudah baik untuk kasus sistem rekomendasi, merujuk pada modul "Machine Learning Terapan".


## Conclusion
Pada projek ini kita telah melalui berbagai tahapan mulai dari memahami ulasan proyek, memahami kasus bisnis yang ingin diselesaikan, lalu mencoba mengerti data yang ada, menyiapkan dataset, modeling hingga evaluasi. Kita juga telah berhasil menyelesaikan masalah bisnis dan mencapai tujuan yang ada melalui pembangunan model dengan 2 pendekatan yaitu **Content Based Filtering** dan **Collaborative Filtering**. Yang mana kedua pendekatan ini relatif dapat saling melengkapi dalam rangka mengoptimalkan performa sistem rekomendasi dalam memberikan rekomendasi yang efektif dan efisien. Harapannya melalui projek ini dapat memberikan manfaat bagi penulis dan pembaca secara luas. Sekian terima kasih telah membaca projek ini.


## Reference

[1]. Putri, N. "Angka siswa yang salah pilih jurusan masih tinggi". Skystar Ventures. 2018.Tersedia: [tautan](http://www.skystarventures.com/youthmanual-angka-siswa-yang-salah-pilih-jurusan-masih-tinggi/).  Diakses pada 14 Maret 2024.

[2]. Indonesia Career Center Network. "Hasil penelitian ICCN(indonesia career center network)". ICCN. 2017. Tersedia: [tautan](https://indonesiacareercenter.id/).

[3]. Setiani, Tia Dwi. "Machine Learning Terapan". Dicoding. 2021. Tersedia: [tautan](https://www.dicoding.com/academies/319/corridor). Diakses pada 14 Maret 2024.

[4]. Eka, Angga Laksana. "COLLABORATIVE FILTERING DAN APLIKASINYA". Universitas Widyatama. 2014. Tersedia: [tautan](https://journal.widyatama.ac.id/index.php/jitter/article/view/44). Diakses pada 14 Maret 2024.

[5]. Handrico, A. "Sistem rekomendasi buku perpustakaan fakultas sains dan teknologi dengan metode collaborative filtering". Google Scholar. 2012. Tersedia: [tautan](https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q=Handrico%2C+A.+%22Sistem+rekomendasi+buku+perpustakaan+fakultas+sains+dan+teknologi+dengan+metode+collaborative+filtering%22.++Jurusan+teknik+informatika%2C+Fakultas+sains+dan+Teknologi+universitas+Islam+negeri+Sultan+Syarif+Kasim+Riau.+Pekanbaru&btnG=). Diakses pada 14 Maret 2024.

[6]. Prasetyo Bondan, et al. "Implementasi Metode Item-Based Collaborative Filtering dalam Pemberian Rekomendasi Calon Pembeli Aksesoris Smartphone". Jurnal Eksplora Informatika. 2019. Tersedia: [tautan](https://eksplora.stikom-bali.ac.id/index.php/eksplora/issue/view/17). Diakses pada 14 Maret 2024.

[7]. Vazrina Putri. "Jurusan Kuliah dengan Pertumbuhan Mahasiswa Terbesar di Indonesia". RevoU. 2023. Tersedia: [tautan](https://journal.revou.co/pertumbuhan-program-studi-2023/). Diakses pada 14 Maret 2024.

[8]. Pragnata Galang, et al. "ANALISIS PROBABILITAS PEMINAT JURUSAN SAINTEK DI UNIVERSITAS JEMBER TAHUN 2021 MENGGUNAKAN METODOLOGI DISTRIBUSI POISSON". ResearchGate. 2021. Tersedia: [tautan](https://www.researchgate.net/publication/352553378_ANALISIS_PROBABILITAS_PEMINAT_JURUSAN_SAINTEK_DI_UNIVERSITAS_JEMBER_TAHUN_2021_MENGGUNAKAN_METODOLOGI_DISTRIBUSI_POISSON). Diakses pada 14 Maret 2024.
