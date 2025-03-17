# GRAPHQLFB
Library yang di rancang untuk menggunakan fitur facebook ( langsung dari graphql api facebook ).
- Menginstall library
```bash
pip install graphqlfb
```
- Menggunakan library
```python
from graphqlfb import Facebook

cookies = 'your cookies string'
fb = Facebook(cookies=cookies)
print(fb.login_status) # True or False
```
# React Post
Memberikan reaksi ke postingan
```python
post_id = ''
reaction_type = 'care'
react_response = fb.post_reaction(post_id=post_id, reaction_type=reaction_type)
```
Reaction type:
- Like
- Love
- Care
- Haha
- Wow
- Sad
- Angry
