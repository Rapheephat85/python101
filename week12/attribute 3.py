class calculate_area:
    def rectangle(self, w, h):
        return w * h

    def triangle_area(self, b, h):
        return 0.5 * b * h

    def circle_area(self, r):
        return 3.14 * r * r
cal = calculate_area()
cal_rec = cal.rectangle(4,5)
cal_tri = cal.triangle_area(4,5)
cal_cir = cal.circle_area(5)

print('Rectangle area:', cal_rec)
print('Triangle area:', cal_tri)
print('Circle area:', cal_cir)

# print('Test Triangle area:', calculate_area.triangle_area(5,6))
# print('Test Circle area:', calculate_area.circle_area(5))
# print('Test Rectangle area:', calculate_area.rectangle_area(4,5))