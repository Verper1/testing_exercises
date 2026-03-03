def genderalize(verb_male: str, verb_female: str, gender: str) -> str:
    """
    Принимает глаголы в мужском и женском роде, а также пол на английском языке.
    Отдаёт нужный глагол, основываясь на введённом поле.

    Пример: genderalize("Пошёл", "Пошла", "male") -> "Пошёл"
    """
    return verb_male if gender == "male" else verb_female
