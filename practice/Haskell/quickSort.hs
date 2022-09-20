quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (p:xs) = (quicksort lesser) ++ [p] ++ (quicksort greater)
    where
        lesser  = filter (< p) xs
        greater = filter (>= p) xs

n :: Integer
n = 1234567890987654321987340982334987349872349874534

--reallyBig :: Integer
--reallyBig = 2^(2^(2^(2^2)))

--numDigits :: Int
--numDigits = length (show reallyBig)