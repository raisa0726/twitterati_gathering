from app import db, User
from werkzeug.security import generate_password_hash

#データベース作成
db.create_all()

#スーパーアドミンの作成
super_account_name = "master"
super_account_id = 89999
super_account_password = str(123456)
super_account_password=generate_password_hash(super_account_password, method='sha256')
super_account = User(id=super_account_id,master_name=super_account_name,password=super_account_password)
db.session.add(super_account)
db.session.commit()