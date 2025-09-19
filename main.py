# initial_weight = float(input("请输入您在地球上的初始体重："))
moon_ratio = 0.165  # 月球重量是地球的16.5%

print("未来10年地球和月球体重变化：")
for year in range(1, 11):
    earth_weight = initial_weight + year * 0.5
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年：地球体重{earth_weight:.2f}kg，月球体重{moon_weight:.2f}kg")
