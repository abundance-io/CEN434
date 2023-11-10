import couchdb
server = couchdb.Server("http://admin:password@127.0.0.1:5984/")
db = server.create("student_data")
student_1 = {
    'name': 'Abundance',
    'matno':'20cj027424'
}


student_2 = { 'name': 'Abundance2',
    'matno':'20cj0274242'
}

db.save(student_1)
db.save(student_2)





