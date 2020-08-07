from ete3 import *
import pickle


def read_evolutionary_event():
    with open("./ENSGT00390000009061_transcript_gene_evolutionary_event.pickle", 'rb') as f:
        evolutionary_event = pickle.load(f)
    return evolutionary_event


def remove_mixed_grey_black(_12_grey_node_or_leaf, result):
    """
    剔除掉7号 8号 12号: 混合黑色和灰色节点
    """
    remove_list = []
    for i in _12_grey_node_or_leaf:
        #leaf
        if i.is_leaf():
            # 先把所有的leaf:1 2 3 4 5 6 都装进去
            result.append(i)
        
        # Node
        else:
            # 看node 的所有children是否都是灰色
            # 会剔除掉7号 8号 12号, 放进去9, 10, 11
            # ----这个会有一个问题：9 10 号节点会被包含进去----
            if all(elem in _12_grey_node_or_leaf for elem in i.children):
                result.append(i)
            else:
                remove_list.append(i)
    return result, remove_list


def remove_false_repeat_node(result, remove_list):
    """
    剔除掉9号, 10号, 6号: 
    """
    for i in result:
        # Node
        if not i.is_leaf():
            # remove_false: 9号
            if any(elem in remove_list for elem in i.children):
                result.remove(i)
            # remove_false: 10号, 6号
            if all(elem in result for elem in i.children):
                for ele in i.children:
                    result.remove(ele)
    return result


def main():
    result = []
    _12_grey_node_or_leaf = read_evolutionary_event()['loss']
    
    # print("original")
    # for i in _12_grey_node_or_leaf:
    #     print(i)
    # print("\n---------------\n")

    result, remove_list = remove_mixed_grey_black(_12_grey_node_or_leaf, result)  
    result = remove_false_repeat_node(result, remove_list)     

    print("result")
    for i in result:
        print(i)


if __name__ == "__main__":
    main()