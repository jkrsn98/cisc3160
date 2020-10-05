-- Multiples of 3 and 5
print("multiples_of_3_and_5")
max = 1000
total = 0
for i = 1, (max-1) do
  if (i%3 == 0) or (i%5 == 0)  then
    total = total + i
  end
end
print(total)
print("----------------------")



-- Even fibonnaci numbers
print("even_fibonacci_numbers")
max = 4000000
a, b, total = 1, 2, 0
while b <= max do
  if b % 2 == 0 then
    total = total + b
  end
  a, b = b, a + b
end
print(total)
print("----------------------")



-- Sum square difference
print("sum_square_difference")
max = 100
sum, sum2 = 0, 0
for i = 1, max do
  sum, sum2 = sum + i, sum2 + (i * i)
end
print((sum*sum) - sum2)
print("----------------------")
