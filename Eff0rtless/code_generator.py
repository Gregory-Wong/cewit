def codegen():
  from random import randint
  #generate code
  code = randint(00000, 99999)
  med = setMed() #swithc this for the function that records the doctor choice of medicines
  mcode = str (code) +med
  return mcode

