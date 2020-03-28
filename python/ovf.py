"""这是OVF迭代过程"""


def next_v(pi, r_list, old_v_list, weight_list):
    new_v_list = []
    for j in range(len(old_v_list)):
        if j != len(old_v_list) - 1:
            max_list = []
            for k in range(len(weight_list[j])):
                if type(weight_list[j][k][0]) is not list:
                    max_list.append(pi * (r_list[weight_list[j][k][1]] + old_v_list[weight_list[j][k][0]]))
                else:
                    m_sum = .0
                    for m in range(len(weight_list[j][k][0])):
                        m_sum += old_v_list[weight_list[j][k][0][m][0]] * weight_list[j][k][0][m][1]
                    max_list.append(pi * (r_list[weight_list[j][k][1]] + m_sum))
            new_v_list.append(max(max_list))

    new_v_list.append(0.0)
    return new_v_list


if __name__ == '__main__':
    my_pi = 1
    # study pass pub facebook quit sleep
    my_r_list = [-2., 10., 1., -1., 0., 0.]
    my_old_v_list = [0, 0, 0, 0, 0]
    my_weight_list = [[[1, 0], [3, 3]],
                      [[2, 0], [4, 5]],
                      [[[[0, 0.2], [1, 0.4], [2, 0.4]], 2], [4, 1]],
                      [[0, 4], [3, 3]],
                      []]

    my_new_v_list = []
    # my_new_v_list = next_v(my_pi, my_r_list, my_old_v_list, my_weight_list)
    for i in range(100):
        my_new_v_list = next_v(my_pi, my_r_list, my_old_v_list, my_weight_list)
        my_old_v_list = my_new_v_list

    print(my_new_v_list)
