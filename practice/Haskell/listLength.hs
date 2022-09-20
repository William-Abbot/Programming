-- Compute the length of a list of Integers
intListLength :: [Integer] -> Integer
intListLength [] = 0
intListLength (x:y) = 1 + intListLength y

main = print (intListLength [1,2,3,4,5])