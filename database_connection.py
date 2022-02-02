import mysql.connector

def feedback(Feedback):
    db = mysql.connector.connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "nohareyli77985",
        database =  "rasafeedback" 
    )
    mycursor = db.cursor()
    feedback_from_slot = Feedback
    # sql = "CREATE TABLE userfeedback (feedback VARCHAR(255))"
    sql = 'INSERT INTO userfeedback (feedback) VALUES (%s)'.format(feedback)
    tuple = (feedback_from_slot,)
    mycursor.execute(sql , tuple)
    db.commit()

if __name__=="__main__":
    feedback("this is a feedback")
