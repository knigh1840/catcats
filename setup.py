from setuptools import setup, find_packages

setup(
    name='ratscats',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk'
    ],
    author='knight1840',
    author_email='yufeng.guo@qq.com',
    description='bigrats',
    license='MIT',
    keywords='rats',
    url='https://github.com/knigh1840/catcats'
)