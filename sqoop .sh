aws s3 cp s3://tej-123/mysql-connector-java-8.0.23.jar .

sudo cp mysql-connector-java-8.0.23.jar /usr/lib/sqoop/lib



sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE customer_count_purchase;"
sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE p_v_c_day;"
sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE purchase_c_s_b;"
sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE purch_date;"
sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE v_date;"
sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE c_date;"
sqoop eval --connect "jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb" --username=admin --password 'tejas1997' --query "TRUNCATE TABLE userid_date;"

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table customer_count_purchase --hcatalog-database default --hcatalog-table customer_count_purchase

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table p_v_c_day --hcatalog-database default --hcatalog-table p_v_c_day

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table purchase_c_s_b --hcatalog-database default --hcatalog-table purchase_c_s_b

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table purch_date --hcatalog-database default --hcatalog-table purch_date

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table v_date --hcatalog-database default --hcatalog-table v_date

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table c_date --hcatalog-database default --hcatalog-table c_date

sqoop export --connect jdbc:mysql://database-1.cxydffrzfnfw.us-east-1.rds.amazonaws.com/testdb --username admin --password tejas1997 --table userid_date --hcatalog-database default --hcatalog-table userid_date






