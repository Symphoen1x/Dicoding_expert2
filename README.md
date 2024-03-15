# Sistem Rekomendasi Program Studi Saintek Menggunakan Teknik Pembuatan Model Conten Based Filtering dan Collaborative Filtering.

## Project Overview

## Business Understanding
- pengenalan/latar belakang
  
- riset terkait latar bealakang salah jurusan
Berdasarkan penelitian dari Youthmanual tentang profil mahasiswa di seluruh Indonesia bahwa hasil penelitian  menunjukan fakta yang cukup menarik, yakni 92% mahasiswa tidak tahu akan menjadi apa kedepannya dan 45% mahasiswa merasa salah mengambil jurusan. Penilitian lain dari Data Indonesia Career Center Network (ICCN) tahun 2017 mengungkapkan demikian bawha lebih dari 71,7% orang bekerja tidak linier dengan pendidikannya dan lebih dari 87% pelajar dan mahasiswa tidak sesuai dengan minatnya ketika mengambil jurusan di dunia pendidikan[]. 

- Jawaban solusi
Maka dari itu, sebuah sistem rekomendasi (recommendation system) diperlukan agar dapat memberikan rekomendasi jurusan masuk perguruan tinggi berdasarkan ketertarikan dan kebutukan dalam pencarian referensi. Dalam sistem rekomendasi, algoritma yang biasanya digunakan adalah collaborative filtering (CF) dan content based filtering(CB). Collaborative filtering(CF) dibagi menjadi dua jenis yaitu user-based CF dan item-based CF. User-based Collaborative Filtering atau user-based CF berasumsi bahwa cara yang baik dalam menemukan konten yang dirasa akan disukai oleh konsumen adalah dengan menemukan orang lain dengan ketertarikan yang sama dengan konsumen tersebut, kemudian merekomendasikan hal yang disukai oleh orang lain tersebut kepada konsumen (handrico, 2012). Item-based Collaborative Filtering berasumsi bahwa jika mayoritas pengguna memberi penilaian beberapa item secara serupa, pengguna yang kita targetkan juga akan memberi penilaian terhadap item-item tersebut secara serupa dengan mayoritas pengguna lain (Sarwar, 2001).. Berbeda dengan content-based filtering yang mana tidak seperti collaborative filtering yang menggunakan parameter semacam rating untuk menghasilkan rekomendasi. Melainkan menggunakan deskripsi dari profil pengguna, atau dari deskripsi suatu item untuk menghasilkan suatu rekomendasi (Ricci, 2011).

- riset tentnag solusi sistem rekomendasi
 
- riset peminat saintek dan kesimpulan
Berdasarkan hasil riset dari jurnal RevoU pada tahun 2023 tentang pertumbuhan peminat jurusan saintek dan non-saintek atau Soshum di 10 kampus terbaik Indonesia, ada sebanyak 29 jurusan saintek dan 21 jurusan non-saintek dengan persentase masing-masing 58% dan 42% dengan selisih 16% []. Kondisi ini menunjukan bahwa daya saing dan minat mahasiswa terhadap kedua pilihan jurusan tersebut hampir setara, tetapi peminat saintek sedikit unggul daripeminat non-saintek. Penelitian lain juga memperkuat hasil tersebut bahwa data jumlah peminat mahasiswa jurusan sanitek dan soshum dari tahun 2016-2020 di salah satu universitas yang ada di Indonesia menunjukan perbedaan pada jurusan saintek yang lebih unggul daripada jurusan soshum. Dapat diambil kesimpulan dari kedua riset tersebut bahwa saintek memiliki peminat yang lebih banyak dari pada jurusan soshum. Jika dikaitakn dengan masalah mahasiswa salah jurusan, project ini akan diarahkan pada penggunaan sampel jumlah peminat dari jurusan saintek. Oleh karena itu, sistem rekomendasi yang akan dibuat akan lebih spesifik terhadap peminat jurusan saintek.

[]. Vazrina Putri. "Jurusan Kuliah dengan Pertumbuhan Mahasiswa Terbesar di Indonesia". RevoU. 2023. Tersedia: [tautan](https://journal.revou.co/pertumbuhan-program-studi-2023/). Diakses pada 14 Maret 2024.

[]. Indonesia Career Center Network. "Hasil penelitian ICCN(indonesia career center network)". ICCN. 2017. Tersedia: [tautan](https://indonesiacareercenter.id/).

[]. Putri, N. "Angka siswa yang salah pilih jurusan masih tinggi". Skystar Ventures. 2018.Tersedia: [tautan](http://www.skystarventures.com/youthmanual-angka-siswa-yang-salah-pilih-jurusan-masih-tinggi/).  Diakses pada 14 Maret 2024.

[]. Pragnata Galang, et al. "ANALISIS PROBABILITAS PEMINAT JURUSAN SAINTEK DI UNIVERSITAS JEMBER TAHUN 2021 MENGGUNAKAN METODOLOGI DISTRIBUSI POISSON". ResearchGate. 2021. Tersedia: [tautan](https://www.researchgate.net/publication/352553378_ANALISIS_PROBABILITAS_PEMINAT_JURUSAN_SAINTEK_DI_UNIVERSITAS_JEMBER_TAHUN_2021_MENGGUNAKAN_METODOLOGI_DISTRIBUSI_POISSON).  Diakses pada 14 Maret 2024.

Handrico, A. (2012). Sistem
rekomendasi buku perpustakaan
fakultas sains dan teknologi dengan
metode collaborative filtering.
Jurusan teknik informatika, Fakultas
sains dan Teknologi universitas Islam
negeri Sultan Syarif Kasim
Riau. Pekanbaru

Ricci, F., Rokach, L., & Saphira, B.
(2010). Introduction to
recommender systems handbook. In
F. Ricci, L. Rokach, B. Saphira, & P. B. Kantor (Eds.), Recommender
systems handbook (pp. 1–29). New
York: Springer.

### 1. Problem Statements
* Berdasarkan data mengenai pengguna, bagaimana membuat sistem rekomendasi yang dipersonalisasi dengan teknik content-based filtering?
* Dengan data rating yang dimiliki, bagaimana perusahaan dapat merekomendasikan buku lain yang mungkin disukai dan belum pernah dikunjungi atau dibaca oleh pengguna?
* Sulitnya dalam memilih ataupun membeli laptop yang tepat dan sesuai keinginan. b) Dibutuhkannya suatu sistem yang dapat memberikan rekomendasi atau saran dalam memilih ataupun membeli laptop.
### 2. Goals
Untuk menjawab pertanyaan tersebut, perusahaan akan membuat sebuah sistem rekomendasi dengan tujuan atau goals sebagai berikut:

* Menghasilkan sejumlah rekomendasi buku yang dipersonalisasi untuk pengguna dengan teknik content-based filtering.
* Menghasilkan sejumlah rekomendasi buku yang sesuai dengan preferensi pengguna dan belum pernah dikunjungi atau dibaca sebelumnya dengan teknik collaborative filtering.


### 3. Solution Statements
Dalam rangka mencapai tujuan sebelumnya yaitu menghasilkan model yang efektif dan efisien. Saya mengajukan dua pendekatan solusi yaitu **Content Based Filtering** dan **Collaborative Filtering**. Kedua pendekatan ini dipilih karena relatif cukup populer dan dapat menjadi solusi yang saling melengkapi. Ide dari sistem rekomendasi berbasis konten (*content-based filtering*) adalah merekomendasikan item yang mirip dengan item yang disukai pengguna di masa lalu. *Collaborative filtering* bergantung pada pendapat komunitas pengguna. Ia tidak memerlukan atribut untuk setiap itemnya seperti pada sistem berbasis konten. Collaborative filtering dibagi lagi menjadi dua kategori, yaitu: model based (metode berbasis model *machine learning*) dan memory based (metode berbasis memori). Yang pada projek kali ini saya menerapkan metode berbasis model *machine learning* lebih spesifiknya *Deep learning atau Neural Network*. *Deep Learning* bekerja dengan membangun 3 tipe yaitu *input layer*, beberapa *hidden layer* dan *output layer* kemudian melakukan pembaruan bobot dsb agar menemukan pola yang optimal dalam mengeneralisasi data.



## Data Understanding
Data yang digunakan pada proyek ini adalah Book Recommendation Dataset yang diunduh dari platform Kaggle. Menurut informasi dari sumber dataset, data dikumpulkan oleh Cai-Nicolas Ziegler selama 4 minggu pada tahun 2004 dari komunitas Book-Crossing. Dataset ini berisi 278.858 pengguna (anonim tetapi dengan informasi demografis) yang memberikan 1.149.780 peringkat (secara eksplisit/implisit) tentang 271.379 buku.

### 1. Variabel - variabel pada Book Recommendation Dataset adalah sebagai berikut:
**Variabel pada dataset Books:**

ISBN : nomor ISBN (International Standard Book Number) dari buku.
Book-Title : judul buku.
Book-Author : nama penulis buku.
Year-Of-Publication : tahun publikasi buku.
Publisher : nama penerbit buku.
Image-URL-S : ukuran gambar small (kecil) dari buku berupa link URL.
Image-URL-M : ukuran gambar medium (sedang) dari buku berupa link URL.
Image-URL-L : ukuran gambar large (besar) dari buku berupa link URL.

**Variabel pada dataset Ratings:**

User-ID : kode unik untuk nama pengguna anonim yang memberikan penilaian.
ISBN : nomor ISBN (International Standard Book Number) dari buku.
Book-Rating : rating atau peringkat buku dari pengguna atau pembaca.
Variabel pada dataset Users:

User-ID : kode unik untuk nama pengguna anonim.
Location : lokasi pengguna.
Age : usia pengguna.


## 2. Exploratory Data Analysis (EDA)
### Dataset Universitas
Droping column
Check Characteristic Dataset
Count Uniq Value
### Dataset Program Studi
Droping column
Check Characteristic Dataset
Count Uniq Value
### Dataset Score Science
Count Mean of Specific Column

### Data Prepocessing
 Merge Third Column Dataset


## Data Preparation - Umum :

### Filtering Irrelevant Values

### Removing Irrelevant Values

### Overcoming Missing Value
Melalui proses penggabungan Data menimbulkan banyak baris yang menjadi missing value. Hal ini disebabkan adanya perbedaan identitas data buku sehingga menimbulkan diantara salah satu hilang (entah pada books atau rating) sehinga teridentifikasi missing value. Terdapat banyak missing value pada sebagian besar fitur. Hanya fitur `User-ID`, `ISBN`, dan `Book-Rating` atau `Book_Rating` saja yang memiliki 0 missing value. Selain itu, `Book-Title`, `Book-Author`, `Year-Of-Publication`, `Publisher`, `Image-URL-S`, `Image-URL-M`, dan `Image-URL-L`. Selanjutnya, kita membuang baris-baris yang meiliki missing value dengan fungsi `dropna()`. Alasan dilakukan proses ini agar ketika proses pelatihan model tidak terdapat informasi yang hilang sehingga menghasilkan model yang lebih optimal.
### Dropping Duplicated Columns


## Data Preparation - Content Based Filtering
### Convert Series-List Data
Proses ini dilakukan agar data yang awalnya berbentuk data frame berbentuk list. Proses ini dilakukan karena persyaratan input TF-IDF Vectorizer membutuhkan list. Proses ini menggunakan fungsi `tolist()`.

### Creating a Dictionary
untuk menentukan pasangan key-value pada data ISBN, Author, dan book_title yang telah kita siapkan sebelumnya. Proses ini menggunakan fungsi `DataFrame({})`.

## Model Development -Content Based Filtering

Model ini bekerja dengan melihat kemiripan suatu konten, dalam kasus ini konten yang dimaksud adalah judul buku. Model berusaha menghitung tingkat kemiripan antar judul buku dan memberikan kepada user tingkat kemiripan yang paling tinggi. Model ini menjadi solusi dalam menghasilkan sistem rekomendasi yang efektif dan efisien karena mempertimbangkan konten user dan hanya dalam hitungan detik dalam memberikan rekomendasi.
### TF-IDF Vectorizer
Teknik penilaian ini disebut TF-IDF, kepanjangan dari *Term Frequency-Inverse Document Frequency*. Ia bertujuan untuk mengukur seberapa penting suatu kata terhadap kata-kata lain dalam dokumen. Secara matematis, TF-IDF didefinisikan dengan dua besaran, yaitu TF dan IDF. TF (*Term Frequency*) mengukur frekuensi atau seberapa sering suatu kata atau term muncul dalam teks tertentu. Teks yang berbeda dalam dokumen mungkin memiliki panjang yang berbeda, tergantung dari panjang dokumen. Oleh karena itu, kita melakukan normalisasi dengan membagi jumlah kemunculan terhadap panjang dokumen. Proses ini menggunakan fungsi ` TfidfVectorizer()`. Kita menggunakan fitur judul buku (`book_title`) karena dirasa lebih relevan dalam memberikan rekomendasi (input `.fit()`)berdasarkan kemiripan, cenderung judul yang mirip relatif memiliki isi buku yang serupa pula. Berbeda dengan yang lainnya seperti nama penulis, misal nama penulis Joni dengan Jonis tentu lebih sering berbeda dari segi konten, judul dsb. Selanjutnya dilakukan fit baru ditransformasikan ke bentuk matrix dengan fungsi `fit_transform()` sehingga menghasilkan ukuran matrix sebesar 20000 adalah ukuran data dan 15924 adalah jenis Judul Buku. Setelah itu, untuk menghasilkan vektor tf-idf dalam bentuk matriks, kita menggunakan fungsi `todense()`. Proses ini diperlukan untuk dapat diproses ketahapan selanjutnya yaitu menghitung tingkat kemiripan.
### Cosine Similarity

Cosine similarity mengukur kesamaan antara dua vektor dan menentukan apakah kedua vektor tersebut menunjuk ke arah yang sama. Ia menghitung sudut cosinus antara dua vektor. Semakin kecil sudut cosinus, semakin besar nilai cosine similarity. Metrik ini sering digunakan untuk mengukur kesamaan dokumen dalam analisis teks. Sebagai contoh, dalam studi kasus ini, cosine similarity digunakan untuk mengukur kesamaan nama judul buku.
Proses ini menggunakan fungsi `cosine_similarity()` dari pustaka *sklearn*. Pada tahapan ini, kita menghitung *cosine similarity* dataframe `tfidf_matrix` yang kita peroleh pada tahapan sebelumnya. Dengan satu baris kode untuk memanggil fungsi cosine similarity dari library sklearn, kita telah berhasil menghitung kesamaan (*similarity*) antar restoran. Kode di atas menghasilkan keluaran berupa matriks kesamaan dalam bentuk array.

### Presenting Top-N Recommendation
Kita membuat fungsi yang dapat memberikan hasil rekomendasi. Fungai ini memiliki parameter yang terdiri dari wajib di isi dan tidak. Parameter yang wajib di isi adalah ISBN dan selain itu sudah terdapat nilai *default*. Parameter yang memiliki nilai *default* seperti similiraity_data yang menggunakan variabel yang telah dihitung pada tahap sebelumnya dengan nama `cosine_sim_df`, lalu parameter items yang akan memberikan hasil berupa informasi `ISBN`, `book_author`, dan `book_title`, kemudian parameter k yang merujuk pada berapa banyak rekomendasi yang ingin diberikan, secara *default* adalah 5. Cara kerja fungsi ini adalah Mengambil data dengan menggunakan `argpartition()` untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan, kemudian mengubah dataframe menjadi numpy dan membuat range yang terdiri dari `range(start, stop, step)`. Setelah itu, mengambil data dengan similarity terbesar dari index yang ada dan menghapus nama buku yang dimasukan oleh pengguna sehingga tidak merekomendasikan nama buku yang sama dengan yang dimasukan pengguna melalui fungsi `drop()`. Setelah itu akan mengembalikan dalam bentuk dataframe.

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



Dari gambar di atas terlihat kita ingin mencari rekomendasi dari buku yang berjudul **Rites of Passage** dan sistem kita sudah dapat merekomendasikan judul buku yang serupa, memberikan judul buku yang memiliki keyword *Rites* atau/dan *of Passage*.

## Data Preparation - Collaborative Filtering

### Encode Dataset
Mengubah `userID` menjadi list tanpa nilai yang sama dengan fungsi `unique()` dan `tolist()` serta menyimpannya dalam variabel `user_ids`. Setelah itu,  Melakukan encoding `user_ids` ke dalam indeks integer dan Melakukan proses encoding angka ke ke `user_ids`. Begitu juga dengan `ISBN`, Mengubah `ISBN` menjadi list tanpa nilai yang sama dengan fungsi `unique()` dan `tolist()` serta menyimpannya dalam variabel `books_ids`. Setelah itu,  Melakukan encoding `books_ids` ke dalam indeks integer dan Melakukan proses encoding angka ke ke `book_ids`.
### Mapping Features
Selanjutnya, memetakan `userID` dan `ISBN` ke dataframe yang berkaitan.
Mengecek beberapa hal dalam data seperti jumlah user sebesar 92106, jumlah buku sebesar 2701145, kemudian mengubah nilai rating menjadi float.

Tahap persiapan ini penting dilakukan agar data siap digunakan untuk pemodelan. Namun sebelumnya, kita perlu membagi data untuk training dan validasi terlebih dahulu yang akan kita pelajari di materi berikutnya.

### Split Data Training and Validation
Pertama kita mengacak dataset ini sebelum membagi data tersebut `sample(frac=1, random_state=42)`. Kemudian Membuat variabel x untuk mencocokkan data user dan books menjadi satu value. Lalu Membuat variabel y untuk membuat rating dari hasil Membagi menjadi 80% data train dan 20% data validasi.


## Model Development -Collaborative Filtering

Model ini bekerja dengan mengidentifikasi buku-buku yang mirip dan tidak pernah dibeli konsumen dengan mempertimbangkan preferensi pengguna berdasarkan rating yang telah diberikan sebelumnya. Model ini menjadi solusi dalam menghasilkan sistem rekomendasi yang efektif dan efisien karena mempertimbangkan preferensi pengguna dan hanya hitungan detik dalam memberikan rekomendasi.

### Generate Class RecommenderNet
Pada tahap ini, model menghitung skor kecocokan antara pengguna dan resto dengan teknik embedding. Pertama, kita melakukan proses embedding terhadap data user dan resto. Selanjutnya, lakukan operasi perkalian dot product antara embedding user dan resto. Selain itu, kita juga dapat menambahkan bias untuk setiap user dan resto. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid. Kita membuat class RecommenderNet dengan [keras Model class](https://keras.io/api/models/model/). Kode class RecommenderNet ini terinspirasi dari tutorial dalam situs [Keras](https://keras.io/examples/structured_data/collaborative_filtering_movielens/) dengan beberapa adaptasi sesuai kasus yang sedang kita selesaikan.
### Complie Model
Kita melakukan insiasai model menggunakan class RecommenderNet yang telah dibuat sebelumnya dengan variabel yang berisi jumlah user dan buku serta ukuran *embedding* yaitu 50. Setelah itu, melakukan *compile* model. Model ini menggunakan *Binary Crossentropy* untuk menghitung *loss function*, Adam (*Adaptive Moment Estimation*) sebagai *optimizer*, dan *root mean squared error* (RMSE) sebagai *metrics evaluation*.
### Implement the Callbacks function
Kita menggunakan fungsi `ReduceLROnPlateau()` dan `EarlyStopping()` untuk meningkatkan efektivitas dan efisiensi proses pelatihan model. Melalui *callbacks* dinamis ini relatif model dapat mengecilkan nilai *learning rate* (kecepatan belajar) seiring pertambahan *epochs* sehingga memudahkan model menemukan titik optimal (konvergen) dalam mengeneralisasi data.

### Training Model
Setelah model telah dibuat, compile dan inisiasi callbacks akan dilakukan pelatihan model dengan fungsi `fit()`. Yang mana mengisi parameter `x`, `y`, `batch_size = 64`, `epochs = 100`, `validation_data = (x_val, y_val)` dan `callbacks = [reduce_lr, early_stop]`.
### Presenting Top-N Recommendation
Kita mulai dengan megambil sampel data kita untuk sebagai contoh. Setelah mendapatkan sampelnya kita membuat variabel terkait buku yang sudah pernah dibeli user. Kemudian kita juga membuat variabel terkait buku yang belum pernah dibeli user. Kemudian mempersiapkan datanya menjadi bentuk array sehingga dapat diprediksi model. Kemudian kita menggunakan model yang telah dilatih untuk memberikan prediksi lalu mengumpulkan hasil prediksi model. Kemudian kita menampilkan hasil kepada user dalam bentuk 2 hal. Pertama terkait 5 buku yang memiliki rating tertinggi yang diberikan user. Kedua terkait 10 buku yang belum pernah dibeli user dan diperkirakan akan digemari user berdasarkan pertimbangan preferensi user (rating), preferensi ini menggunakan nilai median agar dapat melihat nilai rating tengah atau nilai rating yang dapat mewakilkan buku tersebut.

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

[1] Setiani, Tia Dwi. "Machine Learning Terapan". Dicoding. 2021. Tersedia: [tautan](https://www.dicoding.com/academies/319/corridor). Diakses pada 05 November 2022.

[2] Ricci, Francesco, et al. "Recommender Systems Handbook". Springer Media. 2011. Tersedia: [tautan](https://www.cse.iitk.ac.in/users/nsrivast/HCC/Recommender_systems_handbook.pdf). Diakses pada 05 November 2022
