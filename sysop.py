from ladon.ladonizer import ladonize
import sqlite3 as db

class SystemOp(object):
  """
  .
  """
  @ladonize(str,rtype=str)
  def test(self,session_id):
    """
    Reurn a database result
    @rtype: The result of the database
    """
    con = db.connect("test.db")
    cur=con.cursor()
    res=cur.execute('select session_id from m_test')
    result=res.fetchall()
    con.close()
    if(len(result)>0):
      return 'OK'
    else:
      return 'Deny'

  
  @ladonize(str,str,rtype=str)
  def login(self,user,password):
    """
    login function
    @rtype:session_id
    """
    con = db.connect("test.db")
    cur=con.cursor()
    res=cur.execute('insert into m_test(name,session_id) values(?,?)',(user,user+password))
    con.commit()
    con.close()
    return user+password

  @ladonize(str,rtype=bool)
  def logout(self,session_id):
    con = db.connect("test.db")
    cur=con.cursor()
    res=cur.execute('delete  from m_test  where session_id=?',(session_id,))
    con.commit()
    con.close()
    return True
    
