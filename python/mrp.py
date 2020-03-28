"""这是MRP迭代过程"""


# 迭代
def next_v(_lambda, r_list, old_v_list, weight_list):
    new_v_list = []
    for j in range(len(old_v_list)):
        if j != len(old_v_list) - 1:
            j_sum = .0
            # 与当前状态相接的后续状态的值函数相应的状态转移概率的求和的折扣
            for k in range(len(weight_list[j])):
                j_sum += weight_list[j][k][0] * old_v_list[weight_list[j][k][1]]

            # 当前状态在下一阶段的报酬
            new_v_list.append(r_list[j] + _lambda * j_sum)

    # Sleep状态无后续状态，故直接赋值0
    new_v_list.append(0.0)
    return new_v_list


if __name__ == '__main__':
    # γ
    my_lambda = 1

    # 报酬顺序：Class 1、Class 2、Class 3、Pass、Pub、Facebook、Sleep，分别对应0, 1, 2, 3, 4, 5, 6
    # 后续顺序皆与此相同
    my_r_list = [-2., -2., -2., 10., 1., -1., 0.]

    # 初始化值函数
    my_old_v_list = [0, 0, 0, 0, 0, 0, 0]

    # 状态转移概率（这里没有用概率矩阵，方法有点笨，读者可以用矩阵来表示）
    # 这里以[[0.5, 1], [0.5, 5]]为例解释一下，该列表记录Class 1的状态：
    # [0.5, 1]表示以0.5的概率转移到Class 2
    # [0.5, 5]表示以0.5的概率转移到Facebook
    my_weight_list = [[[0.5, 1], [0.5, 5]],
                      [[0.8, 2], [0.2, 6]],
                      [[0.6, 3], [0.4, 4]],
                      [[1, 6]],
                      [[0.2, 0], [0.4, 1], [0.4, 2]],
                      [[0.1, 0], [0.9, 5]],
                      [[0, 0]]]

    my_new_v_list = []
    # 指定迭代次数
    for i in range(1000):
        my_new_v_list = next_v(my_lambda, my_r_list, my_old_v_list, my_weight_list)

        # 用新生成的值函数列表替换旧的值函数列表
        my_old_v_list = my_new_v_list

    print(my_new_v_list)
