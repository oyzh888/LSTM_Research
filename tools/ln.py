import os
#1-20
cmd = []
how_much_part = 1
layer_size = 128
win_size = 20


epochs = 200
LSTM_Layer_Num = 1
maxlen = 20
batch_size = 256
source_path = '/unsullied/sharefs/ouyangzhihao/Share/LSTM/Text_Generation_Capacity/TB_logdir/LSTM'
target_path = '/unsullied/sharefs/ouyangzhihao/Share/LSTM/Text_Generation_Capacity/TB_logdir/ana_6_30_BLSTMvsLSTM'

if __name__ == '__main__':
    for how_much_part in [100,10,1]:
        for LayerSize in [256,512]:
            exp_name = 'LayerN%d_LS%d_WinSize%d_BS%d_%dpart_epoch%d' % (
            LSTM_Layer_Num, LayerSize, maxlen, batch_size, how_much_part, epochs)
            for fpathe, dirs, fs in os.walk(source_path):
                for dir in dirs:
                    if(dir == exp_name):
                        s_path = os.path.join(fpathe,dir)
                        t_path = os.path.join(target_path,exp_name)
                        # print('Find %s in: \n %s' % (exp_name, s_path))
                        cmd = 'ln -s %s %s' % (s_path, t_path)
                        print(cmd)
                        os.system(cmd)
                    # else:
                        # print(exp_name)
                        # print('Wrong: %s VS %s' % (os.path.join(dir),exp_name ))
            # os.system(cmd)
            # cmd.append(rlaunch + 'python3 tmp.py %d %d %d' % (layer_size, win_size, how_much_part)
            #        )
    # print(cmd)
    # print('\n'.join(cmd))
