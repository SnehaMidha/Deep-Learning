import numpy as np



def linear_forward_test_case():

    X = np.array([[-1.02387576, 1.12397796],

 [-1.62328545, 0.64667545],

 [-1.74314104, -0.59664964]])

    W = np.array([[ 0.74505627, 1.97611078, -1.24412333]])

    b = 5

    

    return X, W, b



def linear_activation_forward_test_case():

    X = np.array([[-1.02387576, 1.12397796],

 [-1.62328545, 0.64667545],

 [-1.74314104, -0.59664964]])

    W = np.array([[ 0.74505627, 1.97611078, -1.24412333]])

    b = 5

    return X, W, b



def L_model_forward_test_case():

    X = np.array([[-1.02387576, 1.12397796],

 [-1.62328545, 0.64667545],

 [-1.74314104, -0.59664964]])

    parameters = {'W1': np.array([[ 1.62434536, -0.61175641, -0.52817175],

        [-1.07296862,  0.86540763, -2.3015387 ]]),

 'W2': np.array([[ 1.74481176, -0.7612069 ]]),

 'b1': np.array([[ 0.],

        [ 0.]]),

 'b2': np.array([[ 0.]])}

    return X, parameters



def compute_cost_test_case():

    Y = np.asarray([[1, 1, 1]])

    aL = np.array([[.8,.9,0.4]])

    

    return Y, aL



def linear_backward_test_case():

    z, linear_cache = (np.array([[ 3.1980455 ,  7.85763489]]), (np.array([[-1.02387576,  1.12397796],

       [-1.62328545,  0.64667545],

       [-1.74314104, -0.59664964]]), np.array([[ 0.74505627,  1.97611078, -1.24412333]]), 5))

    

    return z, linear_cache



def linear_activation_backward_test_case():

    aL, linear_activation_cache = (np.array([[ 3.1980455 ,  7.85763489]]), ((np.array([[-1.02387576,  1.12397796], [-1.62328545,  0.64667545], [-1.74314104, -0.59664964]]), np.array([[ 0.74505627,  1.97611078, -1.24412333]]), 5), np.array([[ 3.1980455 ,  7.85763489]])))

    

    return aL, linear_activation_cache



def L_model_backward_test_case():

    X = np.random.rand(3,2)

    Y = np.array([[1, 1]])

    parameters = {'W1': np.array([[ 1.78862847,  0.43650985,  0.09649747]]), 'b1': np.array([[ 0.]])}



    aL, caches = (np.array([[ 0.60298372,  0.87182628]]), [((np.array([[ 0.20445225,  0.87811744],

           [ 0.02738759,  0.67046751],

           [ 0.4173048 ,  0.55868983]]),

    np.array([[ 1.78862847,  0.43650985,  0.09649747]]),

    np.array([[ 0.]])),

   np.array([[ 0.41791293,  1.91720367]]))])



    return X, Y, aL, caches



def update_parameters_test_case():

    parameters = {'W1': np.array([[ 1.78862847,  0.43650985,  0.09649747],

        [-1.8634927 , -0.2773882 , -0.35475898],

        [-0.08274148, -0.62700068, -0.04381817],

        [-0.47721803, -1.31386475,  0.88462238]]),

 'W2': np.array([[ 0.88131804,  1.70957306,  0.05003364, -0.40467741],

        [-0.54535995, -1.54647732,  0.98236743, -1.10106763],

        [-1.18504653, -0.2056499 ,  1.48614836,  0.23671627]]),

 'W3': np.array([[-1.02378514, -0.7129932 ,  0.62524497],

        [-0.16051336, -0.76883635, -0.23003072]]),

 'b1': np.array([[ 0.],

        [ 0.],

        [ 0.],

        [ 0.]]),

 'b2': np.array([[ 0.],

        [ 0.],

        [ 0.]]),

 'b3': np.array([[ 0.],

        [ 0.]])}

    grads = {'dW1': np.array([[ 0.63070583,  0.66482653,  0.18308507],

        [ 0.        ,  0.        ,  0.        ],

        [ 0.        ,  0.        ,  0.        ],

        [ 0.        ,  0.        ,  0.        ]]),

 'dW2': np.array([[ 1.62934255,  0.        ,  0.        ,  0.        ],

        [ 0.        ,  0.        ,  0.        ,  0.        ],

        [ 0.        ,  0.        ,  0.        ,  0.        ]]),

 'dW3': np.array([[-1.40260776,  0.        ,  0.        ]]),

 'da1': np.array([[ 0.70760786,  0.65063504],

        [ 0.17268975,  0.15878569],

        [ 0.03817582,  0.03510211]]),

 'da2': np.array([[ 0.39561478,  0.36376198],

        [ 0.7674101 ,  0.70562233],

        [ 0.0224596 ,  0.02065127],

        [-0.18165561, -0.16702967]]),

 'da3': np.array([[ 0.44888991,  0.41274769],

        [ 0.31261975,  0.28744927],

        [-0.27414557, -0.25207283]]),

 'db1': 0.75937676204411464,

 'db2': 0.86163759922811056,

 'db3': -0.84161956022334572}

    return parameters, grads