import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1:", node1, "node2:", node2)
print("node3:", node3)

tf.print("tf.print: ", [node1, node2])
tf.print(node3)


""" 그래프를 먼저 빌드 한다. 그 후 tf.print를 이용 그래프 실행. 결과 도출 """

""" tensorflow 2.0 버전 부터는 placeholder를 사용하지않고,  @tf.function 으로 함수를 정의해서 사용하는 것 같습니다 """
""" 실행 시점에 값을 넣어주는 방식 @tf.funtion """

@tf.function
def adder(a,b):
    return a+b
a = tf.constant([1,3])
b = tf.constant([2,4])

tf.print(adder(a,b))