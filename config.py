import web

db_host = '	i943okdfa47xqzpy.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'lz6gjcwp6tqvj9c2'
db_user = 'nv1ud6xcdpqyv2j2'
db_pw = 'exyy8c4878431qq0'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
