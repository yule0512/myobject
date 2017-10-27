import os

def run():
	val = os.system('python manage.py runserver 0:8002')
	print(val)

if __name__ == '__main__':
	print('启动服务ing。。。')
	run()
