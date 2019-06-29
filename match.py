import argparse
from video import video_to_matrix
from linear_transformation import *
from utility_tools import *
from csv_tools import *
import body_dictionary as body_dic
from time_tools import *
from dtw import my_dtw
from second_main import *


body = body_dic.body()
# interest_path = 'move/ArmsWarmUp/interest_point.txt'
# action = 'ArmsWarmUp'

type_exercise = ['ArmsWarmUp', 'prova']

#ap = argparse.ArgumentParser()
ex = 0
# while(ex not in type_exercise):  #per eseguire un eventuale controllo
print('Choose your exercise')
print(type_exercise)
#ap.add_argument("-e", "--exercise", required=True, help='Chose exercise')
#ap.add_argument("-v", "--video", required=True, help="Video")  # user video
#args = vars(ap.parse_args())
#print("{}".format(args["exercise"]))
#ex = args["exercise"]
ex= 'prova'
vid_na = 'data/bianca.mp4'
interest_path = 'move/models/' + ex + '/interest_point.txt'

model_path = 'move/models/'+ex+'/cycle/mean.csv'
mean_model = csv_to_matrix(model_path)
mean_model['frame']= mean_model['frame'].astype((int))
mean_model['x']= mean_model['x'].astype(int)
mean_model['y']= mean_model['y'].astype(int)

#model, model_w = get_model(ex)
# mostra a video il tipo di esercizio da fare
let_me_see(mean_model)
#print("{}".format(args["video"]))

# print(model.shape, model_w.shape)
#matrix = video_to_matrix(args["video"])
matrix = video_to_matrix(vid_na)
user_matrix = linear_transformation(matrix)
# matrix_to_csv(matrix,'user')

data = create_dataframe(user_matrix, ['frame', 'x', 'y', 'score'])

data = add_body_parts(data, body.dictionary)
data = remove_not_interest_point(interest_path, data)
data['frame']=data['frame'].astype(int)
data['x']=data['x'].astype(int)
data['y']=data['y'].astype(int)
mid_points = cycle_identify(data)
data_c = generate_cycle_model(data, mid_points)
shape1 = len(pd.unique(mean_model['frame']))
shape2 = len(data_c)
list_p = np.full((shape1,shape2),np.inf)


for i in range(shape2):
    path = my_dtw(mean_model,data_c[i] )
    p = sincro(path)
    for element in p :
        j = element[0]
        value_ = element[1]+data_c[i].iloc[0].frame
        list_p[j][i] = value_
tmp = pd.unique(mean_model['body_part'])
dimv_v = len(tmp)
for i in range(shape2):
    print('lavoro su ciclo',i)
    elenco=[]
    current_cycle = data_c[i]
    print(current_cycle)
    for j in range(shape1):
        if list_p[j][i] != np.inf:
            coppia = [j,list_p[j][i]]
            elenco.append(coppia)
    for elemento in elenco:
        f_u = current_cycle.loc[current_cycle['frame']==elemento[1]]
        v_u = carico_vettore(f_u,dim_v)
        distance_user =distance_cos(v_u,dim_v)
        f_m = mean_model.loc[mean_model['frame']==elemento[0]]
        v_m = carico_vettore(f_m,dim_v)
        distance_model =distance_cos(v_m,dim_v)












