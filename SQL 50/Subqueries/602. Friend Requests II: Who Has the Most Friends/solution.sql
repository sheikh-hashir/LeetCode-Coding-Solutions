WITH virtualrequestaccepted AS
(
       SELECT requester_id AS id FROM   requestaccepted
       UNION ALL
       SELECT accepter_id AS id FROM   requestaccepted
)
SELECT   id, Count(*) AS num
FROM     virtualrequestaccepted
GROUP BY id
ORDER BY num DESC limit 1