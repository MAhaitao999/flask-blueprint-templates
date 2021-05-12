from helloworld import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)


@manager.command
def custom(arg):
    """
    自定义命令
    python3 manager.py custom 123
    :param arg:
    :return:
    """
    print(arg)


@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
    自定义命令
    执行: python3 manager.py cmd -n haitao -u https://www.baidu.com
    :param name:
    :param url:
    :return:
    """
    print(name, url)


if __name__ == '__main__':
    manager.run()
