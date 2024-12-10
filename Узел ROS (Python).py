import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String # Или пользовательский тип сообщения для лучшей структуры
import random

class BuildingScanner:
    def __init__(self):
        rospy.init_node('building_scanner')
        self.pub = rospy.Publisher('/buildings', String, queue_size=10)
        self.buildings = generate_world() # Используем функцию генерации мира

        # Подписка на положение дрона (замените на ваш реальный топик)
        rospy.Subscriber('/drone/pose', PoseStamped, self.scan_callback)
        rospy.sleep(1)  # Ждем подключения подписчиков
        self.start_mission()

    def start_mission(self):
      # Добавьте ваш код взлета дрона и начала миссии здесь, используя соответствующие действия или сервисы ROS.
      rospy.loginfo("Миссия началась. Сканирование зданий...")
      rospy.sleep(5) # Имитация времени полета
      self.scan_buildings()
      # Добавьте ваш код посадки дрона здесь.
      rospy.loginfo("Миссия завершена.")
      rospy.signal_shutdown("Миссия завершена")


    def scan_callback(self, pose_msg):
        # В реальной системе это обрабатывало бы данные датчиков для обнаружения зданий.
        # Здесь мы имитируем обнаружение на основе предварительно сгенерированных местоположений зданий.
        pass # Этот коллбэк не нужен с текущим подходом

    def scan_buildings(self):
        building_data = ""
        for building in self.buildings:
            # Имитация обнаружения с погрешностью
            x_err = random.uniform(-0.5, 0.5)
            y_err = random.uniform(-0.5, 0.5)
            detected_x = building['x'] + x_err
            detected_y = building['y'] + y_err
            building_type = self.get_building_type(building['color'])
            building_data += f"x:{detected_x},y:{detected_y},color:{building['color']},type:{building_type};"

        self.pub.publish(building_data)


    def get_building_type(self, color):
        if color == 'красный':
            return "Административное здание"
        elif color == 'зеленый':
            return "Лаборатория"
        elif color == 'желтый':
            return "Вход в шахту"
        elif color == 'синий':
            return "Здание обогащения угля"
        else:
            return "Неизвестно"

if __name__ == '__main__':
    try:
        scanner = BuildingScanner()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
