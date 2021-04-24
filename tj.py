from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pyspark.sql.functions as f
from pyspark.sql.functions import split
from pyspark.sql.functions import date_format


spark = SparkSession.builder.appName("demo").getOrCreate()
nov_data=spark.read.csv("s3://kaggle-ecommerce/2019-Nov.csv",header=True)
clean_nov=nov_data.na.drop("any")
clean_nov.printSchema()
new_data=clean_nov.withColumn('category', split(('category_code'), '\\.').getItem(0)).withColumn('sub_catogery', split(('category_code'), '\\.').getItem(1))
b=new_data.withColumn('date', split(('event_time'), ' ').getItem(0)).withColumn('time', split(('event_time'), ' ').getItem(1))
d=b.withColumn("day",  date_format('date', 'E').alias('dow_string'))
d.createOrReplaceTempView("nov_data")
Customer_count=spark.sql("select count(user_id) p_customer from nov_data where event_type='purchase' group by user_id having count(user_id)>1")
Customer_count.write.format("orc").saveAsTable("customer_count_purchase")
purch1=spark.sql("select count(event_type) event_type_p,sum(price) total,day from nov_data where event_type='purchase' group by day")
view2=spark.sql("select count(event_type) event_type_v,day from nov_data where event_type='view' group by day")
cart2=spark.sql("select count(event_type) event_type_c,day from nov_data where event_type='cart' group by day")
join2=spark.sql("select a.event_type_p,a.total, a.day, b.event_type_v,c.event_type_c from (select count(event_type) event_type_p,sum(price) total,day from nov_data where event_type='purchase' group by day) as a,(select count(event_type) event_type_v,day from nov_data where event_type='view' group by day) as b,(select count(event_type) event_type_c,day from nov_data where event_type='cart' group by day) as c where a.day=b.day and b.day=c.day")
join2.write.format("orc").saveAsTable("p_v_c_day")
view=spark.sql("select sum(price) total,count(event_type) purchase,category,sub_catogery,brand from nov_data where event_type='purchase' group by category,sub_catogery,brand")
view.write.format("orc").saveAsTable("purchase_c_s_b")
purch=spark.sql("select count(event_type) event_type_p,sum(price) total,date from nov_data where event_type='purchase' group by date")
purch.write.format("orc").saveAsTable("purch_date")
view=spark.sql("select count(event_type) event_type_v,date from nov_data where event_type='view' group by date")
view.write.format("orc").saveAsTable("v_date")
cart=spark.sql("select count(event_type) event_type_c,date from nov_data where event_type='cart' group by date")
cart.write.format("orc").saveAsTable("c_date")
user_id=spark.sql("select count(user_id) count_user_id,date from nov_data group by date")
user_id.write.format("orc").saveAsTable("userid_date")

