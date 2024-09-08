class zfx:
    def __init__(self, x):
        self.x = x

    def mj(self):
        print(f'正方形的面积: {self.x ** 2}')


class zft:
    def __init__(self, x):
        self.x = x

    def bmj(self):
        print(f'正方体的表面积: {self.x ** 2 * 6}')

    def tj(self):
        print(f'正方体的体积: {self.x ** 3}')


class cfx:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mj(self):
        print(f'长方形的面积: {self.x * self.y}')


class cft:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def bmj(self):
        print(f'长方体的表面积: {(self.x * self.y + self.x * self.z + self.y * self.z) * 2}')

    def tj(self):
        print(f'长方体的体积: {self.x * self.y * self.z}')


class wh:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def pxsb(self):
        print(f'平行四边形的面积: {self.w * self.h}')

    def sjx(self):
        print(f'三角形的面积: {(self.w * self.h) / 2}')


class cir:
    def __init__(self, r, h=None):
        self.r = r
        self.h = h

    def d(self):
        print(f'圆的直径: {self.r * 2}')

    def c(self):
        print(f'圆的周长: {self.r * 2 * 3.14}')

    def mj(self):
        print(f'圆的面积: {self.r ** 2 * 3.14}')

    def yzb(self):
        if self.h is not None:
            side_area = 2 * 3.14 * self.r * self.h  # 圆柱的侧面积
            base_area = 2 * 3.14 * self.r ** 2  # 两个底面积
            print(f'圆柱的表面积: {side_area + base_area}')
        else:
            print("请输入高度")

    def yzt(self):
        if self.h is not None:
            print(f'圆柱的体积: {self.r ** 2 * 3.14 * self.h}')
        else:
            print("请输入高度")
