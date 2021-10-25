import math
from typing import Union


class Pos:
    """
    星体坐标
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        """
        获取星体的x轴坐标

        :param: None
        :return: 星体的x轴坐标
        """
        return self._x

    @property
    def y(self):
        """
        获取星体的y轴坐标

        :param: None
        :return: 星体的y轴坐标
        """
        return self._y


class Radian(float):
    """
    弧度
    """
    def to_angle(self):
        """
        弧度转角度

        :param: None
        :return: 角度
        """
        return r2a(self)


class Angle(float):
    """
    角度
    """
    def to_radian(self):
        """
        角度转弧度

        :param: None
        :return: 弧度
        """
        return a2r(self)


class Atom(object):
    """
    星体的参数属性
    """
    def __init__(self, lists):
        """
        :param lists: 星体的参数属性
        """
        # self.port = int(lists[0])
        self.position_x = lists[0]
        self.position_y = lists[1]
        self.velocity_x = lists[2]
        self.velocity_y = lists[3]
        self.mass = lists[4]
        self.radius = lists[5]
        if lists[6] == 1:
            self.isPlayer = True
        else:
            self.isPlayer = False
        if lists[7] == 1:
            self.colliding = True
        else:
            self.colliding = False
        if lists[8] == 1:
            self.isBullet = True
        else:
            self.isBullet = False
        self.dist = float('inf')
        self.id = lists[9]
        self.dist = float("inf")

    def distance_to(self, entity) -> float:
        """
        :param: 游戏中的某一个星体
        :return: 两个星体间的直线距离
        """
        self.dist = ((self.position_x - entity.position_x) ** 2 + (self.position_y - entity.position_y) ** 2) ** 0.5
        return self.dist

    def radian_to(self, x: float, y: float) -> Radian:
        """
        :param: 某位置的x轴坐标
        :param: 某位置的y轴坐标
        :return: 弧度，弧度值取值范围为[-π,π]
        """
        return relative_radian(self.position_x, self.position_y, x, y)

    def angle_to(self, x: float, y: float) -> Angle:
        """
        获取self星体与某坐标(x,y)的角度值，角度值取值范围为[-180°,180°]

        :param: 某位置的x轴坐标
        :param: 某位置的y轴坐标
        :return: 角度，角度取值范围从-180°到180°
        """
        return self.radian_to(x, y).to_angle()

    @property
    def radian(self) -> Radian:
        """
        获取self星体的朝向弧度，朝向弧度取值范围为[-π，π],朝向弧度遵循正常的XY坐标轴，X轴正方形为0，X轴负方向为-π/π，Y轴正方形为π/2，Y轴负方向为-π/2

        :param: None
        :return: 弧度值
        """
        return Radian(math.atan2(self.velocity_y, self.velocity_x))

    @property
    def angle(self) -> Angle:
        """
        获取self星体的朝向角度，朝向角度取值范围为[-180°，180°],朝向角度遵循正常的XY坐标轴，X轴正方形为0°，X轴负方向为-180°/180°，Y轴正方形为90°，Y轴负方向为-90°

        :param: None
        :return: 弧度值
        """
        return r2a(math.atan2(self.velocity_y, self.velocity_x))


def r2a(radian: Union[float, int, Radian]) -> Angle:
    """
    弧度转角度

    :param: radian(Radian, float, int),弧度
    :return: Angle,角度
    """
    return Angle(float(radian) / math.pi * 180.)


def a2r(angle: Union[float, int, Angle]) -> Radian:
    """
    角度转弧度

    :param: 角度
    :return: 弧度
    """
    return Radian(math.pi * (float(angle) / 180.))


def relative_radian(x1: float, y1: float, x2: float, y2: float) -> Radian:
    """
    相对弧度

    :param: 坐标(x1,y1)在x轴上的坐标值
    :param: 坐标(x1,y1)在y轴上的坐标值
    :param: 坐标(x2,y2)在x轴上的坐标值
    :param: 坐标(x2,y2)在y轴上的坐标值
    :return: Radian 弧度值
    """
    dx = x2 - x1
    dy = y2 - y1
    return Radian(math.atan2(dy, dx))


def relative_angle(x1: float, y1: float, x2: float, y2: float) -> Angle:
    """
    相对角度

    :param: 坐标(x1,y1)在x轴上的坐标值
    :param: 坐标(x1,y1)在y轴上的坐标值
    :param: 坐标(x2,y2)在x轴上的坐标值
    :param: 坐标(x2,y2)在y轴上的坐标值
    :return: Angle 角度值
    """
    return relative_radian(x1, y1, x2, y2).to_angle()
