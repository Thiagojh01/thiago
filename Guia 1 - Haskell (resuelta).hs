longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t 
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- [1,2,3,4,5]
-- [5] : [1,2,3,4]
-- 
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = ultimo (x:xs) : reverso (principio (x:xs))

-- 3 [1,2,3,4,5]
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

-- [3,3,3,4]
-- 3 [3,3,4]
-- 3 \= 3
-- otherwise = todosIguales [3,3,4]
-- [3,3,4] 
-- 3 [3,4]
-- 3 \= 3
-- 
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) | longitud xs == 0 = True
                    | x /= head xs = False
                    | otherwise = todosIguales xs

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:xs) | longitud xs == 0 = True
                      | x == head xs = False
                      | otherwise = todosDistintos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs

-- 4 [6,4,4,2]
-- 4 == 6 

quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e /= x = x : quitar e xs
                | otherwise = xs


quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) | e /= x = x : quitarTodos e xs
                     | otherwise = quitarTodos e xs

-- [3,4,4,5,6,5]
-- [4,4,5,6,5]
-- [4,5,6,5]
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = eliminarRepetidos xs
                         | otherwise = x : eliminarRepetidos xs

-- [4,5,5,6,3]
-- [6,5,4,4]

-- [4,5,6,3]
-- [6,5,4]

-- [5,6,3]
-- [6,5]

-- [6,3]
-- [6]

-- [3]
-- []

-- [4,5,5,6]
-- [6,5,4,4,3,3]

-- [4,5,6]
-- [6,5,4,3]

-- [5,6]
-- [6,5,3]

-- [6]
-- [6,3]

-- []
-- [3]
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [x] [] = False
mismosElementos [] [x] = False
mismosElementos l1 l2 | 
