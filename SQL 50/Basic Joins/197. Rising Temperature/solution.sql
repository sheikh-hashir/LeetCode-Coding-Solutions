SELECT w1.id AS Id FROM Weather w JOIN Weather w1 ON DATEDIFF(w1.recordDate, w.recordDate) = 1 WHERE w1.temperature > w.temperature;
