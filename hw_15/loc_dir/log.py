import logging

FORMAT = '{levelname:<8} |{asctime}| msg: {msg}'
path = 'C:\\Users\\Bekinsale\\Desktop\\project_py_charm\\home_work\\home_work_15\\loc_dir\\project.log'
logging.basicConfig(format=FORMAT, style='{', filename=path, filemode='w', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Основной файл проекта')
