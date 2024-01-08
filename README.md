# Kas īsti ir šis repozitorijs:
Tas ir mans gala projekts Python kursā.
Šeit es izstrādāšu mākslīgo intelektu, kurš spēs atšķirt kaķu un suņu bildes.
Es pirmo reizi kaut ko šādu darīšu, taču neskatoties uz to, ka man nav praktiska pieredze dziļā mašīnmācīšanā, es tik un tā ļoti vēlos izstrādāt tādu visai vienkāršu modeli, kurš ir trenēts arī ne uz visai lielu datu kopu.

## Kur es ņēmu datu kopu:
Ņēmu datu kopu no https://www.kaggle.com/datasets/tongpython/cat-and-dog, taču es pamanīju, ka cat.4085.jpg bildē bija suns, un to es samainīju ar nejaušu bildi no interneta, kurā ir attēlots kaķis. Tas tā, lai modelim ir korekti dati, no kā trenēties. Šī datu kopa nāca jau sadalīta vairākās apakšmapēs - divas galvenās mapes: training_set un test_set. Taču viņas dublējās, t.i. mapē training_set atradās mape training_set kurā visbeidzot atradās apakšmapes: cats un dogs. Tāda pati situācija bija ar test_set. Līdz ar to es salaboju mapju struktūru tā, lai tās nedublētos. Finālā izveidojās mapju struktūra, jeb sadalījums, kurš ir redzams repozitorijā. 

## Kā es bez iepriekšējas pieredzes to paveicu:
Kā galvenos mācību materiālus es izmantoju prof. J. Zutera lekciju un treniņu materiālus, kā arī internetā meklēju nepieciešamo informāciju.

## Ko es sagaidu no šī modeļa:
Es sagaidu, ka tas spēs korekti atšķirt suņu vai kaķu bildes ar vismaz 70% precizitāti.

## Iesaistītie cilvēki:
Tikai es pats, Kristofers Elvis Kirilovičs
stud. apl. nr. - KK22100.
