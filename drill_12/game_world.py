#object[0] : 바닥계층
#object[1] : 상위계층
object = [[], [], []]


def add_object(o, depth):
    object[depth].append(o)

def remove_object(o):
    for layer in object:
        if o in layer:
            layer.remove(o)
            del o
            break
    # object.remove(o)  # 리스트에서 날려준다
    # del o  # 메모리에서 날려준다

def all_object():
    for layer in object:
        for o in layer:
            yield o # 제너레이터, 모든 객체들을 하나씩 넘겨준다

def clear():
    for o in all_object():
        del o
    for layer in object:
        layer.clear()