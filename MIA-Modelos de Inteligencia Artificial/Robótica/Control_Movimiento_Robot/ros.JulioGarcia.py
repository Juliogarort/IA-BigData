import rospy
import math
from geometry_msgs.msg import Twist


def mover_recto(publisher, velocidad=0.2, distancia=1.0):
    """Mueve el robot en línea recta."""
    mensaje = Twist()
    mensaje.linear.x = velocidad
    mensaje.angular.z = 0.0
    tiempo = distancia / velocidad
    inicio = rospy.Time.now()
    rospy.loginfo(f"Moviendo recto {distancia} metros...")
    while (rospy.Time.now() - inicio).to_sec() < tiempo:
        publisher.publish(mensaje)
        rospy.sleep(0.1)
    detener_robot(publisher)
    rospy.loginfo("Movimiento recto completado.")


def girar_90_grados(publisher, velocidad_angular=0.5):
    """Gira el robot exactamente 90 grados."""
    mensaje = Twist()
    mensaje.linear.x = 0.0
    mensaje.angular.z = velocidad_angular
    angulo_objetivo = math.pi / 2
    tiempo = angulo_objetivo / velocidad_angular
    inicio = rospy.Time.now()
    rospy.loginfo("Girando 90 grados...")
    while (rospy.Time.now() - inicio).to_sec() < tiempo:
        publisher.publish(mensaje)
        rospy.sleep(0.1)
    detener_robot(publisher)
    rospy.loginfo("Giro completado.")


def detener_robot(publisher):
    """Detiene el robot enviando velocidad cero."""
    mensaje = Twist()
    publisher.publish(mensaje)
    rospy.sleep(0.5)


def main():
    """Inicializa el nodo ROS y ejecuta la secuencia de movimiento."""
    rospy.init_node('control_turtlebot', anonymous=True)
    publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)
    rospy.loginfo("=== Iniciando secuencia ===")
    try:
        mover_recto(publisher, velocidad=0.2, distancia=1.0)
        rospy.sleep(1)
        girar_90_grados(publisher, velocidad_angular=0.5)
        rospy.loginfo("=== Secuencia completada ===")
    except rospy.ROSInterruptException:
        rospy.loginfo("Nodo interrumpido.")


if __name__ == '__main__':
    main()