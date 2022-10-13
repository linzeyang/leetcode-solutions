-- 1393. Capital Gain/Loss

SELECT SELL.stock_name, (SELL.earn - BUY.loss) AS capital_gain_loss
FROM (
    SELECT stock_name, SUM(price) AS earn
    FROM Stocks
    WHERE operation LIKE "Sell"
    GROUP BY stock_name
) AS SELL
JOIN (
    SELECT stock_name, SUM(price) AS loss
    FROM Stocks
    WHERE operation LIKE "Buy"
    GROUP BY stock_name
) AS BUY
ON SELL.stock_name = BUY.stock_name;
