#modülü içeriye aktararak başlıyoruz

# python için turtule standart grafik kitaplığı
import turtle


# koch kar tanesi veya koch eğrisi oluşturma işlevi
def snowflake(lengthSide, levels):
    if levels == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels - 1)
    t.left(60)
    snowflake(lengthSide, levels - 1)
    t.right(120)
    snowflake(lengthSide, levels - 1)
    t.left(60)
    snowflake(lengthSide, levels - 1)


# main 
if __name__ == "__main__":
    t=turtle.Pen()
    t.speed(0)  # çizimin hızını tanımlamak
    length = 300.0  
    t.penup()  # Kalemi yukarı çekin - hareket ederken çizim yapmayın.
    # turtle, turtle'ın gittiği yönün tersi yönde geriye doğru hareket ettirin.
    # turtle'n yönünü değiştirmeyin.
    t.backward(length / 2.0)
    t.pendown()
    for i in range(3):
        # Kalemi aşağı çekin - hareket ederken çizin.
        snowflake(length, 4)
        t.right(120)
    # turtle'n kapanma pencerelerini kontrol etmek için
    #mainloop()

