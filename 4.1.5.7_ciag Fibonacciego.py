# funkcja, która tworzy liste
# od 1 do zadanej liczby
# nastepnie poprzez petle tworzy obliczanie wartosci

def fib (n):
      
    a = 0
    b = 1
    print ("wartość nr:  1 wynosi:", a,)
    licz = 2
  
    for i in range (n-1):
        print ("Wartość nr: ", licz, "wynosi:", b)
        a,b = b, a+b
        licz += 1
      
fib (20)

