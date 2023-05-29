from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from daftarHarga import Harga

class Print:
    def __init__(self, window):
        self.window = window
        self.window.title('FAST PRINT')
        self.window.resizable(0, 0)
        self.create_widgets()


    def center_window(self, width, height):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Mengatur ukuran jendela dan menengahkannya di tengah layar
        window_width = 600
        window_height = 400
        self.center_window(window_width, window_height)

        frame = tk.Frame(self.window)
        frame.pack()

        # label judul
        title_label = tk.Label(text="FAST PRINT", font=("Arial", 24))
        title_label.pack(pady=10)

        # Input Print Hitam Putih
        labelBlackWhite = Label(self.window, text="Print Hitam Putih\t", font=("Arial", 10))
        labelBlackWhite.place(x=30, y=60)

        self.intBlackWhite = IntVar()
        entryBlackWhite = Entry(self.window, textvariable=self.intBlackWhite, font=("Arial", 10))
        entryBlackWhite.place(x=30, y=90, width=40, height=20)

        lembarBlackWhite = Label(self.window, text="Lembar\t", font=("Arial", 10))
        lembarBlackWhite.place(x=75, y=90)

        self.ukuranBlackWhite = StringVar(value="Pilih")
        comboboxBlackWhite = ttk.Combobox(self.window, font=("Arial", 7), textvariable=self.ukuranBlackWhite, state="readonly")
        comboboxBlackWhite.place(x=30, y=120, width=45)
        comboboxBlackWhite["values"] = ("A3", "A4", "F4")

        ukBlackWhite = Label(self.window, text="Ukuran Kertas", font=("Arial", 10))
        ukBlackWhite.place(x=75, y=120)

        # Input Print Berwarna
        labelWarna = Label(self.window, text="Print Berwarna\t", font=("Arial", 10))
        labelWarna.place(x=30, y=150)

        self.intWarna = IntVar()
        entryWarna = Entry(self.window, textvariable=self.intWarna, font=("Arial", 10))
        entryWarna.place(x=30, y=175, width=40, height=20)

        lembarWarna = Label(self.window, text="Lembar\t", font=("Arial", 10))
        lembarWarna.place(x=75, y=175)

        self.ukuranWarna = StringVar(value="Pilih")
        comboboxWarna = ttk.Combobox(self.window, font=("Arial", 7), textvariable=self.ukuranWarna, state="readonly")
        comboboxWarna.place(x=30, y=205, width=45)
        comboboxWarna["values"] = ("A3", "A4", "F4")

        ukWarna = Label(self.window, text="Ukuran Kertas",font=("Arial", 10))
        ukWarna.place(x=75, y=205)

        # Input Fotocopy
        labelCopy = Label(self.window, text="Foto Copy\t", font=("Arial", 10))
        labelCopy.place(x=230, y=60)

        self.intCopy = IntVar()
        entryCopy = Entry(self.window, textvariable=self.intCopy, font=("Arial", 10))
        entryCopy.place(x=230, y=90, width=40, height=20)

        lembarCopy = Label(self.window, text="Lembar\t", font=("Arial", 10))
        lembarCopy.place(x=275, y=90)

        self.ukuranCopy = StringVar(value="Pilih")
        comboboxCopy = ttk.Combobox(self.window, font=("Arial", 7), textvariable=self.ukuranCopy, state="readonly")
        comboboxCopy.place(x=230, y=120, width=45)
        comboboxCopy["values"] = ("A3", "A4", "F4")

        ukCopy = Label(self.window,text="Ukuran Kertas",font=("Arial", 9))
        ukCopy.place(x=275, y=120)

        # Button Hitung Total Bayar
        buttonHitung = Button(self.window, text="Hitung Harga", font=("Arial", 10), command=self.hitung_harga)
        buttonHitung.place(x=230, y=200, width=120, height=30)

        # List Daftar Harga
        price_list_frame = tk.Frame(self.window)
        price_list_frame.place(x=420, y=40)

        price_list_label = tk.Label(price_list_frame, text="Daftar Harga", font=("Arial", 12, "bold"))
        price_list_label.pack(pady=5)

        price_list = Listbox(price_list_frame, font=("Arial", 10))
        price_list.pack(fill=BOTH, expand=True)

        price_list.insert(END, "Harga Print Hitam Putih:")
        for ukuran in ("A3", "A4", "F4"):
            price_list.insert(END, f"{ukuran}: Rp {Harga.get_harga_print_hitam_putih(ukuran)}")

        price_list.insert(END, "")
        price_list.insert(END, "Harga Print Berwarna:")
        for ukuran in ("A3", "A4", "F4"):
            price_list.insert(END, f"{ukuran}: Rp {Harga.get_harga_print_berwarna(ukuran)}")

        price_list.insert(END, "")
        price_list.insert(END, "Harga Fotocopy:")
        for ukuran in ("A3", "A4", "F4"):
            price_list.insert(END, f"{ukuran}: Rp {Harga.get_harga_fotocopy(ukuran)}")


        # Output Harga Total
        labelHargaTotal = Label(self.window, text="Harga Total\t", font=("Arial", 10))
        labelHargaTotal.place(x=30, y=270)

        self.intHargaTotal = IntVar()
        OuputHargaTotal = Entry(self.window, textvariable=self.intHargaTotal, font=("Arial", 10), state="readonly")
        OuputHargaTotal.place(x=30, y=300, width=60, height=20)

        # Input Jumlah Uang yang dibayarkan
        labelJumlahUang = Label(self.window, text="Jumlah Uang\t", font=("Arial", 10))
        labelJumlahUang.place(x=150, y=270)

        self.intJumlahUang = IntVar()
        OuputJumlahUang = Entry(self.window, textvariable=self.intJumlahUang, font=("Arial", 10))
        OuputJumlahUang.place(x=150, y=300, width=60, height=20)

        # Button Bayar
        buttonBayar = Button(self.window, text="Bayar Percetakan", font=("Arial", 10), command=self.bayar_percetakan)
        buttonBayar.place(x=270, y=290, width=120, height=30)

        # Output Kembalian
        labelKembalian = Label(self.window, text="Kembalian\t", font=("Arial", 10))
        labelKembalian.place(x=430, y=270)

        self.intKembalian = IntVar()
        OuputKembalian = Entry(self.window, textvariable=self.intKembalian, font=("Arial", 10), state="readonly")
        OuputKembalian.place(x=430, y=300, width=60, height=20)
        
    def hitung_harga(self):
        lembar_blackWhite = self.intBlackWhite.get()
        ukuran_blackWhite = self.ukuranBlackWhite.get()
        lembar_warna = self.intWarna.get()
        ukuran_warna = self.ukuranWarna.get()
        lembar_copy = self.intCopy.get()
        ukuran_copy = self.ukuranCopy.get()

        total_bayar = (
            Harga.get_harga_print_hitam_putih(ukuran_blackWhite) * lembar_blackWhite +
            Harga.get_harga_print_berwarna(ukuran_warna) * lembar_warna +
            Harga.get_harga_fotocopy(ukuran_copy) * lembar_copy
        )

        self.intHargaTotal.set(total_bayar)

        print("Total Bayar = Rp", total_bayar)

    def bayar_percetakan(self):
        while True:
            lembar_blackWhite = self.intBlackWhite.get()
            ukuran_blackWhite = self.ukuranBlackWhite.get()
            lembar_warna = self.intWarna.get()
            ukuran_warna = self.ukuranWarna.get()
            lembar_copy = self.intCopy.get()
            ukuran_copy = self.ukuranCopy.get()

            total_bayar = (
                Harga.get_harga_print_hitam_putih(ukuran_blackWhite) * lembar_blackWhite +
                Harga.get_harga_print_berwarna(ukuran_warna) * lembar_warna +
                Harga.get_harga_fotocopy(ukuran_copy) * lembar_copy
            )

            jumlah_uang = self.intJumlahUang.get()

            if jumlah_uang < total_bayar:
                messagebox.showerror("Pembayaran Gagal", "Uang yang Anda berikan tidak mencukupi.")
                self.intJumlahUang.set("")  # Mengosongkan entry jumlah uang
                return  # Mengulang proses pembayaran

            kembalian = jumlah_uang - total_bayar

            self.intKembalian.set(kembalian)

            print("Kembalian = Rp", kembalian)
            break
        
class PrintHitamPutih(Print):
    def __init__(self, window):
        super().__init__(window)
        self.window.title('FAST PRINT - Print Hitam Putih')

    def hitung_harga(self):
        lembar_blackWhite = self.intBlackWhite.get()
        ukuran_blackWhite = self.ukuranBlackWhite.get()

        total_bayar = (
            Harga.get_harga_print_hitam_putih(ukuran_blackWhite) * lembar_blackWhite
        )

        self.intHargaTotal.set(total_bayar)

        print("Total Bayar Print Hitam Putih = Rp", total_bayar)

class PrintWarna(Print):
    def __init__(self, window):
        super().__init__(window)
        self.window.title('FAST PRINT - Print Berwarna')

    def hitung_harga(self):
        lembar_warna = self.intWarna.get()
        ukuran_warna = self.ukuranWarna.get()

        total_bayar = (
            Harga.get_harga_print_berwarna(ukuran_warna) * lembar_warna
        )

        self.intHargaTotal.set(total_bayar)

        print("Total Bayar Print Berwarna = Rp", total_bayar)

class Fotocopy(Print):
    def __init__(self, window):
        super().__init__(window)
        self.window.title('FAST PRINT - Fotocopy')

    def hitung_harga(self):
        lembar_copy = self.intCopy.get()
        ukuran_copy = self.ukuranCopy.get()

        total_bayar = (
            Harga.get_harga_fotocopy(ukuran_copy) * lembar_copy
        )

        self.intHargaTotal.set(total_bayar)

        print("Total Bayar Fotocopy = Rp", total_bayar)

window = tk.Tk()
app = Print(window)
window.mainloop()