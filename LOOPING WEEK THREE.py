 #sebuah gedung teater berbentuk trapesium sama kaki
#jumlah kursi pengunjung didalamya adalah 1380 kursi yang terbagi menjadi 15 baris
#selisih tiap baris sebanyak 6 kursi. berapakah masing-masing jumlah baris 1-15?

#diket Sn=1380, n=15, b=6
#rumus suku ke-n=a+((n-1)*b)
#rumus deret aritmatika Sn=(n/2)*(a+Un) atau Sn=(n/2)*((2*a)+((n-1)*b))

Sn=1380
n=15
b=6
#Sn=(n/2)*((2*a)+((n-1)*b))
a=((Sn/(n/2))-((n-1)*b))/2
print("jumlah kursi tiap baris berurt-urut adalah:")
for c in range (1,16):
    c=a
    print(c)
    a=c+6



