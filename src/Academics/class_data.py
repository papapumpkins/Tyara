import os
import time

path1 = "start D:\Learning\PYTHON\Weather\src"
cls = [path1 + "\class_mt2_lec.wav", path1 + "\class_psy_lec.wav", path1 + "\class_ds_lec.wav",
       path1 + "\class_evo_lec.wav", path1 + "\class_mun_lec.wav"]
for sounds in cls:
    os.system(sounds)
    time.sleep(1.7)

    '''makemp3("Mass Transfer, ","class_mt2_lec")
       makemp3("Psychology, ","class_psy_lec")
       makemp3("Data Structures, ", "class_ds_lec")
       makemp3("Evolutionary Optimization, ","class_evo_lec")
       makemp3("Industrial Biotechnology, ","class_ind_bio")
       makemp3("C.P.T. , ", "class_cpt_lec")
       makemp3("C.L.P. Lab , ", "class_clp_lab")
       makemp3("Instrumentation & Automation, ", "class_mun_lec")
       makemp3("Instrumentation Lab , ","class_process_lab") '''