from string import sympy as sp

# Sembolik değişkenleri tanımlama
x, t = sp.symbols('x t')

# --- Soru 1: Türev Alma ---
# f(x) = küp kök(x^2) - 1 / küp kök(x)
# f(x) = x^(2/3) - x^(-1/3) olarak yeniden yazılır.

def soru1():
    f_x = sp.cbrt(x**2) - 1 / sp.cbrt(x)
    # Veya f_x = x**(sp.Rational(2, 3)) - x**sp.Rational(-1, 3)
    türev = sp.diff(f_x, x)
    # Türevi sadeleştirilmiş rasyonel üsler formunda göstermek için:
    sade_türev = türev.simplify()
    return f"Soru 1: f'(x) = {türev}", sade_türev

# --- Soru 2: Parametrik Türev (dy/dx) ---
# x(t) = t^2 + 1, y(t) = t^3 - t. t=2 noktasındaki türev (dy/dx)

def soru2():
    x_t = t**2 + 1
    y_t = t**3 - t

    # dy/dx = (dy/dt) / (dx/dt)
    dy_dt = sp.diff(y_t, t)
    dx_dt = sp.diff(x_t, t)
    
    # Türevi bulma
    dy_dx = dy_dt / dx_dt
    
    # t=2 noktasında değerlendirme
    sonuc = dy_dx.subs(t, 2)
    return f"Soru 2: dy/dx = {dy_dx} (Genel Türev), t=2'de = {sonuc}"

# --- Soru 3: Üstel Fonksiyonun Türevi (x^cos(x)) ---
# f(x) = x^cos(x). Logaritmik türev alma kullanılır.

def soru3():
    # log(f(x)) = cos(x) * log(x)
    # (f'(x) / f(x)) = türev(cos(x) * log(x))
    # f'(x) = f(x) * türev(cos(x) * log(x))
    
    g_x = x**sp.cos(x)
    
    # SymPy doğrudan üstel türevi hesaplayabilir
    türev = sp.diff(g_x, x)
    
    # Sonucu düzenli göstermek için:
    # cos(x) * x^(cos(x)-1) - sin(x) * log(x) * x^cos(x)
    
    # SymPy'nin çıkardığı sonucu kullanacağız.
    return f"Soru 3: f'(x) = {türev}"

# --- Soru 4: Paralel Teğetler (Apsisler Çarpımı) ---
# f(x) = x^3 - 2x^2 + x - 5. y = 5x + 10 doğrusuna paralel teğetlerin apsisleri çarpımı.

def soru4():
    f_x = x**3 - 2*x**2 + x - 5
    
    # Paralel teğetlerin eğimi, y = 5x + 10 doğrusunun eğimine (m=5) eşit olmalıdır.
    m_teget = 5
    
    # f'(x) = 5 denklemini çözmeliyiz.
    f_prime_x = sp.diff(f_x, x) # f'(x) = 3x^2 - 4x + 1
    
    # 3x^2 - 4x + 1 = 5  =>  3x^2 - 4x - 4 = 0 denklemini çöz
    denklem = f_prime_x - m_teget
    
    # Kökleri bulma (teğetlerin değme noktalarının apsisleri)
    kokler = sp.solve(denklem, x)
    
    # Kökler çarpımı (x1 * x2). İkinci dereceden denklemde (ax^2+bx+c=0): c/a
    a = 3
    b = -4
    c = -4
    kokler_carpimi = c / a
    
    # SymPy ile kökleri çarpımı:
    if len(kokler) == 2:
        kokler_carpimi_sympy = kokler[0] * kokler[1]
    else:
        kokler_carpimi_sympy = "Kökler çarpımı (kök sayısı 2 değil)"
        
    return f"Soru 4: f'(x) = 5 denklemi: {f_prime_x} = 5, yani 3x^2 - 4x - 4 = 0. Kökler Çarpımı (c/a) = {-4}/3"

# --- Soru 5: Mutlak Maksimum Değer ---
# f(x) = 2x^3 - 3x^2 - 12x + 5 fonksiyonunun [-2, 3] aralığında alabileceği en büyük değer.

def soru5():
    f_x = 2*x**3 - 3*x**2 - 12*x + 5
    aralik = [-2, 3]
    
    # 1. Kritik noktaları bulma (f'(x) = 0)
    f_prime_x = sp.diff(f_x, x) # f'(x) = 6x^2 - 6x - 12
    kritik_nokta_denklemi = sp.Eq(f_prime_x, 0)
    kritik_noktalar = sp.solve(kritik_nokta_denklemi, x)
    
    # Aralık içindeki kritik noktaları seçme
    test_noktalari = set(aralik)
    for k in kritik_noktalar:
        # SymPy kökleri rasyonel/reel/kompleks olarak döndürebilir. Reel ve aralıkta olanları alıyoruz.
        if k.is_real and aralik[0] <= k <= aralik[1]:
            test_noktalari.add(k)
            
    # 2. Kritik noktalarda ve sınır noktalarında fonksiyon değerlerini hesaplama
    degerler = {}
    for p in test_noktalari:
        deger = f_x.subs(x, p)
        degerler[p] = deger
        
    # 3. En büyük değeri bulma
    mutlak_maksimum = max(degerler.values())
    
    return f"Soru 5: Kritik Noktalar: {kritik_noktalar}. Test Edilen Noktalar: {test_noktalari}. Değerler: {degerler}. Mutlak Maksimum: {mutlak_maksimum}"

# --- Soru 6: Bölümün Türevi (Kuralı) ---
# f(x) = (x^2 + 1) / (x - 2)

def soru6():
    f_x = (x**2 + 1) / (x - 2)
    
    # Bölüm kuralı: (u/v)' = (u'v - uv') / v^2
    türev = sp.diff(f_x, x)
    
    # Sadeleştirilmiş hali
    sade_türev = türev.simplify()
    
    return f"Soru 6: f'(x) = {türev}", sade_türev

# --- Soru 7: Parametrik Teğetin Eğimi (dy/dx) ---
# x(t) = t^2, y(t) = t^3 - 3t. t=2 noktasındaki teğetin eğimi (dy/dx). (Soru 2'ye benzer)

def soru7():
    x_t = t**2
    y_t = t**3 - 3*t

    # dy/dx = (dy/dt) / (dx/dt)
    dy_dt = sp.diff(y_t, t)
    dx_dt = sp.diff(x_t, t)
    
    dy_dx = dy_dt / dx_dt
    
    # t=2 noktasında değerlendirme
    sonuc = dy_dx.subs(t, 2)
    return f"Soru 7: dy/dx = {dy_dx} (Genel Türev), t=2'de = {sonuc}"

# --- Soru 8: Üstel Fonksiyonun Türevi (x^sin(x)) ---
# f(x) = x^sin(x). Logaritmik türev alma kullanılır. (Soru 3'e benzer)

def soru8():
    g_x = x**sp.sin(x)
    türev = sp.diff(g_x, x)
    return f"Soru 8: f'(x) = {türev}"

# --- Soru 9: 4. Dereceden Türev ---
# y = 6x^5 - 8x^4 + 2x^3 - 3x + 5 fonksiyonunun 4. dereceden türevi.

def soru9():
    y_x = 6*x**5 - 8*x**4 + 2*x**3 - 3*x + 5
    
    # sp.diff(fonksiyon, değişken, türev_derecesi)
    dördüncü_türev = sp.diff(y_x, x, 4)
    
    # Not: 5. dereceden bir polinomun 4. türevi bir polinomdur (birinci derece).
    # 5. türevi ise bir sabittir. 6. türevi sıfırdır.
    
    return f"Soru 9: d^4y/dx^4 = {dördüncü_türev}"

# --- Soru 10: Noktadaki Türev (Bölüm Kuralı) ---
# f(x) = e^x / (x + 1). x=0 noktasındaki türev.

def soru10():
    f_x = sp.exp(x) / (x + 1)
    
    # 1. Türevi bulma (Bölüm Kuralı)
    f_prime_x = sp.diff(f_x, x)
    
    # 2. x=0 noktasında değerlendirme
    sonuc = f_prime_x.subs(x, 0)
    
    return f"Soru 10: f'(x) = {f_prime_x} (Genel Türev), x=0'da = {sonuc}"

# --- Çözümleri çalıştırma ve yazdırma ---
print("--- 🔢 Matematik Sorularının SymPy Çözümleri ---")
print("1. ", soru1()[0])
print("   Sadeleştirilmiş: f'(x) =", soru1()[1])
print("-" * 50)
print("2. ", soru2())
print("-" * 50)
print("3. ", soru3())
print("-" * 50)
print("4. ", soru4())
print("-" * 50)
print("5. ", soru5())
print("-" * 50)
print("6. ", soru6()[0])
print("   Sadeleştirilmiş: f'(x) =", soru6()[1])
print("-" * 50)
print("7. ", soru7())
print("-" * 50)
print("8. ", soru8())
print("-" * 50)
print("9. ", soru9())
print("-" * 50)
print("10.", soru10())
print("-" * 50)