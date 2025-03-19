try:
    name = input("Enter the your name : ")
    assert name.isalpha()
except:
    raise ValueError('You did not enter correct username')
else:
    print('your name: ', name)

finally:
    print('it done')
