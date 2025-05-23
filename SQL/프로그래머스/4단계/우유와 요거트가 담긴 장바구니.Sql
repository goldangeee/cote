# SELECT Yogurt.CART_ID
# FROM (SELECT CART_ID
# FROM CART_PRODUCTS
# WHERE NAME = "Yogurt") AS Yogurt

# JOIN (SELECT CART_ID
# FROM CART_PRODUCTS
# WHERE NAME = "Milk") AS Milk ON Yogurt.CART_ID = Milk.CART_ID
# ORDER BY Yogurt.CART_ID;

SELECT CART_ID
FROM (
    SELECT CART_ID,NAME
    FROM CART_PRODUCTS
    WHERE NAME = "Yogurt"
    
    UNION ALL
    
    SELECT CART_ID,NAME
    FROM CART_PRODUCTS
    WHERE NAME = "Milk"
) AS Combined
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) = 2
ORDER BY CART_ID;