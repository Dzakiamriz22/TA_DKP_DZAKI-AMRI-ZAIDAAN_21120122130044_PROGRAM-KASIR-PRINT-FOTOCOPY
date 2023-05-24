class Harga:
    @staticmethod
    def get_harga_print_hitam_putih(ukuran):
        harga_print_hitam_putih = {"A3": 750, "A4": 500, "F4": 500}
        return harga_print_hitam_putih.get(ukuran, 0)

    @staticmethod
    def get_harga_print_berwarna(ukuran):
        harga_print_berwarna = {"A3": 2000, "A4": 1000, "F4": 1500}
        return harga_print_berwarna.get(ukuran, 0)

    @staticmethod
    def get_harga_fotocopy(ukuran):
        harga_fotocopy = {"A3": 500, "A4": 250, "F4": 250}
        return harga_fotocopy.get(ukuran, 0)