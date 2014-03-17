def successiveApproxIntegrate(f, a, b, epsilon):
    parts = 1
    while True:
        tmp1 = integrate(f, a, b, parts)
        tmp2 = integrate(f, a, b, parts*2)
        if abs(tmp1 - tmp2) < epsilon:
            return tmp1
        parts *=2