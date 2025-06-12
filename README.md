<details>
<summary>🇹🇷 Türkçe</summary>

# Python İntegral hesaplama programı.

# Bu program ne işe yarar?
- Bu program ile istediğiniz fonksiyonun integral değerini yaklaşık olarak hesaplayabilirsiniz.

# Hangi yöntemler kullanılır?
- Riemann Toplamı
- Simpson Kuralı
- Trapez Yöntemi

# Nasıl kullanılır?

# Riemann Toplamı

Bu fonksiyon, belirli bir `f(x)` fonksiyonunun yaklaşık integralini **Riemann Toplamı** kullanarak hesaplar. Simpson yöntemi, Riemann toplamına göre genellikle daha hassas sonuçlar verir.


### 🔧 Parametreler

- `a` *(float)* – İntegralin alt sınırı  
- `b` *(float)* – İntegralin üst sınırı  
- `fx` *(function)* – İntegrali alınacak fonksiyon.  
- `n` *(int, varsayılan = 100_000)* – Aralık (dilim) sayısı. Ne kadar büyükse, sonuç o kadar hassas olur.

### 🧪 Örnek Kullanım

```python
def f(x):
    return x**2
result = riemann_sum(0, 1, f)
print(result)  # Çıktı ≈ 0.3333
```

# Simpson Kuralı
Bu fonksiyon, belirli bir `f(x)` fonksiyonunun yaklaşık integralini **Simpson Kuralı** kullanarak hesaplar. Simpson yöntemi, Riemann toplamına göre genellikle daha hassas sonuçlar verir.

---

### 🔧 Parametreler

- `a` *(float)* – İntegralin alt sınırı  
- `b` *(float)* – İntegralin üst sınırı  
- `fx` *(function)* – İntegrali alınacak fonksiyon.  
- `n` *(int, varsayılan = 100_000)* – Aralık (dilim) sayısı. **Çift sayı** olmalıdır. Büyük değerler daha hassas sonuç verir.

---

### 🧪 Örnek Kullanım

```python
def f(x):
    return x**2
result = simpson_rule(0, 1, f)
print(result)  # Çıktı ≈ 0.3333
```

Bu fonksiyon, belirli bir `f(x)` fonksiyonunun yaklaşık integralini **Trapez Yöntemi** kullanarak hesaplar. Bu yöntem, integrali alınan alanı küçük trapezlere bölerek yaklaşık sonuç üretir.

---

### 🔧 Parametreler

- `a` *(float)* – İntegralin alt sınırı  
- `b` *(float)* – İntegralin üst sınırı  
- `fx` *(function)* – İntegrali alınacak fonksiyon.  
- `n` *(int, varsayılan = 100_000)* – Aralık (dilim) sayısı. Daha büyük değerler daha hassas sonuç verir.

---

### 🧪 Örnek Kullanım

```python
def f(x):
    return x**2
result = trapezoidal(0, 1, f)
print(result)  # Çıktı ≈ 0.3333
```


</details>

<details>
<summary>🇬🇧 English</summary>


# Python Integral Calculation Program.

# What is this program for?
- With this program, you can approximately calculate the integral value of any function you want.

# Which methods are used?
- Riemann Sum
- Simpson's Rule
- Trapezoidal Method

# How to use?

# Riemann Sum

This function calculates the approximate integral of a given `f(x)` function using the **Riemann Sum**. Simpson's method generally gives more accurate results compared to the Riemann sum.

### 🔧 Parameters

- `a` *(float)* – Lower limit of the integral  
- `b` *(float)* – Upper limit of the integral  
- `fx` *(function)* – Function to be integrated.  
- `n` *(int, default = 100_000)* – Number of intervals (subdivisions). The larger it is, the more accurate the result.

### 🧪 Example Usage
```python
def f(x):
    return x**2
result = riemann_sum(0, 1, f)
print(result)  # Output approximately 0.3333
```

# Simpson's Rule
This function calculates the approximate integral of a given `f(x)` function using **Simpson's Rule**. Simpson's method generally gives more accurate results compared to the Riemann sum.

---

### 🔧 Parameters

- `a` *(float)* – Lower limit of the integral  
- `b` *(float)* – Upper limit of the integral  
- `fx` *(function)* – Function to be integrated.  
- `n` *(int, default = 100_000)* – Number of intervals (subdivisions). It should be an **even number**. Larger values give more accurate results.

---

### 🧪 Example Usage
```python
def f(x):
    return x**2
result = simpson_rule(0, 1, f)
print(result)  # Output approximately 0.3333
```

This function calculates the approximate integral of a given `f(x)` function using the **Trapezoidal Method**. This method approximates the integral by dividing the area under the curve into small trapezoids.

---

### 🔧 Parameters

- `a` *(float)* – Lower limit of the integral  
- `b` *(float)* – Upper limit of the integral  
- `fx` *(function)* – Function to be integrated.  
- `n` *(int, default = 100_000)* – Number of intervals (subdivisions). Larger values give more accurate results.

---

### 🧪 Example Usage
```python
def f(x):
    return x**2
result = trapezoidal(0, 1, f)
print(result)  # Output approximately 0.3333
Hello! This project does the following...
```
</details>