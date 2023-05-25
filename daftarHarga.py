class Harga:
    @staticmethod
    def get_harga_print_hitam_putih(ukuran):
        if ukuran == "A3":
            return 500
        elif ukuran == "A4":
            return 300
        elif ukuran == "F4":
            return 400
        else:
            return 0

    @staticmethod
    def get_harga_print_berwarna(ukuran):
        if ukuran == "A3":
            return 1000
        elif ukuran == "A4":
            return 700
        elif ukuran == "F4":
            return 800
        else:
            return 0

    @staticmethod
    def get_harga_fotocopy(ukuran):
        if ukuran == "A3":
            return 200
        elif ukuran == "A4":
            return 100
        elif ukuran == "F4":
            return 150
        else:
            return 0
