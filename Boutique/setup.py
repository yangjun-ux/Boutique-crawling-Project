from setuptools import setup, find_packages


setup(name='Boutique_crawling',

          version='0.0.1',

          description='Boutique brand web crawling code',

          author='Jun Yang, Daeseon Cho, Jinkyung Oh',

          author_email='nov16jun@gmail.com',

          url='http://yangjun-ux.github.io',

          license='MIT',

          py_modules=['GUCCI', 'BURBERRY', 'HERMES', 'DIOR', 'JIMMYCHOO'],

          python_requires='>=3',
      
          package_data        = {},

          include_package_data=False,

         zip_safe=False

    )
