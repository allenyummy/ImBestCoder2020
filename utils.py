def query_submission_detail(cursor):
    query = """
        select submission.userid, userid_1.order_count, userid_1.total_amount, userid_1.category_encoded
        from submission
        inner join (select * from purchase_detail
        group by userid) as userid_1
        on userid_1.userid==submission.userid;
        """
    return cursor.execute(query).fetchall()