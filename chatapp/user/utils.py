from django.conf import settings
import jwt,datetime
def encode_token(data):
        print(data.get('email'))
        expiration_time=datetime.datetime.now()+datetime.timedelta(days=30)
        expiration_timestamp=expiration_time.timestamp()
        token=jwt.encode({'email':data.get('email'),'exp':expiration_timestamp},settings.SECRET_KEY,algorithm='HS256')
        return token
