import numpy as np


# π、γ
_pi = 0.5
_lambda = 1

p = [[0, _pi, 0, _pi, 0],
     [0, 0, _pi, 0, _pi],
     [_pi*0.2, _pi*0.4, _pi*0.4, 0, _pi],
     [_pi, 0, 0, _pi, 0],
     [0, 0, 0, 0, 0]]
r = [[_pi*-2 + _pi*-1],
     [_pi*-2 + _pi*0],
     [_pi*1 + _pi*10],
     [_pi*0 + _pi*-1],
     [0]]
i = [[1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1]]

p_mat = np.matrix(p)
r_mat = np.matrix(r)
i_mat = np.matrix(i)

v_mat = (i_mat - _lambda * p_mat).I * r_mat
# v_mat = np.dot(np.linalg.inv(i_mat - p_mat), r_mat)

print(v_mat)
