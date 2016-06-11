use cp.tmp;
ALTER SESSION SET `store.format`='json';
CREATE TABLE `/xampp2/htdocs/python/output6` AS
SELECT B.full_address, B.name, A.text
FROM cp.`xampp2/htdocs/python/apache-drill-1.6.0/yelp_academic_dataset_business.json` B,
cp.`xampp2/htdocs/python/apache-drill-1.6.0/yelp_academic_dataset_review.json` A
WHERE B.city LIKE '%Montreal%' 
AND A.business_id = B.business_id
LIMIT 10000000;


//C:\

xampp2/htdocs/python
