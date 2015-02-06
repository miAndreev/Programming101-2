def what_is_my_sign(day, month):
    if month > 12 or month < 1:
        exit("Invalid month number.")
    if month == 1:
        if day > 20:
            return "Aquarius"
        else:
            return "Capricorn"
    elif month == 2:
        if day > 19:
            return "Pisces"
        else:
            return "Aquarius"
    elif month == 3:
        if day > 20:
            return "Aries"
        else:
            return "Pisces"
    elif month == 4:
        if day > 20:
            return "Taurus"
        else:
            return "Aries"
    elif month == 5:
        if day > 21:
            return "Gemini"
        else:
            return "Taurus"
    elif month == 6:
        if day > 21:
            return "Cancer"
        else:
            return "Gemini"
    elif month == 7:
        if day > 22:
            return "Leo"
        else:
            return "Cancer"
    elif month == 8:
        if day > 22:
            return "Virgo"
        else:
            return "Leo"
    elif month == 9:
        if day > 23:
            return "Libra"
        else:
            return "Virgo"
    elif month == 10:
        if day > 23:
            return "Scorpio"
        else:
            return "Libra"
    elif month == 11:
        if day > 22:
            return "Sagittarius"
        else:
            return "Scorpio"
    else:
        if day > 21:
            return "Capricorn"
        else:
            return "Sagittarius"