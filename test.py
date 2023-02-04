# import pandas as pd
#
#
# # Creearea celor 3 fisiere.csv pt judete, coordonate x si t, lasam in forma de comentarii
#
# dt_jud = pd.read_csv('judetele_final.csv')
# dt_jud = dt_jud.judet
# dt_jud = dt_jud.to_list()
#
# dt_coor = pd.read_csv('coordonate_judete.csv')
# dt_coor = dt_coor.coordonate
# dt_coor = dt_coor.to_list()
#
#
# dt_x = []
# dt_y = []
#
# for element in dt_coor:
#     element = eval(element)
#     dt_x.append(element[0])
#     dt_y.append(element[1])
#
# # print(f"{dt_x}\n{dt_y}")
#
# dict_ = {
#     'judet': dt_jud,
#     'x': dt_x,
#     'y': dt_y
# }
#
# data_ = pd.DataFrame(dict_)
# data_.to_csv('map_Romania.csv')
