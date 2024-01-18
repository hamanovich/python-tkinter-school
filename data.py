project_title = "Биология"

menu_buttons = [
    ("botanika", "Ботаника", "images/botanika/botanika_logo.png"),
    ("anatomy", "Анатомия", "images/anatomy/anatomy_logo.png"),
    ("cytology", "Цитология", "images/cytology/cytology_logo.png")
]

data = {
    "botanika": {
        "intro": "Бота́ника — наука о растениях, раздел биологии.",
        "details": ("Ботаника охватывает широкий круг проблем: закономерности внешнего и внутреннего строения (морфология и анатомия) растений, их систематику, развитие в течение геологического времени (эволюция) и родственные связи (филогенез), особенности прошлого и современного распространения по земной поверхности (география растений), взаимоотношения со средой (экология растений), сложение растительного покрова (фитоценология, или геоботаника), возможности и пути хозяйственного использования растений (ботаническое ресурсоведение, или экономическая ботаника).",
                    "Ботаника пользуется как наблюдением, так и сравнительным, историческим и экспериментальным методами, включающими сбор и составление коллекций, наблюдение в природе и на опытных участках, эксперимент в природе и в условиях специализированных лабораторий, математическую обработку полученной информации."),
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
                "answer": "15483"
            },
            {
                "name": "Решить кроссворд",
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
                "answer": "семязачаток"
            },
            {
                "name": "Создайте цикл растения, располагая картинки в правильной последовательности",
                "options": [
                    (1, {"x": 20, "y": 135,
                     "img_path": "images/botanika/botanika_3_3-01.png"}),
                    (2, {"x": 200, "y": 20,
                     "img_path": "images/botanika/botanika_3_3-02.png"}),
                    (3, {"x": 320, "y": 5,
                     "img_path": "images/botanika/botanika_3_3-03.png"}),
                    (4, {"x": 460, "y": 75,
                     "img_path": "images/botanika/botanika_3_3-04.png"}),
                    (5, {"x": 485, "y": 150,
                     "img_path": "images/botanika/botanika_3_3-05.png"}),
                    (6, {"x": 535, "y": 290,
                     "img_path": "images/botanika/botanika_3_3-06.png"}),
                    (7, {"x": 500, "y": 430,
                     "img_path": "images/botanika/botanika_3_3-07.png"}),
                    (8, {"x": 355, "y": 445,
                     "img_path": "images/botanika/botanika_3_3-08.png"}),
                    (9, {"x": 125, "y": 440,
                     "img_path": "images/botanika/botanika_3_3-09.png"}),
                    (10, {"x": 40, "y": 310,
                     "img_path": "images/botanika/botanika_3_3-10.png"}),
                ],
            }
        ]},

    "anatomy": {
        "intro": "Анато́мия — раздел биологии, изучающий строение тела, организмов и их частей на уровне выше тканевого.",
        "details": ("Анатомия как наука изучает не только внешнее строение организма в целом, но и внутреннюю форму и структуру органов, входящих в его состав.",
                    "Анатомия человека — раздел биологии, изучающий морфологию человеческого организма, его систем и органов, а также структуры и взаимное расположение.",
                    "Анатомия человека — одна из фундаментальных дисциплин в системе медицинского и биологического образования, тесно связанная с такими отделившимися от неё дисциплинами, как антропология и физиология человека, а также сравнительной анатомией, эволюционным учением и генетикой."),
        "tasks": [
            {
                "name": "При лечении заболевания сердца использовали бицилин в виде внутримышечных инъекций в ягодичную мышцу.Проследите путь перемещения лекарства в организме человека до органа мишени, выбрав все подходящие элементы из предложенных:",
                "options": [
                    (1, "Аорта"),
                    (2, "Капилляры ягодичных мышц"),
                    (3, "Нижняя полая вена"),
                    (4, "Венечная артерия сердца"),
                    (5, "Печень"),
                    (6, "Сердце (камеры)"),
                    (7, "Капилляры легких")
                ],
                "answer": "2367614"
            },
            {
                "name": "Подпишите части глаза, перетягивая слова на нужные позиции",
                "options": [
                    # TODO: Fix coords
                    ("стекловидное тело", {"x": 260, "y": 130}),
                    ("зрительный нерв", {"x": 270, "y": 315}),
                    ("передняя камера", {"x": 60, "y": 320}),
                    ("хрусталик", {"x": 85, "y": 120}),
                    ("роговица", {"x": 55, "y": 265}),
                    ("зрачок", {"x": 100, "y": 290}),
                    ("склера", {"x": 295, "y": 80}),
                    ("сетчатка", {"x": 290, "y": 105}),
                ],
                "meta": {
                    "youtube": "https://youtu.be/rSVDJyqHXQk?si=3pPhfFCKeMs-yn3R"
                }
            },
            {
                "name": "Перетащите макро и микроэлементы в соответствующие ячейки",
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
                "meta": {
                    "youtube": "https://youtu.be/617BSY5V4EY?si=dlY24oS5JMbuYpNj"
                }
            }
        ]},

    "cytology": {
        "intro": "Цитоло́гия — раздел биологии, изучающий живые клетки, их органеллы, их строение, функционирование, процессы деления, старения и смерти.",
        "details": ("Термин «клетка» впервые использовал Роберт Гук в 1665 году, при описании своих «исследований строения пробки с помощью увеличительных линз». В 1674 году Антони ван Левенгук установил, что вещество, находящееся внутри клетки, определённым образом организовано. Он первым обнаружил клеточные ядра.",
                    "Важнейшим дополнением клеточной теории явилось утверждение знаменитого немецкого натуралиста Рудольфа Вирхова, что каждая клетка образуется в результате деления другой клетки."),
        "tasks": [
            {
                "name": "Создать растительную клетку. Для этого перетащите только нужные органоиды на нее.",
                "options": [
                    ("аппарат гольджи", {
                     "required": True, "img_path": "images/cytology/аппарат_гольджи.png"}),
                    ("вакуоль", {"required": True,
                     "img_path": "images/cytology/вакуоль.png"}),
                    ("жгутик", {"required": False,
                     "img_path": "images/cytology/жгутик.png"}),
                    ("ядро", {"required": True,
                     "img_path": "images/cytology/ядро.png"}),
                    ("кольцевая днк", {"required": False,
                     "img_path": "images/cytology/кольцевая_днк.png"}),
                    ("лизосома", {"required": True,
                     "img_path": "images/cytology/лизосома.png"}),
                    ("митохондрия", {"required": True,
                     "img_path": "images/cytology/митохондрия.png"}),
                    ("хлоропласт", {"required": True,
                     "img_path": "images/cytology/хлоропласт.png"}),
                    ("центриоль", {"required": False,
                     "img_path": "images/cytology/центриоль.png"}),
                ],
            },
            {
                "name": "Какие органоиды к чему относятся?",
                "options": [
                    ("вакуоль", "одномембранные"),
                    ("хлоропласты", "двумембранные"),
                    ("митохондрии", "двумембранные"),
                    ("лизосомы", "одномембранные"),
                    ("ЭПС", "одномембранные"),
                    ("аппарат гольджи", "одномембранные"),
                    ("рибосомы", "немембранные"),
                    ("центриоли", "немембранные"),
                ]
            },
            {
                "name": "Собрать слои эпидермиса в правильной последовательности",
                "options": [
                    ("дерма", {
                     "x": 0, "y": 415, "hint_y": 450, "img_path": "images/cytology/cytology_3_3_01.jpg"}),
                    ("базальный", {
                     "x": 0, "y": 356, "hint_y": 375, "img_path": "images/cytology/cytology_3_3_02.jpg"}),
                    ("шиповатый", {
                     "x": 0, "y": 285, "hint_y": 300, "img_path": "images/cytology/cytology_3_3_03.jpg"}),
                    ("зернистый", {
                     "x": 0, "y": 164, "hint_y": 210, "img_path": "images/cytology/cytology_3_3_04.jpg"}),
                    ("блестящий", {
                     "x": 0, "y": 94, "hint_y": 120, "img_path": "images/cytology/cytology_3_3_05.jpg"}),
                    ("роговой", {
                     "x": 0, "y": 0, "hint_y": 35, "img_path": "images/cytology/cytology_3_3_06.jpg"}),
                ]
            }
        ]
    },
}
