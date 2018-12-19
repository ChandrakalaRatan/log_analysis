#!/usr/bin/env python3
import psycopg2
from datetime import datetime


# We need two views to solve problem 3
""" CREATE VIEW errors AS
	SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT)  AS no_error_request
	FROM log WHERE NOT status='200 OK' GROUP BY day ORDER BY day;

    CREATE VIEW total AS
	SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT) AS total_requests
	FROM log GROUP BY day ORDER BY day;"""

# Function to open and close the db connection
def db_query(sql_statement):
        conn = psycopg2.connect(database="news")
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        result = cursor.fetchall()
        conn.close()
        return result

# Problem 1 What are the most popular three articles of all time?
def most_popular_articles():
    popular_articles = """SELECT articles.title, count(*) AS number_of_views
                            FROM  articles, log
                            WHERE articles.slug = substring(log.path, 10)
                            AND log.status='200 OK'
                            GROUP BY articles.title
                            ORDER BY number_of_views DESC
                            LIMIT 3;"""
    most_popular_articles = db_query(popular_articles)
    print ("\n\t\tThe most popular three articles of all time\n")
    for title_name, number_of_views in most_popular_articles:
        print(" \"{}\" \t -- {} views".format(title_name, number_of_views))

#Problem 2 Who are the most popular article authors of all time?
def most_popular_authors():
    popular_authors = """SELECT authors.name, count(*) AS number_of_views
                            FROM authors, articles,  log
                            WHERE articles.slug = substring(log.path, 10)
                            AND authors.id = articles.author
                            AND log.status='200 OK'
                            GROUP BY authors.name
                            ORDER BY number_of_views DESC;"""
    most_popular_authors = db_query(popular_authors)
    print("\n\t\tThe most popular authors of all time\n")
    for author_name, number_of_views in most_popular_authors:
        print(" {} \t\t\t -- {} views".format(author_name, number_of_views))

#Problem 3 the days when more than 1% of requests had errors
def error_request_percentage():
    error_percentage = """SELECT  errors.day,
	                      ROUND(((errors.no_error_request/total.total_requests) * 100)::DECIMAL,1)
	                      AS percentage
	                      FROM errors, total
	                      WHERE total.day = errors.day
                          AND ROUND(((errors.no_error_request/total.total_requests) * 100)::DECIMAL,2) > 1.0
	                      ORDER BY errors.day;"""
    error_request_percentage = db_query(error_percentage)
    print("\n\t\tThe days when more than 1% of requests had errors\n")
    for day, percentage in error_request_percentage:
        print(" {} \t\t {}% ".format(datetime.strftime(day,'%b %d, %Y'), percentage)+"errors")

if __name__ == '__main__':
    most_popular_articles()
    most_popular_authors()
    error_request_percentage()
