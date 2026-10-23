QUESTIONS = [
    {
        "question": "1. Ikki Django loyihasi bir kutubxonaning turli versiyalarini talab qilmoqda. Virtual muhit bu muammoni qanday hal qiladi? Muhitni yaratish va faollashtirish ketma-ketligini yozing.",
        "options": [
            "Har bir loyiha uchun alohida Python muhitini yaratadi",
            "Barcha kutubxonalarni bitta umumiy papkaga birlashtiradi",
            "Faqat OS kutubxonalaridan foydalanadi",
            "Kutubxona versiyalarini avtomatik tenglashtiradi"
        ],
        "correct": 0
    },
    {
        "question": "2. Postning author maydoni foydalanuvchiga ForeignKey orqali bog'langan. related_name=\"blog_posts\" nimani anglatadi? Muayyan foydalanuvchining barcha postlarini olish ifodasini yozing.",
        "options": [
            "Foydalanuvchidan postga teskari bog'lanish nomini belgilaydi",
            "Post nomini o'zgartirish uchun xizmat qiladi",
            "Faqat adminlar uchun post yaratishni cheklaydi",
            "Postlar sonini hisoblaydi"
        ],
        "correct": 0
    },
    {
        "question": "3. Bazada mavjud post uchun post.title = \"Yangi sarlavha\" bajarildi. O'zgarishni doimiy saqlash uchun yana nima qilish kerak? Bu yangi post yaratadimi yoki mavjudini yangilaydimi?",
        "options": [
            "post.save() metodini chaqirish kerak, mavjudini yangilaydi",
            "Hech narsa shart emas, o'zi saqlanadi",
            "Post.objects.create() ishlatish kerak",
            "Faqat commit qilish kifoya"
        ],
        "correct": 0
    },
    {
        "question": "4. render() funksiyasiga uzatiladigan asosiy argumentlarni tushuntiring. View kontekstda postsni uzatsa-yu, shablon articles boʻyicha aylansa, postlar nega ko'rinmaydi va xato qanday tuzatiladi?",
        "options": [
            "O'zgaruvchi nomlari mos kelmagani uchun; shablondagi nomni moslash kerak",
            "render() funksiyasi xato ishlaydi",
            "Python versiyasi mos kelmaydi",
            "Baza bilan bog'lanish uziladi"
        ],
        "correct": 0
    },
    {
        "question": "5. Post URLI ID asosidan yil, oy, kun va slug asosiga o'zgartirildi. URL andozasi, post_detail parametrlari va get_absolute_url() nega birgalikda yangilanishi kerak?",
        "options": [
            "Chunki ular bir-biriga bog'langan bo'lib, havolalarning to'g'ri shakllanishini ta'minlaydi",
            "Faqat dizayn uchun",
            "Django shuni talab qilgani uchun",
            "Ma'lumotlar bazasi to'lib qolmasligi uchun"
        ],
        "correct": 0
    },
    {
        "question": "6. SMTP orqali xat yuborishda EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER va EMAIL_USE_TLS sozlamalarining vazifalarini tushuntiring. Ular xat mazmunini yoki ulanishni belgilaydimi?",
        "options": [
            "Ulanish parametrlarini (server, port, foydalanuvchi va xavfsizlikni) belgilaydi",
            "Xatning matni va mavzusini belgilaydi",
            "Faqat shablonni tanlaydi",
            "Foydalanuvchi huquqlarini cheklaydi"
        ],
        "correct": 0
    },
    {
        "question": "7. Izohlar ro'yxati uchun {% for %}, {% empty %} va forloop.counter qanday ishlaydi? Ro'yxatda izohlar bor va bo'sh bo'lgan holatlarni alohida tushuntiring.",
        "options": [
            "for aylanadi, empty bo'sh bo'lsa ishlaydi, counter tartib raqamini beradi",
            "Faqat xato qidirish uchun ishlatiladi",
            "Ma'lumotlarni bazadan o'chiradi",
            "Faqat admin uchun ishlaydi"
        ],
        "correct": 0
    },
    {
        "question": "8. post_list(request, tag_slug=None) viewi teg slugi berilgan va berilmagan holatlarda qanday ishlaydi? Bitta viewdan ikki URL yo'li uchun foydalanish sababini tushuntiring.",
        "options": [
            "Slug berilsa o'sha teg bo'yicha, berilmasa barcha postlarni filtrlab beradi",
            "Faqat bitta postni qaytaradi",
            "Har doim xato beradi",
            "Faqat sahifani yangilaydi"
        ],
        "correct": 0
    },
    {
        "question": "9. mark_safe() Django shablonidagi HTML chiqarishga qanday ta'sir qiladi? Uni foydalanuvchi yuborgan tekshirilmagan matnga qo'llash nega xavfli ekanini tushuntiring.",
        "options": [
            "Matnni xavfsiz HTML sifatida qabul qiladi; XSS hujumlariga olib kelishi mumkin",
            "Matnni shifrlaydi",
            "Faqat matn rangini o'zgartiradi",
            "Hech qanday ta'sir qilmaydi"
        ],
        "correct": 0
    },
    {
        "question": "10. Latest PostsFeed.link atributida reverse_lazy() ishlatilgan. Uning reverse()dan asosiy farqi nimada va klass atributida URLni kechiktirib aniqlash nima uchun foydali?",
        "options": [
            "reverse_lazy() URLlarni yuklanish vaqtida emas, ishlatilganda (kechiktirib) baholaydi",
            "Ularning farqi yo'q",
            "reverse_lazy faqat admin uchun",
            "reverse tezroq ishlaydi"
        ],
        "correct": 0
    },
    {
        "question": "11. Django loyihasi va ilovasi o'rtasidagi farqni tushuntiring. Universitet saytidagi blog, kutubxona va yangiliklar xizmatlarini loyiha hamda ilovalarga qanday ajratgan bo'lardingiz?",
        "options": [
            "Loyiha - butun sayt sozlamalari, ilova - alohida funksional qism (blog, kutubxona)",
            "Ilova bu asosiy papka, loyiha uning ichidagi fayl",
            "Ularning farqi yo'q",
            "Faqat nomida farq bor"
        ],
        "correct": 0
    },
    {
        "question": "12. Muallifning uchta posti bor va author maydonida on_delete=models.CASCADE belgilangan. Muallif Django ORM orqali o'chirilsa, postlar bilan nima bo'ladi? Sababini tushuntiring.",
        "options": [
            "Bog'langan barcha postlar ham avtomatik ravishda o'chib ketadi",
            "Postlar qoladi, muallifi bo'sh bo'ladi",
            "Xatolik yuz beradi",
            "Postlar boshqa muallifga o'tadi"
        ],
        "correct": 0
    },
    {
        "question": "13. Kamida 10 ta postdan iborat qs tartiblangan QuerySet berilgan. qs[:5] va qs[3:6] qaysi o'rindagi postlarni qaytaradi? Kesimning oxirgi indeksi natijaga kirishini izohlang.",
        "options": [
            "qs[:5] 0 dan 4 gacha, qs[3:6] 3 dan 5 gacha elementlarni oladi (oxirgi indeks kirmaydi)",
            "Barcha 10 ta postni oladi",
            "Faqat oxirgi postni oladi",
            "Xatolik beradi"
        ],
        "correct": 0
    },
    {
        "question": "14. E'lon qilinmagan yoki mavjud bo'lmagan post batafsil sahifada ochilmasligi kerak. get_object_or_404() yordamida bunday tekshiruvni qanday yozasiz va topilmagan holatda qanday javob qaytariladi?",
        "options": [
            "get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED) va 404 sahifasi qaytariladi",
            "Avtomatik ravishda 500 xatosi qaytaradi",
            "Bosh sahifaga yo'naltiradi",
            "Hech qanday javob qaytarmaydi"
        ],
        "correct": 0
    },
    {
        "question": "15. 25 ta post har sahifada 10 tadan ko'rsatiladi. Nechta sahifa hosil boʻladi va uchinchi sahifada nechta post bo'ladi? Paginator yaratish kodini ham yozing.",
        "options": [
            "3 ta sahifa hosil bo'ladi, 3-sahifada 5 ta post bo'ladi",
            "2 ta sahifa hosil bo'ladi",
            "5 ta sahifa hosil bo'ladi",
            "1 ta sahifa hosil bo'ladi"
        ],
        "correct": 0
    },
    {
        "question": "16. SMTP parolini kod ichiga yozish o'rniga .env va python-decoupledan foydalanish sababini tushuntiring. .envni .gitignorega kiritish nima uchun zarur?",
        "options": [
            "Maxfiy ma'lumotlarni xavfsiz saqlash va GitHub'ga chiqib ketishining oldini olish uchun",
            "Kod tezroq ishlashi uchun",
            "Faqat tartib uchun",
            "Django shuni talab qilgani uchun"
        ],
        "correct": 0
    },
    {
        "question": "17. Izoh formasi post tafsilotlari sahifasida ham, xato natijasi sahifasida ham ko'rsatiladi. Formani includes/comment_form.htmlga ajratib, {% include %} bilan ishlatish qanday muammoni hal qiladi?",
        "options": [
            "Kodning takrorlanishini oldini oladi va qayta foydalanishni ta'minlaydi",
            "Sayt tezligini pasaytiradi",
            "Ma'lumotlarni bazaga yozmaydi",
            "Faqat dizaynni buzadi"
        ],
        "correct": 0
    },
    {
        "question": "18. Teg boʻyicha filtrlash va sahifalash bir viewda bajariladi. Nima uchun avval QuerySetni teg bo'yicha filtrlab, undan keyin Paginator yaratish kerakligini misolda tushuntiring.",
        "options": [
            "Chunki sahifalash faqat filtrlangan aniq natijalar ustidan bajarilishi kerak",
            "Farqi yo'q, xohlagan tartibda bajarish mumkin",
            "Avval sahifalash, keyin filtr qilish kerak",
            "Paginator filtrni o'chirib yuboradi"
        ],
        "correct": 0
    },
    {
        "question": "19. Markdown yordamida sarlavha, qalin matn va uch elementli ro'yxatdan iborat kichik post yozing. Bu matn HTMLga aylantirilganda qanday ko'rinishini tushuntiring.",
        "options": [
            "Markdown teglari mos ravishda h1, strong, ul/li kabi HTML teglariga o'tadi",
            "Oddiy matn holida qoladi",
            "Faqat xato beradi",
            "Rasmlarga aylanadi"
        ],
        "correct": 0
    },
    {
        "question": "20. Sayt xaritasidagi changefreq=\"weekly\", priority=0.9 va lastmod() qanday turdagi ma'lumotlarni bildiradi? Ularning vazifalarini bir post sahifasi misolida farqlang.",
        "options": [
            "Qidiruv botlari uchun o'zgarish chastotasi, muhimligi va oxirgi o'zgarish sanasini bildiradi",
            "Faqat foydalanuvchi statistikasini ko'rsatadi",
            "Sayt tezligini belgilaydi",
            "Admin huquqlarini belgilaydi"
        ],
        "correct": 0
    },
    {
        "question": "21. MTV arxitekturasidagi Model, Template va View vazifalarini tushuntiring. Blog postini bazadan olib, foydalanuvchiga koʻrsatishda har bir qism qanday ishtirok etadi?",
        "options": [
            "Model ma'lumotlar bazasi, View mantiqiy qism, Template tashqi ko'rinishni boshqaradi",
            "Hammasi bitta vazifani bajaradi",
            "View ma'lumotlar bazasini saqlaydi",
            "Template faqat kodni ishga tushiradi"
        ],
        "correct": 0
    },
    {
        "question": "22. Post modelida id maydoni alohida yozilmagan, lekin Post.objects.get(id=5) ishlamoqda. Buning sababini va birlamchi kalitning vazifasini tushuntiring.",
        "options": [
            "Django har bir modelga avtomatik ravishda unikal id (Primary Key) qo'shadi",
            "Buni o'zimiz qo'lda yozishimiz shart",
            "Bu xatolik, id ishlamasligi kerak",
            "ID faqat admin uchun ishlaydi"
        ],
        "correct": 0
    },
    {
        "question": "23. count() va exists() metodlari qaytaradigan qiymatlarni taqqoslang. \"Postlar nechta?\" va \"Hech bo'lmasa bitta post bormi?\" vazifalari uchun qaysi metodlarni tanlaysiz?",
        "options": [
            "count() sonini qaytaradi, exists() esa True/False qaytaradi",
            "Ikkalasi ham bir xil natija beradi",
            "count() True/False qaytaradi",
            "exists() sonini qaytaradi"
        ],
        "correct": 0
    },
    {
        "question": "24. path(\"<int:id>/\", views.post_detail, name=\"post_detail\") andozasidagi qismlarni tushuntiring. Ilova yo'li ostidagi 7/ va abc/ qiymatlaridan qaysi biri mos keladi? Sababini yozing.",
        "options": [
            "7/ mos keladi, chunki int faqat butun sonni qabul qiladi",
            "abc/ mos keladi",
            "Ikkalasi ham mos keladi",
            "Hech biri mos kelmaydi"
        ],
        "correct": 0
    },
    {
        "question": "25. Foydalanuvchi ?page=abc yubordi. Paginator.page() bilan ishlaydigan viewda qaysi istisno boshqariladi va kitobdagi yechim bo'yicha qaysi sahifa qaytariladi?",
        "options": [
            "PageNotAnInteger yoki EmptyPage istisnolari boshqariladi, odatda 1-sahifa qaytariladi",
            "Server o'chib qoladi",
            "Faqat 500 xatosi chiqadi",
            "Hech qanday istisno chiqmaydi"
        ],
        "correct": 0
    },
    {
        "question": "26. Dasturchida ishlaydigan SMTP server yo'q, ammo tavsiya xatining mazmunini sinash kerak. Console email backend qanday sozlanadi va xat natijasi qayerda ko'rinadi?",
        "options": [
            "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' sozlanadi, terminalda ko'rinadi",
            "Xat yo'qolib qoladi",
            "Faqat brauzerda chiqadi",
            "Faylga saqlanadi"
        ],
        "correct": 0
    },
    {
        "question": "27. Izohlarni koʻrsatish uchun post_detail, saqlash uchun post_comment viewlari ajratilgan. Ularning vazifalari, qabul qiladigan asosiy HTTP so'rovlari va shablonga uzatadigan ma'lumotlarini taqqoslang.",
        "options": [
            "post_detail GET so'rovini olib sahifani ko'rsatadi, post_comment POST so'rovini olib izohni saqlaydi",
            "Ikkalasi ham faqat POST qabul qiladi",
            "Ikkalasi ham bir xil vazifani bajaradi",
            "post_comment ma'lumotni o'chiradi"
        ],
        "correct": 0
    },
    {
        "question": "28. Mavjud bo'lmagan teg slugi va mavjud, lekin e'lon qilingan posti yo'q teg bir xil holatmi? get_object_or_404(Tag, ...) hamda postlarni filtrlash natijalarini taqqoslang.",
        "options": [
            "Yo'q, get_object_or_404 404 qaytaradi, filtrlash esa bo'sh ro'yxat ([] ) qaytarishi mumkin",
            "Ikkalasi ham bir xil 404 beradi",
            "Ikkalasi ham bo'sh ro'yxat qaytaradi",
            "Farqi yo'q"
        ],
        "correct": 0
    },
    {
        "question": "29. sitemap.xml qanday maqsadda yaratiladi va undan kim foydalanadi? Django sayt xaritasidagi post manzillari get_absolute_url() bilan qanday bog'lanishini tushuntiring.",
        "options": [
            "Qidiruv tizimi botlari (Google, Yandex) saytni tezroq indekslashishi uchun ishlatiladi",
            "Faqat oddiy foydalanuvchilar o'qishi uchun",
            "Sayt dizaynini yaxshilash uchun",
            "Parollarni shifrlash uchun"
        ],
        "correct": 0
    },
    {
        "question": "30. Mavjud blog ma'lumotlarini SQLite bazasidan PostgreSQLga ko'chirish bosqichlarini yozing. Eksport, ulanish sozlamalarini almashtirish, migratsiya va import nega shu tartibda bajariladi?",
        "options": [
            "Avval dumpdata bilan ma'lumot olinadi, baza o'zgaradi, migrate qilinadi va loaddata bilan yuklanadi",
            "To'g'ridan-to'g'ri nusxalanadi",
            "Faqat settings o'zgartiriladi",
            "Bazasini o'chirib yuborish kerak"
        ],
        "correct": 0
    },
    {
        "question": "31. Yangi Django loyihasidagi manage.py, settings.py va urls.py fayllari qanday vazifalarni bajaradi? Har biriga tegishli bittadan amaliy ishni misol qiling.",
        "options": [
            "manage.py buyruqlarni bajaradi, settings.py sozlaydi, urls.py manzillarni yo'naltiradi",
            "Hammasi bir xil ishni bajaradi",
            "urls.py bazani boshqaradi",
            "settings.py faqat dizayn uchun"
        ],
        "correct": 0
    },
    {
        "question": "32. makemigrations va migrate buyruqlarini taqqoslang. Modelga yangi maydon qo'shilgach, bazani yangilash uchun ularni qanday ketma-ketlikda bajarish kerak?",
        "options": [
            "Avval makemigrations (fayl yaratish), keyin migrate (bazaga qo'llash) bajariladi",
            "Faqat migrate bajariladi",
            "Avval migrate, keyin makemigrations",
            "Ikkalasini bajarish shart emas"
        ],
        "correct": 0
    },
    {
        "question": "33. Sarlavhasi \"Python\" yoki \"Django\" bilan boshlanadigan postlarni topish uchun Q obyektlari bilan QuerySet yozing. Oddiy filtr argumentlari qanday mantiqiy shart bilan birlashadi?",
        "options": [
            "Q(title__startswith='Python') | Q(title__startswith='Django'); oddiy filtrlar AND bilan birlashadi",
            "Oddiy filtrlar OR bilan birlashadi",
            "Q obyektlari faqat AND ishlatadi",
            "Bularning farqi yo'q"
        ],
        "correct": 0
    },
    {
        "question": "34. Asosiy urls.pyda include(\"blog.urls\") ishlatishning vazifasi nima? Ikki ilovada ham post_list nomli URL boʻlsa, namespace ularni qanday ajratishga yordam beradi?",
        "options": [
            "URL larni modullarga ajratadi; namespace (masalan, blog:post_list) bir xil nomdagi URL larni farqlashga yordam beradi",
            "Faqat tartib uchun",
            "Saytni tezlashtiradi",
            "Xatolarni yashiradi"
        ],
        "correct": 0
    },
    {
        "question": "35. Blogda uchta sahifa mavjud, foydalanuvchi esa ?page=99ni ochdi. EmptyPage holatini qanday boshqarasiz va oxirgi sahifa raqamini qanday olasiz?",
        "options": [
            "EmptyPage ushlanib, paginator.num_pages orqali oxirgi sahifa ko'rsatiladi",
            "Avtomatik ravishda 404 chiqariladi",
            "Hech narsa qilinmaydi",
            "Dastur to'xtaydi"
        ],
        "correct": 0
    },
    {
        "question": "36. send_mail()ning subject, message, from_email va recipient_list argumentlari qanday vazifalarni bajaradi? from_email=None berilganda jo'natuvchi qaysi sozlamadan olinadi?",
        "options": [
            "Mavzu, matn, kimdan va kimga; DEFAULT_FROM_EMAIL sozlamasidan olinadi",
            "Faqat xat matnini yuboradi",
            "Parolni tekshiradi",
            "Faqat adminni belgilaydi"
        ],
        "correct": 0
    },
    {
        "question": "37. comment.post va post.comments.all() ifodalari qaysi yo'nalishdagi bog'lanishni ifodalaydi? Bitta postga bir nechta izoh yozilishi mumkinligini ushbu ifodalar orqali tushuntiring.",
        "options": [
            "comment.post to'g'ridan-to'g'ri postga, post.comments.all() esa teskari yo'nalishda barcha izohlarga bog'lanadi",
            "Ikkalasi bir xil narsani bildiradi",
            "Faqat postni o'chiradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "38. {{ post.tags.all|join:\", \" }} ifodasi nimani chiqaradi? python, django va web teglaridan iborat ro'yxat misolida join filtrining vazifasini tushuntiring.",
        "options": [
            "Teglar ro'yxatini vergul bilan ajratilgan matn ko'rinishida chiqaradi (python, django, web)",
            "Faqat bitta tegnik chiqaradi",
            "Tegni o'chirib yuboradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "39. PostSitemap.items() faqat e'lon qilingan postlarni qaytarishi uchun qanday so'rov yoziladi? lastmod() qaysi sana maydonini qaytarishi va nima uchun kerakligini tushuntiring.",
        "options": [
            "Post.published.all() yoziladi, lastmod() updated o'zgaruvchisini qaytaradi",
            "Barcha postlarni oladi",
            "Faqat o'chirilganlarni oladi",
            "Hech qanday so'rov yozilmaydi"
        ],
        "correct": 0
    },
    {
        "question": "40. Fixture nima va undan qanday foydalaniladi? dumpdata orqali faqat blog.Post modelidagi ma'lumotlarni posts.json fayliga eksport qilish buyrug'ini yozing.",
        "options": [
            "Ma'lumotlar bazasini to'ldirish uchun JSON/XML fayl; python manage.py dumpdata blog.Post --output posts.json",
            "Faqat xatolarni tozalash vositasi",
            "Shablon fayli",
            "Dastur sozlamasi"
        ],
        "correct": 0
    },
    {
        "question": "41. DEBUG=True holatida xatolik sahifasi dasturchiga qanday yordam beradi? Saytni foydalanuvchilarga taqdim etishda bu sozlama nima uchun oʻzgartirilishi kerakligini tushuntiring.",
        "options": [
            "Batafsil xato izlarini (traceback) ko'rsatadi; xavfsizlik uchun productionda False qilinishi kerak",
            "Saytni tezlashtiradi",
            "Faqat dizaynni o'zgartiradi",
            "Hech qanday yordami yo'q"
        ],
        "correct": 0
    },
    {
        "question": "42. python manage.py sqlmigrate blog 0001 buyrug'i nimani koʻrsatadi? Uning natijasini ko'rish migratsiyani bazaga qo'llash bilan bir xil amal hisoblanadimi? Izohlang.",
        "options": [
            "Migratsiyaning SQL kodini ko'rsatadi, bazaga qo'llash bilan bir xil emas (faqat ko'rsatadi)",
            "Bazadagi barcha ma'lumotlarni o'chiradi",
            "Migratsiyani avtomatik bajaradi",
            "Xatolikni tuzatadi"
        ],
        "correct": 0
    },
    {
        "question": "43. PublishedManagerning get_queryset() metodida holat bo'yicha filtr qo'llashdan maqsad nima? Post.objects.all() va Post.published.all() natijalarini taqqoslang.",
        "options": [
            "Faqat e'lon qilingan postlarni olishni avtomatlashtiradi; all() hammasini, published faqat publishedlarni oladi",
            "Ikkalasi bir xil ishlaydi",
            "published faqat qoralarni oladi",
            "all() xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "44. Shablonda havolani qat'iy /blog/5/ deb yozish o'rniga {% url %} tegidan foydalanish qanday qulaylik beradi? blog:post_detailga post IDsi bilan havola yozing.",
        "options": [
            "URL manzili o'zgarganda shablonni o'zgartirish shart emas, avtomatik yangilanadi ({% url 'blog:post_detail' post.id %})",
            "Saytni sekinlashtiradi",
            "Hech qanday qulayligi yo'q",
            "Faqat estetik ko'rinish uchun"
        ],
        "correct": 0
    },
    {
        "question": "45. Sahifalash shablonida oldingi va keyingi sahifa havolalarini shartli chiqarish nega kerak? has_previous, has_next hamda sahifa raqamini olish metodlaridan foydalanishni tushuntiring.",
        "options": [
            "Mavjud bo'lmagan sahifalarga o'tishda xatolik chiqishining oldini oladi",
            "Faqat dizaynni chiroyli qiladi",
            "Ma'lumotlarni tezroq yuklaydi",
            "Kerak emas"
        ],
        "correct": 0
    },
    {
        "question": "46. Elektron xat ichidagi havolani yaratishda request.build_absolute_uri(post.get_absolute_url()) nima uchun ishlatiladi? Nisbiy va toʻliq URL farqini misol bilan tushuntiring.",
        "options": [
            "Domain nomini qo'shib to'liq URL (https://example.com/blog/5/) hosil qiladi",
            "Faqat nisbiy URL (/blog/5/) yaratadi",
            "Xatni shifrlaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "47. Comment Form. Meta.fieldsda faqat name, email va body keltirilgan. Nima uchun post va active maydonlarini foydalanuvchi formasiga kiritmasdan boshqarish ma'qul?",
        "options": [
            "Ularni foydalanuvchi o'zgartira olmasligi va xavfsizlik/avtomatlashtirish uchun viewda belgilanadi",
            "Chunki ular muhim emas",
            "Django ularni qo'llab-quvvatlamaydi",
            "Xato chiqmasligi uchun"
        ],
        "correct": 0
    },
    {
        "question": "48. post.tags.values_list(\"id\", flat=True) ifodasi qanday shakldagi ma'lumot qaytaradi? flat=Truening vazifasi va olingan IDlardan o'xshash postlarni izlashda foydalanishni tushuntiring.",
        "options": [
            "Faqat ID lardan iborat oddiy ro'yxat (masalan, [1, 2, 3]) qaytaradi",
            "Kortejlar ro'yxatini qaytaradi",
            "Matn qaytaradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "49. Mahalliy saytdagi sitemap.xml havolalari example.com domeni bilan chiqmoqda. SITE_ID va Site modeli asosida muammo sababini hamda domenni qayerda tuzatishni tushuntiring.",
        "options": [
            "Django Site framework bazadagi domain nomidan foydalanadi; admin paneldan Site nomini o'zgartirish kerak",
            "settings.py dan o'chiriladi",
            "Bu xato emas",
            "Kodning o'zida o'zgartiriladi"
        ],
        "correct": 0
    },
    {
        "question": "50. psycopg PostgreSQL adapteri qanday vazifani bajaradi? DATABASESdagi ENGINE, NAME va HOST qiymatlari qaysi ulanish ma'lumotlarini belgilashini tushuntiring.",
        "options": [
            "Python bilan PostgreSQL bazasini bog'laydi; ENGINE baza turini, NAME nomini, HOST manzilini belgilaydi",
            "Faqat dizayn uchun",
            "Parolni saqlaydi",
            "Xatolarni tekshiradi"
        ],
        "correct": 0
    },
    {
        "question": "51. blog ilovasi yaratildi, ammo INSTALLED_APPSga qo'shilmadi. Bu sozlama qanday vazifani bajaradi va ilovani loyihada faollashtirish uchun qanday yozuv kiritish kerak?",
        "options": [
            "Django ilovani tanishi uchun 'blog.apps.BlogConfig' yoki 'blog' ni INSTALLED_APPS ga qo'shish kerak",
            "Hech narsa qilish shart emas",
            "Faqat urls.py ga yoziladi",
            "Serverni o'chirish kerak"
        ],
        "correct": 0
    },
    {
        "question": "52. Admin panelida postning sarlavhasi va holatini ustunlarda chiqarish, holat bo'yicha filtrlash va matnidan qidirish kerak. Tegishli uchta ModelAdmin sozlamasini yozing.",
        "options": [
            "list_display, list_filter va search_fields",
            "display, filter, search",
            "fields, filter_horizontal",
            "admin_view, query"
        ],
        "correct": 0
    },
    {
        "question": "53. get() va filter() metodlari qaytaradigan natijalarni taqqoslang. So'rovga hech bir obyekt yoki bir nechta obyekt mos kelsa, har bir metod qanday ishlaydi?",
        "options": [
            "get() bitta obyekt qaytaradi (topilmasa MultipleObjectsReturned yoki DoesNotExist beradi), filter() QuerySet qaytaradi",
            "Ikkalasi bir xil ishlaydi",
            "filter() bitta obyekt qaytaradi",
            "get() har doim ro'yxat qaytaradi"
        ],
        "correct": 0
    },
    {
        "question": "54. base.htmlda title va content bloklari belgilangan. Undan voris oladigan post tafsilotlari shablonida extends va block teglaridan qanday foydalanishni qisqa misolda ko'rsating.",
        "options": [
            "{% extends \"blog/base.html\" %} va {% block content %} ... {% endblock %}",
            "{% include \"base.html\" %}",
            "{% block title %} ...",
            "extends ishlatilmaydi"
        ],
        "correct": 0
    },
    {
        "question": "55. {% include \"pagination.html\" with page=posts %} yozuvi qanday ishlaydi? Sahifalash qismini alohida shablonga ajratish qayta foydalanishga qanday yordam beradi?",
        "options": [
            "pagination.html shablonini chaqiradi va unga page o'zgaruvchisini uzatadi; kodni takrorlamaslikni ta'minlaydi",
            "Faqat dizaynni buzadi",
            "Ma'lumotni o'chiradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "56. Ulashish viewidagi sent o'zgaruvchisi boshlanishida False, xat yuborilgach True bo'ladi. Bu qiymat shablondagi forma va muvaffaqiyat xabarini qanday boshqaradi?",
        "options": [
            "sent=True bo'lsa forma o'rniga muvaffaqiyat xabari chiqadi, False bo'lsa forma chiqadi",
            "Ikkalasi birga chiqadi",
            "Hech qanday o'zgarish bo'lmaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "57. @require_POST bilan bezatilgan izoh saqlash viewiga GET so'rovi yuborildi. Qanday HTTP holat kodi qaytariladi va bu dekorator view vazifasini qanday cheklaydi?",
        "options": [
            "405 (Method Not Allowed) qaytariladi; view faqat POST so'rovlarini qabul qilishga cheklanadi",
            "200 OK qaytariladi",
            "404 Not Found qaytariladi",
            "500 Internal Error"
        ],
        "correct": 0
    },
    {
        "question": "58. O'xshash postlar so'rovida nima uchun .exclude(id=post.id) ishlatiladi? Bu shart olib tashlansa, tavsiyalar ro'yxatida qanday mantiqiy xato yuz berishi mumkin?",
        "options": [
            "Joriy o'qilayotgan postning o'zi o'xshash postlar tavsiyasiga chiqib qolishining oldini oladi",
            "Baza ishlamay qoladi",
            "Hech qanday xato bo'lmaydi",
            "Faqat tezlik pasayadi"
        ],
        "correct": 0
    },
    {
        "question": "59. Blogning RSS oqimi foydalanuvchiga qanday qulaylik beradi? Feed klassidagi items(), item_title() va item_pubdate() metodlarining vazifalarini post misolida tushuntiring.",
        "options": [
            "Yangiliklarni maxsus reader dasturlarida kuzatib borish imkonini beradi",
            "Faqat dizaynni yaxshilaydi",
            "Saytni sekinlashtiradi",
            "Faqat admin uchun"
        ],
        "correct": 0
    },
    {
        "question": "60. Post sarlavhasi va asosiy matnidan birgalikda qidirish uchun Search Vectordan qanday foydalaniladi? To'liq matnli qidiruvning oddiy title_contains qidiruvidan farqini izohlang.",
        "options": [
            "SearchVector('title', 'body') bir nechta ustunni qamrab oladi, tillarni va ma'no qismlarini inobatga oladi",
            "Farqi yo'q",
            "title_contains tezroq ishlaydi",
            "SearchVector ishlamaydi"
        ],
        "correct": 0
    },
    {
        "question": "61. Django ishlab chiqish serverini 8001-portda ishga tushirish buyrug'ini yozing. runserverning vazifasi va undan ishlab chiqish jarayonida foydalanish sababini tushuntiring.",
        "options": [
            "python manage.py runserver 8001; lokal test qilish uchun xizmat qiladi",
            "python manage.py startserver 8001",
            "django-admin run 8001",
            "runserver ishlatilmaydi"
        ],
        "correct": 0
    },
    {
        "question": "62. Admin formasida sarlavhadan slugni avtomatik to'ldirish va koʻp foydalanuvchi orasidan muallif tanlashni qulaylashtirish kerak. prepopulated_fields hamda raw_id_fields bilan yechim yozing.",
        "options": [
            "prepopulated_fields = {'slug': ('title',)} va raw_id_fields = ('author',)",
            "admin_fields lardan foydalaniladi",
            "slug_auto = True",
            "Bu imkoniyat yo'q"
        ],
        "correct": 0
    },
    {
        "question": "63. Post(...) orqali obyekt yaratish va Post.objects.create(...)dan foydalanish o'rtasidagi farqni tushuntiring. Qaysi holatda alohida save() chaqirish kerak va nima uchun?",
        "options": [
            "Post(...) obyektni xotirada yaratadi (save() chaqirish kerak), create() esa darhol bazaga yozadi",
            "Ikkalasi bir xil",
            "create() xatolik beradi",
            "Post(...) darhol bazaga yozadi"
        ],
        "correct": 0
    },
    {
        "question": "64. Blog shabloniga static/css/blog.css faylini ulash kerak. {% load static %} va {% static %} teglarining vazifalarini tushuntirib, CSSni ulash kodini yozing.",
        "options": [
            "{% load static %} yuklaydi, <link href=\"{% static 'css/blog.css' %}\"> ulaydi",
            "<link href=\"css/blog.css\">",
            "{% include css %}",
            "Static ulash shart emas"
        ],
        "correct": 0
    },
    {
        "question": "65. Funksiyaga asoslangan va klassga asoslangan viewlarni taqqoslang. HTTP metodlariga oid kodni ajratish va vorislikdan foydalanishda klassli view qanday qulaylik beradi?",
        "options": [
            "Klassli viewlar (CBV) kodni qayta ishlatish (inheritance) va get/post metodlarini alohida funksiyalarga bo'lishni osonlashtiradi",
            "Funksiyalar har doim yaxshiroq",
            "Farqi yo'q",
            "CBV juda sekin ishlaydi"
        ],
        "correct": 0
    },
    {
        "question": "66. POST orqali yuboriladigan Django formasida {% csrf_token %} tegi nima uchun kerak? U qanday yashirin maydon hosil qiladi va qaysi turdagi soxtalashtirishdan himoyalashga yordam beradi?",
        "options": [
            "CSRF (Cross-Site Request Forgery) hujumlaridan himoya qiladi, unikal token hosil qiladi",
            "Parolni shifrlaydi",
            "Formani tezroq yuboradi",
            "Kerak emas"
        ],
        "correct": 0
    },
    {
        "question": "67. Izoh saqlashda form.save(commit=False), comment.post = post va comment.save() amallari nega shu ketma-ketlikda bajariladi? Har bir bosqichdagi obyekt holatini tushuntiring.",
        "options": [
            "commit=False obyektni bazaga yozmay qaytaradi, unga post biriktirilgach save() orqali bazaga saqlanadi",
            "Tartibining farqi yo'q",
            "Bazaga 2 marta yoziladi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "68. Umumiy teglari bor postlar tanlangach, annotate(same_tags=Count(\"tags\")) qanday qiymat qo'shadi? Bu qiymat tavsiya etiladigan postlarning o'xshashligini baholashda qanday ishlatiladi?",
        "options": [
            "Har bir post uchun umumiy teglar sonini same_tags maydoni sifatida qo'shadi va saralashda ishlatiladi",
            "Tegni o'chiradi",
            "Faqat xato beradi",
            "Hech narsa qo'shmaydi"
        ],
        "correct": 0
    },
    {
        "question": "69. Maxsus blog_tags kutubxonasi shablonda tanilmayapti. templatetags katalogi, __init__.py, register va {% load blog_tags %} boʻyicha nimalarni tekshirish kerakligini tushuntiring.",
        "options": [
            "Katalog tuzilishi, __init__.py borligi, register = template.Library() yozilgani va load qilinganini tekshirish kerak",
            "Faqat serverni yoqish kerak",
            "settings.py ni o'chirish kerak",
            "Xato yo'q"
        ],
        "correct": 0
    },
    {
        "question": "70. Blog qidiruv formasida nima uchun GET metodidan foydalanish qulay? View qidiruv so'zini qayerdan oladi va uni ishlatishdan oldin SearchForm bilan qanday tekshiradi?",
        "options": [
            "URL da so'rov saqlanib qoladi (share qilish qulay); view form.cleaned_data['query'] orqali olib is_valid() bilan tekshiradi",
            "POST xavfsizroq",
            "GET ishlamaydi",
            "Farqi yo'q"
        ],
        "correct": 0
    },
    {
        "question": "71. Sarlavhasi \"Django bilan blog yaratish\" bo'lgan post uchun mos slug yozing. Sarlavha o'rniga slugdan URLda foydalanishning qulayligini tushuntiring.",
        "options": [
            "django-bilan-blog-yaratish; URL larni o'qishga oson va SEO uchun qulay qiladi",
            "12345",
            "blog_post",
            "Slug shart emas"
        ],
        "correct": 0
    },
    {
        "question": "72. Post modelining __str__ metodi self.titleni qaytarsa, bu admin panelidagi obyektlar ko'rinishiga qanday ta'sir qiladi? Mazmunli matn qaytarish sababini tushuntiring.",
        "options": [
            "Admin panelida obyektlar 'Post object (1)' o'rniga o'zining sarlavhasi bilan ko'rinadi",
            "Hech qanday ta'sir qilmaydi",
            "Xato beradi",
            "Admin ishlamay qoladi"
        ],
        "correct": 0
    },
    {
        "question": "73. User.objects.get_or_create(username=\"ali\") qanday ikki qiymat qaytaradi? Foydalanuvchi avvaldan mavjud bo'lgan va yangi yaratilgan holatlarni alohida tushuntiring.",
        "options": [
            "(obyekt, created) – created True bo'lsa yangi yaratilgan, False bo'lsa avvaldan mavjud bo'lgan",
            "Faqat obyekt qaytaradi",
            "Faqat True/False qaytaradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "74. {{ post.title }}, {% for post in posts %} va {{ post.body|linebreaks }} yozuvlarini oʻzgaruvchi, teg va filtr sifatida ajrating. Har birining renderdagi vazifasini tushuntiring.",
        "options": [
            "{{...}} o'zgaruvchi, {%...%} teg, | filtr vazifasini bajaradi",
            "Hammasi o'zgaruvchi",
            "Hammasi teg",
            "Farqi yo'q"
        ],
        "correct": 0
    },
    {
        "question": "75. ListViewda faqat e'lon qilingan postlar chiqishi kerak. model = Post o'rniga maxsus queryset belgilash nega kerak va tegishli yozuv qanday bo'ladi?",
        "options": [
            "queryset = Post.published.all() deb yoziladi, chunki faqat e'lon qilinganlarni chiqarish talab etiladi",
            "Shart emas",
            "model = published",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "76. Postni elektron pochta orqali ulashish uchun Form, izohni saqlash uchun esa ModelForm tanlangan. Ushbu ikki forma turining farqini shu vazifalar orqali tushuntiring.",
        "options": [
            "Form oddiy ma'lumot yig'adi (bazaga yozilmaydi), ModelForm esa to'g'ridan-to'g'ri model bilan bog'lanib bazaga yozadi",
            "Ikkalasi bir xil",
            "Form bazaga yozadi",
            "ModelForm ishlamaydi"
        ],
        "correct": 0
    },
    {
        "question": "77. Admin izohning active qiymatini False qildi. post.comments.filter(active=True) ishlatilgan sahifada izohning koʻrinishi va ko'rsatiladigan faol izohlar soni qanday oʻzgaradi?",
        "options": [
            "Ushbu izoh sahifada ko'rsatilmaydi va faol izohlar soni bittaga kamayadi",
            "Hamma izoh ko'rinaveradi",
            "Xato beradi",
            "Baza tozalanadi"
        ],
        "correct": 0
    },
    {
        "question": "78. Tavsiyalar -same_tags, so'ng -publish bo'yicha saralanadi. A postda 3 ta umumiy teg, B va Cda 2 tadan; C yangiroq. Ularning tartibini asoslang.",
        "options": [
            "A birinchi chiqadi (teglar ko'p), keyin C (yangiroq), oxirida B",
            "Tartib ahamiyatsiz",
            "B birinchi chiqadi",
            "Hammasi bir vaqtda chiqadi"
        ],
        "correct": 0
    },
    {
        "question": "79. simple_tag va inclusion_tagni taqqoslang. Qaysi biri alohida shablonni render qiladi va uning funksiyasi nima uchun kontekst lug'atini qaytarishi kerak?",
        "options": [
            "inclusion_tag alohida shablonni render qiladi va ma'lumotni shablonga uzatish uchun lug'at qaytaradi",
            "simple_tag shablon render qiladi",
            "Farqi yo'q",
            "Ikkalasi ham shablon chiqarmaydi"
        ],
        "correct": 0
    },
    {
        "question": "80. SearchQuery bilan ishlashda stemming va stop so'zlarni chiqarish nima uchun kerak? \"music\" va \"musical\" kabi shakllarni izlash misolida tushuntiring.",
        "options": [
            "So'zlarning o'zak qismini topib, qo'shimchalarni va ma'nosiz so'zlarni tashlab yuborish orqali qidiruvni aniq qiladi",
            "Qidiruvni sekinlashtiradi",
            "Kerak emas",
            "Faqat xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "81. DATABASES sozlamasining vazifasini tushuntiring. Notoʻgʻri baza koʻrsatilsa, postlar ro'yxati viewida qanday muammo yuz beradi?",
        "options": [
            "Ma'lumotlar bazasiga ulanish xatoligi (OperationalError) yuz beradi",
            "Hech qanday muammo bo'lmaydi",
            "Faqat dizayn buziladi",
            "Sayt ishlayveradi"
        ],
        "correct": 0
    },
    {
        "question": "82. Post bazada bor, lekin admin panelida ko'rinmayapti. Modelni ro'yxatdan oʻtkazish kodi va superfoydalanuvchi yaratish buyrug'ini yozing.",
        "options": [
            "admin.site.register(Post) yozish kerak; python manage.py createsuperuser",
            "admin.register(False)",
            "python manage.py runserver",
            "Hech narsa qilish shart emas"
        ],
        "correct": 0
    },
    {
        "question": "83. QuerySetning kechiktirib bajarilishini tushuntiring. Uni oʻzgaruvchiga saqlash, filtrlash va list()ga aylantirishda bazaga murojaat qachon yuz beradi?",
        "options": [
            "QuerySet bahòlanganda (evaluation) yoki list()ga aylantirilganda bazaga so'rov boradi",
            "O'zgaruvchiga yozilishi bilan",
            "Fayl ochilganda",
            "Hech qachon"
        ],
        "correct": 0
    },
    {
        "question": "84. posts kontekst oʻzgaruvchisidagi postlar sarlavhasi va e'lon sanasini HTMLda chiqaradigan shablon parchasini yozing. Nima uchun bu yerda takrorlash tegi kerak?",
        "options": [
            "{% for post in posts %} ... {% endfor %} orqali har bir postni alohida chiqarish uchun",
            "Faqat bitta postni chiqarish uchun",
            "Takrorlash shart emas",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "85. Klassli postlar ro'yxatida shablon posts oʻzgaruvchisini kutmoqda. context_object_name va template_name atributlarini qanday belgilaysiz? Ularning vazifalarini izohlang.",
        "options": [
            "context_object_name = 'posts' va template_name = 'blog/post/list.html'",
            "name = 'posts'",
            "template = 'list'",
            "Bunday atributlar yo'q"
        ],
        "correct": 0
    },
    {
        "question": "86. Django formasidagi maydon turi va widget bir xil tushunchami? EmailField hamda CharField(widget=forms.Textarea) misollarida tekshiruv bilan HTML ko'rinishi o'rtasidagi farqni tushuntiring.",
        "options": [
            "Yo'q, maydon ma'lumotni tekshiradi (validation), widget esa uni HTML da qanday ko'rinishini belgilaydi",
            "Ha, bir xil",
            "Widget faqat tekshiradi",
            "Maydon HTML ni belgilaydi"
        ],
        "correct": 0
    },
    {
        "question": "87. Izohlar uchun Meta.ordering = [\"created\"] belgilangan. Uchta izoh turli vaqtda yaratilgan bo'lsa, ular qanday tartibda chiqadi? Eng yangisini avval chiqarish uchun nima o'zgartiriladi?",
        "options": [
            "Eskidan yangiga qarab chiqadi; eng yangisini avval chiqarish uchun ['-created'] qilib o'zgartiriladi",
            "Tasodifiy tartibda",
            "Teskari o'zgarmaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "88. Joriy postning hech qanday tegi bo'lmasa, umumiy teglar asosidagi tavsiyalar so'rovi qanday natija beradi? Shablonda bu holatni {% empty %} bilan qanday ko'rsatasiz?",
        "options": [
            "Bo'sh QuerySet qaytaradi; {% empty %} orqali 'O'xshash postlar yo'q' deb chiqariladi",
            "Sayt qulab tushadi",
            "Barcha postlarni chiqaradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "89. Jami e'lon qilingan postlarni sanaydigan total_posts shablon tegini yozing. Uni ro'yxatdan o'tkazish va shablonda chaqirishni koʻrsating.",
        "options": [
            "@register.simple_tag yozib, Post.published.count() qaytariladi va {% total_posts %} deb chaqiriladi",
            "{% count posts %}",
            "Python kodi shablonda yozilmaydi",
            "Bu imkoniyat yo'q"
        ],
        "correct": 0
    },
    {
        "question": "90. SearchRank qanday vazifani bajaradi? Natijalarni -rank bo'yicha saralash bilan -publish bo'yicha saralash o'rtasidagi farqni qidiruv misolida tushuntiring.",
        "options": [
            "SearchRank qidiruv so'ziga mos kelish darajasini (relevantligini) o'lchaydi; -rank eng mosini, -publish eng yangisini chiqaradi",
            "Ikkalasi bir xil",
            "Rank sanani bildiradi",
            "Publish qidiruvni belgilaydi"
        ],
        "correct": 0
    },
    {
        "question": "91. mysite loyihasi va uning ichida blog ilovasini yaratish buyruqlarini yozing. Buyruqlar qaysi ketma-ketlikda va qaysi kataloglarda bajarilishini tushuntiring.",
        "options": [
            "django-admin startproject mysite, keyin cd mysite va python manage.py startapp blog",
            "startapp keyin startproject",
            "Hammasi bitta buyruq",
            "django-admin startapp blog"
        ],
        "correct": 0
    },
    {
        "question": "92. Postning sarlavhasi, katta hajmli asosiy matni va URL yorlig'i uchun mos Django model maydonlarini tanlang. Har bir tanlovingizni vazifasiga qarab asoslang.",
        "options": [
            "Charfield (sarlavha uchun), TextField (matn uchun), SlugField (URL uchun)",
            "TextField hammasi uchun",
            "CharField hammasi uchun",
            "IntegerField"
        ],
        "correct": 0
    },
    {
        "question": "93. Sarlavhasida \"django\" so'zi bor postlarni registrni hisobga olmasdan topish uchun QuerySet yozing. exact, iexact va icontains tekshiruvlarining farqini tushuntiring.",
        "options": [
            "Post.objects.filter(title__icontains='django'); exact aniq moslik, iexact registrni inobatga olmagan aniq, icontains ichida borligini tekshiradi",
            "Farqi yo'q",
            "exact kattagina harfni farqlamaydi",
            "icontains aniq moslik"
        ],
        "correct": 0
    },
    {
        "question": "94. {{ post.body|truncatewords:30|linebreaks }} ifodasi matnni qanday qayta ishlaydi? Filtrlar qaysi tartibda bajarilishini va ro'yxat sahifasida bunday qisqartirish nega kerakligini tushuntiring.",
        "options": [
            "Avval 30 so'zga qisqartiradi, keyin HTML qator tashlashlarni qo'shadi; sahifa chiroyli chiqishi uchun kerak",
            "Faqat matnni o'chiradi",
            "Tartib ahamiyatsiz",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "95. ListViewda paginate_by=3 berilgan. Bu sozlama nima qiladi va sahifalash havolalarini chiqarishda nima uchun page_objdan foydalaniladi?",
        "options": [
            "Har bir sahifada 3 tadan post chiqaradi; page_obj joriy sahifa va sahifalash ma'lumotlarini saqlaydi",
            "Barcha postlarni chiqaradi",
            "3 ta postni o'chiradi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "96. Formada name uchun max_length=25, comments uchun required=False berilgan. Ism 30 belgidan iborat, izoh esa bo'sh yuborilsa, qaysi maydon tekshiruvdan o'tmaydi? Asoslang.",
        "options": [
            "name maydoni o'tmaydi, chunki 25 belgidan oshib ketdi; comments bo'sh bo'lishi mumkin (required=False)",
            "Ikkalasi ham o'tadi",
            "comments o'tmaydi",
            "Baza buziladi"
        ],
        "correct": 0
    },
    {
        "question": "97. Dasturchi oddiy EmailPostForm nusxasida save() chaqirmoqchi. Nega bu yondashuv noto'g'ri? ModelForm.save() bilan oddiy forma ma'lumotlarini qayta ishlashni farqlang.",
        "options": [
            "Chunki oddiy formalar model bilan bog'lanmagan va ularda save() metodi mavjud emas; ular cleaned_data orqali ishlov beriladi",
            "Oddiy forma ham save qiladi",
            "Farqi yo'q",
            "Xato chiqmaydi"
        ],
        "correct": 0
    },
    {
        "question": "98. Eng ko'p izohlangan uchta postni olishda Count(\"comments\"), annotate() va order_by() qanday birga ishlaydi? Hisoblangan total_comments modelning doimiy maydoni bo'ladimi?",
        "options": [
            "annotate qo'shimcha maydon qo'shadi, order_by saralaydi; total_comments doimiy baza maydoni emas, vaqtinchalik hisoblanadi",
            "Doimiy baza maydoni bo'ladi",
            "Xato beradi",
            "Ishlamaydi"
        ],
        "correct": 0
    },
    {
        "question": "99. show_latest_posts(count=5) tegi {% show_latest_posts 3 %} tarzida chaqirildi. Qaysi parametr qiymati ishlatiladi va eng yangi postlar sonini so'rovda qanday cheklash kerak?",
        "options": [
            "3 qiymati ishlatiladi; [:count] yoki [:3] yordamida so'rov cheklanadi",
            "5 qiymati ishlatiladi",
            "Xato beradi",
            "Cheklab bo'lmaydi"
        ],
        "correct": 0
    },
    {
        "question": "100. Qidiruvda sarlavhaga A, asosiy matnga B vazn berilgan. Bu qanday ustunlik yaratadi? rank_gte=0.3 shartida reytingi 0.2, 0.3 va 0.7 boʻlgan natijalardan qaysilari qoladi?",
        "options": [
            "Sarlavhadagi mos kelishlar muhimroq bo'ladi; 0.3 va 0.7 natijalari qoladi (0.2 tushib qoladi)",
            "Hammasi qoladi",
            "Faqat 0.7 qoladi",
            "Hech biri qolmaydi"
        ],
        "correct": 0
    },
    {
        "question": "101. Postning e'lon vaqtini saqlashda timezone.nowdan foydalanish sababini tushuntiring. USE_TZ sozlamasi sana va vaqt bilan ishlashga qanday aloqador?",
        "options": [
            "Vaqt zonalariga mos ravishda aniq vaqtni saqlash uchun; USE_TZ=True bo'lganda vaqt UTC da saqlanadi",
            "Faqat lokal vaqtni oladi",
            "Aloqasi yo'q",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "102. publish, created va updated maydonlarining vazifalarini taqqoslang. Post bir haftadan so'ng tahrirlanib saqlansa, auto_now_add va auto_now qiymatlari qanday o'zgaradi?",
        "options": [
            "created o'zgarmaydi (faqat yaratilganda yoziladi), updated har safar saqlanganda yangilanadi",
            "Ikkalasi bir xil o'zgaradi",
            "created ham yangilanadi",
            "Hech qaysi o'zgarmaydi"
        ],
        "correct": 0
    },
    {
        "question": "103. Bazada IDlari 2, 4, 7 va 9 boʻlgan postlar mavjud. id__in=[2,4,7,9] va id__gt=4 shartlari birga berilsa, qaysilari olinadi? So'rovni yozing.",
        "options": [
            "7 va 9 olinadi (4 dan katta bo'lganlar); Post.objects.filter(id__in=[2,4,7,9], id__gt=4)",
            "2, 4, 7, 9 hammasi olinadi",
            "Faqat 2 va 4",
            "Hech biri"
        ],
        "correct": 0
    },
    {
        "question": "104. urlpatternsda <slug:post>/ andozasi archive/ andozasidan oldin yozilgan. archive/ so'rovi qaysi biriga mos keladi? URLlar tartibini qanday tuzatish kerakligini asoslang.",
        "options": [
            "'archive' so'zini slug deb o'ylab xato ishlaydi; 'archive/' yuqoriga yozilishi kerak",
            "To'g'ri ishlayveradi",
            "Django buni o'zi tushunadi",
            "Xato bermaydi"
        ],
        "correct": 0
    },
    {
        "question": "105. PostListView klassini URLga bog'lashda nima uchun as_view() chaqiriladi? Klassli viewni path() bilan ulaydigan qisqa kod yozing.",
        "options": [
            "Klassni chaqiriladigan funksiyaga aylantirish uchun; path('', PostListView.as_view(), name='list')",
            "Shart emas",
            "Faqat bezak uchun",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "106. EmailPostForm() va EmailPostForm(request.POST) nusxalarini taqqoslang. Ulashish sahifasi GET bilan ochilganda va forma POST orqali yuborilganda qaysi biri ishlatiladi?",
        "options": [
            "GET da bo'sh forma () ishlatiladi, POST da ma'lumotlar bilan (request.POST) ishlatiladi",
            "Ikkalasi bir xil",
            "GET da request.POST ishlatiladi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "107. Formani {{ form.as_p }} bilan chiqarish va maydonlarini alohida chiqarishni taqqoslang. Maxsus joylashuvda maydonning yorlig'i, oʻzi va xatolari qanday olinadi?",
        "options": [
            "as_p hammasini avtomatik chiqaradi, alohida chiqarishda {{ form.name.label }}, {{ form.name }} va {{ form.name.errors }} ishlatiladi",
            "Farqi yo'q",
            "Alohida chiqarib bo'lmaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "108. Blogga django-taggit orqali teglar qo'shishning asosiy bosqichlarini yozing. Paketni o'rnatish, ilovani faollashtirish, TaggableManager qo'shish va migratsiya o'rtasidagi bog'liqlikni tushuntiring.",
        "options": [
            "pip install, INSTALLED_APPS ga qo'shish, modelga TaggableManager() yozish va makemigrations/migrate qilish",
            "Faqat install qilish yetarli",
            "Migratsiya shart emas",
            "Teggit ishlamaydi"
        ],
        "correct": 0
    },
    {
        "question": "109. {% get_most_commented_posts as most_commented_posts %} yozuvida as qanday vazifa bajaradi? Olingan natijani shablonda ro'yxatga aylantirishni qisqa kodda ko'rsating.",
        "options": [
            "Natijani yangi o'zgaruvchiga (most_commented_posts) saqlaydi va {% for %} bilan chiqariladi",
            "Ma'lumotni o'chiradi",
            "Xato beradi",
            "Faqat nom beradi"
        ],
        "correct": 0
    },
    {
        "question": "110. Search Vector va SearchQuerydagi config=\"spanish\" nimani belgilaydi? Bu sozlama matnni tarjima qilishdan qanday farqlanadi va ikki obyektga bir xil konfiguratsiya berish nega kerak?",
        "options": [
            "Qaysi til qoidalariga ko'ra stemming (so'z o'zagini topish) bajarilishini belgilaydi (tarjima qilmaydi)",
            "Matnni tarjima qiladi",
            "Farqi yo'q",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "111. requirements.txt faylidan barcha paketlarni o'rnatish buyrug'ini yozing. Bu fayl loyihani boshqa kompyuterda ishga tushirishda nima uchun kerakligini tushuntiring.",
        "options": [
            "pip install -r requirements.txt; kerakli kutubxona versiyalarini bir xilda o'rnatish uchun",
            "pip install requirements",
            "python manage.py install",
            "Kerak emas"
        ],
        "correct": 0
    },
    {
        "question": "112. Meta.ordering va Meta.indexes sozlamalarining vazifalari qanday farqlanadi? publish bo'yicha saralash hamda indeks yaratish nima uchun alohida belgilanishini tushuntiradi.",
        "options": [
            "ordering natija tartibini belgilaydi, indexes esa bazadan qidirish tezligini oshirish uchun indeks yaratadi",
            "Ikkalasi bir xil",
            "ordering bazani tezlashtiradi",
            "indexes tartiblaydi"
        ],
        "correct": 0
    },
    {
        "question": "113. Muallifining foydalanuvchi nomi \"ali\" boʻlgan, 2026-yil oktabrda e'lon qilingan postlarni oladigan QuerySet yozing. Bog'liq model maydoniga murojaat qanday yozilishini izohlang.",
        "options": [
            "Post.objects.filter(author__username='ali', publish__year=2026, publish__month=10)",
            "Post.objects.filter(author='ali')",
            "Post.objects.filter(date='2026-10')",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "114. Postlar ro'yxati va bitta post tafsilotlari uchun viewlar qaysi ma'lumotlarni shablonga uzatishi kerak? Har biri uchun kontekst lug'ati misolini yozing.",
        "options": [
            "Ro'yxat posts ni, tafsilot esa bitta post ni va form ni uzatishi kerak",
            "Faqat raqam uzatadi",
            "Hech narsa uzatmaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "115. Postning kanonik URLi nima? get_absolute_url() ichida reverse()dan foydalanish havolalarni boshqarishni qanday yengillashtiradi? Bitta post misolida tushuntiring.",
        "options": [
            "Kanonik URL - postning asosiy rasmiy manzili; reverse nom bo'yicha URL generatsiya qilib, o'zgarishlarni osonlashtiradi",
            "Tasodifiy URL",
            "Faqat IP manzil",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "116. Ulashish formasida noto'g'ri elektron pochta kiritildi. is_valid() natijasi qanday bo'ladi va foydalanuvchi xatoni tuzatishi uchun view shablonga nimani qaytarishi kerak?",
        "options": [
            "is_valid() False qaytaradi, form xatolari bilan birga yana o'sha shablonga qaytariladi",
            "True qaytaradi",
            "Bosh sahifaga o'tkazib yuboradi",
            "Server o'chadi"
        ],
        "correct": 0
    },
    {
        "question": "117. Django 5dagi as_field_group qanday ma'lumotlarni birga chiqaradi? Ism va elektron pochta maydonlarini alohida HTML konteynerlarga joylashtirishda undan qanday foydalaniladi?",
        "options": [
            "Maydon yorlig'i, input va xatolarni birgalikda render qilish uchun ishlatiladi",
            "Faqat input chiqaradi",
            "Xato beradi",
            "Ishlamaydi"
        ],
        "correct": 0
    },
    {
        "question": "118. Postda avval teg yo'q. post.tags.add(\"python\", \"django\") va keyin post.tags.remove(\"python\") bajarilsa, qanday teglar qoladi? Teglarni olish ifodasini yozing.",
        "options": [
            "Faqat 'django' tegi qoladi; post.tags.all() orqali olinadi",
            "Ikkalasi ham qoladi",
            "Hech biri qolmaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "119. Python funksiyasi markdown_format, lekin u @register.filter(name=\"markdown\") bilan ro'yxatdan o'tkazilgan. Shablonda filtr qaysi nom bilan chaqiriladi va natijada nima qaytaradi?",
        "options": [
            "|markdown nomi bilan chaqiriladi va matnni HTML ga aylantirib qaytaradi",
            "|markdown_format nomi bilan",
            "Xato beradi",
            "Hech narsa qaytarmaydi"
        ],
        "correct": 0
    },
    {
        "question": "120. PostgreSQLda trigram o'xshashligi bilan qidirish uchun pg_trgm kengaytmasi nima sababdan kerak? TrigramExtension() qatnashgan migratsiya bazada qanday tayyorgarlikni bajaradi?",
        "options": [
            "Matnlarning o'xshashligini foizda topish uchun bazada pg_trgm modulini yoqadi",
            "Bazani o'chiradi",
            "Kerak emas",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "121. Model maydonidagi default=timezone.now va db_default=Now() yozuvlarini taqqoslang. Standart sana-vaqt qiymati har bir holatda qayerda hisoblanadi?",
        "options": [
            "timezone.now Python tomonida, db_default=Now() esa to'g'ridan-to'g'ri ma'lumotlar bazasi tomonida hisoblanadi",
            "Ikkalasi bazada hisoblanadi",
            "Ikkalasi Pythonda",
            "Farqi yo'q"
        ],
        "correct": 0
    },
    {
        "question": "122. Post.Status ichida DRAFT va PUBLISHED tanlovlarini belgilashdan maqsad nima? Tanlovning nomi, bazada saqlanadigan qiymati va foydalanuvchiga ko'rinadigan yorlig'ini farqlang.",
        "options": [
            "Post holatini (qoralama yoki e'lon qilingan) boshqarish; kodda nom, bazada qisqa qiymat, ekranda yorliq ko'rinadi",
            "Faqat tartib uchun",
            "Kerak emas",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "123. 2026-yilda e'lon qilingan postlardan sarlavhasi \"Sinov\" bilan boshlanadiganlarini chiqarib tashlaydigan QuerySet yozing. filter() va exclude() bu yerda qanday hamkorlik qiladi?",
        "options": [
            "Post.objects.filter(publish__year=2026).exclude(title__startswith='Sinov')",
            "filter hammasini tashlaydi",
            "exclude hammasini oladi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "124. Brauzer /blog/33/ manzilini so'radi. URLni aniqlashdan boshlab model, view va shablon orqali HttpResponse qaytarilguncha bajariladigan asosiy bosqichlarni ketma-ket yozing.",
        "options": [
            "URL mos keladi -> View ishlaydi -> Model orqali baza olinadi -> Shablon render qilinadi -> HttpResponse qaytadi",
            "Shablon oldin ishlaydi",
            "Baza o'chadi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "125. slug maydonidagi unique_for_date=\"publish\" qanday noyoblik qoidasini bildiradi? Bir xil slugning bir sanada va turli sanalarda ishlatilishini misolda taqqoslang.",
        "options": [
            "Slug faqat bitta sanada unikal bo'lishi kerak; bir xil slug turli sanalarda takrorlanishi mumkin",
            "Slug har doim mutlaqo unikal bo'lishi shart",
            "Qoida ishlamaydi",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "126. form.cleaned_data nima uchun ishlatiladi? Xat yuborishdan oldin formani tekshirish va ma'lumotni request.POST o'rniga cleaned_datadan olish sababini tushuntiring.",
        "options": [
            "Tekshiruvdan o'tgan, toza va xavfsiz ma'lumotlarni olish uchun",
            "Faqat xom ma'lumotni oladi",
            "Kerak emas",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "127. {% with comments.count as total_comments %} yozuvining vazifasini tushuntiring. total_comments qayergacha amal qiladi va bir natijani qayta ishlatishda qanday qulaylik beradi?",
        "options": [
            "Qiymatni o'zgaruvchida saqlab turadi ({% endwith %} gacha amal qiladi), baza so'rovini kamaytiradi",
            "Doimiy saqlaydi",
            "Xato beradi",
            "Ishlamaydi"
        ],
        "correct": 0
    },
    {
        "question": "128. Post va teg orasidagi bog'lanish nima uchun ko'pdan ko'pga hisoblanadi? Ikki post hamda uchta teg misolida bitta tegning bir nechta postga bog'lanishini tushuntiring.",
        "options": [
            "Bitta postda bir nechta teg bo'lishi mumkin va bitta teg bir nechta postga tegishli bo'lishi mumkin",
            "Faqat bittaga bir",
            "Bog'lanish yo'q",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "129. Markdown matnini HTMLga aylantirish va uni 30 soʻzgacha qisqartirish kerak. markdown() hamda truncatewords_html()ni qaysi tartibda qoʻllaysiz va nima uchun HTMLga mos qisqartirish kerak?",
        "options": [
            "Avval markdown() bilan HTMLga o'girilib, keyin truncatewords_html() qo'llaniladi (taglar buzilmasligi uchun)",
            "Ters tartibda",
            "Farqi yo'q",
            "Xato beradi"
        ],
        "correct": 0
    },
    {
        "question": "130. Foydalanuvchi \"Django\" o'rniga \"Djnago\" deb yozdi. TrigramSimilarity bunday qidiruvda qanday yordam beradi? O'xshashlik chegarasini oshirish natijalar soniga qanday ta'sir qilishi mumkin?",
        "options": [
            "Harflar xatolariga qaramay o'xshash so'zlarni topadi; chegarani oshirish natijalar sonini kamaytiradi, lekin aniqlikni oshiradi",
            "Qidiruvni o'chiradi",
            "Farqi yo'q",
            "Xato beradi"
        ],
        "correct": 0
    }
] 