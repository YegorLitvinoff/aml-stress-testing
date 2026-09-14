SELECT 
    client_id,
    COUNT(transaction_id) as count_suspicious_tx,
    SUM(amount) as total_amount_rub
FROM 
    dwh.transactions
WHERE 
    amount BETWEEN 550000 AND 599999
    AND transaction_date >= '2026-09-01'
GROUP BY 
    client_id
HAVING 
    COUNT(transaction_id) >= 3
ORDER BY 
    total_amount_rub DESC;
