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
    测试方法，测试该session_id是否在登陆状态。
    """
    con = db.connect("test.db")
    cur=con.cursor()
    res=cur.execute('select session_id from m_test where session_id=?',(session_id,))
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
    登陆，输入用户名密码，返回session_id。
    """
    session_id=hash(user+password)
    con = db.connect("test.db")
    cur=con.cursor()
    res=cur.execute('insert into m_test(name,session_id) values(?,?)',(user,session_id))
    con.commit()
    con.close()
    return session_id

  @ladonize(str,rtype=bool)
  def logout(self,session_id):
    """
    logout function
    @rtype:bool
    注销账户，注销成功则返回True。
    """
    con = db.connect("test.db")
    cur=con.cursor()
    res=cur.execute('delete  from m_test  where session_id=?',(session_id,))
    con.commit()
    con.close()
    return True
    
