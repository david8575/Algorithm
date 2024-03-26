# 하노이 탑 hanoi tower
def hanoiTower(a,b,c,n,m,cnt):
    if (m == cnt):
        print(f"{a} {c}")
        return None
    else:
        hanoiTower(a,c,b,n-1,m,cnt+1)
        hanoiTower(b,a,c,n-1,m,cnt+1)