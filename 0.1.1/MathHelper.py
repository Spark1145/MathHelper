import depG
import depJ

print("欢迎使用MathHelper")
print('版本:1.0.0', '更新内容：新添“几何”模式，可以计算基本几何图形计算需要')

while True:
    print('请选择模式:')
    print('1.几何')
    print('2.解决实际问题')
    print('0.退出')
    ans = input()

    if ans == '1':
        while True:
            print('请选择图形:')
            print('1.正方形')
            print('2.正方体')
            print('3.长方形')
            print('4.长方体')
            print('5.三角形与平行四边形')
            print('6.(关于)圆')
            print('0.返回上级菜单')

            ans = input()
            if ans == '1':
                try:
                    print('请输入边长')
                    length = float(input())
                    shape = depG.zfx(length)  # 创建 zfx 类的实例
                    shape.mj()
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '2':
                try:
                    print('请输入边长')
                    length = float(input())
                    shape = depG.zft(length)  # 创建 zft 类的实例
                    shape.bmj()
                    shape.tj()
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '3':
                try:
                    print('请输入长')
                    x = float(input())
                    print('请输入宽')
                    y = float(input())
                    shape = depG.cfx(x, y)  # 创建 cfx 类的实例
                    shape.mj()
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '4':
                try:
                    print('请输入长')
                    x = float(input())
                    print('请输入宽')
                    y = float(input())
                    print('请输入高')
                    z = float(input())
                    shape = depG.cft(x, y, z)  # 创建 cft 类的实例
                    shape.bmj()
                    shape.tj()
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '5':
                try:
                    print('请输入底长')
                    w = float(input())
                    print('请输入高')
                    h = float(input())
                    print('三角形还是平行四边形?')
                    print('1.三角形')
                    print('2.平行四边形')
                    ans = input()
                    shape = depG.wh(w, h)  # 创建 wh 类的实例
                    if ans == '1':
                        shape.sjx()
                    elif ans == '2':
                        shape.pxsb()
                    else:
                        print('无效的选择')
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '6':
                try:
                    print('请输入半径')
                    r = float(input())
                    print('圆或圆柱?')
                    print('1.圆')
                    print('2.圆柱')
                    ans = input()
                    if ans == '1':
                        shape = depG.cir(r)  # 创建 cir 类的实例（圆）
                        shape.d()
                        shape.c()
                        shape.mj()
                    elif ans == '2':
                        print('请输入高')
                        h = float(input())
                        shape = depG.cir(r, h)  # 创建 cir 类的实例（圆柱）
                        shape.yzb()
                        shape.yzt()
                    else:
                        print('无效的选择')
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '0':
                break
            else:
                print('无效的选择')

    elif ans == '2':
        while True:
            print('请选择问题类型:')
            print('1.路程问题')
            print('2.工程问题')
            print('0.返回上级菜单')

            ans = input()
            if ans == '1':
                try:
                    print('如求路程，请输入时间和速度，路程处输入？')
                    print('请输入速度(km/h)')
                    v = input()
                    v = None if v in ['?', '？'] else float(v)

                    print('请输入时间(h)')
                    t = input()
                    t = None if t in ['?', '？'] else float(t)

                    print('请输入路程(km)')
                    d = input()
                    d = None if d in ['?', '？'] else float(d)

                    # 实例化 glc 类
                    if v is not None and t is not None:
                        glc_instance = depJ.glc(v, t, d)
                        glc_instance.vt()
                    elif v is not None and d is not None:
                        glc_instance = depJ.glc(v, t, d)
                        glc_instance.vd()
                    elif t is not None and d is not None:
                        glc_instance = depJ.glc(v, t, d)
                        glc_instance.td()
                    else:
                        print('请输入完整的信息')
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '2':
                try:
                    print('如求工程总量，请输入施工时间和施工速度，工程总量处输入？')
                    print('请输入速度(km/h)')
                    v = input()
                    v = None if v in ['?', '？'] else float(v)

                    print('请输入施工时间(h)')
                    t = input()
                    t = None if t in ['?', '？'] else float(t)

                    print('请输入工程总量(km)')
                    d = input()
                    d = None if d in ['?', '？'] else float(d)

                    # 实例化 glc 类
                    if v is not None and t is not None:
                        glc_instance = depJ.glc(v, t, d)
                        glc_instance.vt()
                    elif v is not None and d is not None:
                        glc_instance = depJ.glc(v, t, d)
                        glc_instance.vd()
                    elif t is not None and d is not None:
                        glc_instance = depJ.glc(v, t, d)
                        glc_instance.td()
                    else:
                        print('请输入完整的信息')
                except ValueError:
                    print("输入无效，请输入数字")

            elif ans == '0':
                break
            else:
                print('无效的选择')

    elif ans == '0':
        print('程序终止')
        break
    else:
        print('无效的选择')