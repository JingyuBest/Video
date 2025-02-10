import shutil
import os
def delete():
    shutil.rmtree('Camera_Output')
    os.mkdir('Camera_Output')
    shutil.rmtree('Histogram')
    os.mkdir('Histogram')
    shutil.rmtree('runs')   
    os.mkdir('runs')