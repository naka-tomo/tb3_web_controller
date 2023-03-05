from nicegui import ui
import rospy
from geometry_msgs.msg import Twist


def move(x, y):
    t = Twist()
    t.linear.x = y * 0.5
    t.angular.z = -x

    label_vel.set_text(f"{x:.3f}, {y:.3f}")
    pub_cmdvel.publish(t)


def stop():
    t = Twist()
    t.linear.x = 0
    t.angular.z = 0
    pub_cmdvel.publish(t)
    label_vel.set_text(f"0, 0")


ui.markdown("# Turtlebot Controller")

ui.joystick(
    color="blue",
    size=100,
    on_move=lambda e: move(e["data"]["vector"]["x"], e["data"]["vector"]["y"]),
    on_end=lambda _: stop(),
    throttle=0.05,
)
label_vel = ui.label("0, 0")

rospy.init_node("controller")
pub_cmdvel = rospy.Publisher("cmd_vel", Twist, queue_size=1)

ui.run()
