-- Running Spark Queries (20 pts)

-- 1. What is the total number of RDF rows in the data? (2 pts)

select count(*) from fbFacts
--Result
--563,980,447

-- 2. What is the number of distinct predicates in the data? (2 pts) 

select count(distinct predicates) from fbFacts;
--Result
--18,944

-- 3. In the example in the description, we showed some tuples with the
-- subject of mid /m/0284r5q. What are all the tuples with the subject
-- of mid /m/0284r5q? (3 pts)

select * from fbFacts
where subject like '/m/0284r5q';
--Result

-- subject	predicate	obj	context
-- /m/0284r5q	/type/object/key	/wikipedia/en_id	9,327,603
-- /m/0284r5q	/type/object/key	/wikipedia/en	Flyte_$0028chocolate_bar$0029
-- /m/0284r5q	/type/object/key	/wikipedia/en_title	Flyte_$0028chocolate_bar$0029
-- /m/0284r5q	/common/topic/article	/m/0284r5t	
-- /m/0284r5q	/type/object/type	/common/topic	
-- /m/0284r5q	/type/object/type	/food/candy_bar	
-- /m/0284r5q	/type/object/type	/business/brand	
-- /m/0284r5q	/type/object/type	/base/tagit/concept	
-- /m/0284r5q	/food/candy_bar/manufacturer	/m/01kh5q	
-- /m/0284r5q	/common/topic/notable_types	/business/brand	
-- /m/0284r5q	/common/topic/notable_types	/food/candy_bar
-- /m/0284r5q	/food/candy_bar/sold_in	/m/09c7w0	
-- /m/0284r5q	/common/topic/notable_for		{"types":[], "id":"/food/candy_bar", "property":"/type/object/type", "name":"Candy bar"}
-- /m/0284r5q	/type/object/name	/lang/en	Flyte
-- /m/0284r5q	/common/topic/image	/m/04v6jtv

-- 4. How many travel destinations does Freebase have? To do this, we'll
-- use the type /travel/travel_destination. In particular, we want to
-- find the number of subjects that have a /type/object/type predicate
-- with the object equal to /travel/travel_destination. (3 pts)

select count(distinct(subject))
from fbFacts
where predicate like '/travel/travel_destination'
and obj like '/type/object/type predicate' 
--Result
--295

-- 5. Building off the previous query, what 20 travel destination have
-- the most tourist attractions? Return the location name and count.
-- Use the /travel/travel_destination/tourist_attractions predicate to
-- find the tourist attractions for each destination. Use the
-- /type/object/name predicate and /lang/en object to get the name of
-- each location (the name will be the context of the tuple with
-- predicate /type/object/name and object /lang/en). Sort your result
-- by the number of tourist attractions from largest to smallest and
-- then on the destination name alphabetically and only return the top
-- 20. (4 pts)

select dest.context as destination_name,
attr.num_attractions
from fbFacts dest,
(select subject, count(*) as num_attractions
from fbFacts
where predicate like '/travel/travel_destination/tourist_attractions'
group by subject) as attr

where dest.subject = attr.subject
and dest.predicate like '/type/object/name'
and dest.obj like '/lang/en'
order by num_attractions desc
limit 20

--Result

-- destination_name	num_attractions
-- London	108
-- Norway	74
-- Finland	59
-- Burlington	41
-- Rome	40
-- Toronto	36
-- Beijing	32
-- Buenos Aires	28
-- San Francisco	26
-- Bangkok	20
-- Vienna	19
-- Munich	19
-- Sierra Leone	19
-- Montpelier	18
-- Atlanta	17
-- Athens	17
-- Tanzania	17
-- Berlin	16
-- Laos	16
-- Portland	15

-- 6. Generate a histogram of the number of distinct predicates per
-- subject? This is more than a count of the number of distinct
-- predicates per subject. This is asking for computing a distribution
-- of the number of distinct predicates. For your answer, still put
-- the query in queries.sql, but instead of copying the result as a
-- comment, make a chart of your results in Zeppelin (the little icons
-- below the query allow you to toggle output modes). Take a
-- screenshot of a barchart of your histogram and submit it as
-- histogram.pdf/jpg/png (6 pts)

--Result

-- num_predicate	_c1
-- 31	1,623
-- 32	1,348
-- 33	1,222
-- 34	1,348
-- 35	1,674
-- 36	1,596
-- 37	1,100
-- 38	662
-- 39	466
-- 40	423
-- 41	337
-- 42	300
-- 43	264
-- 44	197
-- 45	150
-- 46	117
-- 47	101


-- Multiple Choice (8 pts) You do not need a cluster to answer the
-- following multiple choice questions. For each question, choose only
-- one answer.

-- Note: Please include the question number and answer to each
-- multiple choice questions below your queries in your queries.sql
-- file!

-- 1. In the setup code, you ran the command hadoop fs -put /data
-- /freebase-datadump-quadruples.tsv /data/spark_data.tsv to put data
-- in HDFS for Spark to read. By default, Spark looks in HDFS for
-- data, but you can actually tell Spark to read files locally, rather
-- than from HDFS. For this to work, what additional preprocessing
-- step would I need to take before even opening my Zeppelin notebook
-- to prepare the data? 

-- Answer c. Replicate the data to be on all the nodes in the cluster. 


-- 2. How is Spark different from Hadoop MapReduce? 

-- Answer b. Spark writes intermediate results (after Map-Reduce phases) to memory while
-- Hadoop writes to disk. 


-- 3. Which of the following is NOT a good use case of Map-Reduce?

-- Answer b. Running a large number of transactions for
-- a major bank. 


-- 4. In a simple Map-Reduce job with m mapper tasks and r reducer tasks,
-- how many output files do you get? 

-- Answer: c. r 


-- 5. True/False: One of the key features of Map-Reduce and Spark is
-- their ability to cope with server failure. For each statement below
-- indicate whether it is true or false. 

-- In MapReduce, every map task and every reduce task is replicated across several workers. 
-- Answer: False

-- When a server fails, Spark recomputes the RDD partitions at that server
-- from parent RDD partitions. 
-- Answer: True 

-- In Spark, when the programmer calls the persist() function, the data is stored on disk, to facilitate
-- recovery from failure. 
-- Answer: False

-- When a server running a reduce task fails,
-- MapReduce restarts that reduce task either at the same or another
-- server, reusing data stored in local files at the mappers. 
-- Answer: True


