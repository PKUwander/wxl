# alpha2fund
To build a trading system for alpha2fund.

## How to add a user?

###1. Run the server with the shell:
	$ python manage.py shell

###2. In the shell, use following commands:
	>>> from werkzeug.security import generate_password_hash
	>>> u=User()
	>>> u.username='test01'
	>>> u.password='123456'
	>>> u.role=1 #可选,暂时没有定义权限级别
	>>> db.session.add(u)
	>>> db.session.commit()

###3. Close the shell by `ctrl+c` or `exit()`