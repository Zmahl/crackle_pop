def crackle_pop():
  end = 100

  for num in range(1, end + 1):
    message = ""

    if num % 3 == 0:
      message += "Crackle"
    if num % 5 == 0:
      message += "Pop"

    if message:
      print(message)
    else:
      print(num)

  return


crackle_pop()