from tkinter import *
from tkinter import messagebox
import statistics
from tkinter.ttk import Treeview

from PIL import Image, ImageTk



sayac=0
def goz():
    global sayac
    sayac+=1
    if sayac%2==1:
        gozbuton.config(image=gostertk)
        sifreentry.config(show="")
    else:
        gozbuton.config(image=gizletk)
        sifreentry.config(show="*")

def yonetici():
    def buton1ekran():
        def personelekle():
            try:
                isim = personelentry.get()
                sifre = psifreentry.get()
                karakter=len(sifre)
                if karakter==4:
                    with open("personel.txt","a",encoding="utf-8") as dosya:

                        pkullanici=f"{isim},{sifre}\n"
                        dosya.write(pkullanici)
                    eklebilgi.config(text="Personel Başarıyla Eklendi.")
                    eklebilgi.update()
                    eklebilgi.after(1500,yonetici)
                    buton1ekran.withdraw()

                else:
                    messagebox.showerror("İşlem Başarısız","Lütfen 4 Haneli Bir Şifre Belirleyiniz.")



            except FileNotFoundError:
                open("personel.txt","w",encoding="utf-8")
                messagebox.showinfo("Belge Oluşturuldu","Kayıp Belge Başarıyla Oluşturuldu!")

        yonekran.withdraw()
        buton1ekran = Toplevel(yonekran)
        x=(penceregenislik-400)//2
        y=(pencereyukseklik-200)//2

        buton1ekran.geometry(f"400x200+{x}+{y}")
        buton1ekran.title("Personel Ekle")
        buton1ekran.resizable(False, False)
        buton1ekran.iconbitmap("firefly.ico")
        personellabel = Label(buton1ekran, text="Personel İsmi")
        personellabel.place(x=50, y=30)

        personelentry = Entry(buton1ekran)
        personelentry.place(x=52, y=50)

        psifrelabel = Label(buton1ekran, text="Personel Şifresi")
        psifrelabel.place(x=50, y=85)

        psifreentry = Entry(buton1ekran)
        psifreentry.place(x=52, y=105)

        gorsel = Image.open("personel.png")
        gorsel = gorsel.resize((100, 100))
        gorseltk = ImageTk.PhotoImage(gorsel)

        gorsellabel = Label(buton1ekran, image=gorseltk)
        gorsellabel.image = gorseltk
        gorsellabel.place(x=200, y=30)

        eklebuton = Button(buton1ekran, text="Personel Ekle", width=17, relief="groove",command=personelekle)
        eklebuton.place(x=50, y=135)

        eklebilgi= Label(buton1ekran, text="")
        eklebilgi.place(x=45,y=160)

    def buton2ekran():
        tablo=Treeview(yonekran)
        tablo["columns"]=("Anahtar","Değer")
        tablo.heading("#1",text="Personel")
        tablo.heading("#2",text="Veri")
        tablo.pack(padx=20, pady=50)


        def kapat():
            tablo.destroy()
            kapabuton.destroy()

        try:
            verilist={}
            with open("veri.txt","r",) as dosya:
                satirlar=dosya.readlines()
                for satir in satirlar:
                    satir=satir.strip()
                    isim,veri=satir.split(",")
                    if isim in verilist:
                        verilist[isim].append(veri)
                    else:
                        verilist[isim]=[veri]




        except FileNotFoundError:
            open("veri.txt", "w", encoding="utf-8")
            messagebox.showinfo("Belge Oluşturuldu", "Kayıp Belge Başarıyla Oluşturuldu!")

        for key, value in verilist.items():
            tablo.insert("", "end", values=(key, ", ".join(value)))

        kapabuton=Button(yonekran,text="Tabloyu Kapat",relief="groove",command=kapat)
        kapabuton.place(x=325,y=500)

    def buton3ekran():
        veriler=[]
        with open("veri.txt","r",encoding="utf-8") as dosya:
            for satir in dosya:
                satir = satir.strip()
            
                if satir:
                    isim,veri=satir.split(",")
                    veri=int(veri)
                    veriler.append(veri)
                    enyuksek=max(veriler)
            messagebox.showinfo("Yüksek Veri Bilgisi",f"En Yüksek Veri Girişi: {enyuksek}")

    def buton4ekran():
        veriler=[]
        with open("veri.txt","r",encoding="utf-8") as dosya:
            for satir in dosya:
                satir=satir.strip()
                if satir:
                    isim,veri=satir.split(",")
                    veri=int(veri)
                    veriler.append(veri)
            endusuk=min(veriler)
            messagebox.showinfo("En Düşük Veri",f"En Düşük Veri Girişi: {endusuk}")

    def buton5ekran():
        tablo=Treeview(yonekran)
        tablo["columns"]=("Anahtar","Değer")
        tablo.heading("#1",text="Personel")
        tablo.heading("#2",text="Veri")
        tablo.pack(padx=20, pady=50)


        def kapat():
            tablo.destroy()
            kapabuton.destroy()

        try:
            verilist={}
            with open("veri.txt","r",) as dosya:
                satirlar=dosya.readlines()
                for satir in satirlar:
                    satir=satir.strip()
                    isim,veri=satir.split(",")
                    if isim in verilist:
                        verilist[isim].append(veri)
                    else:
                        verilist[isim]=[veri]

        


        except FileNotFoundError:
            open("veri.txt", "w", encoding="utf-8")
            messagebox.showinfo("Belge Oluşturuldu", "Kayıp Belge Başarıyla Oluşturuldu!")

        sorted_verilist = sorted(verilist.items(), key=lambda x: x[1], reverse=True)

        for key, value in sorted_verilist:
            sortedvalues=sorted(value,reverse=True)
            tablo.insert("", "end", values=(key, ", ".join(map(str, sortedvalues))))

        kapabuton=Button(yonekran,text="Tabloyu Kapat",relief="groove",command=kapat)
        kapabuton.place(x=325,y=500)

    def buton6ekran():
        veriler=[]
        with open("veri.txt","r",encoding="utf-8") as dosya:
            for satir in dosya:
                satir=satir.strip()
                if satir:
                    isim,veri=satir.split(",")
                    veri=int(veri)
                    veriler.append(veri)
            mod=statistics.mode(veriler)
            medyan=statistics.median(veriler)
            ort=statistics.mean(veriler)
            sapma=statistics.stdev(veriler)
            messagebox.showinfo("Veri Hesaplamaları",f"Verilerin Modu: {mod}\nVerilerin Medyanı: {medyan}\nVerilerin Aritmetik Ortalaması: {ort}\nVerilerin Standart Sapması: {sapma}")





    ekran.withdraw()
    yonekran=Toplevel(ekran)
    yonekran.title("Yönetici Ekranı")
    yonekran.resizable(False,False)
    yonekran.iconbitmap("firefly.ico")
    x=(penceregenislik-750)//2
    y=(pencereyukseklik-600)//2
    yonekran.geometry(f"750x600+{x}+{y}")

    admin = Image.open("admin.png")
    admin=admin.resize((100,100))
    admintk = ImageTk.PhotoImage(admin)

    buton1=Button(yonekran, text="Personel Ekle", relief="groove", width=30,command=buton1ekran)
    buton1.place(x=260,y=100)
    buton2 = Button(yonekran, text="Verileri Görüntüle", relief="groove", width=30,command=buton2ekran)
    buton2.place(x=260, y=125)
    buton3 = Button(yonekran, text="En Yüksek Veriyi Görüntüle", relief="groove", width=30,command=buton3ekran)
    buton3.place(x=260, y=150)
    buton4 = Button(yonekran, text="En Düşük Veriyi Görüntüle", relief="groove", width=30,command=buton4ekran)
    buton4.place(x=260, y=175)
    buton5 = Button(yonekran, text="Personel Sıralaması", relief="groove", width=30,command=buton5ekran)
    buton5.place(x=260, y=200)
    buton6 = Button(yonekran, text="Veri Hesapları", relief="groove", width=30,command=buton6ekran)
    buton6.place(x=260, y=225)

    adminimg=Label(yonekran, image=admintk)
    adminimg.image=admintk
    adminimg.place(x=325,y=300)






def giris():
    try:
        kullaniciadi = kullanicientry.get().strip()
        parola = sifreentry.get()
        if kullaniciadi=="admin" and parola=="admin":
            bilgi.config(text="Yönetici Ekranına Yönlendiriliyorsunuz...")
            bilgi.update()
            bilgi.after(1000, yonetici)
        else:
            veriler={}
            with open("personel.txt","r",encoding="utf-8") as dosya:
                satirlar=dosya.readlines()

                for satir in satirlar:
                    satir=satir.strip()
                    isim,sifre=satir.split(",")
                    veriler[isim]=sifre

            if kullaniciadi in veriler and parola==veriler[kullaniciadi]:
                bilgi.config(text="Personel Ekranına Yönlendiriliyorsunuz...")
                bilgi.update()
                bilgi.after(1000, personel)

            else:
                messagebox.showerror("Giriş Başarısız!","Kullanıcı Adı veya Şifre Yanlış!")

    except FileNotFoundError:
        open("personel.txt","w",encoding="utf-8")
        messagebox.showinfo("Dosya Oluşturuldu","Personel Dosyası Başarıyla Oluşturuldu.")
    except ValueError:
        messagebox.showinfo("Dosya Hatası","Personel Dosyası Boş!")

def personel():

    def veriekle():
        
        with open("veri.txt","a",encoding="utf-8") as dosya:
            everi=int(verientry.get())
            if 0<everi<=1000:
                everi=verientry.get()
                kullaniciadi=kullanicientry.get()
                eklenecek=kullaniciadi+","+ everi+"\n"
                dosya.write(eklenecek)
            else:
                messagebox.showerror("Hata","Gireceğiniz Değer 0-1000 Arası Olmalıdır!")


    ekran.withdraw()
    perekran=Toplevel(ekran)
    perekran.geometry("300x300")
    perekran.title("Personel Girişi")
    perekran.resizable(False,False)
    perekran.iconbitmap("firefly.ico")
    x=(penceregenislik-300)//2
    y=(pencereyukseklik-300)//2
    perekran.geometry(f"300x300+{x}+{y}")

    verilabel=Label(perekran,text="Lütfen Bir Veri Değeri Giriniz (0-1000)")
    verilabel.place(x=50,y=50)
    verientry=Entry(perekran)
    verientry.place(x=90,y=80)
    veributon=Button(perekran,text="Veri Ekle", width=20,relief="groove",command=veriekle)
    veributon.place(x=77,y=120)

    perimg=Image.open("personel.png")
    perimg=perimg.resize((100,100))
    perimgtk=ImageTk.PhotoImage(perimg)

    perlabel=Label(perekran,image=perimgtk)
    perlabel.image=perimgtk
    perlabel.place(x=100,y=160)



ekran=Tk()

penceregenislik=ekran.winfo_screenwidth()
pencereyukseklik=ekran.winfo_screenheight()
ekran.resizable(False,False)
ekran.title("Giriş Ekranı")
x=(penceregenislik-400)//2
y=(pencereyukseklik-250)//2

ekran.geometry(f"400x250+{x}+{y}")
ekran.iconbitmap("firefly.ico")

goster=Image.open("eye.png")
goster=goster.resize((20,20))
gostertk=ImageTk.PhotoImage(goster)
gizle=Image.open("hidden.png")
gizle=gizle.resize((20,20))
gizletk=ImageTk.PhotoImage(gizle)
kullanici=Image.open("user.png")
kullanici=kullanici.resize((100,100))
kullanicitk=ImageTk.PhotoImage(kullanici)


kullanicilabel=Label(ekran, text="Kullanıcı Adı")
kullanicilabel.place(x=70,y=40)

kullanicientry=Entry(ekran)
kullanicientry.place(x=70,y=65)

sifrelabel=Label(ekran, text="Şifre")
sifrelabel.place(x=70,y=100)

sifreentry=Entry(ekran,show="*")
sifreentry.place(x=70,y=125)

kullaniciresim=Label(ekran,image=kullanicitk)
kullaniciresim.place(x=230, y=70)

girisbuton=Button(ekran, text="Giriş",width=17,relief="groove",command=giris)
girisbuton.place(x=68,y=160)

gozbuton=Button(ekran, image=gizletk, bd=0,command=goz)
gozbuton.place(x=45,y=123)


bilgi=Label(ekran,text="")
bilgi.place(x=65,y=200)




ekran.mainloop()