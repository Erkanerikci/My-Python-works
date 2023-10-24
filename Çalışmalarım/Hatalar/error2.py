while True:
    try:
        x = int(input('x:  '))
        y = int(input('y:  '))
        print(x/y)
    # except ZeroDivisionError:
    #     print('y için 0 girilemez...')
    # except ValueError:
    #     print('x ve y için sayısal değerler girin')

    except (ZeroDivisionError,ValueError) as e:
        print('Hata yaptınız.')
        print(e)
    else:
        break
    finally:
        print('Döngü sonlandı.')