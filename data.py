project_title = "Биология"

menu_buttons = [
    ("Ботаника", "images/botanika_logo.png"),
    ("Анатомия", "images/anatomy_logo.png"),
    ("Цитология", "images/cytology_logo.png")
]

data = {
    "Ботаника": {
        "tasks": [
            {
                "name": "Необходимо классифицировать вишню обыкновенную, расположив в порядке иерархичности (начиная с наименьшего ранга) 5 подходящих элементов из предложенных",
                "options": [
                    (1, "род Вишня"),
                    (2, "отряд Цветковые"),
                    (3, "царство Растения"),
                    (4, "класс Двудольные"),
                    (5, "семейство Розовые"),
                    (6, "семейство Бобовые"),
                    (7, "класс Однодольные"),
                    (8, "отдел Покрытосеменные"),
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
                "name": "Сопоставьте слова слева с определениями справа, перетягивая их друг на друга",
                "options": [
                    ("Кислород", "Входит в состав большинства органических и многих неорганических веществ. Обеспечивает клеточное дыхание и другие окислительные процессы, в ходе которых выделяется необходимая организму энергия"),
                    ("Калий", "Участвует в генерации нервных импульсов, регули-рует ритм сердечной деятельности. Также участвует в процессе фотосинтеза"),
                    ("Магний", "Входит в состав хлорофилла, многих ферментов, а также в состав костной ткани и эмали зубов"),
                    ("Цинк", "Входит в состав инсулина и многих ферментов. Принимает участие в процессах синтеза гормонов растений"),
                    ("Кобальт", "Входит в состав витамина В12, участвует в процессах кроветворения. Необходим для синтеза хлорофилла"),
                ],
                "answer": None
            }
        ]},

    "Анатомия": {
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

    "Цитология": {
        "intro": "Цитоло́гия — раздел биологии, изучающий живые клетки, их органеллы, их строение, функционирование, процессы деления, старения и смерти.",
        "tasks": []
    },
}
