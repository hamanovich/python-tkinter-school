project_title = "Биология"

menu_buttons = [
    ("botanika", "Ботаника", "images/botanika_logo.png"),
    ("anatomy", "Анатомия", "images/anatomy_logo.png"),
    ("cytology", "Цитология", "images/cytology_logo.png")
]

copyrights = "СШ №8, 2024"

messages = {
    "task_success_title": "Задание пройдено!",
    "task_success_text": "Вы набрали 1 бал и готовы к выполнению следующего задания",
    "task_error_title": "Задание пройдено с ошибкой!",
    "task_error_text": "Вы ошиблись при выполнении задания и не набрали 1 бал. Переходим к выполнению следующего задания",
    "msg_result_0": "Вы не решили ни одного задания. Возможно вы были не готовы и вам необходимо повторить материал и начать прохождение заново.",
    "msg_result_less_5": "К сожалению вы смогли справиться только с несколькими заданиями. Попробуйте заново, как будете готовы.",
    "msg_result_5_6": "Вы неплохо справились с большинством заданий, но допустили несколько ошибок. Попробуйте заново и у вас непременно получится еще лучше!",
    "msg_result_7_8": "Поздравляем, вы отлично справились практически со всеми заданиями и прошли игру! Не останавливайтесь на достигнутом!",
    "msg_result_9": "Невероятно! Вы прошли всю игру без ошибок. Так держать! Гордимся вами!",
}

results = {
    "awfull": {
        "msg_result": messages["msg_result_0"],
        "msg_image_path": "images/sunflower_spoiled.png",
        "msg_audio_path": "audio/msg_result_0.mp3"
    },
    "bad": {
        "msg_result": messages["msg_result_less_5"],
        "msg_image_path": "images/sunflower_sad.png",
        "msg_audio_path": "audio/msg_result_less_5.mp3"
    },
    "ok": {
        "msg_result": messages["msg_result_5_6"],
        "msg_image_path": "images/sunflower_ok.png",
        "msg_audio_path": "audio/msg_result_5_6.mp3"
    },
    "great": {
        "msg_result": messages["msg_result_7_8"],
        "msg_image_path": "images/sunflower_smile.png",
        "msg_audio_path": "audio/msg_result_7_8.mp3"
    },
    "awesome": {
        "msg_result": messages["msg_result_9"],
        "msg_image_path": "images/sunflower_smile.png",
        "msg_audio_path": "audio/msg_result_9.mp3"
    },
}

intro = {
    "title": "Правила игры",
    "rules": [
        "Доброе пожаловать в увлекательный мир Биологии!",
        "Впереди вас ждёт множество увлекательных, интерактивных и интересных заданий.",
        "Постарайтесь не спешить, внимательно прочитайте задание и приступайте к его выполнению.",
        "Когда задание будет сделано, нажмите на кнопку \"Проверить результат\" или просто клавишу Enter.",
        "Если во время прохождения игры вы нажмёте на элементы в боковом меню или закроете приложение, то вам придется начинать игру с самого начала.",
        "Каждое задание сопровождается голосовым сообщением, которое можно отключить или прослушать заново.",
        "В конце игры мы посчитаем количество набранных баллов и поделимся результатом с вами."
    ],
    "image_path": "images/bio_rules.png",
}

content = {
    "botanika": {
        "title": "Бота́ника — наука о растениях, раздел биологии.",
        "details": ("Ботаника охватывает широкий круг проблем: закономерности внешнего и внутреннего строения растений, их систематику, развитие в течение геологического времени и родственные связи, особенности прошлого и современного распространения по земной поверхности, взаимоотношения со средой, сложение растительного покрова, возможности и пути хозяйственного использования растений.",
                    "Ботаника пользуется как наблюдением, так и сравнительным, историческим и экспериментальным методами, включающими сбор и составление коллекций, наблюдение в природе и на опытных участках, эксперимент в природе и в условиях специализированных лабораторий, математическую обработку полученной информации."),
        "preview": {
            "img_path": "images/botanika_landing.png",
            "width": 650,
            "height": 386
        },
        "meta": {
            "link_text": "Узнать больше на Википедии",
            "link": "https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D1%82%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0"
        },
        "audio": "audio/botanika.mp3",
        "tasks": [
            {
                "name": "Необходимо классифицировать вишню обыкновенную, расположив в порядке иерархичности (начиная с наименьшего ранга) 5 подходящих элементов из предложенных",
                "options": [
                    (1, "Род Вишня"),
                    (2, "Отряд Цветковые"),
                    (3, "Царство Растения"),
                    (4, "Класс Двудольные"),
                    (5, "Семейство Розовые"),
                    (6, "Семейство Бобовые"),
                    (7, "Класс Однодольные"),
                    (8, "Отдел Покрытосеменные"),
                ],
                "answer": "15483",
                "audio": "audio/task_1_1.mp3"
            },
            {
                "name": "Решите кроссворд, ответив на 11 вопросов. В результате по вертикали у вас получится ключевое слово",
                "options": [
                    {
                        "question": "Орган растения, осуществляющий процесс фотосинтеза",
                        "answer": "лист",
                        "padLeft": 5
                    },
                    {
                        "question": "Многолетнее растение с одревесневшим стволом и лиственной кроной",
                        "answer": "дерево",
                        "padLeft": 6
                    },
                    {
                        "question": "Проводящая ткань растений",
                        "answer": "флоэма",
                        "padLeft": 3
                    },
                    {
                        "question": "Многоклеточная структура растений, содержащая зародыш",
                        "answer": "семя",
                        "padLeft": 4
                    },
                    {
                        "question": "Лиственное белоствольное дерево",
                        "answer": "береза",
                        "padLeft": 3
                    },
                    {
                        "question": "Наука о растениях",
                        "answer": "ботаника",
                        "padLeft": 4
                    },
                    {
                        "question": "Мужской репродуктивный орган растения, в котором образуется пыльца",
                        "answer": "тычинка",
                        "padLeft": 5
                    },
                    {
                        "question": "Пластиды, содержащие фотосинтезирующий пигмент",
                        "answer": "хлоропласты",
                        "padLeft": 0
                    },
                    {
                        "question": "Многолетнее деревянистое растение, не имеющее во взрослом состоянии главного ствола",
                        "answer": "кустарник",
                        "padLeft": 4
                    },
                    {
                        "question": "Осевой подземный вегетативный орган растения",
                        "answer": "корень",
                        "padLeft": 6
                    },
                    {
                        "question": "Система пучков в листовых пластинах, посредством которых осуществляется транспорт веществ",
                        "answer": "жилкование",
                        "padLeft": 4
                    },
                ],
                "answer": "семязачаток",
                "audio": "audio/task_1_2.mp3"
            },
            {
                "name": "Создайте цикл растения, располагая картинки в правильной последовательности",
                "options": [
                    (1, {"x": 20, "y": 135,
                     "img_path": "images/botanika_3_3-01.png"}),
                    (2, {"x": 200, "y": 20,
                     "img_path": "images/botanika_3_3-02.png"}),
                    (3, {"x": 320, "y": 5,
                     "img_path": "images/botanika_3_3-03.png"}),
                    (4, {"x": 460, "y": 75,
                     "img_path": "images/botanika_3_3-04.png"}),
                    (5, {"x": 485, "y": 150,
                     "img_path": "images/botanika_3_3-05.png"}),
                    (6, {"x": 535, "y": 290,
                     "img_path": "images/botanika_3_3-06.png"}),
                    (7, {"x": 500, "y": 430,
                     "img_path": "images/botanika_3_3-07.png"}),
                    (8, {"x": 355, "y": 445,
                     "img_path": "images/botanika_3_3-08.png"}),
                    (9, {"x": 125, "y": 440,
                     "img_path": "images/botanika_3_3-09.png"}),
                    (10, {"x": 40, "y": 310,
                     "img_path": "images/botanika_3_3-10.png"}),
                ],
                "bg": "images/botanika_3_3-00.png",
                "audio": "audio/task_1_3.mp3"
            }
        ]},

    "anatomy": {
        "title": "Анато́мия — раздел биологии, изучающий строение тела, организмов и их частей на уровне выше тканевого.",
        "details": ("Анатомия как наука изучает не только внешнее строение организма в целом, но и внутреннюю форму и структуру органов, входящих в его состав.",
                    "Анатомия человека — одна из фундаментальных дисциплин в системе медицинского и биологического образования, тесно связанная с такими отделившимися от неё дисциплинами, как антропология и физиология человека, а также сравнительной анатомией, эволюционным учением и генетикой."),
        "preview": {
            "img_path": "images/anatomy_landing.png",
            "width": 650,
            "height": 484
        },
        "meta": {
            "link_text": "Узнать больше на Википедии",
            "link": "https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D0%B0%D1%82%D0%BE%D0%BC%D0%B8%D1%8F"
        },
        "audio": "audio/anatomy.mp3",
        "tasks": [
            {
                "name": "При лечении заболевания сердца использовали бициллин в виде внутримышечных инъекций в ягодичную мышцу. Проследите путь перемещения лекарства в организме человека до органа мишени, выбрав все подходящие элементы из предложенных",
                "options": [
                    (1, "Аорта"),
                    (2, "Капилляры ягодичных мышц"),
                    (3, "Нижняя полая вена"),
                    (4, "Венечная артерия сердца"),
                    (5, "Печень"),
                    (6, "Сердце (камеры)"),
                    (7, "Капилляры легких")
                ],
                "answer": "2367614",
                "audio": "audio/task_2_1.mp3"
            },
            {
                "name": "Подпишите части глаза, перетягивая слова на нужные позиции",
                "options": [
                    ("стекловидное тело", {"x": 455, "y": 190}),
                    ("зрительный нерв", {"x": 430, "y": 470}),
                    ("передняя камера", {"x": 50, "y": 480}),
                    ("хрусталик", {"x": 85, "y": 175}),
                    ("роговица", {"x": 60, "y": 385}),
                    ("зрачок", {"x": 85, "y": 430}),
                    ("склера", {"x": 465, "y": 100}),
                    ("сетчатка", {"x": 470, "y": 145}),
                ],
                "bg": "images/eye.png",
                "meta": {
                    "link_text": "Узнать больше на Youtube.com",
                    "link": "https://youtu.be/rSVDJyqHXQk?si=3pPhfFCKeMs-yn3R"
                },
                "audio": "audio/task_2_2.mp3"
            },
            {
                "name": "Перетащите макро и микроэлементы в соответствующие ячейки",
                "elements": [
                    ("микроэлемент", {"x": 110, "y": 15}),
                    ("макроэлемент", {"x": 435, "y": 15}),
                ],
                "options": [
                    ("Fe", "микроэлемент"),
                    ("Zn", "микроэлемент"),
                    ("Cu", "микроэлемент"),
                    ("F", "микроэлемент"),
                    ("I", "микроэлемент"),
                    ("Mn", "микроэлемент"),
                    ("Co", "микроэлемент"),
                    ("C", "макроэлемент"),
                    ("O", "макроэлемент"),
                    ("H", "макроэлемент"),
                    ("Cl", "макроэлемент"),
                    ("N", "макроэлемент"),
                    ("Ca", "макроэлемент"),
                    ("P", "макроэлемент"),
                    ("K", "макроэлемент"),
                    ("S", "макроэлемент"),
                    ("Na", "макроэлемент"),
                    ("Mg", "макроэлемент"),
                ],
                "answers": [
                    (290, 205),
                    (335, 205),
                ],
                "meta": {
                    "link_text": "Узнать больше на Youtube.com",
                    "link": "https://youtu.be/617BSY5V4EY?si=dlY24oS5JMbuYpNj"
                },
                "audio": "audio/task_2_3.mp3"
            }
        ]},

    "cytology": {
        "title": "Цитоло́гия — раздел биологии, изучающий живые клетки, их органеллы, их строение, функционирование, процессы деления, старения и смерти.",
        "details": ("Термин «клетка» впервые использовал Роберт Гук в 1665 году, при описании своих «исследований строения пробки с помощью увеличительных линз». В 1674 году Антони ван Левенгук первым обнаружил клеточные ядра.",),
        "preview": {
            "img_path": "images/cytology_landing.png",
            "width": 650,
            "height": 571
        },
        "meta": {
            "link_text": "Узнать больше на Википедии",
            "link": "https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F"
        },
        "audio": "audio/cytology.mp3",
        "tasks": [
            {
                "name": "Создайте растительную клетку. Перетащите только нужные органоиды",
                "options": [
                    ("аппарат гольджи", {
                     "required": True, "img_path": "images/аппарат_гольджи.png"}),
                    ("вакуоль", {"required": True,
                     "img_path": "images/вакуоль.png"}),
                    ("жгутик", {"required": False,
                     "img_path": "images/жгутик.png"}),
                    ("ядро", {"required": True,
                     "img_path": "images/ядро.png"}),
                    ("кольцевая днк", {"required": False,
                     "img_path": "images/кольцевая_днк.png"}),
                    ("лизосома", {"required": True,
                     "img_path": "images/лизосома.png"}),
                    ("митохондрия", {"required": True,
                     "img_path": "images/митохондрия.png"}),
                    ("хлоропласт", {"required": True,
                     "img_path": "images/хлоропласт.png"}),
                    ("центриоль", {"required": False,
                     "img_path": "images/центриоль.png"}),
                ],
                "answers": [15, 350, 30, 380],
                "bg": "images/клетка.png",
                "audio": "audio/task_3_1.mp3"
            },
            {
                "name": "Какие органоиды к какому типу относятся? Для каждого органа выберите один из трех вариантов ответа",
                "options": [
                    ("вакуоль", "одномембранные"),
                    ("хлоропласты", "двумембранные"),
                    ("митохондрии", "двумембранные"),
                    ("лизосомы", "одномембранные"),
                    ("ЭПС", "одномембранные"),
                    ("аппарат гольджи", "одномембранные"),
                    ("рибосомы", "немембранные"),
                    ("центриоли", "немембранные"),
                ],
                "audio": "audio/task_3_2.mp3"
            },
            {
                "name": "Соберите слои эпидермиса в правильной последовательности",
                "options": [
                    ("дерма", {
                     "x": 0, "y": 415, "hint_y": 450, "img_path": "images/cytology_3_3_01.png"}),
                    ("базальный", {
                     "x": 0, "y": 356, "hint_y": 375, "img_path": "images/cytology_3_3_02.png"}),
                    ("шиповатый", {
                     "x": 0, "y": 285, "hint_y": 300, "img_path": "images/cytology_3_3_03.png"}),
                    ("зернистый", {
                     "x": 0, "y": 164, "hint_y": 210, "img_path": "images/cytology_3_3_04.png"}),
                    ("блестящий", {
                     "x": 0, "y": 94, "hint_y": 120, "img_path": "images/cytology_3_3_05.png"}),
                    ("роговой", {
                     "x": 0, "y": 0, "hint_y": 35, "img_path": "images/cytology_3_3_06.png"}),
                ],
                "bg": "images/cytology_3_3_00.png",
                "audio": "audio/task_3_3.mp3"
            }
        ]
    },
}
