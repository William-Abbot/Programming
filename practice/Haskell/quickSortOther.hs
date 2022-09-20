import Debug.Trace

quickSort :: Ord a => [a] -> [a]
quickSort []     = []
quickSort (x:xs) = quickSort (filter (<x) xs)
                   ++ [x] ++
                   quickSort (filter (>=x) xs)


main = print (quickSort [5, 4, 6, 7, 1, 99])