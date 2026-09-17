# -*- coding: utf-8 -*-
import random
import math
from fractions import Fraction

# ---------- 工具 ----------

def fmt(v):
    f = Fraction(v)
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"

_FW = {}
for _n in range(10):
    _FW[chr(0xFF10 + _n)] = str(_n)
for _a_, _b_ in (("\uFF0E", "."), ("\uFF0C", ","), ("\uFF1B", ";"),
                 ("\uFF0F", "/"), ("\uFF0D", "-"), ("\u2212", "-"),
                 ("\uFE63", "-"), ("\u3000", ""), ("\uFF05", "%"),
                 ("\uFF08", "("), ("\uFF09", ")")):
    _FW[_a_] = _b_

def norm(s):
    s = "".join(_FW.get(ch, ch) for ch in str(s))
    s = s.strip()
    s = s.replace(" ", "").replace("\u3000", "")
    return s

def parse_list(s):
    s = s.replace("[", "").replace("]", "")
    items = []
    for tok in s.split(","):
        if tok.strip() == "":
            continue
        items.append(Fraction(tok.replace(";", ",")))
    return items

def check(user, ans):
    u = norm(user)
    a = norm(ans)
    if u == a:
        return True
    try:
        if ";" in a or ";" in u:
            lu = [Fraction(x) for x in u.replace(";", ",").split(",") if x != ""]
            la = [Fraction(x) for x in a.replace(";", ",").split(",") if x != ""]
            return lu == la
        if "," in a or "," in u:
            return parse_list(u) == parse_list(a)
        return Fraction(u) == Fraction(a)
    except Exception:
        return False

def gcd_ints(a, b):
    return math.gcd(a, b)

def lcm_ints(a, b):
    return a // math.gcd(a, b) * b

# ---------- 各年級題目產生器 ----------
# 每個 (名稱, 函式(回傳 (題目文字, 答案字串)))

G = {}

# ---- 小一 ----
def p1():
    a = 10 + random.randint(0, 79)
    b = random.randint(2, 9)
    return f"{a} + {b} = ?", str(a + b)

def p2():
    a = random.randint(11, 98)
    while a % 10 < 2 or a % 10 > 8:
        a = random.randint(11, 98)
    b = random.randint(a % 10 + 1, 9)
    if b > a:
        b = 9
        a = random.randint(18, 98)
    while b >= a:
        a += 1
    return f"{a} - {b} = ?", str(a - b)

def p3():
    a = random.randint(10, 90)
    b = random.randint(10, 90)
    c = random.randint(1, 9)
    if a + b - c > 99:
        a = random.randint(10, 60 + c)
    return f"{a} + {b} - {c} = ?", str(a + b - c)

def p4():
    a = random.randint(11, 90)
    b = random.randint(10, a - 1)
    return f"{a} - {b} + {random.randint(1, 9)} = ?", str(a - b + random.randint(1, 9))

def p5():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    while a == b:
        b = random.randint(1, 20)
    return f"比較大小：{a} 和 {b}，比較大的數是多少？", str(max(a, b))

G["小一"] = [("二位數加法", p1), ("二位數減法", p2), ("加減混合(一)", p3), ("加減混合(二)", p4), ("比較大小", p5)]

# ---- 小二 ----
def p2a():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    return f"{a} × {b} = ?", str(a * b)

def p2b():
    d = random.randint(2, 9)
    q = random.randint(2, 9)
    return f"{d * q} ÷ {d} = ?", str(q)

def p2c():
    return f"{random.randint(100, 998)} + {random.randint(100, 899)} = ?", str(random.randint(100, 998) + random.randint(100, 899))

def p2d():
    a = random.randint(200, 999)
    b = random.randint(100, a - 1)
    return f"{a} - {b} = ?", str(a - b)

def p2e():
    n = random.randint(1, 9)
    return f"{n * 100} 公分等於幾公尺？", str(n)

def p2f():
    n = random.randint(2, 9)
    return f"1 公斤 = 1000 公克。{n * 1000} 公克等於幾公斤？", str(n)

G["小二"] = [("九九乘法", p2a), ("除法口訣", p2b), ("三位數加法", p2c), ("三位數減法", p2d), ("長度換算", p2e), ("重量換算", p2f)]

# ---- 小三 ----
def p3a():
    d = random.randint(3, 9)
    q = random.randint(3, 9)
    r = random.randint(1, d - 1)
    return f"{d * q + r} ÷ {d} = ?（輸入「商,餘」）", f"{q},{r}"

def p3b():
    den = random.randint(2, 12)
    a = random.randint(1, den - 1)
    b = random.randint(1, den - a)
    return f"分數加法：{fmt(Fraction(a, den))} + {fmt(Fraction(b, den))} = ?", fmt(Fraction(a + b, den))

def p3c():
    den = random.randint(3, 12)
    a = random.randint(2, den - 1)
    b = random.randint(1, a - 1)
    return f"分數減法：{fmt(Fraction(a, den))} - {fmt(Fraction(b, den))} = ?", fmt(Fraction(a - b, den))

def p3d():
    a = random.randint(2, 30)
    b = random.randint(2, 30)
    return f"長方形的長是 {a} 公分、寬是 {b} 公分，周長是多少公分？", str(2 * (a + b))

def p3e():
    a = random.randint(2, 30)
    b = random.randint(2, 30)
    return f"長方形的長是 {a} 公分、寬是 {b} 公分，面積是多少平方公分？", str(a * b)

G["小三"] = [("除法(商與餘數)", p3a), ("分數加法", p3b), ("分數減法", p3c), ("長方形周長", p3d), ("長方形面積", p3e)]

# ---- 小四 ----
def p4a():
    a = random.randint(12, 98)
    b = random.randint(3, 9)
    return f"{a} × {b} = ?", str(a * b)

def p4b():
    q = random.randint(12, 99)
    d = random.randint(3, 9)
    return f"{d * q} ÷ {d} = ?", str(q)

def p4c():
    d1 = random.randint(2, 9)
    d2 = random.randint(3, 9)
    while d1 == d2:
        d2 = random.randint(3, 9)
    a = random.randint(1, d1 - 1)
    b = random.randint(1, d2 - 1)
    return f"分數加法：{fmt(Fraction(a, d1))} + {fmt(Fraction(b, d2))} = ?（答案化到最簡）", fmt(Fraction(a, d1) + Fraction(b, d2))

def p4d():
    a = random.randint(10, 200)
    x = random.randint(1, 9)
    b = random.randint(10, 200)
    y = random.randint(1, 9)
    op = random.choice(["+", "-"])
    n1 = a * 10 + x
    n2 = b * 10 + y
    if op == "+":
        return f"{a}.{x} + {b}.{y} = ?", str(Fraction(n1 + n2, 10))
    while n1 < n2:
        a = random.randint(60, 200)
        x = random.randint(1, 9)
        n1 = a * 10 + x
    return f"{a}.{x} - {b}.{y} = ?", str(Fraction(n1 - n2, 10))

def p4e():
    a = random.randint(2, 99)
    b = random.randint(2, 99)
    return f"24 點小考：{a} × {b} 的積是多少？", str(a * b)

G["小四"] = [("二位數乘法", p4a), ("除法(二位數商)", p4b), ("分數加法(異分母)", p4c), ("小數加減", p4d), ("乘法練習", p4e)]

# ---- 小五 ----
def p5a():
    a = random.randint(12, 90)
    b = random.randint(10, a - 1)
    return f"求 {a} 和 {b} 的最大公因數 (GCD)？", str(gcd_ints(a, b))

def p5b():
    a = random.randint(12, 90)
    b = random.randint(10, a - 1)
    return f"求 {a} 和 {b} 的最小公倍數 (LCM)？", str(lcm_ints(a, b))

def p5c():
    n1 = random.randint(1, 9)
    d1 = random.randint(2, 9)
    n2 = random.randint(1, 9)
    d2 = random.randint(2, 9)
    while n2 == d2:
        d2 = random.randint(2, 9)
    a = Fraction(n1, d1) * Fraction(n2, d2)
    return f"分數乘法：{fmt(Fraction(n1, d1))} × {fmt(Fraction(n2, d2))} = ?（化到最簡）", fmt(a)

def p5d():
    n1 = random.randint(1, 9)
    d1 = random.randint(2, 9)
    n2 = random.randint(1, 9)
    d2 = random.randint(2, 9)
    a = Fraction(n1, d1) / Fraction(n2, d2)
    return f"分數除法：{fmt(Fraction(n1, d1))} ÷ {fmt(Fraction(n2, d2))} = ?（化到最簡）", fmt(a)

def p5e():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    x = random.randint(1, 9)
    return f"小數乘法：{a}.{x} × {b} = ?", str(Fraction((a * 10 + x) * b, 10))

def p5f():
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    z = random.randint(2, 9)
    return f"長方體的長 {x} 公分、寬 {y} 公分、高 {z} 公分，體積是多少立方公分？", str(x * y * z)

G["小五"] = [("最大公因數", p5a), ("最小公倍數", p5b), ("分數乘法", p5c), ("分數除法", p5d), ("小數乘法", p5e), ("長方體體積", p5f)]

# ---- 小六 ----
def p6a():
    r = random.randint(1, 6)
    a12 = r * 12
    return f"有 {a12} 顆蘋果，每 {r} 顆裝一袋，共可裝幾袋？", str(12)

def p6b():
    k = random.randint(2, 9)
    n = random.randint(2, 9)
    return f"比例：{k} : {n} = {k * 4} : ?（求問號）", str(n * 4)

def p6c():
    r = random.choice([10, 20, 30, 40, 50])
    return f"圓的半徑是 {r} 公分，圓周長是多少公分？（取 π = 3.14）", str(int(2 * 3.14 * r))

def p6d():
    r = random.choice([10, 20, 30])
    return f"圓的半徑是 {r} 公分，圓面積是多少平方公分？（取 π = 3.14）", str(int(3.14 * r * r))

def p6e():
    while True:
        nums = [random.randint(10, 99) for _ in range(3)]
        if sum(nums) % 3 == 0:
            break
    return f"求 {nums[0]}、{nums[1]}、{nums[2]} 的平均數。", str(sum(nums) // 3)

def p6f():
    d = random.randint(2, 9)
    q = random.randint(2, 9)
    total = d * q
    print_a = d
    return f"{total} 顆糖果平分給 {d} 人，每人分幾顆？", str(q)

G["小六"] = [("比例應用", p6a), ("比例求未知", p6b), ("圓周長", p6c), ("圓面積", p6d), ("平均數", p6e), ("平均分配", p6f)]

# ---- 國一 ----
def p7a():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = random.randint(2, 9)
    r = -a * b + c
    return f"計算：-({a}×{b}) + {c} = ?", str(r)

def p7b():
    x = random.randint(-9, 9)
    while x == 0:
        x = random.randint(-9, 9)
    a = random.randint(2, 9)
    b = random.choice([-1, 1]) * random.randint(2, 9)
    c = a * x - b
    return f"解一元一次方程式：{a}x {('+' if b >= 0 else '-')} {abs(b)} = {c}，求 x。", str(x)

def p7c():
    a = random.randint(30, 70)
    b = random.randint(30, 70)
    c = 180 - a - b
    while c <= 0:
        a = random.randint(30, 70)
        b = random.randint(30, 70)
        c = 180 - a - b
    return f"三角形兩內角分別是 {a}° 和 {b}°，第三個角是幾度？", str(c)

def p7d():
    x = random.randint(2, 99)
    return f"|{-x}| = ?（絕對值）", str(x)

def p7e():
    a = random.randint(2, 9)
    n = random.randint(2, 9)
    return f"計算：{a} × (-{n}) + {a} × {n} = ?", "0"

G["國一"] = [("負數四則運算", p7a), ("一元一次方程式", p7b), ("三角形內角", p7c), ("絕對值", p7d), ("分配律練習", p7e)]

# ---- 國二 ----
def gen_binary():
    while True:
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        a1 = random.randint(1, 9)
        b1 = random.randint(1, 9)
        c1 = a1 * x + b1 * y
        denom = a1 * 1 - 1 * a1
        # 找第二條方程式：手動確定非平行
        a2 = random.randint(1, 9)
        b2 = random.randint(1, 9)
        while a1 * b2 == a2 * b1:
            a2 = random.randint(1, 9)
            b2 = random.randint(1, 9)
        c2 = a2 * x + b2 * y
        return (a1, b1, c1, a2, b2, c2, x, y)

def p8a():
    a1, b1, c1, a2, b2, c2, x, y = gen_binary()
    return (f"解方程組：\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}\n輸入「x,y」", f"{x},{y}")

def p8b():
    m = random.randint(2, 5)
    n = random.randint(1, 4)
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return f"直角三角形兩股為 {a} 和 {b}，斜邊長多少？", str(c)

def p8c():
    a = random.randint(2, 9)
    b = random.randint(-9, 9)
    k = random.randint(-9, 9)
    return f"f(x) = {a}x + {b}，求 f({k})。", str(a * k + b)

def p8d():
    n = random.randint(3, 10)
    return f"{n} 邊形的內角和為幾度？", str((n - 2) * 180)

def p8e():
    a = random.randint(2, 9)
    return f"化簡：(x + {a})² 中 x 的一次項係數。", str(2 * a)

G["國二"] = [("二元一次方程組", p8a), ("畢氏定理", p8b), ("多項式代入", p8c), ("多邊形內角和", p8d), ("乘法公式", p8e)]

# ---- 國三 ----
def p9a():
    r1 = random.randint(-7, 7)
    r2 = random.randint(-7, 7)
    while r2 == r1:
        r2 = random.randint(-7, 7)
    s = r1 + r2
    p = r1 * r2
    sign_s = "+" if -s >= 0 else "-"
    sign_p = "+" if p >= 0 else "-"
    return f"方程式 x² {sign_s} {abs(s)}x {sign_p} {abs(p)} = 0 的兩根之和是多少？", str(s)

def p9b():
    r = random.randint(2, 8)
    a = random.randint(1, 9)
    b = r * a
    if a == 6:
        b = r * a
    return f"兩個相似三角形，邊長比為 {a}:{r}，大三角形對應邊長 {b}，小三角形對應邊長是多少？", str(a)

def p9c():
    h = random.randint(-5, 5)
    k = random.randint(-5, 5)
    return f"二次函數 y = (x - {h})² + {k} 的頂點座標「h,k」？", f"{h},{k}"

def p9d():
    ang = random.choice([60, 80, 100, 120, 140, 160, 180])
    return f"圓心角 {ang}° 對應的圓周角是幾度？", str(ang // 2)

def p9e():
    a = random.randint(2, 9)
    return f"y = {a}x² 通過點 (2, ??)，當 x=2 時 y 是多少？", str(a * 4)

G["國三"] = [("兩根之和", p9a), ("相似三角形", p9b), ("二次函數頂點", p9c), ("圓周角", p9d), ("二次函數代入", p9e)]

# ---- 高一 ----
def p10a():
    a = random.randint(1, 9)
    b = random.randint(-9, 9)
    k = random.randint(1, 9)
    return f"f(x) = x² + {a}x + {b}，除以 (x - {k}) 的餘數 f({k})？", str(k * k + a * k + b)

def p10b():
    a = random.randint(2, 9)
    n = random.randint(2, 4)
    return f"{a} 的 {n} 次方（{a}^{n}）= ?", str(a ** n)

def p10c():
    b = random.choice([2, 3, 4, 5])
    n = random.randint(2, 6)
    return f"log₍{b}₎({b ** n}) = ?", str(n)

def p10d():
    sq = [2, 3, 5, 6, 7, 10, 11]
    k = random.randint(2, 6)
    m = random.choice(sq)
    return f"化簡 √({k * k * m}) = ?（輸入 a√b 格式，如 3√2）", f"{k}√{m}"

def p10e():
    t = random.choice([("sin", 30, "1/2"), ("cos", 60, "1/2"), ("tan", 45, "1")])
    return f"sin/cos/tan 值：{t[0]} {t[1]}° = ?（可用分數）", t[2]

G["高一"] = [("綜合除法餘式", p10a), ("指數運算", p10b), ("對數", p10c), ("根號運算", p10d), ("特別角三角函數", p10e)]

# ---- 高二 ----
def p11a():
    a = random.randint(1, 9)
    d = random.randint(2, 9)
    n = random.randint(6, 15)
    return f"等差數列的首項是 {a}、公差是 {d}，第 {n} 項是多少？", str(a + (n - 1) * d)

def p11b():
    a = random.randint(1, 3)
    r = random.randint(2, 3)
    n = random.randint(4, 6)
    return f"等比數列的首項是 {a}、公比是 {r}，第 {n} 項是多少？", str(a * (r ** (n - 1)))

def p11c():
    a1, a2 = random.randint(1, 9), random.randint(1, 9)
    b1, b2 = random.randint(1, 9), random.randint(1, 9)
    return f"向量 (a) = ({a1},{a2})、(b) = ({b1},{b2})，(a)·(b) 內積？", str(a1 * b1 + a2 * b2)

def p11d():
    ang = random.choice([("sin", 150, "1/2"), ("cos", 120, "-1/2"), ("tan", 135, "-1"),
                         ("sin", 30, "1/2"), ("cos", 240, "-1/2"), ("sin", 210, "-1/2"),
                         ("cos", 180, "-1"), ("sin", 180, "0")])
    return f"{ang[0]} {ang[1]}° = ?（可用分數）", ang[2]

def p11e():
    a = random.randint(1, 9)
    b = random.randint(1, 5)
    return f"數列 aₙ = {a}n + {b}，求第 10 項。", str(10 * a + b)

G["高二"] = [("等差數列", p11a), ("等比數列", p11b), ("向量內積", p11c), ("廣義角三角函數", p11d), ("數列公式", p11e)]

# ---- 高三 ----
def p12a():
    n = random.randint(5, 10)
    r = random.randint(2, n - 1)
    return f"排列：從 {n} 個不同物品選 {r} 個排列，方法數 P({n},{r})？", str(math.perm(n, r))

def p12b():
    n = random.randint(5, 15)
    r = random.randint(2, n // 2 + 1)
    return f"組合：從 {n} 個不同物品選 {r} 個，方法數 C({n},{r})？", str(math.comb(n, r))

def p12c():
    a, b = random.randint(1, 5), random.randint(1, 5)
    c, d = random.randint(1, 5), random.randint(1, 5)
    e, f = random.randint(1, 5), random.randint(1, 5)
    g, h = random.randint(1, 5), random.randint(1, 5)
    return (f"矩陣乘法：\n[{a} {b}; {c} {d}] × [{e} {f}; {g} {h}] = ?\n輸入「p,q;r,s」",
            f"{a*e+b*g},{a*f+b*h};{c*e+d*g},{c*f+d*h}")

def p12d():
    a = random.randint(2, 9)
    n = random.randint(2, 4)
    k = random.randint(1, 3)
    return f"f(x) = {a}x^{n}，求 f'({k})（導數）？", str(a * n * (k ** (n - 1)))

def p12e():
    a = random.randint(1, 9)
    n = random.randint(1, 4)
    return f"定積分 ∫₀¹ {a}x^{n} dx = ?（答案可用分數 a/(n+1)）", fmt(Fraction(a, n + 1))

G["高三"] = [("排列 P", p12a), ("組合 C", p12b), ("矩陣乘法", p12c), ("微分", p12d), ("定積分", p12e)]

# ---------- v2.1 新增題型 ----------

# 小一：十以內加減
def q1_10():
    if random.random() < 0.5:
        a = random.randint(1, 8)
        b = random.randint(1, 10 - a)
        return f"{a} + {b} ＝ ?", str(a + b)
    b = random.randint(1, 9)
    a = random.randint(b + 1, 10)
    return f"{a} - {b} ＝ ?", str(a - b)

# 小二：時間換算
def q2_time():
    h = random.choice([1, 2, 3, 5, 6])
    return f"{h} 小時 ＝ 幾分鐘？", str(h * 60)

# 小三：正方形周長與面積
def q3_sq():
    s = random.randint(3, 12)
    if random.random() < 0.5:
        return f"邊長 {s} 公分的正方形，周長 ＝ 幾公分？", str(s * 4)
    return f"邊長 {s} 公分的正方形，面積 ＝ 幾平方公分？", str(s * s)

# 小四：四則混合（先乘除後加減）
def q4_mixed():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = random.randint(2, 9)
    return f"{a} + {b} × {c} ＝ ?", str(a + b * c)

# 小五：分數化成小數
def q5_fracdec():
    pair = random.choice([(1, 2), (1, 4), (3, 4), (1, 5), (2, 5),
                          (3, 5), (4, 5), (1, 8), (1, 10), (7, 10), (1, 25)])
    return f"分數 {pair[0]}/{pair[1]} 化成小數 ＝ ?", str(Fraction(*pair))

# 小五：質數判斷
def q5_prime():
    n = random.randint(2, 29)
    is_p = all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    return f"{n} 是質數嗎？（回答『是』或『否』）", "是" if is_p else "否"

# 小六：百分率求值
def q6_pct():
    pct = random.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 75, 80, 90, 95])
    k = random.randint(1, 9)
    return f"{pct}% 的 {k * 100} ＝ ?", str(pct * k)

# 國一：科學記號（還原為數字）
def q7_sci():
    mant = random.choice([1.2, 2.5, 3.5, 4.8, 6.4, 8.2, 9.6])
    n = random.randint(2, 4)
    v = int(mant * 10 ** n)
    return f"{mant} × 10^{n} 用一般數字表示 ＝ ?", str(v)

# 國一：一元一次不等式
def q7_ineq():
    k = random.randint(-9, 9)
    c = random.randint(1, 9)
    while k == c:
        k = random.randint(-9, 9)
    op = random.choice([">", "<", "≥", "≤"])
    sym = ">" if op in (">", "≥") else "<"
    return (f"x + {k} {op} {c}，求 x（輸入如 x>3 或 x<2）？",
            f"x{sym}{c - k}")

# 國二：直線斜率
def q8_slope():
    dx = random.randint(1, 4)
    while True:
        m = random.randint(-3, 3)
        if m != 0:
            break
    dy = dx * m
    x1 = random.randint(0, 6)
    y1 = random.randint(0, 6)
    return (f"直線通過 ({x1},{y1}) 與 ({x1 + dx},{y1 + dy})，斜率 m ＝ ?",
            str(m))

# 國二：畢氏三元組（求另一股）
def q8_pythleg():
    while True:
        m = random.randint(2, 6)
        n = random.randint(1, m - 1)
        if (m - n) % 2 == 1:
            break
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    if random.random() < 0.5:
        return f"直角三角形斜邊 {c}、一股 {b}，求另一股。", str(a)
    return f"直角三角形斜邊 {c}、一股 {a}，求另一股。", str(b)

# 國三：判別式 b²-4ac
def q9_disc():
    a = random.randint(1, 9)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    return f"二次方程 {a}x² + ({b})x + ({c}) ＝ 0，判別式 b²-4ac ＝ ?", str(b * b - 4 * a * c)

# 國三：兩根之積
def q9_prod():
    r1 = random.randint(-6, 6)
    r2 = random.randint(-6, 6)
    while r2 == r1:
        r2 = random.randint(-6, 6)
    return f"方程兩根為 {r1} 與 {r2}，兩根之積 ＝ ?", str(r1 * r2)

# 高一：對數相加
def q10_logadd():
    b = random.randint(2, 5)
    m = random.randint(1, 4)
    n = random.randint(1, 4)
    return (f"log₍{b}₎{b ** m} + log₍{b}₎{b ** n} ＝ ?",
            str(m + n))

# 高一：指數求值
def q10_exp():
    b = random.randint(2, 5)
    k = random.randint(1, 4)
    return f"{b}^? ＝ {b ** k}，求指數 ＝ ?", str(k)

# 高一：(x+a)(x+b) 一次項係數
def q10_fact2():
    a = random.randint(1, 8)
    b = random.randint(1, 8)
    return f"(x+{a})(x+{b}) 展開後 x 的係數 ＝ ?", str(a + b)

# 高二：等差級數和
def q11_apsum():
    while True:
        a = random.randint(1, 5)
        d = random.randint(2, 5)
        n = random.randint(6, 12)
        s2 = n * (2 * a + (n - 1) * d)
        if s2 % 2 == 0:
            break
    return (f"等差級數：首項 {a}、公差 {d}，前 {n} 項和 S{n} ＝ ?",
            str(s2 // 2))

# 高二：向量長度
def q11_veclen():
    k = random.choice([1, 2, 3])
    vec = random.choice([(3, 4), (5, 12), (8, 15)])
    v = (vec[0] * k, vec[1] * k)
    L = int(math.hypot(*v))
    return f"向量 ({v[0]},{v[1]}) 的長度 |v| ＝ ?", str(L)

# 高二：等比級數和
def q11_gpsum():
    a = random.randint(1, 3)
    r = random.choice([2, 3])
    n = random.randint(4, 6)
    S = a * (r ** n - 1) // (r - 1)
    return (f"等比級數：首項 {a}、公比 {r}，前 {n} 項和 S{n} ＝ ?",
            str(S))

# 高三：矩陣行列式
def q12_det():
    a, b, c, d = (random.randint(-4, 4) for _ in range(4))
    return (f"行列式 |{a}  {b}；{c}  {d}|（ad − bc）＝ ?",
            str(a * d - b * c))

# 高三：公正骰子機率
def q12_prob():
    case = random.choice([
        ("偶數", Fraction(1, 2)),
        ("奇數", Fraction(1, 2)),
        ("質數（2,3,5）", Fraction(1, 2)),
        ("大於 4", Fraction(1, 3)),
        ("6 的倍數", Fraction(1, 6)),
    ])
    return (f"擲一粒公正骰子，出現『{case[0]}』的機率 ＝ ?",
            fmt(case[1]))

# 高三：矩陣加法
def q12_matadd():
    vals = [random.randint(1, 9) for _ in range(8)]
    a, b, c, d, e, f2, g, h = vals
    return (f"[{a} {b}；{c} {d}] + [{e} {f2}；{g} {h}] ＝ ?（輸入「p,q；r,s」格式）",
            f"{a + e},{b + f2};{c + g},{d + h}")

G["小一"] = G["小一"] + [("十以內加減", q1_10)]
G["小二"] = G["小二"] + [("時間換算", q2_time)]
G["小三"] = G["小三"] + [("正方形周長面積", q3_sq)]
G["小四"] = G["小四"] + [("四則混合", q4_mixed)]
G["小五"] = G["小五"] + [("分數化小數", q5_fracdec), ("質數判斷", q5_prime)]
G["小六"] = G["小六"] + [("百分率求值", q6_pct)]
G["國一"] = G["國一"] + [("科學記號", q7_sci), ("一元一次不等式", q7_ineq)]
G["國二"] = G["國二"] + [("直線斜率", q8_slope), ("畢氏求股", q8_pythleg)]
G["國三"] = G["國三"] + [("判別式", q9_disc), ("兩根之積", q9_prod)]
G["高一"] = G["高一"] + [("對數相加", q10_logadd), ("指數求值", q10_exp),
                        ("展開一次項", q10_fact2)]
G["高二"] = G["高二"] + [("等差級數和", q11_apsum), ("向量長度", q11_veclen),
                        ("等比級數和", q11_gpsum)]
G["高三"] = G["高三"] + [("行列式", q12_det), ("骰子機率", q12_prob),
                        ("矩陣加法", q12_matadd)]

# ---------- 應用題（生活情境） ----------

# 小一：水果攤加減
def a1_shop():
    kind = random.choice(["蘋果", "柳丁", "糖果", "氣球", "鉛筆"])
    if random.random() < 0.5:
        b = random.randint(2, 6)
        a = random.randint(7, 10)
        return f"水果攤有 {b} 顆{kind}，媽媽又買了 {a} 顆，現在一共有幾顆？", str(a + b)
    a = random.randint(6, 10)
    b = random.randint(2, 5)
    return f"姊姊有 {a} 顆{kind}，分給弟弟 {b} 顆後，姊姊還剩幾顆？", str(a - b)

# 小二：平分點心
def a2_share():
    k = random.randint(2, 6)
    m = random.randint(2, 5)
    kind = random.choice(["糖果", "餅乾", "果凍", "貼紙"])
    return f"老師把 {k * m} 顆{kind}平分給 {m} 位小朋友，每位小朋友拿到幾顆？", str(k)

# 小三：購物找錢
def a3_money():
    price = random.randint(6, 24)
    n = random.randint(2, 4)
    pay = 100
    cost = price * n
    return f"一枝筆 {price} 元，買 {n} 枝給 100 元，應找回多少元？", str(pay - cost)

# 小四：行車距離
def a4_dist():
    v = random.choice([45, 60, 75, 80, 90])
    t = random.randint(2, 5)
    return (f"巴士以時速 {v} 公里行駛 {t} 小時，共行駛多少公里？",
            str(v * t))

# 小五：折扣價
def a5_discount():
    p = random.choice([40, 50, 60, 80, 120, 150])
    d = random.choice([("八", 8), ("五", 5), ("九", 9)])
    rate = d[1] / 10
    return (f"原價 {p} 元的玩具打{d[0]}折，特價是多少元？",
            str(int(p * rate)))

# 小六：圓面積（圓周率＝3.14）
def a6_circle():
    r = random.choice([10, 20, 30])
    return f"半徑 {r} 公分的圓，面積是多少平方公分？（圓周率用 3.14）", str(int(3.14 * r * r))

# 國一：年齡問題
def a7_age():
    a = random.randint(8, 12)
    b = random.randint(2, 7)
    return (f"小明今年 {a} 歲，哥哥比他大 {b} 歲，再過 5 年哥哥是幾歲？",
            str(a + b + 5))

# 國二：平均速率
def a8_speed():
    v = random.choice([60, 75, 90, 105])
    t = random.choice([2, 3, 4])
    return (f"阿忠開車共行駛 {v * t} 公里，花了 {t} 小時，平均時速是多少公里？",
            str(v))

# 國三：影子相似三角形
def a9_shadow():
    h = random.choice([140, 150, 160, 170])
    s = h // 2
    k = random.randint(2, 7)
    S = s * k
    return (f"身高 {h} 公分的小華影子長 {s} 公分。同時間旗杆的影子長 {S} 公分，旗杆高幾公分？",
            str(h * k))

# 高一：單利本利和
def a10_interest():
    P = random.choice([10000, 20000, 50000])
    r = random.choice([1, 2, 3, 5])
    n = random.choice([2, 3, 5])
    return (f"存款 {P} 元，年利率 {r}%，存單利 {n} 年，共可領回多少本利和？",
            str(P + P * r * n // 100))

# 高二：期望值（抽球得分）
def a11_expect():
    case = random.choice([(3, 1, 100), (1, 1, 50), (2, 2, 60), (4, 1, 80)])
    x, y, prize = case
    val = prize * x // (x + y)
    return (f"袋中有 {x} 顆紅球、{y} 顆白球。抽中紅球得 {prize} 元、抽中白球得 0 元（抽後放回）。抽一次的期望值是多少元？",
            str(val))

# 高三：行列式求平行四邊形面積
def a12_area():
    while True:
        a, b, c, d = (random.randint(1, 9) for _ in range(4))
        area = abs(a * d - b * c)
        if area:
            break
    return (f"以向量 ({a},{b})、({c},{d}) 為相鄰兩邊的平行四邊形，以行列式求面積為多少？",
            str(area))

G["小一"] = G["小一"] + [("應用題", a1_shop)]
G["小二"] = G["小二"] + [("應用題", a2_share)]
G["小三"] = G["小三"] + [("應用題", a3_money)]
G["小四"] = G["小四"] + [("應用題", a4_dist)]
G["小五"] = G["小五"] + [("應用題", a5_discount)]
G["小六"] = G["小六"] + [("應用題", a6_circle)]
G["國一"] = G["國一"] + [("應用題", a7_age)]
G["國二"] = G["國二"] + [("應用題", a8_speed)]
G["國三"] = G["國三"] + [("應用題", a9_shadow)]
G["高一"] = G["高一"] + [("應用題", a10_interest)]
G["高二"] = G["高二"] + [("應用題", a11_expect)]
G["高三"] = G["高三"] + [("應用題", a12_area)]

# ---------- v2.4 多元題型（第二波） ----------

def b1_round():
    tens = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    if random.random() < 0.5:
        a = random.choice([10, 20, 30, 40, 50])
        b = random.choice([t for t in tens if t <= 100 - a])
        return f"{a} + {b} ＝ ?", str(a + b)
    a = random.choice([20, 30, 40, 50, 60, 70, 80, 90])
    b = random.choice([t for t in tens if t < a])
    return f"{a} - {b} ＝ ?", str(a - b)

def b2_factor():
    a = random.randint(2, 9)
    f = random.randint(3, 9)
    kind = random.choice(["袋", "盒", "箱", "組"])
    return f"{a * f} 顆糖果，每{a}顆裝一{kind}，可裝幾{kind}？", str(f)

def b3_mixed():
    w = random.randint(2, 5)
    d = random.choice([3, 4, 5, 6])
    n = random.randint(1, d - 1)
    return (f"帶分數 {w} 又 {n}/{d} 化成假分數（輸入 n/m 格式）＝ ?",
            f"{w * d + n}/{d}")

def b4_dist():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = random.randint(2, 9)
    return (f"用分配律計算 {a} × {b} + {a} × {c} ＝ {a} ×（{b} + {c}）＝ ?",
            str(a * (b + c)))

def b5_volume():
    a, b, c = (random.randint(2, 9) for _ in range(3))
    return f"長方體長 {a} cm、寬 {b} cm、高 {c} cm，體積是多少立方公分？", str(a * b * c)

def b6_scale():
    x = random.randint(2, 9)
    k = random.choice([10000, 50000, 100000])
    meters = x * k // 100
    return (f"地圖比例尺 1 : {k}，圖上距離 {x} 公分，實際距離是多少公尺？",
            str(meters))

def b7_system():
    while True:
        x0 = random.randint(-5, 5)
        y0 = random.randint(-5, 5)
        m = random.choice([1, 2, -1, 3])
        n = random.choice([-1, 2, 0, 3])
        if m != n:
            break
    b = y0 - m * x0
    d = y0 - n * x0
    return (f"解聯立方程組：\ny＝{m}x + ({b})\ny＝{n}x + ({d})\n求交點坐標（輸入 x,y 格式）＝ ?",
            f"{x0},{y0}")

def b8_triangle():
    a = random.randint(30, 60)
    b = random.randint(30, 110 - a)
    return f"三角形的兩個內角分別是 {a}°、{b}°，「第三個內角」是幾度？", str(180 - a - b)

def b9_vertex():
    a = random.choice([1, 2, 3])
    k = random.randint(-4, 4)
    b = -2 * a * k
    c = random.randint(-9, 9)
    return (f"二次函數 y ＝ {a}x² + ({b})x + ({c})，頂點的 x 座標是多少？",
            str(k))

def b10_distance():
    k = random.randint(1, 2)
    pair = random.choice([(3, 4), (5, 12), (6, 8), (8, 15)])
    dx, dy = pair[0] * k, pair[1] * k
    return f"點 A({0},{0}) 與 點 B({dx},{dy}) 的距離是多少？", str(int(math.hypot(dx, dy)))

def b11_perm():
    n = random.randint(5, 8)
    r = random.randint(2, 3)
    v = 1
    for i in range(r):
        v *= n - i
    return f"排列 P({n},{r}) ＝ ?", str(v)

def b12_limit():
    a = random.randint(1, 9)
    k = random.randint(-5, 5)
    b = random.randint(-9, 9)
    return f"lim(x→{k})（{a}x + {b}）＝ ?", str(a * k + b)

G["小一"] = G["小一"] + [("整十加減", b1_round)]
G["小二"] = G["小二"] + [("裝箱問題", b2_factor)]
G["小三"] = G["小三"] + [("帶分數化假分數", b3_mixed)]
G["小四"] = G["小四"] + [("分配律簡算", b4_dist)]
G["小五"] = G["小五"] + [("長方體體積", b5_volume)]
G["小六"] = G["小六"] + [("比例尺", b6_scale)]
G["國一"] = G["國一"] + [("聯立方程組(交點)", b7_system)]
G["國二"] = G["國二"] + [("三角形內角和", b8_triangle)]
G["國三"] = G["國三"] + [("拋物線頂點 x", b9_vertex)]
G["高一"] = G["高一"] + [("兩點距離", b10_distance)]
G["高二"] = G["高二"] + [("排列 P 進階", b11_perm)]
G["高三"] = G["高三"] + [("極限值", b12_limit)]

if __name__ == "__main__":
    import sys
    for g, tlist in G.items():
        for name, fn in tlist:
            for _ in range(50):
                q, a = fn()
                assert q and a, (g, name, q, a)
    print("ALL OK", sum(len(v) for v in G.values()), "topics")
