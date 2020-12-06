import numpy as np
import sys;  

from tensorflow.keras import backend as K

from tensorflow.keras.models import Model
from tensorflow.keras.layers import ( 
    Input,
    Multiply,
    Dense,
    Dropout,
    Activation,
    Flatten,
    Convolution1D,
    AveragePooling1D
)

def build_models():
    Seq_deepCpf1_Input_SEQ = Input(shape=(34,4))
    Seq_deepCpf1_C1 = Convolution1D(80, 5, activation='relu')(Seq_deepCpf1_Input_SEQ)
    Seq_deepCpf1_P1 = AveragePooling1D(2)(Seq_deepCpf1_C1)
    Seq_deepCpf1_F = Flatten()(Seq_deepCpf1_P1)
    Seq_deepCpf1_DO1= Dropout(0.3)(Seq_deepCpf1_F)
    Seq_deepCpf1_D1 = Dense(80, activation='relu')(Seq_deepCpf1_DO1)
    Seq_deepCpf1_DO2= Dropout(0.3)(Seq_deepCpf1_D1)
    Seq_deepCpf1_D2 = Dense(40, activation='relu')(Seq_deepCpf1_DO2)
    Seq_deepCpf1_DO3= Dropout(0.3)(Seq_deepCpf1_D2)
    Seq_deepCpf1_D3 = Dense(40, activation='relu')(Seq_deepCpf1_DO3)
    Seq_deepCpf1_DO4= Dropout(0.3)(Seq_deepCpf1_D3)
    Seq_deepCpf1_Output = Dense(1, activation='linear')(Seq_deepCpf1_DO4)
    Seq_deepCpf1 = Model(inputs=[Seq_deepCpf1_Input_SEQ], outputs=[Seq_deepCpf1_Output])
    
    DeepCpf1_Input_SEQ = Input(shape=(34,4))
    DeepCpf1_C1 = Convolution1D(80, 5, activation='relu')(DeepCpf1_Input_SEQ)
    DeepCpf1_P1 = AveragePooling1D(2)(DeepCpf1_C1)
    DeepCpf1_F = Flatten()(DeepCpf1_P1)
    DeepCpf1_DO1= Dropout(0.3)(DeepCpf1_F)
    DeepCpf1_D1 = Dense(80, activation='relu')(DeepCpf1_DO1)
    DeepCpf1_DO2= Dropout(0.3)(DeepCpf1_D1)
    DeepCpf1_D2 = Dense(40, activation='relu')(DeepCpf1_DO2)
    DeepCpf1_DO3= Dropout(0.3)(DeepCpf1_D2)
    DeepCpf1_D3_SEQ = Dense(40, activation='relu')(DeepCpf1_DO3)
    
    DeepCpf1_Input_CA = Input(shape=(1,))
    DeepCpf1_D3_CA = Dense(40, activation='relu')(DeepCpf1_Input_CA)
    DeepCpf1_M = Multiply()([DeepCpf1_D3_SEQ, DeepCpf1_D3_CA])
    
    DeepCpf1_DO4= Dropout(0.3)(DeepCpf1_M)
    DeepCpf1_Output = Dense(1, activation='linear')(DeepCpf1_DO4)
    DeepCpf1 = Model(inputs=[DeepCpf1_Input_SEQ, DeepCpf1_Input_CA], outputs=[DeepCpf1_Output])
    
    Seq_deepCpf1.load_weights('weights/Seq_deepCpf1_weights.h5')
    DeepCpf1.load_weights('weights/DeepCpf1_weights.h5')
    
    return Seq_deepCpf1, DeepCpf1


def run_on_seq(sequences, chromatin_acessibilities=None):
    if chromatin_acessibilities is None:
        chromatin_acessibilities = [0 for _ in sequences]

    Seq_deepCpf1, DeepCpf1 = build_models()

    SEQ, CA = PREPROCESS(sequences, chromatin_acessibilities)
    
    Seq_deepCpf1_SCORE = Seq_deepCpf1.predict([SEQ], batch_size=50, verbose=0)
    DeepCpf1_SCORE = DeepCpf1.predict([SEQ, CA], batch_size=50, verbose=0) * 3

    Seq_deepCpf1_SCORE = Seq_deepCpf1_SCORE[0, 0]
    DeepCpf1_SCORE = DeepCpf1_SCORE[0, 0]

    return Seq_deepCpf1_SCORE, DeepCpf1_SCORE


def PREPROCESS(sequences, chromatin_acessibilities):
    data_n = len(sequences) - 1
    SEQ = np.zeros((data_n + 1, 34, 4), dtype=int)
    CA = np.zeros((data_n + 1, 1), dtype=int)

    
    for j, (seq, ca) in enumerate(zip(sequences, chromatin_acessibilities)):
        for i in range(34):
            if seq[i] in "Aa":
                SEQ[j, i, 0] = 1
            elif seq[i] in "Cc":
                SEQ[j, i, 1] = 1
            elif seq[i] in "Gg":
                SEQ[j, i, 2] = 1
            elif seq[i] in "Tt":
                SEQ[j, i, 3] = 1

        CA[j,0] = ca*100

    return SEQ, CA

