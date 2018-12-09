def get_vat(payment, percent=18):
    print(percent)
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * 18
        vat = round(vat, 2)
        return print("Summ NDS: {}".format(vat))
    except (TypeError, ValueError):
        return "Did not calculate youre digits"
    pass

result = get_vat(150000,18)
print(result)
